# Decompiled from: fs_image/cactuscon/game/auto_battle.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

time = time
struct = struct
urandom = urandom
const = const
GameBTComms = GameBTComms
BattleSession = BattleSession
AVAILABILITY_OPEN = AVAILABILITY_OPEN
AVAILABILITY_IDLE = AVAILABILITY_IDLE
AVAILABILITY_IN_BATTLE = AVAILABILITY_IN_BATTLE
MSG_BATTLE_STATUS = MSG_BATTLE_STATUS
MSG_BATTLE_RESULT = MSG_BATTLE_RESULT
SESSION_BATTLING = SESSION_BATTLING
SESSION_COMPLETE = SESSION_COMPLETE
PROTOCOL_VERSION = PROTOCOL_VERSION
MOVE_TIMEOUT_MS = MOVE_TIMEOUT_MS
Logger = Logger
BattleRules = BattleRules
get_move = get_move
MOVE_CAT_DAMAGE = MOVE_CAT_DAMAGE
MOVE_CAT_HEAVY = MOVE_CAT_HEAVY
MOVE_CAT_SUPPORT = MOVE_CAT_SUPPORT
MOVE_CAT_RECOVERY = MOVE_CAT_RECOVERY
get_station = get_station
DIFFICULTY_EASY = DIFFICULTY_EASY
DIFFICULTY_MEDIUM = DIFFICULTY_MEDIUM
DIFFICULTY_HARD = DIFFICULTY_HARD
CharacterStats = CharacterStats
prefs = prefs
make_key = make_key
AUTO_BATTLE_IDLE = 0
AUTO_BATTLE_CHALLENGE_PENDING = 1
AUTO_BATTLE_ACTIVE = 2
AUTO_BATTLE_TIMEOUT = 3
DEFAULT_AUTO_BATTLE_DURATION_MS = 10000
DEFAULT_AUTO_BATTLE_HP = 100
DEFAULT_AUTO_BATTLE_MOVE_INTERVAL_MS = 2000
KEY_STATION_WINS = make_key('st', 'win')
KEY_STATION_LOSSES = make_key('st', 'loss')
KEY_STATION_CHALLENGES = make_key('st', 'ch')
calculate_winner_by_hp_percent = <func_0>
AutoBattleComms = __build_class__(<func_1>, 'AutoBattleComms', GameBTComms)
4 = 1
5 = 1
6 = 100
7 = 100
return 0
return 1
return 2
__init__ = 0
_get_player_data = <func_1>
start_auto_battle_mode = (None, None)
stop_auto_battle_mode = <func_3>
get_auto_battle_stats = <func_4>
_sync_wins_losses_from_prefs = <func_5>
_persist_stats_to_prefs = <func_6>
_clear_pending_callbacks = <func_7>
_reset_battle_state = <func_8>
update = 0
_select_ai_move = <func_10>
set_difficulty = <func_11>
_handle_challenge_request = <func_12>
_handle_challenge_accept = 0
_handle_battle_status = 0
_handle_battle_result = 0
_handle_disconnect = 0
_handle_error = 0
return 0
1.rules = BattleRules()
1.station_id = 6
1.station = None
1.character_moves = [0, 1, 2, 3]
1.station = get_station(6)
5 = 1.station.difficulty
1.character_moves = 1.station
1.auto_battle_duration_ms = 4
1.auto_battle_mode_enabled = False
1.difficulty = 5
1.our_stats = 1.station
1.our_hp = 1.our_stats.hp
1.our_max_hp = 1.our_stats.max_hp
1.our_stats = CharacterStats()
1.our_hp = 100
1.our_max_hp = 100
1.opponent_stats = CharacterStats()
1.opponent_hp = 100
1.opponent_max_hp = 100
1.auto_battle_state = 0
1.battle_start_time = 0
1.last_move_time = 0
8 = 0
9 = 0
10 = 0
11 = Exception
8 = 0
9 = 0
10 = 0
11 = None
1.stats = 'losses'
1.player_data_provider = 1._get_player_data
1 = 'deeno'
1 = 0.station.character_id
return 'is_station'
0.auto_battle_duration_ms = 1
0.difficulty = 2
return False
0.auto_battle_mode_enabled = True
0.auto_battle_state = 0
0.our_hp = 0.our_stats.hp
0.our_max_hp = 0.our_stats.max_hp
0.our_hp = 100
0.our_max_hp = 100
0.opponent_hp = 100
0.opponent_max_hp = 100
3 = ['EASY', 'MEDIUM', 'HARD']
4 = 'UNKNOWN'
return True
0.auto_battle_mode_enabled = False
1 = 'duration_ms'
return 1
1 = KEY_WINS
2 = KEY_LOSSES
3 = 0
4 = 0
5 = Exception
5 = None
1 = Exception
1 = None
0.pending_turn_resolve = None
0.pending_challenges = {}
0.our_stats = 0.station
0.our_hp = 0.our_stats.hp
0.our_max_hp = 0.our_stats.max_hp
0.our_stats = CharacterStats()
0.our_hp = 100
0.our_max_hp = 100
0.opponent_stats = CharacterStats()
0.opponent_hp = 100
0.opponent_max_hp = 100
0.battle_start_time = 0
0.last_move_time = 0
2 = time
1.battle_start_time = 2
1.last_move_time = 2
1.auto_battle_state = 2
1.auto_battle_state = 3
1.auto_battle_state = 3
1.auto_battle_state = 3
3 = 1
1.last_move_time = 2
1.auto_battle_state = 3
1.auto_battle_state = 0
1 = [0, 1, 2, 3]
2 = DIFFICULTY_HARD
3 = 0.4
return 1
4 = getattr(0, 'our_max_hp', 100)
5 = 4
6 = 100
7 = []
8 = []
9 = []
10 = []
11 = 1
12 = get_move(11)
13 = 12.category
return 7
14 = 9
return 14
return 9
return 7
return 8
return 1
0.difficulty = 1
2 = ['EASY', 'MEDIUM', 'HARD']
3 = 'UNKNOWN'
2 = 1
3 = 1
4 = 'Unknown'
4 = 'utf-8'
5 = 0.bt
6 = 'addr'
0.auto_battle_state = 1
3 = 0
1.opponent_max_hp = 3
1.opponent_hp = 3
1.auto_battle_state = 3
1.auto_battle_state = 0
1.auto_battle_state = 0