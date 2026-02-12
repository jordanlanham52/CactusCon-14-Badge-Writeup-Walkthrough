# Decompiled from: fs_image/cactuscon/ui/wifi_flow/wifi_keyboard.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

lv = lvgl
WifiKeyboard = __build_class__(<func_0>, 'WifiKeyboard')
__init__ = (None)
set_handlers = (None, None)
get_keyboard = <func_2>
get_shift = <func_3>
set_shift_root = <func_4>
show = (None, 0)
hide = <func_6>
destroy = <func_7>
is_visible = <func_8>
_ensure_keyboard = <func_9>
_on_keyboard_ready = <func_10>
_on_keyboard_cancel = <func_11>
_position_keyboard = <func_12>
_apply_shift = <func_13>
_restore_shift = <func_14>
_max_allowed_shift = <func_15>
_bind_textarea = <func_16>
_obj_show = <func_17>
_obj_hide = <func_18>
_update_layout = <func_19>
_get_coords = <func_20>
_get_screen_size = <func_21>
_warn_once = <func_22>
0.screen = 1
0._viewport = 2
0._shift_root = 3
0._logger = 4
0._keyboard = None
0._keyboard_hidden = True
0._kb_warned = set()
0._shift = 0
0._shift_root_y0 = 0
0._min_shift = 0
0._textarea = None
0._footer = None
0._on_ready = None
0._on_cancel = None
0._shift_root_y0 = 0._shift_root
0._shift_root_y0 = 0
0._on_ready = 1
0._on_cancel = 2
return 0._keyboard
return 0._shift
0._shift_root = 1
0._shift_root_y0 = 0._shift_root
0._shift_root_y0 = 0
0._textarea = 1
0._footer = 2
0._min_shift = 0
return False
return False
return False
4 = Exception
4 = None
return True
return False
0._min_shift = 0
return True
0._keyboard = None
0._keyboard_hidden = True
return False
return lv.obj.FLAG.HIDDEN
return 0._keyboard_hidden
1 = 0.screen
1 = lv
1 = 0.screen
0._keyboard = 1
2 = Exception
0._keyboard = None
2 = None
1 = 0
2 = 0._keyboard
1 = 240
2 = 320
3 = 2
4 = 140
5 = 2(0.6)
3 = 4
3 = 5
1 = 0._keyboard
2 = None
3 = None
0._shift = 0._min_shift
4 = None
4 = 3
4 = 3(3, 3)
0._shift = 0._min_shift
5 = 6
6 = 5
6 = 0
6 = 0._min_shift
7 = 0
6 = 7
0._shift = 6
0._shift = 0
0._shift = 0
0._min_shift = 0
1 = 0._shift_root
2 = 0._viewport
3 = 3
4 = 1
5 = 4
5 = 0
return 5
return False
return False
1 = Exception
return False
1 = None
return True
return False
return False
2 = Exception
return False
2 = None
0._keyboard_hidden = False
return True
return False
return False
2 = Exception
return False
2 = None
0._keyboard_hidden = True
return True
2 = 1
return (2.x1, 2.y1, 2.x2, 2.y2)
1 = 0
2 = 0
1 = 0.screen
2 = 0.screen
1 = 0
2 = 0
3 = lv
1 = 3
2 = 3
return (1, 2)