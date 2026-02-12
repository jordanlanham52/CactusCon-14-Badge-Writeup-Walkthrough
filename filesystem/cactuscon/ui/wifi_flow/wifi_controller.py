# Decompiled from: fs_image/cactuscon/ui/wifi_flow/wifi_controller.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

time = time
network = network
network = None
STAT_IDLE = 0
STAT_CONNECTING = 1
STAT_WRONG_PASSWORD = -3
STAT_NO_AP_FOUND = -2
STAT_CONNECT_FAIL = -1
STAT_GOT_IP = 3
_now_ms = <func_0>
_elapsed_ms = <func_1>
_decode_ssid = <func_2>
WifiController = __build_class__(<func_3>, 'WifiController')
return time
return time(1000)
return 0
return 0
return 0
return 'utf-8'
return 'latin-1'
return Exception
return str(0)
return Exception
__init__ = (None, None)
set_wifi_manager = <func_1>
get_last_error = <func_2>
get_last_scan_ms = <func_3>
get_networks = <func_4>
refresh_scan = <func_5>
disconnect = <func_6>
start_connect = (15)
cancel_connect = <func_8>
poll_connect = <func_9>
_get_wlan = <func_10>
_safe_status = <func_11>
_is_connected = <func_12>
_status_reason = <func_13>
_normalize_scan = <func_14>
0._wifi_mgr = 1
0._wlan = None
0._networks = []
0._last_error = None
0._last_scan_ms = None
0._connect_active = False
0._connect_started_ms = None
0._connect_timeout_ms = None
0._connect_ssid = None
0._connect_password = None
0._last_status = None
0._logger = 2
0._wifi_mgr = 1
0._wlan = None
return 0._last_error
return 0._last_scan_ms
return list(0._networks)
0._last_error = None
1 = 0
0._networks = []
0._last_error = 'wlan unavailable'
return 0._networks
2 = 1
3 = Exception
0._networks = []
0._last_error = 3
return 0._networks
3 = None
0._networks = 2
0._last_scan_ms = _now_ms()
return 0._networks
0._last_error = None
1 = 0
0._last_error = 'wlan unavailable'
return False
return True
2 = Exception
0._last_error = 2
return False
2 = None
0._last_error = None
4 = 0
0._last_error = 'wlan unavailable'
return False
5 = Exception
0._last_error = 5
return False
5 = None
0._connect_active = True
0._connect_started_ms = _now_ms()
0._connect_timeout_ms = 3(1000)
0._connect_ssid = 1
0._connect_password = 2
0._last_status = None
return True
0._connect_active = False
0._connect_started_ms = None
0._connect_timeout_ms = None
return 'state'
1 = 0
0._connect_active = False
return 'reason'
0._connect_active = False
return 'reason'
2 = 1
0._last_status = 2
0._connect_active = False
return 'reason'
0._connect_active = False
return 'reason'
3 = _elapsed_ms(0._connect_started_ms)
0._connect_active = False
return 'reason'
return 'status'
return 0._wlan
0._wlan = 0._wifi_mgr.wlan
return 0._wlan
0._wlan = 0._wifi_mgr
return 0._wlan
0._wlan = network.STA_IF
return 0._wlan
return 1
2 = 0
return True
return True
return False
return 'wrong_password'
return 'no_ap'
return 'connect_fail'
return 'got_ip'
return 'connecting'
return 'idle'
return 1
2 = {}
3 = []
4 = 0
5 = None
6 = None
7 = None
8 = _decode_ssid(4)
8 = '<hidden>'
9 = int(5)
9 = -999
10 = 'raw'
11 = 8
12 = list(2)
return 12
return -999