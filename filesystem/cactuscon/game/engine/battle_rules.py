# Decompiled from: fs_image/cactuscon/game/engine/battle_rules.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

urandom = urandom
const = const
DeterministicRNG = DeterministicRNG
get_move = get_move
Move = Move
MOVE_TYPE_PHYSICAL = MOVE_TYPE_PHYSICAL
MOVE_TYPE_SPECIAL = MOVE_TYPE_SPECIAL
MOVE_TYPE_STATUS = MOVE_TYPE_STATUS
MOVE_TYPE_HEAL = MOVE_TYPE_HEAL
MOVE_CAT_DAMAGE = MOVE_CAT_DAMAGE
MOVE_CAT_HEAVY = MOVE_CAT_HEAVY
MOVE_CAT_SUPPORT = MOVE_CAT_SUPPORT
MOVE_CAT_RECOVERY = MOVE_CAT_RECOVERY
get_character = get_character
get_care_catalog = get_care_catalog
Character = Character
CharacterStats = CharacterStats
ACHIEVEMENT_POWERS = ACHIEVEMENT_POWERS
StatusEffect = StatusEffect
StatusEffectType = StatusEffectType
create_burn_effect = create_burn_effect
create_poison_effect = create_poison_effect
create_paralyze_effect = create_paralyze_effect
create_sleep_effect = create_sleep_effect
create_confuse_effect = create_confuse_effect
BATTLE_CONTINUES = 0
PLAYER_WINS = 1
OPPONENT_WINS = 2
BATTLE_DRAW = 3
BattleContext = __build_class__(<func_0>, 'BattleContext')
BattleRules = __build_class__(<func_1>, 'BattleRules')
SimpleBattleRules = __build_class__(<func_2>, 'SimpleBattleRules', BattleRules)
__slots__ = ('player_char', 'player_stats', 'player_moves', 'opponent_char', 'opponent_stats', 'opponent_moves', 'turn_number', 'battle_log')
__init__ = (None, None)
log = <func_1>
advance_turn = <func_2>
get_player_stats_dict = <func_3>
get_opponent_stats_dict = <func_4>
is_battle_over = <func_5>
0.player_char = 1
0.opponent_char = 2
0.player_stats = 1
0.player_moves = list(1.moves)
0.player_stats = CharacterStats()
0.player_moves = [0, 1, 2, 3]
0.opponent_stats = 2
0.opponent_moves = list(2.moves)
0.opponent_stats = CharacterStats()
0.opponent_moves = [0, 1, 2, 3]
0.turn_number = 0
0.battle_log = []
1.turn_number = 0.turn_number
return 0.player_stats
return 0.opponent_stats
return 0
BASE_DAMAGE_MULTIPLIER = 2.15
CRIT_MULTIPLIER = 1.85
CRIT_CHANCE = 0.075
MIN_DAMAGE = 5
DAMAGE_VARIATION_MIN = 0.75
DAMAGE_VARIATION_MAX = 1
EVASION_EFFECT_MULT = 2.5
DEFENSE_EFFICIENCY_MULT = 0.9
__init__ = <func_0>
_get_care_effect = <func_1>
_get_power_effect = <func_2>
normalize_care_effects = <func_3>
apply_care_modifiers = <func_4>
normalize_power_effects = <func_5>
apply_power_modifiers = <func_6>
set_rng = <func_7>
clear_rng = <func_8>
get_random = <func_9>
get_random_uniform = <func_10>
execute_action = <func_11>
_apply_damage = (None)
_apply_heal = (None)
_execute_damage_move = (None)
_get_move_element = <func_15>
calculate_damage = <func_16>
get_type_effectiveness = <func_17>
_check_accuracy = <func_18>
_execute_heal_move = <func_19>
_execute_status_move = (None, None)
apply_status_effect = (None)
_apply_stat_boost = (None, None)
_apply_evasion_boost = (None)
_consume_defense_evasion = <func_24>
update_status_effects = <func_25>
check_action_prevented = <func_26>
get_move_priority = <func_27>
calculate_turn_order = (True)
check_victory_condition = <func_29>
validate_move = (None)
get_initial_stats = (None)
on_battle_start = <func_32>
on_battle_end = (None, None, None, None)
on_turn_start = <func_34>
on_turn_end = <func_35>
is_battle_over = <func_36>
get_available_moves = (None)
get_battle_state = (0)
validate_action = (None)
execute_move = <func_40>
0._rng = None
3 = {}
4 = []
return 4
return 1
2 = 'food'
return 2
3 = ('activity', 'food')
4 = 3
return 2
3 = 2
4 = 0
5 = 0
6 = 0
7 = ('activity', 'food')
8 = 7
9 = None
4 = 0
5 = 0
6 = 0
1.attack = 1(1.attack, 4)
1.defense = 1(1.defense, 5)
return 'xp_boost_pct'
return []
2 = []
3 = 1
return dict(2)
3 = 2
4 = 0
5 = 0
6 = 0
7 = 0
8 = 3
9 = 8
4 = 0
5 = 0
10 = 0
6 = 3
7 = 0
1.attack = 1(1.attack, 4)
1.defense = 1(1.defense, 5)
1.speed = 1(1.speed, 6)
return 'xp_boost_pct'
0._rng = 1
0._rng = None
1 = 0._rng
return 1
return urandom
3 = 2
return 3
return 1
1 = get_move(1)
return (['Unknown move!'], 'messages')
4 = 2
5 = 3
6 = 'messages'
7 = 3
8 = 5
9 = 4
10 = 4
11 = 2
return ('healed', 6)
3.hp = 'hp'
4 = 100
3.hp = 'hp'
return (0, False, False)
5 = 3
6 = 2
return (5, True, 6)
return 'element'
4 = 10
5 = 10
5 = 'defense_mult'(1.0)
4 = 10
5 = 10
5 = 'sp_defense_mult'(1.0)
5 = 5(0.DEFENSE_EFFICIENCY_MULT)
6 = max(5, 1)
6 = 0.BASE_DAMAGE_MULTIPLIER
7 = 1
6 = 0.025
8 = 3
6 = 8
9 = 1
6 = 0.5
6 = 0.5
10 = 0.DAMAGE_VARIATION_MAX
11 = 10
12 = 0.CRIT_CHANCE
12 = False
11 = 0.CRIT_MULTIPLIER
13 = max(0.MIN_DAMAGE, int(11))
return (13, 12)
return 1.0
4 = 10
5 = 10
6 = 4(0.EVASION_EFFECT_MULT, 0.2)
7 = 5(4, 0.5)
8 = 0
8 = 0.EVASION_EFFECT_MULT
9 = 8
9 = max(5.0, min(100.0, 9))
10 = 100
return 9
3 = 100
4 = 25
return 4(100)
return 'reason'
6 = 1.effect
return 5
return 1
return 4
4 = 'confuse'
return 'reason'
5 = 1
6 = 4
7 = []
8 = 7
return 'reason'
9 = 6()
3.status_effects = 7
return 'effect'
return create_sleep_effect(3)
return create_confuse_effect(3)
5 = 'sp_defense_mult'
6 = 'sp_defense_turns'
7 = 'sp_defense_elem'
8 = 1
return 'new_value'
9 = 'attack_up'
return 'success'
10 = 1
11 = 9
12 = 10
return 'new_value'
3 = 0
2.evasion = 'evasion'
2.evasion_turns = 'evasion_turns'
return 'new_value'
2.defense_turns = 0
2.defense_mult = 1.0
2.defense_elem = None
2.sp_defense_turns = 0
2.sp_defense_mult = 1.0
2.sp_defense_elem = None
2.evasion_turns = 0
2.evasion = 0
2 = 1
3 = []
4 = []
5 = []
6 = 4
7 = 2
8 = 6
9 = isinstance(6, StatusEffect)
1.hp = 'hp'
1.status_effects = 5
return 3
2 = 1
3 = []
4 = 3
5 = 0._rng
6 = 'rng'
return (True, 6)
return (False, None)
1 = get_move(1)
return 1.priority
return 0
6 = 1
7 = 3
8 = 6
9 = 7
return True
return False
10 = 2
11 = 4
12 = 10
13 = 10
return True
return False
return 5
3 = 1
4 = 2
5 = 0
6 = 0
return 3
return 1
return 2
return 0
1 = get_move(1)
return (False, 'Unknown move')
return (3.name, 1.name)
4 = 2
5 = 0
return (False, 5)
return (True, None)
1 = get_character(1)
return 1
return 'sp_defense_elem'
8 = 'battle_log'
9 = 100
10 = 100
11 = 2('hp', 0)
12 = 2
13 = 12(9, 11)
14 = 0
15 = 6
14 = 0
14 = 0
return 8
3 = []
return 3
3 = []
4 = 1
5 = 2
return 3
return 0
1 = get_character(1)
return []
3 = []
4 = 1.moves
5 = get_move(4)
6 = 1
7 = 2
return 3
4 = 1
5 = 2
return 'winner'
return 3
return 3
BASE_DAMAGE_MULTIPLIER = 1.5
CRIT_CHANCE = 0.0
calculate_damage = <func_0>
apply_status_effect = (None)
4 = 10
5 = 10
4 = 10
5 = 10
6 = max(5, 1)
6 = 0.BASE_DAMAGE_MULTIPLIER
return (max(0.MIN_DAMAGE, int(6)), False)
return 'reason'