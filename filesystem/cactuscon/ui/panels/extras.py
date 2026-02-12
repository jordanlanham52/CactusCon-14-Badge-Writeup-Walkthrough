# Decompiled from: fs_image/cactuscon/ui/panels/extras.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

gc = gc
lv = lvgl
BasePanel = BasePanel
mem_info = mem_info
unlocks = unlocks
_add_back_button = <func_0>
ExtrasPanel = __build_class__(<func_1>, 'ExtrasPanel', BasePanel)
2 = 0.screen
3 = 2
return 2
__init__ = 0
create_ui = <func_1>
on_show = <func_2>
on_hide = <func_3>
on_cleanup = <func_4>
on_back_pressed = (None)
_on_textarea_defocus = <func_6>
_on_textarea_ready = <func_7>
_on_textarea_cancel = <func_8>
_on_textarea_clicked = <func_9>
_on_keyboard_ready = <func_10>
_on_keyboard_cancel = <func_11>
_on_submit_clicked = <func_12>
_show_keyboard = <func_13>
_hide_keyboard = <func_14>
_destroy_keyboard = <func_15>
_ensure_keyboard = <func_16>
_apply_keyboard_shift = <func_17>
_restore_keyboard_shift = <func_18>
_obj_show = <func_19>
_obj_hide = <func_20>
_keyboard_is_visible = <func_21>
_bind_keyboard_textarea = <func_22>
_update_layout = <func_23>
_get_abs_y = <func_24>
_get_screen_size = <func_25>
_position_keyboard = <func_26>
_warn_once = <func_27>
_set_status = (None)
_update_status_timer = <func_29>
_start_status_timer = <func_30>
_stop_status_timer = <func_31>
_refresh_status = (None)
_submit_code = <func_33>
return 0
1._content_root = None
1._content_root_y0 = 0
1._kb_shift = 0
1._code_ta = None
1._status_label = None
1._status_timer = None
1._keyboard = None
1._keyboard_hidden = True
1._kb_warned = set()
0._content_root = 0.screen
0._content_root_y0 = 0
0._kb_shift = 0
1 = 0.screen
2 = 0._content_root
3 = 0._content_root
4 = 0._content_root
0._code_ta = 0._content_root
5 = 0._on_submit_clicked
0._status_label = 0._content_root
return True
return False
1 = Exception
1 = None
0._keyboard = None
0._keyboard_hidden = True
1 = 0.screen
0._keyboard = 1
2 = Exception
0._keyboard = None
2 = None
1 = 0
2 = 0._keyboard
3 = 0._keyboard
4 = 0._keyboard
4 = 1(2, 2)
3 = 4
5 = 0._code_ta
6 = 0._code_ta
7 = 6
8 = 6
9 = 8
10 = 0
0._kb_shift = 10
0._kb_shift = 0
0._kb_shift = 0
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
return False
return lv.obj.FLAG.HIDDEN
return 0._keyboard_hidden
return False
return False
1 = Exception
return False
1 = None
return True
return 0
2 = 1
return 2.y1
3 = 0
4 = 1
3 = 4
4 = 4
return 3
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
1 = 0
2 = 0._keyboard
1 = 240
2 = 320
3 = 2
3 = 140
3 = 8947848
3 = 65280
3 = 16737792
2 = 'Too many attempts. Wait '
0._status_timer = None
0._status_timer = None
2 = unlocks
1 = 0._code_ta
1 = Exception
2 = 'battle_manager'
3 = 0.battle_manager