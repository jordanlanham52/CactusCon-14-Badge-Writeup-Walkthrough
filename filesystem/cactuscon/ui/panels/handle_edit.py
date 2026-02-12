# Decompiled from: fs_image/cactuscon/ui/panels/handle_edit.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

lv = lvgl
BasePanel = BasePanel
prefs = prefs
HANDLE_KEY = HANDLE_KEY
LEGACY_HANDLE_KEY = LEGACY_HANDLE_KEY
config = config
HANDLE_MAX_LEN = HANDLE_MAX_LEN
normalize_handle = normalize_handle
validate_handle = validate_handle
HandleEditPanel = __build_class__(<func_0>, 'HandleEditPanel', BasePanel)
__init__ = 0
set_api_client = <func_1>
create_ui = <func_2>
on_show = <func_3>
on_hide = <func_4>
on_cleanup = <func_5>
on_back_pressed = (None)
_load_handle = <func_7>
_get_handle_value = <func_8>
_set_status = (None)
_on_submit_clicked = <func_10>
_on_cancel_clicked = <func_11>
_cancel_and_back = <func_12>
_save_handle = <func_13>
_set_submit_enabled = <func_14>
_push_handle_update = <func_15>
_apply_handle_runtime = <func_16>
_on_textarea_clicked = <func_17>
_on_textarea_defocus = <func_18>
_on_textarea_ready = <func_19>
_on_textarea_cancel = <func_20>
_on_keyboard_ready = <func_21>
_on_keyboard_cancel = <func_22>
_show_keyboard = <func_23>
_hide_keyboard = <func_24>
_destroy_keyboard = <func_25>
_ensure_keyboard = <func_26>
_position_keyboard = <func_27>
_apply_keyboard_shift = <func_28>
_restore_keyboard_shift = <func_29>
_obj_show = <func_30>
_obj_hide = <func_31>
_keyboard_is_visible = <func_32>
_bind_keyboard_textarea = <func_33>
_update_layout = <func_34>
_get_abs_y = <func_35>
_get_screen_size = <func_36>
_warn_once = <func_37>
return 0
1._content_root = None
1._content_root_y0 = 0
1._kb_shift = 0
1._handle_ta = None
1._status_label = None
1._keyboard = None
1._keyboard_hidden = True
1._kb_warned = set()
1._original_handle = 0
1._submit_btn = None
1.api_client = None
1.wifi = None
0.api_client = 1
0._content_root = 0.screen
0._content_root_y0 = 0
0._kb_shift = 0
1 = 0._content_root
2 = 0
3 = 'title'
4 = 30
4 = 90
0._handle_ta = 0._content_root
0._status_label = 0._content_root
5 = 90
5 = min(120, 2(40, 2))
6 = 30
7 = 12
8 = 2
9 = 120
9 = 9(int, 3(0.6))
10 = 6
11 = 6
0._submit_btn = 11
return True
1 = ?
1 = prefs(LEGACY_HANDLE_KEY)
1 = Exception
0._original_handle = 1
return 0._handle_ta
1 = 0._handle_ta
1 = Exception
return normalize_handle(1)
1 = 0
2 = validate_handle(1)
3 = False
4 = 0
5 = Exception
5 = None
return True
return False
return True
return True
return False
return False
2 = None
return False
3 = getattr(config, 'WIFI_CONNECT_TIMEOUT_S', 10)
4 = time
5 = 4
return False
return True
6 = Exception
return False
6 = None
2 = 0.battle_manager.game_bt
2 = None
2.device_name = 1
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
3 = 2
3 = 140
1 = 0
2 = 0._keyboard
3 = 0._keyboard
4 = 0._keyboard
4 = 1(2, 2)
3 = 4
5 = 0._handle_ta
6 = 0._handle_ta
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
3 = lv
1 = 3
2 = 3
return (1, 2)