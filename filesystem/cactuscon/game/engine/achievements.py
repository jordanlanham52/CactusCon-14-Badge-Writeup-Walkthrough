# Decompiled from: fs_image/cactuscon/game/engine/achievements.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

time = time
os = os
Logger = Logger
config = config
prefs = prefs
ACHIEVEMENTS = [{'SAO crossover: A rogue Hackachu teaches your creature some hacky tricks. Grants +5 Attack +5 Defense for 15m (30m cooldown).', 'desc', 'sao_buff_easy', 'action'}, 'sao_unlock_enigmox', 'id', 'SAO Enigmox', 'name', {'SAO crossover: Enigmox, the evasive cipher-mage casts wards on your creatures. Grants +5 Defense +5 Evasion for 15m (60m cooldown).', 'desc', 'sao_buff_medium', 'action'}, 'sao_unlock_glyphbat', 'id', 'SAO Glyphbat', 'name', 'SAO crossover: Glyphbat, an aerial radiowave antagonist helps flank your enemies. Grants +10 Attack +5 Defense +5 Evasion for 15m (60m cooldown).', 'desc', 'sao_buff_hard', 'action']
_ICON_CANDIDATES = ('/assets/images/icons/{id}.rgb565', 'assets/images/icons/{id}.rgb565', 'badge/src/assets/images/icons/{id}.rgb565', 'releases/badge/assets/images/icons/{id}.rgb565')
ACHIEVEMENT_ICON_PATH = 0
_MINUTE_MS = 60000
ACHIEVEMENT_POWERS = 'sao_unlock_glyphbat'
KEY_POWER_ACTIVE = 'ach_actv'
KEY_POWER_COOLDOWN = 'ach_cdwn'
KEY_WORK_PLAY_STATE = 'ach_wp_on'
get_achievement_ids = <func_0>
get_achievement_icon_path = <func_1>
get_achievement_icon_paths = <func_2>
KEY_PACK_ACH = 'ach'
KEY_WIN_STREAK = 'ws'
KEY_LOSS_STREAK = 'ls'
KEY_CLEAN_STREAK = 'ccs'
get_owned_achievements = (None)
_save_owned_achievements = <func_4>
_parse_power_csv = <func_5>
_serialize_power_csv = <func_6>
_now_ms = <func_7>
_ticks_diff = <func_8>
_ticks_add = <func_9>
Achievements = __build_class__(<func_10>, 'Achievements')
return <func_0>(ACHIEVEMENTS)
1 = 0
return 'id'
1 = _ICON_CANDIDATES
2 = 0
return 2
return 0
return <func_0>(get_achievement_ids())
1 = 0
return get_achievement_icon_path(1)
2 = KEY_PACK_ACH
return 2(',')
return 1([])
1 = 0
return 1
1 = {}
return 1
2 = ','
3 = 1
4 = ':'
return 1
1 = []
2 = {}
3 = 0
return 1
return time
return time(1000)
return 1
return 1
return 1
return 1
__init__ = (None, config.LOG_LEVEL)
_bump_streak = <func_1>
list_all = <func_2>
list_owned = <func_3>
_award = <func_4>
_load_power_state = (None)
_save_power_state = <func_6>
get_active_powers = (None)
get_power_status = (None)
use_power = (None)
first_battle = <func_10>
clean_care = <func_11>
collector = <func_12>
discipline_use = <func_13>
treat_use = <func_14>
temperament_max = <func_15>
win_streak = <func_16>
loss_streak = <func_17>
reset_streaks = <func_18>
0.prefs = prefs
0.logger = Logger(2)
5 = 1
return 5
return ACHIEVEMENTS
return get_owned_achievements(0.prefs)
2 = 0([])
return False
return True
1 = _now_ms()
2 = KEY_POWER_ACTIVE
3 = KEY_POWER_COOLDOWN
4 = _parse_power_csv(2)
5 = _parse_power_csv(3)
6 = False
7 = list(4)
8 = 0.prefs
6 = True
7 = list(5)
9 = None
6 = True
return (4, 5)
2 = 1
3 = 'now_ms'
return list(2)
1 = _now_ms()
2 = 1
3 = 'now_ms'
return 'cooldowns'
2 = 1
3 = {}
return 2
2 = 1
3 = {}
return 2
2 = _now_ms()
return 'msg'
return 'msg'
3 = 1
4 = KEY_WORK_PLAY_STATE(0)
5 = 4
return 'cooldown_until'
6 = 2
7 = 'now_ms'
return 'cooldown_until'
8 = _ticks_add(2, 86400000)
return 'cooldown_until'
9 = 6(1, 2)
return 'power'
9 = 7(1, 2)
return 'power'
10 = get_care_state
11 = CARE_TEMPERAMENT_MAX
12 = {}
13 = 0
return 'power'
return 'cooldown_until'
14 = 0
15 = 0
11 = CARE_TEMPERAMENT_MAX
return 'cooldown_until'
2 = []
2 = set(1([]))