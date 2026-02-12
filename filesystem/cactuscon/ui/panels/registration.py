# Decompiled from: fs_image/cactuscon/ui/panels/registration.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

lv = lvgl
gc = gc
ubinascii = ubinascii
uhashlib = uhashlib
urandom = urandom
network = network
time = time
ujson = ujson
BasePanel = BasePanel
prefs = prefs
HANDLE_KEY = HANDLE_KEY
LEGACY_HANDLE_KEY = LEGACY_HANDLE_KEY
HANDLE_PENDING_KEY = HANDLE_PENDING_KEY
HANDLE_REG_ERROR_KEY = HANDLE_REG_ERROR_KEY
HANDLE_MAX_LEN = HANDLE_MAX_LEN
normalize_handle = normalize_handle
validate_handle = validate_handle
config = config
NetworkError = NetworkError
APIError = APIError
RegistrationPanel = __build_class__(<func_0>, 'RegistrationPanel', BasePanel)
__init__ = 0
_generate_anon_handle = <func_1>
set_api_client = <func_2>
create_ui = <func_3>
_on_textarea_clicked = <func_4>
_on_textarea_defocus = <func_5>
_on_textarea_ready = <func_6>
_on_textarea_cancel = <func_7>
_on_keyboard_ready = <func_8>
_on_keyboard_cancel = <func_9>
_show_keyboard = <func_10>
_hide_keyboard = <func_11>
_destroy_keyboard = <func_12>
_ensure_keyboard = <func_13>
_position_keyboard = <func_14>
_apply_keyboard_shift = <func_15>
_restore_keyboard_shift = <func_16>
_obj_show = <func_17>
_obj_hide = <func_18>
_keyboard_is_visible = <func_19>
_bind_keyboard_textarea = <func_20>
_update_layout = <func_21>
_get_abs_y = <func_22>
_get_screen_size = <func_23>
_warn_once = <func_24>
_get_handle_value = <func_25>
_on_skip_clicked = <func_26>
_on_register_clicked = <func_27>
_do_registration = <func_28>
_on_registration_success = <func_29>
_on_registration_failed = <func_30>
_on_registration_deferred = <func_31>
_should_defer_registration = <func_32>
_save_local_handle = (False)
_extract_api_detail = <func_34>
_clear_registration_error = <func_35>
_save_registration_error = <func_36>
_set_status = <func_37>
_create_error_modal = <func_38>
_show_error_modal = <func_39>
_hide_error_modal = <func_40>
_on_error_modal_close = <func_41>
on_show = <func_42>
update = <func_43>
_prime_wifi_connection = <func_44>
_refresh_mac = <func_45>
on_hide = <func_46>
on_cleanup = <func_47>
on_back_pressed = <func_48>
return 0
1.api_client = None
1._handle_value = 0
1._handle_ta = None
1._status_label = None
1._register_btn = None
1._skip_btn = None
1._registering = False
1._pending_character_redirect = False
1._error_modal = None
1._error_modal_msg = None
1._error_modal_close = None
1._device_info_label = None
1._keyboard = None
1._keyboard_hidden = True
1._kb_warned = set()
1._content_root = None
1._content_root_y0 = 0
1._kb_shift = 0
7 = None
7 = 3.wifi
7 = None
8 = network.WLAN.IF_STA
7 = 'mac'
7 = None
1.mac_str = <func_0>(7)
1.mac_str = None
1 = 0
return 1
1 = 100000000
2 = 1
3 = 2
4 = 8
return 4
0.api_client = 1
0._content_root = 0.screen
0._content_root_y0 = 0
0._kb_shift = 0
1 = 0._content_root
2 = 0._content_root
0._handle_ta = 0._content_root
0._status_label = 0._content_root
0._register_btn = 0._content_root
3 = 0._register_btn
0._skip_btn = 0._content_root
4 = 0._skip_btn
5 = 0._content_root
0._device_info_label = 5
0._keyboard = None
0._keyboard_hidden = True
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
1 = 0._handle_ta
return 1
return 1
return 0._handle_ta
2 = 0
3 = Exception
3 = None
2 = normalize_handle(0)
3 = validate_handle(2)
4 = 0
5 = 0._registering
0._registering = True
2 = getattr(0.game_ui, 'wifi', None)
3 = getattr(config, 'WIFI_CONNECT_TIMEOUT_S', 10)
4 = time
5 = 1000
6 = None
7 = Exception
7 = None
0._registering = False
0._registering = False
2 = 'Registration failed'
3 = 1
2 = 'Handle already in use. Choose another.'
2 = 3
2 = str(1)
2 = 80
0._registering = False
0._registering = False
0._registering = False
return True
return True
return False
return True
3 = Exception
return False
3 = None
2 = getattr(1, 'response_body', None)
3 = 2
4 = 'detail'
return str(4)
return str(2)
1 = 0.screen
2 = 1
3 = 2
4 = 2
0._error_modal_msg = 4
5 = 2
6 = 5
0._error_modal_close = 5
0._error_modal = 1
0._registering = False
0._pending_character_redirect = False
1 = prefs(LEGACY_HANDLE_KEY)
2 = HANDLE_REG_ERROR_KEY
0._pending_character_redirect = True
0._pending_character_redirect = False
1 = getattr(0.game_ui, 'wifi', None)
2 = getattr(config, 'WIFI_CONNECT_TIMEOUT_S', 10)
3 = Exception
3 = None
1 = None
2 = getattr(0.game_ui, 'wifi', None)
1 = 2
1 = None
3 = network.WLAN.IF_STA
1 = 'mac'
1 = None
0.mac_str = <func_0>(1)
1 = 0
return 1
return True