# Decompiled from: fs_image/cactuscon/ui/panels/character_care.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

lv = lvgl
time = time
BasePanel = BasePanel
get_care_catalog = get_care_catalog
get_care_state = get_care_state
set_care_effect = set_care_effect
prefs = prefs
TEMPERAMENT_VAL_TO_STATE = 10
CharacterCarePanel = __build_class__(<func_0>, 'CharacterCarePanel', BasePanel)
__init__ = 0
create_ui = <func_1>
on_show = 0
_refresh_state = <func_3>
_on_temperament_info = <func_4>
_show_info_modal = <func_5>
_close_info_modal = <func_6>
_effect_name = <func_7>
_effect_desc = <func_8>
_format_effect_summary = <func_9>
_show_error_throttled = (1000)
_on_effect_clicked = <func_11>
return 0
1._busy = False
1._last_action_ms = 0
1._last_error_msg = None
1._last_error_ts = 0
1 = 0.screen
2 = 26
3 = 0.screen
4 = 3
5 = 0.screen
6 = {}
7 = 78
8 = ('activity', 'food')
9 = 0.screen
10 = 0.screen
11 = []
12 = []
13 = 10
14 = 140
15 = 48
7 = 76
1 = {}
2 = Exception
1 = {}
2 = None
3 = {}
2 = Exception
3 = {}
2 = None
4 = {}
5 = {}
6 = 'id'
7 = 'id'
8 = 0
9 = 0
10 = 0
11 = 0
12 = 0
13 = 'status'
14 = 'hint'
15 = None
1 = 0
return 1
3 = 'info_modal'
3 = 0.screen
4 = 3
5 = 4
6 = 4
7 = 24
2 = 'info_modal'
4 = []
return 2
return 2
4 = []
return 'desc'
return 4
2 = []
3 = 0
4 = 0
5 = 0
6 = 0
7 = 'desc'
return 2
3 = time
0._last_error_msg = 1
0._last_error_ts = 3
3 = time
0._last_action_ms = 3
0._busy = True
4 = {}
5 = {}
6 = 'food_cooldown'
7 = 0
0._busy = False
0._busy = False
0._busy = False