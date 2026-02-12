# Decompiled from: fs_image/cactuscon/ui/panels/settings.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

lv = lvgl
BasePanel = BasePanel
prefs = prefs
HANDLE_KEY = HANDLE_KEY
LEGACY_HANDLE_KEY = LEGACY_HANDLE_KEY
HANDLE_MAX_LEN = HANDLE_MAX_LEN
normalize_handle = normalize_handle
fuel_gauge = fuel_gauge
clear_saved_credentials = clear_saved_credentials
SettingsPanel = __build_class__(<func_0>, 'SettingsPanel', BasePanel)
__init__ = 0
create_ui = <func_1>
_create_label_row = <func_2>
on_show = <func_3>
on_hide = <func_4>
_stop_status_timer = <func_5>
show_status_message = (2500)
_clear_status_message = <func_7>
_load_settings = <func_8>
_save_settings = <func_9>
_fast_update = <func_10>
_update_display = <func_11>
_get_wifi_manager = <func_12>
_update_wifi_status = <func_13>
_update_device_id = <func_14>
_update_battery_level = <func_15>
_on_handle_edit_clicked = <func_16>
_update_ssid = <func_17>
_on_wifi_toggle = <func_18>
_on_brightness_changed = <func_19>
_get_slider_from_event = <func_20>
_apply_brightness = <func_21>
on_back_pressed = <func_22>
return 0
1._wifi_mgr = None
1._brightness = 100
1._handle_edit_btn = None
1._status_timer = None
1 = 0.screen
2 = 0.screen
3 = 40
4 = 30
5 = 3
6 = 0.screen
7 = 0.screen
8 = 7
0._handle_edit_btn = 7
5 = 4
9 = 0.screen
10 = 0.screen
11 = 10
5 = 4
12 = 0.screen
13 = 0.screen
5 = 4
14 = 0.screen
5 = 4
15 = 0.screen
3 = 0.screen
return 3
1 = getattr(0.game_ui, 'wifi_status_message', None)
0.game_ui.wifi_status_message = None
0._update_timer = None
return 0
0._update_timer = None
0._status_timer = None
3 = 'status_label'
0._status_timer = None
return 0
1 = 'status_label'
0._brightness = 100
0._brightness = max(10, min(100, 0._brightness))
1 = Exception
0._brightness = 100
1 = None
1 = Exception
1 = None
1 = Exception
1 = None
1 = prefs(LEGACY_HANDLE_KEY)
1 = HANDLE_MAX_LEN
1 = 'Not Set'
2 = Exception
2 = None
return 0._wifi_mgr
0._wifi_mgr = 0.game_ui.wifi
return 0._wifi_mgr
1 = 0
2 = 'Disconnect'
3 = 65280
2 = 'Connect'
3 = 16737792
1 = 0
2 = 1
3 = <func_0>(2)
4 = Exception
4 = None
1 = 0
return 1
1 = 0
2 = 1
3 = Exception
3 = None
2 = 0
2 = 1
3 = 2
0._brightness = 3
2 = 'brightness_slider'
return 2
return 1
return 1
2 = Exception
2 = None