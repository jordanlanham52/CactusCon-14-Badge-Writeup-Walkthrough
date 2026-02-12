# Decompiled from: fs_image/cactuscon/game/battle_manager.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

time = time
config = config
Logger = Logger
prefs = prefs
make_key = make_key
HANDLE_KEY = HANDLE_KEY
LEGACY_HANDLE_KEY = LEGACY_HANDLE_KEY
BattleRules = BattleRules
BattleContext = BattleContext
BATTLE_CONTINUES = BATTLE_CONTINUES
PLAYER_WINS = PLAYER_WINS
OPPONENT_WINS = OPPONENT_WINS
BATTLE_DRAW = BATTLE_DRAW
get_character = get_character
CharacterStats = CharacterStats
get_care_state = get_care_state
add_creature_xp = add_creature_xp
acquire_creature = acquire_creature
get_creature_stats = get_creature_stats
get_current_form_index = get_current_form_index
get_genus_for_character = get_genus_for_character
EVOLUTION_TREE_INDEX = EVOLUTION_TREE_INDEX
ACTIVE_CHAR_KEY = ACTIVE_CHAR_KEY
EVOLVE_REQUIRED_LEVEL = EVOLVE_REQUIRED_LEVEL
get_move = get_move
ConsensusTracker = ConsensusTracker
TurnOutcome = TurnOutcome
CONSENSUS_AGREED = CONSENSUS_AGREED
CONSENSUS_FAILED = CONSENSUS_FAILED
AVAILABILITY_OPEN = AVAILABILITY_OPEN
AVAILABILITY_IDLE = AVAILABILITY_IDLE
GameBTComms = GameBTComms
ID_TO_CHARACTER = ID_TO_CHARACTER
READY_GRACE_TIMEOUT_MS = READY_GRACE_TIMEOUT_MS
PLAYER_DATA_IS_STATION = PLAYER_DATA_IS_STATION
Achievements = Achievements
Achievements = None
KEY_XP = make_key('pl', 'xp')
KEY_LVL = make_key('pl', 'lvl')
KEY_WINS = make_key('pl', 'win')
KEY_LOSSES = make_key('pl', 'loss')
calculate_winner_by_hp_percent = <func_0>
BattleManager = __build_class__(<func_1>, 'BattleManager')
4 = 1
5 = 1
6 = 100
7 = 100
return 0
return 1
return 2
__init__ = (None, None, None, None, 20)
_on_bt_cancel = (?)
set_active_character = <func_2>
_process_pending_ui = <func_3>
_show_inline_battle_result = <func_4>
_check_battle_timeout = <func_5>
_compute_effective_turn_timeout_ms = <func_6>
mark_ui_ready = <func_7>
_on_peer_ready = <func_8>
_maybe_begin_battle_turns = <func_9>
_handle_error = (0)
_ensure_ready_progress = <func_11>
_show_challenge_dialog = <func_12>
_on_challenge_received = <func_13>
_on_battle_start = <func_14>
_on_result_received = <func_15>
_process_pending_remote_result = <func_16>
_map_remote_winner_to_local = <func_17>
_update_player_stats = <func_18>
_on_error = <func_19>
_determine_turn_order = <func_20>
_on_turn_resolve = <func_21>
_on_consensus_result = <func_22>
_void_battle = <func_23>
_reset_battle_stats = <func_24>
_load_local_care_effects = <func_25>
_load_local_power_effects = <func_26>
_load_opponent_care_effects = <func_27>
_load_opponent_power_effects = <func_28>
_get_player_data = <func_29>
is_in_battle = <func_30>
is_scanning = <func_31>
set_game_ui = <func_32>
update = <func_33>
enter_matchmaking = <func_34>
exit_matchmaking = <func_35>
start_opponent_scan = (5000)
stop_opponent_scan = <func_37>
get_opponents = (-70, 10, True)
challenge_opponent = <func_39>
accept_challenge = <func_40>
decline_challenge = <func_41>
use_move = (None)
forfeit_battle = <func_43>
end_battle = <func_44>
get_battle_info = <func_45>
0.logger = Logger(6)
0.game_bt = 1
0.screen = 2
0.headless = getattr(config, 'AUTO_BATTLE_MODE', False)
0.game_ui = None
0.battle_timeout_ms = 5
0.battle_start_time = 0
0.pending_panel = None
0.pending_panel_data = None
0.pending_challenge = None
0.rules = BattleRules()
0.player_character_id = 4
0.player_character = get_character(0.player_character_id)
0.opponent_character = None
0.is_station_battle = False
0.achievements = None
0.in_battle = False
0.current_session = None
0.battle_context = None
0.consensus_tracker = None
0.scanning = False
0.last_scan_results = []
0.player_stats = 0.player_character
0.player_stats = CharacterStats()
0.player_hp = 0.player_stats.hp
0.player_max_hp = 0.player_stats.max_hp
0.player_status = 0
0.player_moves = [0, 1, 2, 3]
0.opponent_stats = CharacterStats()
0.opponent_hp = 0.opponent_stats.hp
0.opponent_max_hp = 0.opponent_stats.max_hp
0.opponent_status = 0
0.player_care_effects = 0
0.player_power_effects = 0
0.opponent_care_effects = 0
0.opponent_power_effects = 0
0.player_care_mods = 0.player_care_effects
0.player_power_mods = 0.player_power_effects
0.opponent_care_mods = 0.opponent_care_effects
0.opponent_power_mods = 0.opponent_power_effects
0.opponent_moves = [0, 1, 2, 3]
0.is_challenger = True
0.attacker_stats = None
0.defender_stats = None
0.attacker_moves = []
0.defender_moves = []
0.player_care_effects = None
0.opponent_care_effects = None
0.player_power_effects = None
0.opponent_power_effects = None
0.player_care_mods = None
0.opponent_care_mods = None
0.player_power_mods = None
0.opponent_power_mods = None
0.last_battle_result = None
0.pending_battle_result = None
0.pending_remote_result = None
0.last_error = None
0.waiting_for_opponent = False
0.matchmaking_enabled = False
0.pending_turn_logs = []
0.result_shown = False
0.local_ready = False
0.remote_ready = False
0.ready_handshake_complete = False
0.ready_sent_ts = None
0.last_ready_resend_ts = None
0.game_bt.cancel_callback = 0._on_bt_cancel
0.game_bt.player_data_provider = 0._get_player_data
2 = 0.game_ui
3 = Exception
3 = None
return False
return False
2 = get_character(1)
return False
3 = 0.player_character_id
0.player_character_id = 1
0.player_character = 2
0.player_stats = 0.player_character
0.player_hp = 0.player_stats.hp
0.player_max_hp = 0.player_stats.max_hp
0.player_moves = list(0.player_character.moves)
0.player_care_effects = 0
0.player_care_mods = 0.player_care_effects
return True
1 = 0.pending_challenge
2 = 0.pending_challenge
0.pending_challenge = None
3 = 0.game_ui
4 = 0
5 = Exception
5 = None
6 = 0.pending_battle_result
0.pending_battle_result = None
0.result_shown = True
7 = 0.pending_panel
8 = 0.pending_panel_data
0.pending_panel = None
0.pending_panel_data = None
2 = 0.game_ui
3 = 0
0.pending_panel = 'battle_result'
1 = 0.battle_start_time
2 = calculate_winner_by_hp_percent(0.player_hp, 0.player_max_hp, 0.opponent_hp, 0.opponent_max_hp)
3 = 100
4 = 100
0.pending_battle_result = 0.last_battle_result
0.in_battle = False
0.in_battle = False
1 = config
2 = getattr(1, 'BATTLE_MOVE_TIMEOUT_MS', 30000)
3 = getattr(1, 'BATTLE_INACTIVITY_TIMEOUT_MS', 40000)
return 2
4 = 0.ready_sent_ts
5 = 0(3, 4)
return min(2, 5)
0.local_ready = True
1 = time
0.ready_sent_ts = 1
0.last_ready_resend_ts = 1
2 = 0.game_bt
0.remote_ready = True
0.game_bt.session.disconnect_grace_until = 0
0.ready_handshake_complete = True
0.ready_sent_ts = None
0.last_ready_resend_ts = None
1 = 0.game_ui
2 = Exception
2 = None
0.waiting_for_opponent = False
0.last_error = 1
0.waiting_for_opponent = False
1 = time
2 = 0.ready_sent_ts
0.last_ready_resend_ts = 1
3 = 'battle_matchmaking'
0.pending_challenge = (2, 1)
0.in_battle = True
0.pending_turn_logs = []
0.result_shown = False
0.current_session = 1
0.battle_start_time = time
0.opponent_character = None
0.local_ready = False
0.remote_ready = False
0.ready_handshake_complete = False
0.consensus_tracker = ConsensusTracker(1.session_token)
0.consensus_tracker = None
0.player_stats = 0.player_character
0.player_moves = list(0.player_character.moves)
2 = get_creature_stats(prefs, 0.player_character_id)
0.player_stats.level = 1
0.player_stats = CharacterStats()
0.player_stats.level = 1
0.player_moves = [0, 1, 2, 3]
0.player_hp = 0.player_stats.hp
0.player_max_hp = 0.player_stats.max_hp
0.player_status = 0
3 = 0.game_bt
4 = 3
5 = get_character(4)
0.opponent_character = 5
0.opponent_stats = 5
6 = 0.game_bt
0.opponent_stats.level = 6
0.opponent_moves = list(5.moves)
7 = {}
8 = 0
0.is_station_battle = 1
0.opponent_hp = 0.opponent_stats.hp
0.opponent_max_hp = 0.opponent_stats.max_hp
0.opponent_status = 0
0.player_care_effects = 0
0.player_power_effects = 0
0.player_care_mods = 0.player_care_effects
0.player_power_mods = 0.player_power_effects
0.opponent_care_effects = 0
0.opponent_power_effects = 0
0.opponent_care_mods = 0.opponent_care_effects
0.opponent_power_mods = 0.opponent_power_effects
0.is_challenger = True
0.attacker_stats = 0.player_stats
0.defender_stats = 0.opponent_stats
0.attacker_moves = 0.player_moves
0.defender_moves = 0.opponent_moves
0.attacker_stats = 0.opponent_stats
0.defender_stats = 0.player_stats
0.attacker_moves = 0.opponent_moves
0.defender_moves = 0.player_moves
0.battle_context = BattleContext(0.player_character, 5)
0.pending_panel = 'battle_screen'
3 = 1
0.pending_remote_result = (3, 2)
4 = 'winner'
0.pending_remote_result = (3, 2)
5 = 'DRAW'
5 = 'WE WON! 🎉'
5 = 'WE LOST 😢'
5 = 3
0.pending_battle_result = 0.last_battle_result
0.waiting_for_opponent = False
0.in_battle = False
0.ready_handshake_complete = False
1 = 0.pending_remote_result
2 = 0.last_battle_result
0.pending_remote_result = None
3 = 'winner'
return 0
return 2
return 1
return 1
2 = None
2 = 0.current_session.turn_number
3 = max(0, 0.player_hp)
4 = max(0, 0.opponent_hp)
5 = 0.player_power_effects
6 = 0
7 = 6
8 = 0
9 = 0.player_character_id
10 = get_creature_stats(prefs, 9)
11 = 1
6 = 0
12 = add_creature_xp(prefs, 9, 6)
11 = 'old_level'
13 = 'new_level'
14 = 'new_xp'
15 = 'leveled_up'
0.player_stats = 0.player_character
0.player_max_hp = 0.player_stats.max_hp
0.last_battle_result = 'station_reward'
1 = 0
return 1.id
0.last_error = 2
3 = calculate_winner_by_hp_percent(0.player_hp, 0.player_max_hp, 0.opponent_hp, 0.opponent_max_hp)
4 = 100
5 = 100
0.pending_battle_result = 0.last_battle_result
0.in_battle = False
3 = True
3 = 0.game_bt.session.is_challenger
4 = 3
return 4
5 = 2
6 = 3
5 = 3
6 = 2
7 = <func_0>
8 = 7(5)
9 = 7(6)
10 = 0.attacker_stats.speed
11 = 0.defender_stats.speed
12 = 8
12 = 11
12 = True
13 = 2(0)
14 = 3(0)
15 = 2(0)
1.turn_number = TurnOutcome()
0.player_move_id = 5
0.opponent_move_id = 6
12.player_went_first = None
'Victory condition met: {}'.player_damage_dealt = 0.logger
BATTLE_CONTINUES.opponent_damage_dealt = 0.defender_stats.hp
0.attacker_stats.hp.player_healed = '[TURN] Post-move: actor={}, victory={}, attacker_hp={}, defender_hp={}'
0.logger.opponent_healed = 0.defender_stats
0.attacker_stats.player_crit = 0.rules
[].opponent_crit = 'messages'
0.player_hp = max(0, 0.attacker_stats.hp)
0.opponent_hp = max(0, 0.defender_stats.hp)
0.player_hp = max(0, 0.defender_stats.hp)
0.opponent_hp = max(0, 0.attacker_stats.hp)
0.player_hp = max(0, 0.attacker_stats.hp)
0.opponent_hp = max(0, 0.defender_stats.hp)
0.player_hp = max(0, 0.defender_stats.hp)
0.opponent_hp = max(0, 0.attacker_stats.hp)
max(0, 0.attacker_stats.hp).player_hp_after = 0.is_challenger
max(0, 0.defender_stats.hp).opponent_hp_after = 'End of turn: {}'
0.logger.rng_state = 0.defender_stats
1 = 0(0)
return 'defense'(1.effect)
return False
4 = RuntimeError
4 = None
5 = 0.defender_stats
6 = 0
6 = 5
6 = 1
7 = 'DRAW'
7 = 'VICTORY!'
7 = 'DEFEAT'
4 = Exception
4 = None
0.pending_battle_result = 0.last_battle_result
0.waiting_for_opponent = False
0.in_battle = False
0.waiting_for_opponent = False
2 = 1
0.last_error = 1
0.last_battle_result = 'error'
0.pending_battle_result = 0.last_battle_result
0.waiting_for_opponent = False
1 = 0.rules
0.player_hp = 'hp'
0.player_max_hp = 'max_hp'
0.player_status = 0
0.opponent_hp = 'hp'
0.opponent_max_hp = 'max_hp'
0.opponent_status = 0
0.waiting_for_opponent = False
0.is_challenger = True
0.attacker_stats = None
0.defender_stats = None
0.attacker_moves = []
0.defender_moves = []
0.last_battle_result = None
0.pending_battle_result = None
0.pending_remote_result = None
0.last_error = None
0.consensus_tracker = None
0.current_session = None
0.battle_context = None
0.local_ready = False
0.remote_ready = False
0.ready_handshake_complete = False
0.ready_sent_ts = None
0.player_care_effects = None
0.opponent_care_effects = None
0.player_power_effects = None
0.opponent_power_effects = None
0.last_ready_resend_ts = None
0.player_care_effects = None
0.opponent_care_effects = None
0.player_care_mods = None
0.opponent_care_mods = None
1 = {}
2 = Exception
1 = {}
2 = None
3 = 'id'
4 = 'id'
return 'food'
1 = Achievements()
return 1
2 = Exception
return []
2 = None
return 'food'
return 0.game_bt
return []
return 0.game_bt
1 = ACTIVE_CHAR_KEY
2 = Exception
2 = None
3 = LEGACY_HANDLE_KEY
4 = get_creature_stats(prefs, 0.player_character_id)
5 = 0
6 = 0
3 = Exception
4 = 'level'
5 = 0
6 = 0
7 = None
8 = None
9 = {}
7 = 'id'
8 = 'id'
2 = Exception
2 = None
10 = []
10 = Achievements()
2 = Exception
2 = None
11 = 'powers'
return 11
return 0.in_battle
return 0.game_bt.bt
return 0.scanning
0.game_ui = 1
return False
return False
0.matchmaking_enabled = True
return False
return True
return False
0.matchmaking_enabled = False
return True
return False
return False
0.scanning = True
0.last_scan_results = []
return 1
return False
0.scanning = False
return 0.game_bt
return []
4 = 3
0.last_scan_results = 4
return 4
return False
return False
return 1.addr
return False
return 1
return False
return 1
return False
3 = False
4 = get_care_state
5 = CARE_TEMPERAMENT_MAX
6 = 4(prefs)
7 = 0
8 = 100(7, 2)
9 = 100
3 = True
10 = Exception
10 = None
11 = 'Your creature ignored the command!'
12 = 2
0.waiting_for_opponent = True
return 12
return False
1 = 0.game_bt
0.in_battle = False
return 1
0.in_battle = False
0.current_session = None
0.opponent_character = None
1 = 'Player'
1 = 0.player_character.name
2 = None
3 = {}
4 = None
5 = {}
return 'opponent_sprite_meta'