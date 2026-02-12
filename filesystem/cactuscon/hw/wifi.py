# Decompiled from: fs_image/cactuscon/hw/wifi.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

Logger = Logger
config = config
logger = Logger(config.LOG_LEVEL)
asyncio = asyncio
network = network
time = time
prefs = prefs
config = config
WIFI_PERSIST_DEBUG = False
_WIFI_SAVED_FLAG_KEY = 'wifi_saved'
_WIFI_SAVED_SSID_KEY = 'wifi_ssid'
_WIFI_SAVED_PASS_KEY = 'wifi_pass'
_WIFI_SAVED_FAIL_KEY = 'wifi_fail'
_log_persist = (None)
load_saved_credentials = <func_1>
save_credentials = <func_2>
clear_saved_credentials = <func_3>
load_saved_failure_count = <func_4>
increment_saved_failure = <func_5>
reset_saved_failure = <func_6>
WiFiManager = __build_class__(<func_7>, 'WiFiManager')
0 = False
1 = _WIFI_SAVED_SSID_KEY
2 = _WIFI_SAVED_PASS_KEY
3 = Exception
return (None, None)
3 = None
return (None, None)
return (1, 2)
return False
return True
2 = Exception
return False
2 = None
return True
0 = Exception
return False
0 = None
0 = 0
1 = Exception
return 0
1 = None
return 0
0 = 0
0 = 1
return 0
1 = Exception
return 0
1 = None
return True
0 = Exception
return False
0 = None
__init__ = <func_0>
_now_ms = <func_1>
_elapsed_ms = <func_2>
_log_snapshot = (False)
_status_is_connecting = <func_4>
_driver_reset = ('reset')
connect = (None, None, None, False, True)
scan = <func_7>
set_auto_reconnect = <func_8>
get_auto_reconnect = <func_9>
cancel_connect = ('cancelled')
disconnect = <func_11>
is_connected = <func_12>
get_ip = <func_13>
get_mac = <func_14>
get_ssid = <func_15>
get_rssi = <func_16>
get_channel = <func_17>
get_bssid = <func_18>
get_authmode = <func_19>
get_link_info = <func_20>
get_status_snapshot = <func_21>
_schedule_reconnect = (None, None)
_reset_reconnect_backoff = <func_23>
mark_connected = ('init')
loop = <func_25>
loop_forever = <func_26>
0.logger = Logger(config.LOG_LEVEL)
0.wlan = network.WLAN.IF_STA
0.connecting = False
0._auto_reconnect = True
0._connect_started_ms = None
0._connect_timeout_s = getattr(config, 'WIFI_CONNECT_TIMEOUT_S', 10)
0._last_snapshot = None
0._reconnect_backoff_ms = getattr(config, 'WIFI_RECONNECT_BACKOFF_MS', 1000)
0._reconnect_backoff_max_ms = getattr(config, 'WIFI_RECONNECT_BACKOFF_MAX_MS', 15000)
0._next_reconnect_ms = 0
0._reconnect_attempts = 0
0._missing_ssid_logged = False
0._busy_since_ms = None
return time
return time(1000)
return 0
return 1
return 1
3 = 0
0._last_snapshot = 3
return False
return True
return True
return False
6 = load_saved_credentials()
7 = None
1 = 6
2 = 7
1 = getattr(config, 'OTA_WIFI_SSID', None)
2 = getattr(config, 'OTA_WIFI_PASSWORD', None)
3 = getattr(config, 'WIFI_CONNECT_TIMEOUT_S', 10)
0._auto_reconnect = bool(5)
0._missing_ssid_logged = True
8 = 0.wlan
8 = None
0.connecting = True
0._connect_timeout_s = 3
0._connect_started_ms = 0
0.connecting = False
0._connect_started_ms = None
9 = Exception
0.connecting = False
0._connect_started_ms = None
9 = None
return 0.wlan
1 = Exception
return []
1 = None
0._auto_reconnect = bool(1)
return bool(0._auto_reconnect)
0.connecting = False
0._connect_started_ms = None
0.connecting = False
0._auto_reconnect = False
0._connect_started_ms = None
return 0.wlan
return 0
return 'mac'
return 'essid'
return 'rssi'
return 'channel'
return 'bssid'
return 'authmode'
return 'authmode'
1 = 'active'
return 1
1._reconnect_attempts = 0._reconnect_attempts
2 = 0._reconnect_attempts(1, 0._reconnect_backoff_max_ms)
0._reconnect_attempts = 0
0._next_reconnect_ms = int(2)
0._reconnect_attempts = 0
0._next_reconnect_ms = 0
0._missing_ssid_logged = False
0._busy_since_ms = None
0.connecting = False
0._connect_started_ms = None
0.connecting = False
0._connect_started_ms = None
1 = 0._connect_started_ms
2 = 0
3 = 0.wlan
3 = None
0._busy_since_ms = 2
0._busy_since_ms = None
0._busy_since_ms = None
4 = Exception
4 = None