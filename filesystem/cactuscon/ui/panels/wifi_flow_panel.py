# Decompiled from: fs_image/cactuscon/ui/panels/wifi_flow_panel.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

gc = gc
time = time
lv = lvgl
BasePanel = BasePanel
mem_info = mem_info
WifiController = WifiController
build_list_view = build_list_view
build_password_view = build_password_view
build_status_overlay = build_status_overlay
PAGE_SIZE = PAGE_SIZE
WifiKeyboard = WifiKeyboard
wifi_debug = wifi_debug
save_credentials = save_credentials
WifiConnectFlowPanel = __build_class__(<func_0>, 'WifiConnectFlowPanel', BasePanel)
__init__ = 0
_now_ms = <func_1>
_elapsed_ms = <func_2>
create_ui = <func_3>
on_show = <func_4>
on_hide = <func_5>
on_cleanup = <func_6>
_ensure_wifi_manager = <func_7>
_show_list_view = <func_8>
_show_password_view = <func_9>
_destroy_view = <func_10>
_refresh_scan = (False)
_update_list_page = <func_12>
_set_row_state = <func_13>
_get_row_index = <func_14>
_on_row_clicked = <func_15>
_on_back_from_list = <func_16>
_on_back_from_password = <func_17>
_on_refresh_clicked = <func_18>
_on_prev_clicked = <func_19>
_on_next_clicked = <func_20>
_remember_checked = <func_21>
_on_connect_clicked = (None)
_on_password_clicked = <func_23>
_on_password_defocus = <func_24>
_on_password_ready = <func_25>
_on_password_cancel = <func_26>
_on_keyboard_ready = <func_27>
_on_keyboard_cancel = <func_28>
_show_keyboard = <func_29>
_hide_keyboard = <func_30>
_start_connect_timer = <func_31>
_stop_connect_timer = <func_32>
_on_connect_timer = <func_33>
_reason_to_message = <func_34>
_set_password_status = (None)
_symbol_ok = <func_36>
_set_overlay_text = (None, None, None)
_show_status_overlay = (True, None, False)
_hide_status_overlay = <func_39>
_schedule_overlay_hide = (False)
_stop_overlay_timer = <func_41>
_on_overlay_timer = <func_42>
_begin_scan = (False, 30)
_apply_scan_results = (False, None)
_debug_overlay_state = <func_45>
_show_scanning_placeholders = <func_46>
_schedule_scan = (False, None)
_stop_scan_timer = <func_48>
_on_scan_timer = <func_49>
_debug_nav = <func_50>
_debug_blocked = <func_51>
_debug_connect_terminal = <func_52>
_total_pages = <func_53>
_coords = <func_54>
_snapshot = <func_55>
return 0
1._wifi_mgr = None
1._controller = WifiController(None, 1.logger)
1._content_root = None
1._keyboard = None
1._view_root = None
1._list_view = None
1._password_view = None
1._active_view = None
1._networks = []
1._page_index = 0
1._selected_ssid = None
1._row_index_by_obj = {}
1._status_overlay = None
1._status_spinner = None
1._status_label = None
1._status_ssid_label = None
1._connect_timer = None
1._overlay_timer = None
1._scan_timer = None
1._connect_started_ms = None
1._connect_timeout_ms = None
1._scanning = False
1._connecting = False
1._scan_seq = 0
1._scan_nav_counter = 0
1._nav_counter = 0
1._remember_choice = False
1._remember_ssid = None
1._remember_password = None
1._last_connect_success = False
1._last_connect_ssid = None
1._overlay_nav_to_settings = False
return time
return time(1000)
return 0
return 1
return 1
0._content_root = 0.screen
0._keyboard = WifiKeyboard(0.screen, 0.screen, 0._content_root, 0.logger)
1 = build_status_overlay(0._content_root)
0._status_overlay = 'overlay'
0._status_spinner = 'spinner'
0._status_label = 'label'
0._status_ssid_label = 'label_secondary'
0._keyboard = None
return 0._wifi_mgr
0._wifi_mgr = 0.game_ui.wifi
return 0._wifi_mgr
0._list_view = build_list_view(0._content_root, 0.create_button)
0._view_root = 'root'
0._active_view = 'list'
0._row_index_by_obj = {}
1 = 0._list_view('rows')
2 = enumerate
3 = 'btn'
0._selected_ssid = 1
0._password_view = build_password_view(0._content_root, 0.create_button)
0._view_root = 'root'
0._active_view = 'password'
2 = 'ssid_label'
3 = 'password_ta'
0._view_root = None
0._active_view = None
0._row_index_by_obj = {}
0._list_view = None
0._password_view = None
2 = 0._controller
2 = []
1 = len(0._networks)
2 = PAGE_SIZE(1, PAGE_SIZE)
0._page_index = 1
0._page_index = 0
3 = 'page_label'
4 = PAGE_SIZE
5 = 0._list_view('rows')
6 = enumerate
7 = 5
8 = 'btn'
9 = 7
10 = '---'
11 = 'rssi'
2 = None
2 = 1
2 = 1
return 2
2 = 1
3 = 2
4 = 'entry_idx'
5 = 'ssid'
2 = 0._page_index
3 = len(0._networks)
4 = PAGE_SIZE(1, PAGE_SIZE)
1._page_index = 0._page_index
1._nav_counter = 0._nav_counter
5 = 0._page_index
2 = len(0._networks)
3 = PAGE_SIZE(1, PAGE_SIZE)
4 = 0._page_index
1._page_index = 0._page_index
1._nav_counter = 0._nav_counter
5 = 0._page_index
return False
1 = 'remember_cb'
return False
return 0
return lv.STATE.CHECKED
return False
0._last_connect_success = False
0._last_connect_ssid = None
2 = 0
3 = None
2 = 3
2 = Exception
2 = 2
0._remember_choice = 0
0._remember_ssid = 0._selected_ssid
0._remember_password = 2
4 = 15
0._connecting = False
0._connecting = True
0._connect_started_ms = 0
0._connect_timeout_ms = 15000
1 = 'footer'
2 = 'password_ta'
0._connect_timer = None
0._connect_timer = None
0._connect_started_ms = None
0._connect_timeout_ms = None
0._connecting = False
2 = 0._controller
3 = 'state'
0._connecting = False
4 = 0._selected_ssid
5 = 0
6 = 5
6 = 'CONNECTED'
0._last_connect_success = True
0._last_connect_ssid = 4
0.game_ui.wifi_status_message = 4
3 = 'fail'
7 = 'connect_fail'
8 = 7
0._connecting = False
0._last_connect_success = False
0._last_connect_ssid = None
return 'Wrong password'
return 'Network not found'
return 'Connection timeout'
return 'Connect failed'
return 'WiFi unavailable'
return 'Connect failed'
3 = 'status_label'
1 = 1
4 = 8947848
4 = 65280
4 = 16737792
return lv.SYMBOL.OK
5 = 65280
6 = 16777215
5 = 14540253
6 = 8947848
0._connecting = False
0._overlay_nav_to_settings = 2
0._overlay_timer = None
0._overlay_timer = None
0._overlay_nav_to_settings = False
2 = 0._overlay_nav_to_settings
0._overlay_nav_to_settings = False
1._scan_seq = 0._scan_seq
0._scan_nav_counter = 0._nav_counter
0._scanning = True
0._networks = []
0._page_index = 0
0._scanning = False
2 = None
2 = lv.obj.FLAG.HIDDEN
2 = None
3 = 0._status_overlay
1 = 0._list_view('rows')
2 = enumerate
0._scan_timer = None
return 2
0._scan_timer = None
6 = None
6 = 0
6 = 5
3 = None
3 = lv.obj.FLAG.HIDDEN
3 = None
1 = len(0._networks)
return PAGE_SIZE(1, PAGE_SIZE)
2 = 1
return (2.x1, 2.y1, 2.x2, 2.y2)
2 = 0._content_root
3 = None
3 = (1, 1)
4 = None
5 = None
4 = 'footer'
4 = 'footer'
6 = 1
7 = 3
5 = 7
8 = None
9 = None
10 = None
9 = 8
9 = None
10 = 8