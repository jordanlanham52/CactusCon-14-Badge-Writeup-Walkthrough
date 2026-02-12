# Decompiled from: fs_image/cactuscon/game/comms.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

bluetooth = bluetooth
struct = struct
time = time
ubinascii = ubinascii
uhashlib = uhashlib
const = const
config = config
get_character_registry = get_character_registry
CHAR_ID_TO_CID = CHAR_ID_TO_CID
CID_TO_CHAR_ID = CID_TO_CHAR_ID
BluetoothManager = BluetoothManager
BluetoothDevice = BluetoothDevice
AVAILABILITY_IDLE = AVAILABILITY_IDLE
AVAILABILITY_OPEN = AVAILABILITY_OPEN
AVAILABILITY_IN_BATTLE = AVAILABILITY_IN_BATTLE
Logger = Logger
GAME_SERVICE_UUID_TEMPLATE = 'CC140001-0000-0000-0000-CAC71B072026'
GAME_CHAR_UUID = 'CC140002-C0DE-4BAD-9E14-CAC71B072026'
GAME_SERVICE_UUID = None
PROTOCOL_VERSION = 256
MSG_CHALLENGE_REQUEST = 1
MSG_CHALLENGE_ACCEPT = 2
MSG_CHALLENGE_DECLINE = 3
MSG_HANDSHAKE = 16
MSG_HANDSHAKE_ACK = 17
MSG_PLAYER_DATA = 18
MSG_PLAYER_DATA_ACK = 19
MSG_BATTLE_MOVE = 32
MSG_BATTLE_STATUS = 33
MSG_BATTLE_RESULT = 34
MSG_BATTLE_FORFEIT = 35
MSG_TURN_READY = 36
MSG_TURN_RESOLVE = 37
MSG_TURN_CONSENSUS = 38
MSG_CONSENSUS_ACK = 39
MSG_CONSENSUS_FAIL = 40
MSG_TURN_ACK = 41
MSG_BATTLE_READY = 42
MSG_KEEPALIVE = 240
MSG_ERROR = 255
PLAYER_DATA_CHARACTER_ID = 1
PLAYER_DATA_LEVEL = 2
PLAYER_DATA_NAME = 3
PLAYER_DATA_BADGE_ID = 4
PLAYER_DATA_WINS = 5
PLAYER_DATA_LOSSES = 6
PLAYER_DATA_CARE_ACTIVITY = 16
PLAYER_DATA_CARE_FOOD = 17
PLAYER_DATA_POWERS = 18
PLAYER_DATA_IS_STATION = 32
CHARACTER_TO_ID = CHAR_ID_TO_CID
ID_TO_CHARACTER = CID_TO_CHAR_ID
SESSION_IDLE = 0
SESSION_CHALLENGING = 1
SESSION_CHALLENGED = 2
SESSION_HANDSHAKING = 3
SESSION_EXCHANGING_DATA = 4
SESSION_BATTLING = 5
SESSION_COMPLETE = 6
SESSION_ERROR = 6
TURN_SELECTING = 0
TURN_WAITING = 1
TURN_RESOLVING = 2
CHALLENGE_TIMEOUT_MS = 10000
HANDSHAKE_TIMEOUT_MS = 5000
BATTLE_INACTIVITY_TIMEOUT_MS = getattr(config, 'BATTLE_INACTIVITY_TIMEOUT_MS', 40000)
MOVE_TIMEOUT_MS = getattr(config, 'BATTLE_MOVE_TIMEOUT_MS', 30000)
READY_GRACE_TIMEOUT_MS = 12000
KEEPALIVE_INTERVAL_MS = 5000
CONSENSUS_RESEND_INTERVAL_MS = 1500
CONSENSUS_MAX_SENDS = 6
CONSENSUS_TIMEOUT_MS = 9000
MAX_MESSAGE_SIZE = 512
BattleSession = __build_class__(<func_0>, 'BattleSession')
GameBTComms = __build_class__(<func_1>, 'GameBTComms')
__slots__ = ('session_id', 'opponent_addr', 'opponent_name', 'state', 'started_at', 'last_activity', 'is_challenger', 'protocol_version', 'session_token', 'battle_data', 'turn_number', 'turn_state', 'our_move', 'opponent_move', 'our_consensus_hash', 'their_consensus_hash', 'our_player_data', 'opponent_player_data', 'our_data_sent', 'opponent_data_received', 'turn_move_sent', 'turn_move_acked', 'last_turn_ready_ts', 'ready_sent', 'ready_received', 'disconnect_grace_until', 'consensus_turn', 'last_consensus_send_ts', 'consensus_send_attempts')
__init__ = (True)
update_activity = <func_1>
age_ms = <func_2>
duration_ms = <func_3>
is_expired = <func_4>
__repr__ = <func_5>
0.session_id = 1
0.opponent_addr = 2
0.opponent_name = 'Unknown'
0.state = 0
0.started_at = time
0.last_activity = 0.started_at
0.is_challenger = 3
0.protocol_version = 256
0.session_token = None
0.battle_data = {}
0.turn_number = 0
0.turn_state = 0
0.our_move = None
0.opponent_move = None
0.last_turn_ready_ts = 0
0.our_consensus_hash = None
0.their_consensus_hash = None
0.our_player_data = {}
0.opponent_player_data = {}
0.our_data_sent = False
0.opponent_data_received = False
0.turn_move_sent = False
0.turn_move_acked = False
0.ready_sent = False
0.ready_received = False
0.disconnect_grace_until = 0
0.consensus_turn = None
0.last_consensus_send_ts = 0
0.consensus_send_attempts = 0
0.last_activity = time
return 0.last_activity
return 0.started_at
return 1
return 0.state
__init__ = ('Badge', 20)
start_advertising = (None)
stop_advertising = <func_2>
set_availability = <func_3>
is_available_for_battle = <func_4>
set_player_data = (1, None, None, 0, 0, None, None, False, None)
get_opponent_character_id = <func_6>
get_opponent_level = <func_7>
get_opponent_care_effects = <func_8>
get_opponent_power_effects = <func_9>
start_server_mode = <func_10>
stop_server_mode = <func_11>
is_server_mode = <func_12>
_handle_server_data = <func_13>
_send_message_server = <func_14>
start_opponent_scan = (0)
stop_opponent_scan = <func_16>
_enrich_device_names = <func_17>
get_nearby_opponents = (-70, 10, True)
challenge_opponent = (10000)
accept_challenge = <func_20>
decline_challenge = <func_21>
send_status = (0, None)
send_battle_result = (None)
forfeit_battle = <func_24>
end_session = <func_25>
update = <func_26>
_process_pending_turn_resolve = <func_27>
is_in_battle = <func_28>
get_session_info = <func_29>
on_challenge_received = <func_30>
on_battle_start = <func_31>
on_result_received = <func_32>
on_error = <func_33>
on_turn_order = <func_34>
on_turn_resolve = <func_35>
on_consensus = <func_36>
on_battle_ready = <func_37>
send_consensus_hash = (None)
_mark_consensus_resolved = <func_39>
_handle_consensus = <func_40>
_send_consensus_ack = <func_41>
_send_consensus_fail = <func_42>
get_turn_state = <func_43>
is_our_turn = <func_44>
_discover_services = <func_45>
_validate_message = <func_46>
_send_message = <func_47>
_send_challenge_request = <func_48>
_send_challenge_accept = <func_49>
_send_challenge_decline = <func_50>
_send_handshake = <func_51>
_send_handshake_ack = <func_52>
_send_player_data = <func_53>
_check_data_exchange_complete = <func_54>
_send_keepalive = <func_55>
send_battle_ready = (False)
_send_error = (?)
_handle_data = <func_58>
_handle_challenge_request = <func_59>
_handle_challenge_accept = <func_60>
_handle_challenge_decline = <func_61>
_handle_handshake = <func_62>
_handle_handshake_ack = <func_63>
_handle_player_data = <func_64>
_handle_battle_status = <func_65>
_handle_battle_result = <func_66>
_handle_battle_forfeit = <func_67>
_handle_error_message = <func_68>
_handle_turn_ready = <func_69>
_send_turn_ack = <func_70>
_handle_turn_ack = <func_71>
_handle_turn_resolve = <func_72>
send_turn_ready = (None)
_send_turn_ready_message = (False)
_resolve_turn = <func_75>
_maybe_resolve_turn = (None)
_handle_consensus_ack = <func_77>
_handle_consensus_fail = <func_78>
_handle_battle_ready = <func_79>
_handle_disconnect = <func_80>
_handle_error = (0)
_notify_ui_cancel = (?)
0.logger = Logger(3)
0.bt = 1
0.device_name = 2
GAME_SERVICE_UUID = GAME_SERVICE_UUID_TEMPLATE
0.service_uuid = GAME_SERVICE_UUID
0.bt.service_uuid = 0.service_uuid
0.bt.char_uuid = GAME_CHAR_UUID
0.session = None
0.pending_challenges = {}
0.last_keepalive = 0
0.availability = AVAILABILITY_IDLE
0._is_advertising = False
0._resume_server_after_scan = False
0.player_data_provider = None
0.challenge_callback = None
0.battle_start_callback = None
0.result_callback = None
0.error_callback = None
0.cancel_callback = None
0.turn_order_callback = None
0.turn_resolve_callback = None
0.consensus_callback = None
0.battle_ready_callback = None
0.pending_turn_resolve = None
0.server_mode = False
0.server_conn_handle = None
0.availability = 1
2 = 0.service_uuid
0._is_advertising = 2
3 = 0.availability
return 0._is_advertising
0._is_advertising = False
return 0.bt
2 = 0.availability
0.availability = 1
3 = 1
return (0, 6, 6)
11 = 1
11 = 1
12 = 32
13 = 10
13 = str(10)
0.session.our_player_data = 12
1 = 1
return 1
return 1
return 1
return 'food'
1 = None
2 = None
return 'food'
return []
1 = 18
return []
return list(1)
return 1(',')
return []
1 = 0
return 1
return True
1 = GAME_CHAR_UUID
0.server_mode = True
return 1
return True
0.server_mode = False
0.server_conn_handle = None
return True
return 0.server_mode
0.server_conn_handle = 1
return False
return 0.server_conn_handle
return False
return True
0._resume_server_after_scan = True
return True
1 = 0.bt
0._resume_server_after_scan = False
return 1
3 = 0._is_advertising
4 = 800
4 = 1
4 = 1
4 = <func_0>(4)
4 = 1
4 = 1
4 = <func_2>(4)
4 = 2
return 4
1 = 0
return 1
1 = 0
1 = 0
return 1
return False
1 = 1
3 = 8
0.session = ?(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0.session, 0.session.state, (3, 5), 0.logger, 'Already in battle session', isinstance(1, str), BluetoothManager, 0, 0.bt, 0.bt, time, 150, 0.bt, uhashlib, 1, str(time), None, BattleSession, 3, 1, 'is_challenger', True)
0.session.state = 1
4 = 1
5 = 0
0._resume_server_after_scan = False
6 = 5
return 6
4 = Exception
4 = None
1 = 1
return False
2 = 1
3 = 2
4 = isinstance(2, tuple)
4 = 'Unknown'
5 = 8
0.session = ?(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, isinstance(1, str), BluetoothManager, 1, 0.pending_challenges, 0.logger, 'No pending challenge from that opponent', 0.pending_challenges, uhashlib, 1, str(time), None, BattleSession, 5, 1, 'is_challenger', False)
0.session.opponent_name = 4
0.session.state = 2
return True
1 = 1
return False
return True
return False
return False
4 = 2
4 = 3
return 4
return False
3 = 1
3 = 2
4 = 3
0.session.state = 6
return 4
return False
return False
1 = 35
2 = 1
0.session.state = 6
return 2
0.session = None
0.pending_turn_resolve = None
0.server_conn_handle = None
1 = time
0.last_keepalive = 1
0.session.turn_move_acked = True
2 = 0
2 = 0
3 = 0.session.consensus_turn
3 = 16
1.consensus_send_attempts = 0.session.consensus_send_attempts
0.session.last_consensus_send_ts = time
0.session.last_consensus_send_ts = 0
4 = []
5 = 0.pending_challenges
6 = 0
7 = 6
5 = 4
1 = 0.pending_turn_resolve
2 = None
3 = 0.pending_turn_resolve
4 = ?
0.pending_turn_resolve = None
5 = 4
5 = 3
6 = Exception
5 = 4
6 = None
6 = Exception
6 = None
return (3, 5)
return 'age_ms'
0.challenge_callback = 1
0.battle_start_callback = 1
0.result_callback = 1
0.error_callback = 1
0.turn_order_callback = 1
0.turn_resolve_callback = 1
0.consensus_callback = 1
0.battle_ready_callback = 1
return False
2 = 0(0.session.turn_number, 1)
3 = 2
3 = 16
0.session.our_consensus_hash = 16
0.session.consensus_turn = 2
0.session.last_consensus_send_ts = time
0.session.last_consensus_send_ts = 0
0.session.consensus_send_attempts = 1
4 = 0.session.their_consensus_hash
5 = 4
6 = Exception
6 = None
return 3
0.session.consensus_turn = None
0.session.last_consensus_send_ts = 0
0.session.consensus_send_attempts = 0
2 = 0
3 = 19
0.session.their_consensus_hash = 3
4 = 0.session.our_consensus_hash
5 = 3
6 = Exception
6 = None
2 = 1
2 = 1
return (0, 0)
return (0.session.turn_number, 0.session.turn_state)
return False
1 = 0.bt
2 = 'conn_handle'
3 = 0
3 = 0
4 = Exception
4 = None
return False
return False
2 = -16
3 = None
4 = 16
return 4
return False
2 = 0
3 = 16
1 = 3
return 0.server_conn_handle
return False
4 = False
return 4
1 = 32
2 = len(1)
2 = 1
3 = 2
1 = 32
2 = len(1)
2 = 1
0.session.state = 3
2 = 3
1 = str(time)
0.session.session_token = 16
2 = 256
2 = 0.session.session_id
2 = 0.session.session_token
1 = 17
1 = 0.session.session_id
0.session.state = 4
1 = 0
2 = 'character_id'
2 = 2
0.session.our_player_data = 2
3 = 'powers'
3 = <func_0>(3)
3 = str(3)
4 = bytearray([18])
5 = 0.session.our_player_data
2 = 1
6 = 'UNKNOWN'
7 = 5
8 = len(5)
9 = 32
0.session.our_data_sent = True
1 = 0
return 1
0.session.state = 5
0.session.disconnect_grace_until = 12000
1 = Exception
1 = None
1 = 240
return False
return True
2 = 42
3 = 2
0.session.ready_sent = True
return 3
3 = 128
4 = len(3)
4 = 3
2 = 0
3 = 2
1 = -16
4 = Exception
4 = None
2 = 1
3 = 1
4 = 'Unknown'
4 = 'utf-8'
5 = 0.bt
6 = 'addr'
7 = Exception
7 = None
2 = 1
3 = 1
4 = 'Unknown'
4 = 'utf-8'
0.session.opponent_name = 4
0.session.state = 3
2 = 0
3 = 11
4 = 27
0.session.session_token = 4
0.session.state = 4
2 = 1
3 = 2
4 = set()
5 = False
6 = 0
7 = 3
8 = 1
3 = 2
9 = 8
3 = 8
5 = True
10 = 0
10 = 0
10 = 'utf-8'
10 = bytes(9)
10 = 'utf-8'
10 = bytes(9)
11 = None
0.session.opponent_data_received = True
12 = 11
2 = 1
3 = 1
4 = None
2 = 1
3 = None
0.session.state = 6
4 = Exception
4 = None
0.session.state = 6
2 = Exception
2 = None
2 = 1
3 = 1
4 = '<BB'
4 = 'utf-8'
2 = 1
3 = 1
4 = None
0.session.opponent_move = (3, 4)
2 = 1
2 = 0
0.session.turn_move_acked = True
0.session.last_turn_ready_ts = 0
0.session.turn_state = 2
return False
return True
0.session.our_move = (1, 2)
return False
return False
0.session.turn_state = 1
return True
return False
return True
2 = 0.session.our_move
3 = '_send_turn_ready_message: already sent, skipping'
4 = 2
4 = 3
5 = 4
0.session.turn_move_sent = True
0.session.turn_state = 1
0.session.last_turn_ready_ts = time
0.session.last_turn_ready_ts = 0
return 5
1 = 0.session.our_move
2 = 0.session.opponent_move
3 = 0.session.turn_number
4 = 0.session.is_challenger
0.pending_turn_resolve = (3, 1, 2, 4)
1.turn_number = 0.session.turn_number
0.session.turn_state = 0
0.session.our_move = None
0.session.opponent_move = None
0.session.turn_move_sent = False
0.session.turn_move_acked = False
0.session.last_turn_ready_ts = 0
0.session.our_consensus_hash = None
0.session.their_consensus_hash = None
0.session.consensus_turn = None
0.session.last_consensus_send_ts = 0
0.session.consensus_send_attempts = 0
0.session.turn_state = 2
2 = 0
0.session.their_consensus_hash = 19
0.session.their_consensus_hash = 0.session.our_consensus_hash
3 = 0.session.their_consensus_hash
4 = Exception
4 = None
2 = 0
0.session.ready_received = True
2 = Exception
2 = None
4 = 0.session
0.session = None
5 = time
0.session = 4
3 = Exception
3 = None
3 = Exception
3 = None
2 = Exception
2 = None