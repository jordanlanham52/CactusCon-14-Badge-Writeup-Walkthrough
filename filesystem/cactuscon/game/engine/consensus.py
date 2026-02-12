# Decompiled from: fs_image/cactuscon/game/engine/consensus.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

Logger = Logger
config = config
logger = Logger(config.LOG_LEVEL)
struct = struct
uhashlib = uhashlib
const = const
DeterministicRNG = DeterministicRNG
create_turn_seed = create_turn_seed
CONSENSUS_PENDING = 0
CONSENSUS_AGREED = 1
CONSENSUS_FAILED = 2
TurnOutcome = __build_class__(<func_0>, 'TurnOutcome')
ConsensusTracker = __build_class__(<func_1>, 'ConsensusTracker')
__slots__ = ('turn_number', 'player_move_id', 'opponent_move_id', 'player_went_first', 'player_damage_dealt', 'opponent_damage_dealt', 'player_hp_after', 'opponent_hp_after', 'player_healed', 'opponent_healed', 'player_crit', 'opponent_crit', 'player_effects_applied', 'opponent_effects_applied', 'rng_state')
__init__ = <func_0>
compute_hash = <func_1>
to_dict = <func_2>
0.turn_number = 0
0.player_move_id = 0
0.opponent_move_id = 0
0.player_went_first = True
0.player_damage_dealt = 0
0.opponent_damage_dealt = 0
0.player_hp_after = 0
0.opponent_hp_after = 0
0.player_healed = 0
0.opponent_healed = 0
0.player_crit = False
0.opponent_crit = False
0.player_effects_applied = []
0.opponent_effects_applied = []
0.rng_state = b'\x00\x00\x00\x00'
1 = 0
1 = len(0.opponent_effects_applied)
1 = 0.rng_state
return 16
return 'opponent_crit'
__slots__ = ('session_token', 'current_turn', 'pending_outcome', 'our_hash', 'their_hash', 'history', '_rng')
__init__ = <func_0>
begin_turn = <func_1>
get_rng = <func_2>
record_outcome = <func_3>
get_our_hash = <func_4>
receive_opponent_hash = <func_5>
_check_consensus = <func_6>
commit_turn = <func_7>
get_battle_hash = <func_8>
void_battle = ('consensus_failed')
0.session_token = 1
0.current_turn = 0
0.pending_outcome = None
0.our_hash = None
0.their_hash = None
0.history = []
0._rng = None
4 = create_turn_seed(0.session_token, 1, 2, 3)
5 = 'None'
0._rng = DeterministicRNG(4)
0.pending_outcome = TurnOutcome()
0.pending_outcome.turn_number = 1
0.pending_outcome.player_move_id = 2
0.pending_outcome.opponent_move_id = 3
0.our_hash = None
0.their_hash = None
return 0._rng
return 0._rng
1.rng_state = 0._rng
0.pending_outcome = 1
0.our_hash = 1
return 0.our_hash
0.their_hash = 1
return 0
return 0
return 1
return 2
1 = 0.pending_outcome
1.current_turn = 0.current_turn
0.pending_outcome = None
0.our_hash = None
0.their_hash = None
0._rng = None
return 1
1 = len(0.history)
2 = 0.history
1 = 2
return 16
return 'their_hash'