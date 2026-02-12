# CactusCon 14 Badge - Full Reverse Engineering Walkthrough

> Everything I found tearing apart the CactusCon 14 electronic badge firmware. This covers the battle engine, BLE chat crypto, the CactIOT API, unlock codes, LED hacking, portability data extraction, easter eggs, and how to mod the badge yourself.

**Badge**: CactusCon 14 "CactIOT" Badge
**Hardware**: ESP32-S3 (16MB Flash, 2MB+ PSRAM)
**Firmware**: MicroPython 1.26.1 + LVGL 9.4.0 (custom fork of [lvgl_micropython](https://github.com/lvgl/lv_micropython))
**Tools Used**: Python 3, pyserial, binwalk, hexdump, curl

---

## Table of Contents

1. [Firmware Extraction](#1-firmware-extraction)
2. [Filesystem & Code Layout](#2-filesystem--code-layout)
3. [Configuration Secrets](#3-configuration-secrets)
4. [The Creature System](#4-the-creature-system)
5. [Battle Engine Deep Dive](#5-battle-engine-deep-dive)
6. [Predictable RNG - Every Battle is Predetermined](#6-predictable-rng---every-battle-is-predetermined)
7. [Battle Consensus Protocol](#7-battle-consensus-protocol)
8. [Unlock Code System & Bypass](#8-unlock-code-system--bypass)
9. [Achievement System](#9-achievement-system)
10. [Portability System & Data Extraction](#10-portability-system--data-extraction)
11. [BLE Chat Encryption](#11-ble-chat-encryption)
12. [CactIOT API](#12-cactiot-api)
13. [NeoPixel LED Control](#13-neopixel-led-control)
14. [OTA Update System](#14-ota-update-system)
15. [Buzzer Mod - Freeing GPIO 19](#15-buzzer-mod---freeing-gpio-19)
16. [Modding the Badge](#16-modding-the-badge)
17. [Easter Eggs & Fun Stuff](#17-easter-eggs--fun-stuff)
18. [Unsolved Mysteries](#18-unsolved-mysteries)

---

## 1. Firmware Extraction

The gym station firmware is a single 8MB binary (`lvgl_micropy_ESP32_GENERIC_S3-8MB-STATION.bin`) that contains the full ESP32-S3 flash image. The badge firmware is a separate 16MB image that includes additional image assets — available through the badge's /flash website. This walkthrough was done against the station (gym) firmware.

### Partition Layout (8MB Station/Gym Firmware)

| Offset | Size | Content |
|--------|------|---------|
| `0x0000` | 4KB | Bootloader header |
| `0x8000` | 4KB | Partition table |
| `0x10000` | ~2.8MB | MicroPython application (with LVGL 9.4.0) |
| `0x2D0000` | ~5.2MB | FAT12 filesystem (user code + assets) |
| `0x40254` | ~570KB | JPEG splash screen (CactusCon branding) |

### Extracting the Filesystem

All the MicroPython source code lives on a FAT12 filesystem starting at `0x2D0000`. You can pull it out and poke around:

```bash
dd if=firmware.bin of=fat12.img bs=1 skip=$((0x2D0000))
```

Or just connect over serial and browse directly from the REPL:

```python
import os
print(os.listdir('/'))
# ['assets', 'boot.py', 'cactiotpad', 'cactuscon', 'config.mpy',
#  'main.py', 'saguarota', 'thirdparty', 'versions.json', 'patch.log']
```

---

## 2. Filesystem & Code Layout

```
/
├── boot.py                    # Boot sequence (27,211 bytes) - PSRAM, OTA, display init
├── main.py                    # Entry point, launches BadgeApplication
├── config.mpy                 # Badge configuration (OTA-updated)
├── versions.json              # Firmware version tracking
├── cactuscon/                  # Main game engine
│   ├── application.py         # BadgeApplication main loop
│   ├── prefs.mpy              # NVS preferences + portability system
│   ├── unlocks.mpy            # Unlock code validation (SHA-256)
│   ├── game/
│   │   └── engine/
│   │       ├── characters.mpy # 15 creatures, evolution trees
│   │       ├── moves.mpy      # 42 battle moves
│   │       ├── battle_rules.mpy      # Damage formulas, type effectiveness
│   │       ├── deterministic_random.mpy  # LCG-based RNG
│   │       ├── consensus.mpy  # Battle integrity verification
│   │       └── achievements.mpy      # 14 achievements + powers
│   ├── hw/
│   │   └── pixels.mpy         # NeoPixel LED controller
│   └── ui/
│       └── panels/            # LVGL UI screens
├── cactiotpad/                 # IoT communication pad
│   ├── crypto.mpy             # AES-128-CBC encryption
│   ├── storage.mpy            # SecureStorage (API keys)
│   ├── config.mpy             # BLE UUIDs, endpoints
│   └── auth.mpy               # Device authentication
└── saguarota/                  # OTA update system
```

Everything interesting is compiled to `.mpy` bytecode, so you can't just read the source. But since it's still Python under the hood, you can explore everything at runtime through the REPL with `dir()`, attribute access, and monkey-patching.

---

## 3. Configuration Secrets

### WiFi Credentials

Sitting in plaintext in the firmware binary:

```python
OTA_WIFI_SSID     = "CactusCon"
OTA_WIFI_PASSWORD  = "Cactus2026!"
```

### API & Network

```python
CACTIOT_URL          = "https://badge.cactuscon.com"
OTA_PROD_BASE_URL    = "http://badge-ota.cactuscon.com/"  # HTTP, no TLS
CACTIOT_VERIFY_SSL   = False  # SSL verification disabled
```

### Per-Badge Secrets

Each badge has its own API key and device ID stored in `SecureStorage`. You can pull them over REPL:

```python
>>> from cactiotpad.storage import SecureStorage
>>> ss = SecureStorage()
>>> print(ss.get_api_key())    # sk_XXXX...  (unique per badge)
>>> print(ss.get_device_id())  # XX:XX:XX:XX:XX:XX  (badge MAC)
```

### BLE Configuration

```python
AUTO_BATTLE_MODE   = False
CHAT_ADV_PREFIX    = "CC14PEER"  # BLE advertisement prefix
```

### Hardware Pins

```python
PIN_NEOPIXEL   = 18   # WS2812B data line
PIN_BUZZER     = 19   # FUET-9032 passive buzzer (blocked by USB OTG in stock firmware)
NUM_NEOPIXELS  = 6    # LED count
PIN_STATUS_LED = 21   # Status indicator
PINS_LED       = [13, 14, 15, 16, 17, 46]  # Additional LEDs
```

### BLE UUIDs

The badge uses custom BLE UUIDs that are packed with leetspeak:

| Service | UUID |
|---------|------|
| Game Service | `CC140001-0000-0000-0000-CAC71B072026` |
| Game Characteristic | `CC140002-C0DE-4BAD-9E14-CAC71B072026` |
| Chat Service | `CC14C001-0000-0000-0000-CAC71B072026` |
| Chat Characteristic | `CC14C002-C0DE-4BAD-9E14-CAC71B072026` |

Breaking down the leetspeak:
- `CC14` = CactusCon 14
- `C0DE` = CODE
- `4BAD` = 4BAD
- `9E14` = GE14
- Put together: `C0DE-4BAD-9E14` reads something like "Code 4 Badge 14"
- `CAC71B072026` = CACTI B 07/2026 (maybe?)
- Game services use `0001`/`0002`, Chat uses `C001`/`C002`

---

## 4. The Creature System

### 15 Creatures Across 5 Evolution Lines

| Element | Stage 1 | Stage 2 | Stage 3 |
|---------|---------|---------|---------|
| Cacti | Hacktarchu | Hackachu | Hackachimon |
| Electricity | Voltiny | Voltqueen | Voltreign |
| Poison | Cinderlet | Cinderserp | Cindervipe |
| Radiowaves | Blipbat | Glyphbat | Runewing |
| Shadow | Cipherkit | Enigmox | Cryptilox |

### Evolution

```python
EVOLVE_REQUIRED_LEVEL = 5
CARE_TEMPERAMENT_MAX  = 10
```

### Care System

Four actions affect your creature's stats:

| Action | Effect |
|--------|--------|
| Bathe | Hygiene boost |
| Discipline | Temperament adjustment |
| Feed | Hunger/energy restore |
| Treat | Happiness boost |

### Stats

Each creature tracks: `hp`, `max_hp`, `attack`, `defense`, `sp_attack`, `sp_defense`, `speed`, `level`, `evasion`, `status_effects`, plus temporary battle modifiers like `defense_mult`, `defense_turns`, and `defense_elem`.

---

## 5. Battle Engine Deep Dive

### Damage Formula Constants

| Constant | Value | What It Does |
|----------|-------|--------------|
| `BASE_DAMAGE_MULTIPLIER` | 2.15 | Scales raw damage output |
| `DEFENSE_EFFICIENCY_MULT` | 0.90 | How much defense actually reduces damage |
| `DAMAGE_VARIATION_MIN` | 0.75 | Minimum damage roll |
| `DAMAGE_VARIATION_MAX` | 1.00 | Maximum damage roll |
| `CRIT_CHANCE` | 0.075 (7.5%) | Critical hit probability |
| `CRIT_MULTIPLIER` | 1.85x | Crit damage multiplier |
| `MIN_DAMAGE` | 5 | Damage floor |
| `EVASION_EFFECT_MULT` | 2.5 | Evasion effectiveness scaling |

### Type Effectiveness: It's All Neutral

I tested every single one of the 25 element matchups (5 attack types x 5 defense types) for both physical and special moves. Every combination returns `1.0`. There are no type advantages or disadvantages at all - the five elements (cacti, electricity, poison, radiowaves, shadow) are purely cosmetic in battle.

```
cacti -> cacti:        1.0    electricity -> cacti:      1.0
cacti -> electricity:  1.0    electricity -> poison:     1.0
cacti -> poison:       1.0    electricity -> radiowaves: 1.0
...every single matchup returns 1.0
```

### All 42 Battle Moves

Pulled these from `MoveRegistry().register_defaults()`:

**Move Types**: Physical (0), Special (1), Status (2), Heal (3)
**Move Categories**: Damage (0), Heavy (1), Support (2), Recovery (3)

| ID | Name | Power | Accuracy | Element | Type | Category |
|----|------|-------|----------|---------|------|----------|
| 0 | BrambleRush | 9 | 95 | cacti | Physical | Damage |
| 1 | NeedleBarrage | 14 | 85 | cacti | Physical | Heavy |
| 2 | ThornWhip | 7 | 100 | cacti | Physical | Damage |
| 3 | SporeCloud | 0 | 90 | cacti | Status | Support |
| 4 | PhotoBlast | 12 | 90 | cacti | Special | Damage |
| 5 | VoltTackle | 10 | 95 | electricity | Physical | Damage |
| 6 | ThunderSlam | 15 | 80 | electricity | Physical | Heavy |
| 7 | SparkJab | 7 | 100 | electricity | Physical | Damage |
| 8 | Overcharge | 0 | 85 | electricity | Status | Support |
| 9 | ArcFlash | 13 | 88 | electricity | Special | Damage |
| 10 | VenomStrike | 9 | 95 | poison | Physical | Damage |
| 11 | ToxicCrush | 14 | 82 | poison | Physical | Heavy |
| 12 | AcidSpit | 8 | 100 | poison | Physical | Damage |
| 13 | MiasmaVeil | 0 | 90 | poison | Status | Support |
| 14 | CorrosivePulse | 12 | 90 | poison | Special | Damage |
| 15 | FrequencySlash | 9 | 95 | radiowaves | Physical | Damage |
| 16 | WaveCannon | 15 | 80 | radiowaves | Physical | Heavy |
| 17 | PingStrike | 7 | 100 | radiowaves | Physical | Damage |
| 18 | StaticField | 0 | 88 | radiowaves | Status | Support |
| 19 | SignalBurst | 13 | 88 | radiowaves | Special | Damage |
| 20 | ShadowClaw | 10 | 95 | shadow | Physical | Damage |
| 21 | VoidCrush | 14 | 82 | shadow | Physical | Heavy |
| 22 | DarkSwipe | 7 | 100 | shadow | Physical | Damage |
| 23 | Obfuscate | 0 | 90 | shadow | Status | Support |
| 24 | NightPulse | 12 | 90 | shadow | Special | Damage |
| 25-99 | *(reserved)* | | | | | |
| **100** | **Patch** | 0 | 100 | - | **Heal** | **Recovery** |
| **101** | **Debug** | 0 | 100 | - | **Heal** | **Recovery** |

The two healing moves are the most interesting:
- **Patch** (ID 100) restores 25% HP
- **Debug** (ID 101) restores 50% HP

Love the dev-themed naming here - fixing bugs literally heals your creature.

### Battle State Constants

```python
BATTLE_CONTINUES = 0
PLAYER_WINS      = 1
OPPONENT_WINS    = 2
BATTLE_DRAW      = 3
```

---

## 6. Predictable RNG - Every Battle is Predetermined

This is probably the biggest finding. The battle system uses a textbook Linear Congruential Generator for all its "randomness."

### The Algorithm

```python
# Numerical Recipes LCG - published in textbooks since the 1980s
MULTIPLIER = 1664525
INCREMENT  = 1013904223
MODULUS    = 4294967296  # 2^32

state = (state * MULTIPLIER + INCREMENT) % MODULUS
```

This is the classic [Numerical Recipes LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator#Parameters_in_common_use). Given the seed, the entire sequence of "random" numbers is completely predictable.

### Proof

```python
>>> rng1 = DeterministicRNG(12345)
>>> print(rng1.randint(0, 100), rng1.randint(0, 100), rng1.randint(0, 100))
56 80 85

>>> rng2 = DeterministicRNG(12345)
>>> print(rng2.randint(0, 100), rng2.randint(0, 100), rng2.randint(0, 100))
56 80 85  # Identical sequence
```

### Available Methods

```python
DeterministicRNG(seed)
  .randint(min, max)    # Random integer in range
  .random()             # Float [0, 1)
  .uniform(a, b)        # Float in range
  .choice(sequence)     # Random element from list
  .get_state()          # Returns 4-byte state
  .get_seed()           # Returns initial seed
```

### What This Means

Since the seed is derived from values exchanged during battle setup, if you know the seed you know everything:
- Every damage roll (the 0.75-1.0 variation range)
- Every critical hit (7.5% chance, but predetermined)
- Every accuracy check
- You could pick moves knowing which ones will crit or miss before the turn even happens

---

## 7. Battle Consensus Protocol

When two badges battle, they use a consensus system to make sure both sides compute the same results.

### How It Works

```
Badge A                              Badge B
   |                                    |
   |-- begin_turn(turn, moveA, moveB) ->|
   |<- begin_turn(turn, moveB, moveA) --|
   |                                    |
   |   [Both compute battle outcome     |
   |    using identical DeterministicRNG]|
   |                                    |
   |-- record_outcome(TurnOutcome) ---->|
   |<- record_outcome(TurnOutcome) -----|
   |                                    |
   |-- get_our_hash() = H_A ---------->|
   |<- get_our_hash() = H_B -----------|
   |                                    |
   |   receive_opponent_hash(H_B)       |
   |   receive_opponent_hash(H_A)       |
   |                                    |
   |   if H_A == H_B:                   |
   |     commit_turn()  ← CONSENSUS     |
   |   else:                            |
   |     void_battle()  ← MISMATCH      |
```

### ConsensusTracker

```python
ct = ConsensusTracker(session_token)

# State:
ct.session_token      # Battle session ID
ct.current_turn       # Turn counter (starts at 0)
ct.our_hash           # Our computed turn hash
ct.their_hash         # Opponent's turn hash
ct.pending_outcome    # TurnOutcome awaiting consensus
ct.history            # Committed TurnOutcome list

# Methods:
ct.begin_turn(turn, player_move_id, opponent_move_id)
ct.record_outcome(turn_outcome)
ct.get_our_hash()              # 128-bit hash
ct.receive_opponent_hash(h)    # Returns 1 if match
ct.commit_turn()               # Adds to history
ct.void_battle()               # Aborts on mismatch
ct.get_rng()                   # The battle's DeterministicRNG
ct.get_battle_hash()           # Unique hash for the whole battle
```

### TurnOutcome

Every detail of a turn gets recorded for hash verification:

```python
to = TurnOutcome()

to.turn_number              # Turn index
to.player_move_id           # Move used by player
to.opponent_move_id         # Move used by opponent
to.player_went_first        # Who went first (speed check)
to.player_damage_dealt      # Damage dealt by player
to.opponent_damage_dealt    # Damage dealt by opponent
to.player_healed            # HP recovered by player
to.opponent_healed          # HP recovered by opponent
to.player_crit              # Did player crit?
to.opponent_crit            # Did opponent crit?
to.player_hp_after          # Player HP after turn
to.opponent_hp_after        # Opponent HP after turn
to.rng_state                # RNG state snapshot
to.player_effects_applied   # Status effects applied to player
to.opponent_effects_applied # Status effects applied to opponent

to.to_dict()       # Serialize
to.compute_hash()  # 128-bit hash of all fields
```

### Verified Example

```python
>>> ct = ConsensusTracker(42)
>>> to = TurnOutcome()
>>> ct.record_outcome(to)
>>> ct.get_our_hash().hex()
'ddcd6b75ef89b8d672e392bd5394bf78'
>>> to.compute_hash().hex()
'ddcd6b75ef89b8d672e392bd5394bf78'  # Match

>>> ct.receive_opponent_hash(ct.get_our_hash())
1  # Consensus

>>> ct.commit_turn()
>>> len(ct.history)
1  # Turn committed
```

---

## 8. Unlock Code System & Bypass

### How It Works

The badge has 6 secret unlock codes that grant special abilities. These were obtained at the convention as part of CTF challenges and SAO board soldering challenges.

The validation is straightforward:

```python
_SALT = b'CC14:'

def _verify_digest(code_string, expected_hash_hex):
    normalized = code_string.strip().upper()
    computed = sha256(b'CC14:' + normalized.encode()).hexdigest()
    return computed == expected_hash_hex
```

You enter a code, it gets uppercased and trimmed, salted with `CC14:`, SHA-256'd, and compared against a registry of known hashes.

### The 6 Hash Targets

Pulled from the firmware binary at offset `0x2FBDDD`:

| Hash (SHA-256) | Unlock Function | Source |
|----------------|-----------------|--------|
| `2e1e001c4330...d87001` | `unlock_focus` | CTF Badge Challenge |
| `04bf72c2c207...246d09` | `unlock_rage` | CTF Badge Challenge |
| `b4ba99622b64...0293f7` | `unlock_workhard_playhard` | CTF Badge Challenge |
| `8be810a27627...041874` | `unlock_complete_1` | SAO Badge Challenge |
| `7625dfdb07a2...10d06c` | `unlock_complete_2` | SAO Badge Challenge |
| `b0e1e7a7aa07...14d117` | `unlock_complete_3` | SAO Badge Challenge |

<details>
<summary>Full hashes</summary>

```
2e1e001c43305cf9d9f4ba4c9f82fd36a4de67c4608e1285eb62918a71d87001  →  unlock_focus
04bf72c2c207bd86151af0345169797df6e89bb966bd854ff7668dda64246d09  →  unlock_rage
b4ba99622b643921c168451571b230c95f47c3a3efcb87d3bfe2532eac0293f7  →  unlock_workhard_playhard
8be810a276278511cbd07c0141f23a6f898606e698826ca85673e8a2d9041874  →  unlock_complete_1
7625dfdb07a223ee07a9475bc42b406230171cf700fe96d006494f8b8310d06c  →  unlock_complete_2
b0e1e7a7aa077388e1c58f2304b037abaa4bbb2ccde058288c19772f8314d117  →  unlock_complete_3
```

</details>

To crack any of these, find a string `X` where:
```
SHA256(b"CC14:" + X.strip().upper().encode()).hexdigest() == target_hash
```

### The Bypass

Since the badge exposes a full MicroPython REPL over serial, you can just patch the verification function at runtime:

```python
>>> from cactuscon import unlocks
>>> from cactuscon.prefs import prefs

# Make _verify_digest always return True
>>> unlocks._verify_digest = lambda normalized, expected_hex: True

# Any string now triggers all unlocks
>>> unlocks.try_redeem(prefs, achievements, "BYPASS")
(True, 'Unlocked!')
```

All six unlocked successfully:

| Function | Result |
|----------|--------|
| `unlock_focus` | `(True, 'Unlocked!')` |
| `unlock_rage` | `(True, 'Unlocked!')` |
| `unlock_workhard_playhard` | `(True, 'Unlocked!')` |
| `unlock_complete_1` | `(True, 'Unlocked!')` |
| `unlock_complete_2` | `(True, 'Unlocked!')` |
| `unlock_complete_3` | `(True, 'Unlocked!')` |

---

## 9. Achievement System

### All 14 Achievements

| Category | Achievement | How to Get It |
|----------|-------------|---------------|
| Gameplay | `first_battle` | Win your first battle |
| Gameplay | `clean_care` | Complete a care routine |
| Gameplay | `collector` | Collect multiple creatures |
| Gameplay | `win_streak_3` | Win 3 battles in a row |
| Gameplay | `loss_streak_3` | Lose 3 in a row (consolation prize) |
| Gameplay | `tough_love` | Discipline-focused care |
| Gameplay | `sweet_tooth` | Treat-focused care |
| Gameplay | `temper_max` | Max out temperament |
| CTF Unlock | `focus` | Secret code from CTF challenge |
| CTF Unlock | `rage` | Secret code from CTF challenge |
| CTF Unlock | `work_play` | Secret code from CTF challenge |
| SAO | `sao_unlock_hackachu` | Plug in the Hackachu SAO board |
| SAO | `sao_unlock_enigmox` | Plug in the Enigmox SAO board |
| SAO | `sao_unlock_glyphbat` | Plug in the Glyphbat SAO board |

### Achievement Powers

```python
ACHIEVEMENT_POWERS = {
    'focus': {
        'effect': '+20% XP gain',
        'duration': 900,     # 15 minutes
        'cooldown': 1800,    # 30 minutes
    },
    'rage': {
        'effect': '+5 ATK stat',
        'duration': 900,     # 15 minutes
        'cooldown': 5400,    # 90 minutes
    },
    'work_play': {
        'effect': 'rgb_rainbow',  # Permanent rainbow LEDs
        'duration': -1,           # Never expires
        'cooldown': 0,
    },
}
```

---

## 10. Portability System & Data Extraction

The badge can export its full state as an encrypted blob. This is gated behind a SHA-1 key check.

### The Gate

```python
_PORTABILITY_ID = "f598682777ca9c75daa4b1b2a978d44ae9752035"
```

The `_portability_check(key)` function hashes your input with SHA-1 and compares it to this value. Without the right passphrase, you get one of these:

```
"secret_key required"
"Invalid extraction key"
"No data provided"
"Invalid portability secret"
```

### Bypass

```python
>>> from cactuscon.prefs import prefs
>>> prefs._portability_check = lambda key: True
>>> data = prefs.portability_extract("anything", prefs)
```

This gives you a Base64-encoded blob that's been XOR'd.

### The "Encryption"

The portability data is protected by `_loop_swoop_pull()`, which is just a repeating XOR cipher with a fun name:

```python
def _loop_swoop_pull(key_bytes, data_bytes):
    result = bytearray(len(data_bytes))
    key_len = len(key_bytes)
    for i in range(len(data_bytes)):
        result[i] = data_bytes[i] ^ key_bytes[i % key_len]
    return bytes(result)
```

### What's Inside

After decoding, you get the full badge state as JSON:

```json
{
  "entries": [
    {"k": "hdl_handle", "t": "s", "v": "<player_handle>"},
    {"k": "cx_hackachimon", "t": "i", "v": 999999},
    {"k": "cl_hackachimon", "t": "i", "v": 99},
    {"k": "cx_voltreign", "t": "i", "v": 999999},
    {"k": "cl_voltreign", "t": "i", "v": 99},
    {"k": "cx_cindervipe", "t": "i", "v": 999999},
    {"k": "cl_cindervipe", "t": "i", "v": 99},
    {"k": "cx_runewing", "t": "i", "v": 999999},
    {"k": "cl_runewing", "t": "i", "v": 99},
    {"k": "cx_cryptilox", "t": "i", "v": 999999},
    {"k": "cl_cryptilox", "t": "i", "v": 99},
    {"k": "cx_blipbat", "t": "i", "v": 999999},
    {"k": "cl_blipbat", "t": "i", "v": 99}
  ],
  "ts": 26738452,
  "v": 1
}
```

### NVS Key Schema

| Prefix | Meaning | Example |
|--------|---------|---------|
| `hdl_` | Handle/username | `hdl_handle` |
| `cx_` | Creature XP | `cx_hackachimon` = 999999 |
| `cl_` | Creature Level | `cl_hackachimon` = 99 |
| `pl_` | Player stats | `pl_xp`, `pl_lvl`, `pl_win`, `pl_loss` |
| `st_` | Station stats | `st_win`, `st_loss`, `st_ch` |
| `pc_` | Pack data | `pc_chars` = comma-separated creature IDs |
| `ws` | Win streak | Current consecutive wins |
| `ls` | Loss streak | Current consecutive losses |
| `ach` | Achievements | Comma-separated achievement IDs |

---

## 11. BLE Chat Encryption

Badge-to-badge chat uses AES-128-CBC with a multi-step key exchange.

### Key Derivation

```
1. Each badge generates a random key fragment
   generate_symkey1() → 8 hex chars (4 random bytes)

2. Fragments are combined with both MACs
   derive_symkey2(sk1_a, sk1_b, mac_a, mac_b) → 16 hex chars

3. Full session key derivation
   derive_session_hash_and_key(sk1_a, sk1_b, mac_a, mac_b, sk2)
   → (SHA-256 session hash, AES-128 key)

4. Encrypt/decrypt
   encrypt_message(key_hex, plaintext_hex) → Base64 ciphertext
   decrypt_message(key_hex, ciphertext_b64) → plaintext hex
```

### Details

- **Algorithm**: AES-128-CBC via `ucryptolib`
- **Padding**: PKCS7
- **Key**: 128-bit (16 bytes / 32 hex chars)
- **IV**: Prepended to ciphertext
- **I/O**: Hex strings for plaintext, Base64 for ciphertext

### Working Example

```python
>>> from cactiotpad import crypto
>>> import ubinascii

# Generate key fragments
>>> sk1_a = crypto.generate_symkey1()
>>> sk1_b = crypto.generate_symkey1()

# Derive shared key (MACs must be hex WITHOUT colons)
>>> mac_a = "aabbccddeeff"
>>> mac_b = "112233445566"
>>> sk2 = crypto.derive_symkey2(sk1_a, sk1_b, mac_a, mac_b)

# Get session key
>>> session_hash, aes_key = crypto.derive_session_hash_and_key(
...     sk1_a, sk1_b, mac_a, mac_b, sk2)

# Encrypt
>>> plaintext_hex = ubinascii.hexlify(b"Hello from badge A!").decode()
>>> ciphertext = crypto.encrypt_message(aes_key, plaintext_hex)

# Decrypt
>>> decrypted_hex = crypto.decrypt_message(aes_key, ciphertext)
>>> ubinascii.unhexlify(decrypted_hex)
b'Hello from badge A!'
```

**Gotcha**: The signature is `encrypt_message(KEY, message)` - key first. Swap them and you get `ValueError: Key must be 16 bytes`. Also, MAC addresses must be plain hex (`"aabbccddeeff"`) without colons.

---

## 12. CactIOT API

### Endpoints

```bash
$ curl https://badge.cactuscon.com/
{"name": "CactIOT Core API", "version": "1.0.0"}

$ curl https://badge.cactuscon.com/health
{"status": "healthy", "database": "connected"}

$ curl https://badge.cactuscon.com/docs
# 403 Forbidden (IP-restricted to convention network)
```

### Device Registration

Registration is a 2-step nonce challenge. The interesting part is that the PIN computation is trivial:

**Step 1** - Request a nonce:
```bash
$ curl -X POST https://badge.cactuscon.com/devices/register \
  -H "Content-Type: application/json" \
  -d '{"id": "<device_mac>", "handle": "<your_handle>"}'

# → {"nonce": "<random_nonce>"}
```

**Step 2** - Compute the PIN and submit:
```python
import hashlib
pin = hashlib.sha1((device_id + nonce).encode()).hexdigest()[:8]
```

```bash
$ curl -X POST https://badge.cactuscon.com/devices/register \
  -H "Content-Type: application/json" \
  -d '{"id": "<device_mac>", "handle": "<your_handle>", "pin": "<pin>", "nonce": "<nonce>"}'

# → {"api_key": "sk_XXXX..."}
```

The PIN uses SHA-1, not SHA-256 (figured that out through trial and error). You can also register completely fake device IDs and get valid API keys back - the API doesn't verify that the MAC address belongs to a real badge.

### Notes
- Registration expects `"id"` not `"device_id"` in the JSON body
- `/docs` returns 403
- `/chat/messages` returns 502 (probably needs an active BLE session)

---

## 13. NeoPixel LED Control

### Hardware

- 6x WS2812B NeoPixels on GPIO 18
- Status LED on GPIO 21
- 6 additional LEDs on GPIOs 13, 14, 15, 16, 17, 46

### Direct Control

```python
>>> from cactuscon.hw.pixels import NeoPixelController, NeoPixel
>>> from machine import Pin
>>> from cactuscon import config as cfg

>>> np = NeoPixel(Pin(cfg.PIN_NEOPIXEL), cfg.NUM_NEOPIXELS)
>>> len(np)
6

# Solid colors
>>> np.fill((255, 0, 0)); np.write()    # Red
>>> np.fill((0, 255, 0)); np.write()    # Green
>>> np.fill((0, 0, 255)); np.write()    # Blue
>>> np.fill((0, 180, 0)); np.write()    # CactusCon Green

# Rainbow
>>> colors = [(255,0,0), (255,127,0), (255,255,0),
...           (0,255,0), (0,0,255), (75,0,130)]
>>> for i, c in enumerate(colors): np[i] = c
>>> np.write()

# Chase animation
>>> for i in range(6):
...     np.fill((0,0,0))
...     np[i] = (128, 0, 255)
...     np.write()
...     time.sleep(0.1)

# Off
>>> np.fill((0,0,0)); np.write()
```

### NeoPixelController

The higher-level controller has some nice built-in effects:

```python
['fade_in', 'fade_out', 'fill', 'off', 'start_rainbow',
 'flash_chat_alert', 'start_blink', 'stop_blink']
```

- `start_rainbow()` - Continuous rainbow cycling
- `flash_chat_alert()` - Quick flash for incoming BLE messages
- `start_blink()` / `stop_blink()` - Blinking pattern
- `fade_in()` / `fade_out()` - Smooth brightness transitions

**Note**: `NeoPixelController(np)` throws `ValueError: invalid pin`. You need to pass the pin number and count directly: `NeoPixelController(cfg.PIN_NEOPIXEL, cfg.NUM_NEOPIXELS)`.

---

## 14. OTA Update System

```
Base URL: http://badge-ota.cactuscon.com/
Protocol: HTTP (no TLS)
Auth:     None
```

The OTA server hands out firmware and config updates without any authentication. The badge checks for updates over WiFi at boot. Since there's no auth, you can `curl` the server and download every `.mpy` file the badge runs.

### Boot Sequence

```python
# boot.py (27,211 bytes):
# 1. Initialize PSRAM
# 2. Configure display (LVGL 9.4.0)
# 3. Connect to "CactusCon" WiFi
# 4. Check OTA server for updates
# 5. Download and apply new .mpy files
# 6. Detect headless mode (no display attached)
# 7. Launch main application
```

The headless mode detection means the badge can operate without a display - it works as a standalone BLE battle/chat node.

---

## 15. Buzzer Mod - Freeing GPIO 19

### The Problem

The badge has an populated buzzer pad on the PCB connected to GPIO 19. The component is a **FUET-9032-3.6V passive magnetic buzzer** with a 2700Hz resonant frequency, driven low-side. But in stock firmware, GPIO 19 is claimed by the ESP32-S3's native USB OTG peripheral (USB D-), so any attempt to use it throws an error:

```python
>>> from machine import Pin, PWM
>>> PWM(Pin(19))
# ValueError: Pin(19) is used by USB
```

GPIO 19 = USB D- and GPIO 20 = USB D+ are hardwired to the ESP32-S3's internal USB controller. Even though the badge uses an external CH340 USB-to-serial chip (on UART0, GPIO 43/44) for all serial communication, the firmware still initializes the native USB peripheral at boot, locking both pins.

### The Fix

The fix is rebuilding the firmware with `--enable-cdc-repl=n`, which inserts the following into `mpconfigport.h`:

```c
#define MICROPY_HW_ENABLE_USBDEV  (0)
#define MICROPY_HW_USB_CDC  (0)
#define MICROPY_HW_ESP_USB_SERIAL_JTAG  (0)
```

This prevents `usb_init()` from being called at boot, freeing GPIO 19 and 20. The UART REPL over the CH340 chip is completely unaffected — that's a separate hardware path.

### Building the Fixed Firmware

The firmware is built from the [CactusCon LVGL MicroPython fork](https://github.com/cactuscon/lvgl_micropython) using Docker:

```dockerfile
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    software-properties-common && \
    add-apt-repository ppa:git-core/ppa -y && \
    apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    git wget curl make gcc g++ flex bison gperf \
    cmake ninja-build ccache libffi-dev libssl-dev \
    dfu-util libusb-1.0-0 \
    python3-serial python3-click python3-cryptography \
    python3-future python3-pyparsing python3-pyelftools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

RUN git clone --depth=1 --recursive --shallow-submodules \
    https://github.com/cactuscon/lvgl_micropython.git /workspace

# Fix ESP-IDF lockfile version mismatch (expects 5.4.2, submodule is 5.4.0)
RUN sed -i 's/version: 5.4.2/version: 5.4.0/' \
    /workspace/lib/micropython/ports/esp32/lockfiles/dependencies.lock.esp32s3

ENTRYPOINT ["python3", "make.py", "esp32", \
    "BOARD=ESP32_GENERIC_S3", "--flash-size=16", \
    "--enable-cdc-repl=n", "--enable-jtag-repl=n", "--enable-uart-repl=y", \
    "DISPLAY=rgb_display", "DISPLAY=st7796", "DISPLAY=st7789", \
    "DISPLAY=st7735", "DISPLAY=ili9488", "DISPLAY=ili9486", \
    "DISPLAY=ili9481", "DISPLAY=ili9341", "DISPLAY=ili9225", \
    "DISPLAY=ili9163", "DISPLAY=gc9a01", \
    "INDEV=xpt2046", "INDEV=gt911", "INDEV=ft6x36", \
    "INDEV=ft6x06", "INDEV=ft5x16", "INDEV=ft5x06", \
    "MICROPY_HW_ESP_NEW_I2C_DRIVER=1"]
```

```bash
# Build the Docker image and run the firmware compilation
docker build -t cc14-buzzer .
docker run --name cc14-build cc14-buzzer

# Extract the built firmware
docker cp cc14-build:/workspace/build/lvgl_micropy_ESP32_GENERIC_S3-16.bin ./firmware_combined.bin
docker cp cc14-build:/workspace/lib/micropython/ports/esp32/build-ESP32_GENERIC_S3/bootloader/bootloader.bin ./bootloader.bin
docker cp cc14-build:/workspace/lib/micropython/ports/esp32/build-ESP32_GENERIC_S3/micropython.bin ./micropython.bin
```

**Critical gotcha**: You MUST use `BOARD=ESP32_GENERIC_S3` with **no** `BOARD_VARIANT`. The badge uses **quad PSRAM** (`quad_psram`). Using `BOARD_VARIANT=SPIRAM_OCT` configures octal PSRAM mode, which causes the badge to hang during boot at "Cleaning up..." because the PSRAM is incorrectly initialized.

### Creating the Full 16MB Image

The Docker build produces only the ~2.8MB firmware (bootloader + partition table + app). To preserve the badge's filesystem (all the game code, sprites, config), you need to merge the new firmware into the original 16MB flash image:

```python
# merge_firmware.py
ORIG = 'lvgl_micropy_ESP32_GENERIC_S3-16MB.bin'  # Original 16MB badge image
BOOT = 'bootloader.bin'                            # Docker-built bootloader
APP  = 'micropython.bin'                           # Docker-built app

with open(ORIG, 'rb') as f:
    merged = bytearray(f.read())

with open(BOOT, 'rb') as f:
    boot = f.read()
merged[0:len(boot)] = boot                        # Replace bootloader

with open(APP, 'rb') as f:
    app = f.read()
APP_START = 0x10000
APP_END = 0x2D0000
merged[APP_START:APP_START + len(app)] = app       # Replace app
merged[APP_START + len(app):APP_END] = b'\xFF' * (APP_END - APP_START - len(app))

with open('cc14_full_16MB_buzzer_fix.bin', 'wb') as f:
    f.write(merged)
```

This preserves:
- Original partition table at `0x8000` (factory app: `0x10000`-`0x2D0000`, ffat: `0x2D0000`-`0x1000000`)
- NVS data at `0x9000` (WiFi creds, game saves, achievements)
- The entire FAT filesystem at `0x2D0000` (all `.mpy` game code, sprites, configs)

### Flashing

```bash
python3 -m esptool --chip esp32s3 -p (PORT) -b 460800 \
    --before default-reset --after hard-reset \
    write-flash --flash-mode dio --flash-size 16MB --flash-freq 80m \
    0x0 cc14_full_16MB_buzzer_fix.bin
```

### Using the Buzzer

With the fixed firmware, GPIO 19 is free for PWM:

```python
from machine import Pin, PWM
import time

buzzer = PWM(Pin(19))
buzzer.freq(2700)        # Resonant frequency - loudest tone
buzzer.duty_u16(32768)   # 50% duty cycle
time.sleep(1)            # Beep for 1 second
buzzer.duty_u16(0)       # Silence
buzzer.deinit()          # Release the pin
```

Play different tones:

```python
# Simple melody
def beep(freq, duration_ms):
    buzzer = PWM(Pin(19))
    buzzer.freq(freq)
    buzzer.duty_u16(32768)
    time.sleep_ms(duration_ms)
    buzzer.duty_u16(0)
    buzzer.deinit()

beep(2700, 200)  # High beep
beep(1800, 200)  # Mid beep
beep(1200, 400)  # Low beep
```

### What Changed in the Binary

The fixed firmware is 384 bytes smaller than the original. Comparing the two:

| Check | Result |
|-------|--------|
| TinyUSB strings removed | 10 references eliminated |
| PSRAM driver | `quad_psram` (matches original) |
| Board config | `ESP32_GENERIC_S3` (matches original) |
| MicroPython version | 1.26.1 (identical) |
| IDF version | 67c1de1e-dirty (identical) |
| LVGL version | 9.4.0 (identical) |
| Filesystem | Byte-identical to original |
| UART REPL | Still works at 115200 via CH340 |

---

## 16. Modding the Badge

### The main.py Trick

All the game logic is compiled `.mpy` bytecode, but `main.py` is plain Python and runs at boot. Replace it and you have a hook into everything before the game engine loads.

```python
# Modded main.py
from cactuscon.game.engine import characters

reg = characters.get_character_registry()
for c in reg.all():
    c.base_stats.level = 99
    c.base_stats.hp = 255
    c.base_stats.max_hp = 255
    c.base_stats.attack = 99
    c.base_stats.defense = 99
```

### NVS Persistence

The badge stores data across **two** NVS namespaces: `"cactuscon"` and `"write"`. If you only write to one, your changes won't survive a reboot.

```python
from cactuscon.prefs import prefs, make_key

for ns in ['cactuscon', 'write']:
    prefs.begin(ns, True, context="mod")
    prefs.set_int32(make_key("cl", "hackachimon"), 99)
    prefs.set_int32(make_key("cx", "hackachimon"), 999999)
    prefs.set_string("ach", ",".join(ALL_ACHIEVEMENTS))
    prefs.end()
```

---

## 17. Easter Eggs & Fun Stuff

**Embedded Splash Screen** - There's a ~570KB JPEG buried in the firmware at `0x40254`. It's the CactusCon boot splash. You can rip it out:
```bash
dd if=firmware.bin of=splash.jpg bs=1 skip=$((0x40254)) count=$((0xCC9C7 - 0x40254))
```

**Leetspeak UUIDs** - Details in [Configuration Secrets](#3-configuration-secrets).

**Creature Names** - All infosec puns:
- Hacktarchu / Hackachu / Hackachimon (hacker + Pikachu)
- Cipherkit / Enigmox / Cryptilox (cryptography)
- Blipbat / Glyphbat / Runewing (signals and encoding)
- Voltiny / Voltqueen / Voltreign (voltage)
- Cinderlet / Cinderserp / Cindervipe (venom/malware)

**Venue Maps** - Four `MAP_VARIANTS` built in, one for each area of the convention.

**CactIOTPad SDK** - The `cactiotpad` module ships with an `examples` submodule containing 9 demo functions showing off the badge's IoT capabilities. Mini SDK for attendees who want to build on the platform.

**Ghost Devices** - The CactIOT API happily registers fake device IDs. The PIN is just `SHA1(device_id + nonce)[:8]` - compute it yourself and register whatever MAC address you want.

---

## 18. Unsolved Mysteries

**The Portability Key** - Whatever string SHA-1 hashes to `f598682777ca9c75daa4b1b2a978d44ae9752035` remains unknown. Bypassed via monkey-patching, but the real key is still out there.

**`create_turn_seed` Arguments** - This function takes 4 arguments but nothing works:
- Strings: `'str' object has no attribute 'ljust'`
- Bytes: `'bytes' object has no attribute 'ljust'`
- Bytearrays: `'bytearray' object has no attribute 'ljust'`
- Integers: `object of type 'int' has no len()`

MicroPython doesn't implement `.ljust()` on standard types. The function probably only works through internal code paths in the compiled battle manager.

**NeoPixelController Init** - `NeoPixelController(np)` and `NeoPixelController(np, Pin(21))` both throw `ValueError: invalid pin`. Passing raw pin number and count works but the effects may need additional setup.

**`execute_action` Integration** - Direct calls to `rules.execute_action()` fail because the battle manager sets up internal context that isn't exposed. The full battle flow runs through a higher-level orchestrator.

---

## Methodology

1. **Static analysis** - `hexdump`, `strings`, `binwalk` on the 8MB binary
2. **Filesystem extraction** - FAT12 at `0x2D0000` via `dd`
3. **Runtime exploration** - Serial REPL at 115200 baud (CH340 USB-serial)
4. **Bytecode analysis** - String constants and signatures from `.mpy` files
5. **Monkey-patching** - Runtime bypass of security checks via Python's dynamic nature
6. **API probing** - `curl` against `badge.cactuscon.com`
7. **LED control** - NeoPixel manipulation for visual confirmation

### Connecting to Your Badge

```bash
# Find the serial port
# macOS:
ls /dev/cu.usbserial-*
# Linux:
ls /dev/ttyUSB*

# Connect
screen /dev/cu.usbserial-XX 115200

# Or with Python
import serial
ser = serial.Serial('<port>', 115200, timeout=2)
ser.write(b'\x03\x03')  # Ctrl+C to get REPL
```

---

*CactusCon 14 - February 2026*
