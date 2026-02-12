# Decompiled from: fs_image/cactuscon/ui/panels/chat.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

gc = gc
lv = lvgl
ujson = ujson
network = network
time = time
bluetooth = bluetooth
BasePanel = BasePanel
ListContainer = ListContainer
Logger = Logger
config = config
generate_symkey1 = generate_symkey1
derive_symkey2 = derive_symkey2
derive_session_hash_and_key = derive_session_hash_and_key
default_device_id_generator = default_device_id_generator
BluetoothManager = BluetoothManager
CHAT_ADV_PREFIX = 'CC14PEER'
CHAT_SERVICE_UUID_TEMPLATE = 'CC14C001-0000-0000-0000-CAC71B072026'
CHAT_CHAR_UUID = 'CC14C002-C0DE-4BAD-9E14-CAC71B072026'
ubinascii = ubinascii
ubinascii = None
ChatPanel = __build_class__(<func_0>, 'ChatPanel', BasePanel)
__init__ = 0
set_api_client = <func_1>
create_ui = <func_2>
on_show = <func_3>
on_hide = <func_4>
on_cleanup = <func_5>
update = <func_6>
_on_back = <func_7>
_on_add_clicked = <func_8>
_refresh_chat_list = <func_9>
_last_message_ts = <func_10>
_on_chat_selected = <func_11>
_create_chat_modal = <func_12>
_open_chat_modal = <func_13>
_close_chat_modal = (None)
_on_chat_input_focus = <func_15>
_on_chat_send = (None)
_on_chat_scroll_end = <func_17>
_count_chat_messages = <func_18>
_render_chat_messages = (False)
_clear_chat_message_rows = <func_20>
_load_chat_batch = <func_21>
_set_chat_status = (False)
_prepend_chat_row = ('self')
_chat_row_color = <func_24>
_chat_sender_label = <func_25>
_format_message_ts = <func_26>
_format_chat_row_text = <func_27>
_is_scroll_at_bottom = <func_28>
_is_low_memory = <func_29>
_create_add_modal = <func_30>
_open_add_modal = <func_31>
_close_add_modal = (None)
_on_add_submit = <func_33>
_try_store_pending_session = <func_34>
_create_delete_modal = <func_35>
_create_confirm_modal = <func_36>
_open_delete_modal = <func_37>
_refresh_delete_list = <func_38>
_on_delete_chat = <func_39>
_on_delete_active_chat = <func_40>
_on_delete_done = <func_41>
_is_chat_empty = <func_42>
_ensure_keyboard = <func_43>
_show_keyboard = <func_44>
_hide_keyboard = <func_45>
_on_keyboard_ready = <func_46>
_on_keyboard_cancel = <func_47>
_on_confirm_name_focus = <func_48>
_on_ta_ready = <func_49>
_on_ta_cancel = <func_50>
_on_ta_defocus = <func_51>
_bt_reset_state = <func_52>
_bt_stop_all = <func_53>
_bt_start_scan = <func_54>
_bt_update_scan_state = <func_55>
_bt_start_receive = <func_56>
_bt_on_scan_result = <func_57>
_bt_refresh_list = <func_58>
_bt_select_device = <func_59>
_bt_on_server_data = <func_60>
_bt_on_client_data = <func_61>
_bt_finalize_pairing = <func_62>
_on_receive_toggle = <func_63>
_on_confirm_pair = <func_64>
_on_confirm_pressed = <func_65>
_on_cancel_pressed = <func_66>
_on_cancel_pair = <func_67>
_obj_show = <func_68>
_obj_hide = <func_69>
_keyboard_is_visible = <func_70>
_apply_keyboard_shift = <func_71>
_restore_keyboard_shift = <func_72>
_bind_keyboard_textarea = <func_73>
_get_screen_size = <func_74>
_update_layout = <func_75>
_get_abs_y = <func_76>
_position_keyboard = <func_77>
_warn_once = <func_78>
_get_event_target = <func_79>
_set_obj_enabled = <func_80>
_set_chat_api_buttons_enabled = <func_81>
_set_chat_composer_enabled = <func_82>
_create_modal = <func_83>
_show_modal = <func_84>
_hide_modal = <func_85>
_style_textarea = <func_86>
_spinner_pause = (60)
_get_local_device_id = <func_88>
_compact_device_id = <func_89>
_looks_like_device_id = <func_90>
_display_chat_handle = <func_91>
_canonical_device_id = <func_92>
_build_pairing_key = <func_93>
_wifi_connected = <func_94>
_ensure_wifi_connected = <func_95>
_ticks_ms = <func_96>
_ticks_diff = <func_97>
_schedule_wifi_rearm = <func_98>
_maybe_rearm_wifi = <func_99>
_maybe_poll_active_chat_session = <func_100>
_maybe_sync_remote_messages = <func_101>
return 0
1.logger = Logger(5)
1.api_client = None
1.wifi = None
1._chat_list = None
1._chat_buttons = {}
1._active_session_hash = None
1._chat_modal = None
1._chat_modal_title = None
1._chat_modal_content = None
1._chat_modal_messages = None
1._chat_input_ta = None
1._chat_send_btn = None
1._chat_status_label = None
1._chat_page_size = 10
1._chat_loaded_count = 0
1._chat_total_count = 0
1._chat_history_limited = False
1._add_modal = None
1._add_submit_btn = None
1._add_symkey_label = None
1._add_status = None
1._pairing_symkey1 = None
1._content_root = None
1._content_root_y0 = 0
1._kb_shift = 0
1._delete_modal = None
1._delete_list = None
1._delete_status = None
1._pending_session = None
1._keyboard = None
1._keyboard_hidden = True
1._kb_warned = set()
1._active_textarea = None
1.bt = None
1._bt_scanning = False
1._bt_receiving = False
1._bt_devices = []
1._bt_list_dirty = False
1._bt_selected = None
1._bt_local_symkey1 = None
1._bt_peer_symkey1 = None
1._bt_peer_device_id = None
1._bt_session_hash = None
1._bt_confirm_code = None
1._bt_list = None
1._bt_receive_btn = None
1._bt_confirm_btn = None
1._bt_cancel_btn = None
1._confirm_submit_btn = None
1._bt_code_label = None
1._bt_adv_label = None
1._confirm_modal = None
1._confirm_content = None
1._confirm_code_label = None
1._confirm_name_ta = None
1._confirm_status_label = None
1._confirm_hidden_for_spinner = False
1._api_action_inflight = False
1._chat_sync_interval_ms = 60000
1._last_chat_sync_ms = 0
1._active_chat_poll_interval_ms = 30000
1._last_active_chat_poll_ms = 0
1._last_chat_hide_ms = 0
1._wifi_rearm_delay_ms = 1200
1._wifi_rearm_ready_ms = 0
1._wifi_rearm_pending = False
0.api_client = 1
1 = 0.screen
2 = 1
3 = 0.screen
4 = 0.screen
5 = 4
0._chat_list = ListContainer(0.screen)
6 = 0.screen
7 = 200
8 = 0._chat_list.obj
7 = 8
0._chat_scroll_lane = 0.screen
0.game_ui.chat_has_unread = False
0._last_chat_sync_ms = 0
0._last_chat_hide_ms = 0
0._wifi_rearm_pending = False
0._last_chat_hide_ms = 0
0._wifi_rearm_pending = False
0._bt_list_dirty = False
0._chat_buttons = {}
1 = {}
1 = {}
2 = Exception
2 = None
3 = []
4 = 1
5 = None
6 = 4
4 = 3
7 = True
6 = 'reverse'
8 = 7
8 = 0
9 = 8
10 = lv.EVENT.CLICKED
10 = lv.EVENT.SHORT_CLICKED
11 = 0
return (0, 2)
return 1
2 = 1
3 = None
4 = 0
3 = id(2)
2 = 2
0._chat_modal = 0
1 = 0._chat_modal
0._chat_modal_content = 1
2 = 1
3 = 2
4 = 3
0._chat_modal_title = 2
5 = 2
6 = 5
7 = 2
8 = 7
0._chat_send_btn = 7
0._chat_input_ta = 1
0._chat_status_label = 1
0._chat_modal_messages = 1
0._active_session_hash = 1
0._content_root = 0._chat_modal_content
0._content_root_y0 = 0
0._kb_shift = 0
2 = 'Chat'
3 = {}
4 = 3
2 = 4
0._chat_loaded_count = 0
0._chat_total_count = 1
0._chat_history_limited = False
0._last_active_chat_poll_ms = 0
0._active_session_hash = None
0._last_active_chat_poll_ms = 0
0._content_root = 'add_content'
0._content_root_y0 = 0
0._kb_shift = 0
0._active_textarea = 0._chat_input_ta
2 = 0._active_session_hash
3 = 0.api_client
3 = 0._chat_input_ta
3 = Exception
4 = {}
5 = 'session_key'
0._api_action_inflight = True
6 = 3
7 = 6
8 = None
8 = 'ts'
1._chat_total_count = 0._chat_total_count
1._chat_loaded_count = 0._chat_loaded_count
9 = Exception
9 = None
0._api_action_inflight = False
0._chat_history_limited = True
return 0
return 1(0)
return 0
0._chat_loaded_count = 0
2 = 0._chat_page_size
3 = 2
4 = 0._chat_modal_messages
len(2)._chat_loaded_count = 0._chat_loaded_count
1 = 0
return []
4 = True
return []
5 = {}
6 = 'session_key'
7 = []
8 = 4
9 = 'msg'
10 = 9
11 = 'peer'
10 = 9
10 = '[decrypt error]'
12 = 'ts'
return 7
3 = 8947848
return False
4 = 0._chat_modal_messages
5 = 'sender'
return True
return False
return False
2 = 'peer'
return 65280
return 13421772
2 = 'peer'
return 'You'
3 = {}
return 'Peer'
1 = 1
2 = 4
3 = 7
4 = 10
5 = 13
6 = 16
7 = 19
return 7
return 17
2 = 'ts'
3 = 1
return 'text'
return False
return 2
return False
1 = gc
2 = gc
3 = 2
return False
return 0.1
return False
0._add_modal = 0
1 = 0._add_modal
0._content_root = 1
0._content_root_y0 = 0
0._kb_shift = 0
2 = 1
3 = 2
4 = 3
5 = 2
6 = 2
7 = 6
0._add_submit_btn = 6
8 = 1
0._add_symkey_label = 8
9 = 1
10 = 9
0._bt_receive_btn = 9
11 = 1
0._bt_adv_label = 11
12 = 1
0._bt_list = ?(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, lv, 1, lv, 100, lv, 100, 1, lv.ALIGN.TOP_MID, 0, 0, 1, 0, 0, 1, 0, 0, 1, lv.FLEX_FLOW.COLUMN, 1, 6, 0, 1, 8, 0, 1, 24, 0, 1, lv.obj.FLAG.SCROLLABLE, hasattr(1, 'set_scroll_dir'), hasattr(lv, 'DIR'), 1, lv.DIR.VER, hasattr(1, 'set_scrollbar_mode'), hasattr(lv, 'SCROLLBAR_MODE'), 1, lv.SCROLLBAR_MODE.AUTO, 1, 0.ui_elements, 'add_content', lv, 2, lv, 100, 2, 34, 2, 0, 0, 2, 0, 0, 2, lv.obj.FLAG.SCROLLABLE, 2, 0.ui_elements, 'add_header', lv, 3, 60, 28, 3, lv.ALIGN.LEFT_MID, 0, 0, 3, lv, 1710618, 0, 3, lv, 65280, 0, 3, 1, 0, 3, 0._close_add_modal, lv.EVENT.CLICKED, None, lv, 4, 'Back', 4, lv, 65280, 0, 4, lv, 5, 'Add Contact', 5, lv, 16776960, 0, 5, lv.ALIGN.CENTER, 0, 0, 5, 0.ui_elements, 'add_title', lv, 6, 60, 26, 6, lv.ALIGN.RIGHT_MID, 0, 0, 6, lv, 65280, 0, 6, lv, 65280, 0, 6, 1, 0, 6, 0._on_add_submit, lv.EVENT.CLICKED, None, lv, 7, 'Scan', 7, lv, 0, 0, 7, lv, 8, 'Key (share this): --', 8, lv, 65280, 0, 8, lv.obj.FLAG.HIDDEN, lv, 9, 120, 28, 9, lv, 1710618, 0, 9, lv, 65280, 0, 9, 1, 0, 9, 0._on_receive_toggle, lv.EVENT.CLICKED, None, lv, 10, 'Receive', 10, lv, 65280, 0, 10, lv, 11, 'Your peering ID: --', 11, lv.font_montserrat_12, 0, 11, lv, 13421772, 0, lv, 12, 'Nearby peers', 12, lv, 13421772, 0, ListContainer, 1, 'width', lv, 100, 'height', 120)
0._bt_code_label = 1
0._add_status = 0._add_modal
0._pending_session = None
1 = 0
2 = generate_symkey1
3 = 0.api_client
0._pairing_symkey1 = 'symkey1'
1 = 1
4 = Exception
0._pairing_symkey1 = 2()
4 = None
0._pairing_symkey1 = 2()
5 = None
2 = Exception
2 = None
return True
1 = 0.api_client.storage
2 = {}
3 = ujson(1)
return False
return True
0._delete_modal = 0
1 = 0._delete_modal
2 = 0._delete_modal
0._delete_list = 0._delete_modal
3 = 0._delete_modal
4 = 3
0._delete_status = 0._delete_modal
0._confirm_modal = 0
0._confirm_content = 0._confirm_modal
1 = 0._confirm_content
0._confirm_name_ta = 0._confirm_content
2 = 0._confirm_content
3 = 0._confirm_content
0._confirm_code_label = 3
4 = (1, 2, 3)
0._confirm_status_label = 0._confirm_content
5 = 0._confirm_content
6 = 5
7 = 6
8 = 5
9 = 8
1 = 0
2 = 1
3 = {}
4 = []
5 = 3
6 = 'sessions'
7 = 5
8 = 5
9 = <func_0>(4)
10 = <func_1>(4)
11 = 10
0._delete_buttons = {}
5 = 11
12 = 9
7 = <func_2>
8 = 'key'
13 = 0._delete_list
14 = 13
15 = 13
1 = 0
return 1
1 = 0
return 1
return 3
2 = 1
3 = id(2)
0._api_action_inflight = True
4 = Exception
0._api_action_inflight = False
4 = None
0._api_action_inflight = False
2 = 0._active_session_hash
0._api_action_inflight = True
3 = Exception
0._api_action_inflight = False
3 = None
0._active_session_hash = None
0._api_action_inflight = False
2 = 'session_hash'
0._pending_session = None
return 0
0._keyboard = 0.screen
1 = 0._active_textarea
2 = Exception
2 = None
0._active_textarea = 0._confirm_name_ta
0._active_textarea = None
0._active_textarea = None
0._active_textarea = None
0._bt_scanning = False
0._bt_receiving = False
0._bt_devices = []
0._bt_selected = None
0._bt_local_symkey1 = None
0._bt_peer_symkey1 = None
0._bt_peer_device_id = None
0._bt_session_hash = None
0._bt_confirm_code = None
0._bt_receiving = False
0._bt_scanning = True
1 = Exception
1 = None
0._bt_scanning = False
0._bt_receiving = True
0._bt_local_symkey1 = generate_symkey1()
1 = CHAT_SERVICE_UUID_TEMPLATE
0.bt.service_uuid = 1
0.bt.char_uuid = CHAT_CHAR_UUID
2 = 0
3 = 'UNKNOWN'
4 = Exception
4 = None
2 = 1.name
2 = 'utf-8'
1.name = 2
0._bt_list_dirty = True
1 = set()
2 = 0._bt_devices
3 = 'Unknown'
4 = (3, getattr(2, 'addr', None))
5 = 2.rssi
6 = 5
return 2
2 = 0.bt
0._bt_selected = 1
0._bt_local_symkey1 = generate_symkey1()
3 = 0
0.bt.service_uuid = CHAT_SERVICE_UUID_TEMPLATE
0.bt.char_uuid = CHAT_CHAR_UUID
4 = Exception
4 = None
0.bt.service_uuid = CHAT_SERVICE_UUID_TEMPLATE
0.bt.char_uuid = CHAT_CHAR_UUID
4 = 0
5 = 0._bt_local_symkey1
6 = Exception
6 = None
3 = bytes(2)
4 = 6
5 = 10
0._bt_peer_device_id = 4
0._bt_peer_symkey1 = 5
0._bt_local_symkey1 = generate_symkey1()
6 = Exception
6 = None
0._bt_peer_symkey1 = bytes(1)
2 = None
0._bt_peer_device_id = 2
3 = Exception
3 = None
1 = 0
2 = derive_symkey2(0._bt_local_symkey1, 0._bt_peer_symkey1, 1, 0._bt_peer_device_id)
3 = derive_session_hash_and_key(0._bt_local_symkey1, 0._bt_peer_symkey1, 2, 1, 0._bt_peer_device_id)
4 = 0._bt_local_symkey1
0._bt_session_hash = 3
5 = 10000
0._bt_confirm_code = 5
0._content_root = 0._confirm_content
0._content_root_y0 = 0
0._kb_shift = 0
6 = Exception
6 = None
0._api_action_inflight = True
0._api_action_inflight = False
2 = 0._confirm_name_ta
2 = Exception
0._api_action_inflight = False
0._confirm_hidden_for_spinner = True
0._confirm_hidden_for_spinner = False
0._api_action_inflight = False
3 = 0
4 = derive_symkey2(0._bt_local_symkey1, 0._bt_peer_symkey1, 3, 0._bt_peer_device_id)
5 = derive_session_hash_and_key(0._bt_local_symkey1, 0._bt_peer_symkey1, 4, 3, 0._bt_peer_device_id)
6 = 0._bt_peer_device_id
0._pending_session = 'peer_device_id'
0._confirm_hidden_for_spinner = False
7 = Exception
0._confirm_hidden_for_spinner = False
7 = None
0._api_action_inflight = False
0._content_root = 'add_content'
0._content_root_y0 = 0
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
1 = 0
2 = 0._keyboard
3 = 0._keyboard
4 = 0._keyboard
4 = 1(2, 2)
3 = 4
5 = 0._active_textarea
6 = 0._active_textarea
7 = 6
8 = 6
9 = 8
10 = 0
0._kb_shift = 10
0._kb_shift = 0
0._kb_shift = 0
1 = 0._active_textarea
return False
return False
2 = Exception
return False
2 = None
return True
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
return 0
2 = 1
return 2.y1
3 = 0
4 = 1
3 = 4
4 = 4
return 3
1 = 0
2 = 0._keyboard
1 = 240
2 = 320
3 = 2
3 = 140
return 1
return 1
2 = (0._add_submit_btn, 0._bt_confirm_btn, 0._confirm_submit_btn)
1 = 0.screen
return 1
1 = 0
2 = 0.api_client.auth
3 = 1(2)
return 3
2 = default_device_id_generator()
3 = 1(2)
return 3
4 = 0.wifi
return ':'(<func_1>(4))
5 = network.WLAN.IF_STA
4 = 'mac'
return ':'(<func_2>(4))
return 1
1 = 0
return 1
1 = 0
return 1
2 = <func_0>(1)
return 2
1 = 0
2 = 1
return len(2)(12)
return 'Unknown'
2 = 'handle'
3 = 'peer_device_id'
return 'Unknown'
return 'Unknown'
return 'Unknown'
return 2
3 = 1
2 = 3(range(0, 12, 2))
return 2
2 = 1
return 2
return '--'
return '--'
return '--'
3 = 'utf-8'
4 = 'utf-8'
return '='
return 0.wifi(0.wifi)
return False
return False
return 0.wifi
return False
return time
return time(1000)
return 2
return 2
1 = 0
2 = 0._last_chat_hide_ms
3 = 2
0._wifi_rearm_ready_ms = 3
0._wifi_rearm_pending = True
0._wifi_rearm_pending = True
0._wifi_rearm_ready_ms = 1
0._wifi_rearm_pending = False
1 = 0
0._wifi_rearm_pending = False
1 = 0
0._last_active_chat_poll_ms = 1
2 = True(0)
0._chat_total_count = 0._active_session_hash
1 = 0
0._last_chat_sync_ms = 1
2 = {}
2 = {}
3 = 0
4 = 2
3 = True(0)
0._chat_total_count = 0._active_session_hash