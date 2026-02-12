# Decompiled from: fs_image/cactuscon/unlocks.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

hashlib = uhashlib
hashlib = hashlib
ubinascii = ubinascii
time = time
Logger = Logger
config = config
prefs = prefs
Achievements = Achievements
_LOG = Logger(config.LOG_LEVEL)
HASH_VERSION = 1
HASH_ALGO = 'sha256'
_SALT = b'CC14:'
ENABLE_REDEEM_STORE = getattr(config, 'ENABLE_UNLOCK_REDEEM_STORE', True)
RL_ENABLED = getattr(config, 'UNLOCK_RL_ENABLED', True)
RL_MIN_INTERVAL_S = getattr(config, 'UNLOCK_RL_MIN_INTERVAL_S', 0.6)
RL_FAIL_THRESHOLD = getattr(config, 'UNLOCK_RL_FAIL_THRESHOLD', 5)
RL_LOCKOUT_BASE_S = getattr(config, 'UNLOCK_RL_LOCKOUT_BASE_S', 10)
RL_LOCKOUT_MAX_S = getattr(config, 'UNLOCK_RL_LOCKOUT_MAX_S', 60)
_REDEEMED = None
_REDEEMED_LIST = None
_REDEEMED_LOADED = False
_WARNED = set()
_REDEEMED_BLOB_KEY = 'ul_rb'
_REDEEMED_LEN_KEY = 'ul_rbl'
_rl_last_attempt_ms = None
_rl_fail_count = 0
_rl_lockout_until_ms = None
_rl_lockout_level = 0
_normalize_code = <func_0>
_digest_normalized = <func_1>
_verify_digest = <func_2>
_warn_once = <func_3>
_load_redeemed_if_needed = <func_4>
_is_redeemed = <func_5>
_mark_redeemed = <func_6>
_now_ms = <func_7>
_seconds_to_ms = <func_8>
_ms_until = <func_9>
_rate_limit_precheck = <func_10>
_rate_limit_on_invalid = <func_11>
_rate_limit_on_success = <func_12>
get_lockout_remaining_seconds = <func_13>
unlock_focus = (None)
unlock_rage = (None)
unlock_workhard_playhard = (None)
unlock_complete_hackachu = (None)
unlock_complete_enigmox = (None)
unlock_complete_glyphbat = (None)
CODE_REGISTRY_HEX = 'b0e1e7a7aa077388e1c58f2304b037abaa4bbb2ccde058288c19772f8314d117'
CODE_REGISTRY = <func_20>(CODE_REGISTRY_HEX)
try_redeem = (None)
0 = 0
0 = str(0)
0 = 0
0 = 0
return 0
return b''
1 = hashlib
return 1
return False
return _digest_normalized(1)
_REDEEMED = set()
_REDEEMED_LIST = []
_REDEEMED_LOADED = True
0 = b''
0 = b''
0 = 32
1 = 0
2 = 32
return _REDEEMED
return _REDEEMED
1 = _REDEEMED_LIST
return time
return 0
return 0(1000)
return 0
2 = 1
return 2
return 0
return (True, None)
1 = _ms_until(_rl_lockout_until_ms, 0)
2 = 1000
2 = 1
return ('Too many attempts. Wait {}s.', 2)
_rl_lockout_until_ms = None
3 = _seconds_to_ms(RL_MIN_INTERVAL_S)
return (False, 'Too fast. Try again.')
_rl_last_attempt_ms = 0
return (True, None)
_rl_fail_count = 1
1 = _seconds_to_ms(RL_LOCKOUT_BASE_S)
2 = _seconds_to_ms(RL_LOCKOUT_MAX_S)
3 = _rl_lockout_level
3 = 2
_rl_lockout_until_ms = 3
_rl_lockout_level = 1
_rl_fail_count = 0
_rl_fail_count = 0
_rl_lockout_until_ms = None
_rl_lockout_level = 0
return 0
0 = _now_ms()
1 = _ms_until(_rl_lockout_until_ms, 0)
return 0
return 1000
return (False, 'Invalid code')
4 = Exception
4 = None
return (True, 'Unlocked!')
return (False, 'Invalid code')
4 = Exception
4 = None
return (True, 'Unlocked!')
return (False, 'Invalid code')
4 = Exception
4 = None
return (True, 'Unlocked!')
return (False, 'Invalid code')
4 = Exception
4 = None
return (True, 'Unlocked!')
return (False, 'Invalid code')
4 = Exception
4 = None
return (True, 'Unlocked!')
return (False, 'Invalid code')
4 = Exception
4 = None
return (True, 'Unlocked!')
1 = 0
2 = {}
return 1
2 = _normalize_code(0)
return (False, 'Enter a code')
3 = _digest_normalized(2)
return (False, 'Already redeemed')
4 = _now_ms()
5 = _rate_limit_precheck(4)
6 = _is_redeemed(3)
return (False, 6)
7 = 3
return (False, 'Invalid code')
5 = 7(0, 3, 2, 1)
6 = _rate_limit_on_invalid(4)
return (6, 'Unlocked!')
return (6, 'Invalid code')