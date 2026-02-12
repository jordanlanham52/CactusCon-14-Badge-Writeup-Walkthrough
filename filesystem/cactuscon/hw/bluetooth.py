# Decompiled from: fs_image/cactuscon/hw/bluetooth.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

bluetooth = bluetooth
network = network
struct = struct
time = time
_thread = _thread
const = const
Logger = Logger
config = config
logger = Logger(config.LOG_LEVEL)
STATE_IDLE = 0
STATE_SCANNING = 1
STATE_CONNECTING = 2
STATE_CONNECTED = 3
STATE_DISCONNECTING = 4
DEFAULT_SCAN_DURATION_MS = 2000
DEFAULT_SCAN_INTERVAL_US = 100000
DEFAULT_SCAN_WINDOW_US = 50000
DEFAULT_MAX_DEVICES = 12
DEFAULT_RSSI_THRESHOLD = -85
DEFAULT_RXBUF_SIZE = 256
AVAILABILITY_IDLE = 0
AVAILABILITY_OPEN = 1
AVAILABILITY_IN_BATTLE = 2
CACTUSCON_UUID_PREFIX_LE = bytes([1, 0, 20, 204])
CACTUSCON_UUID_SUFFIX_LE = bytes([38, 32, 7, 27, 199, 202])
CACTUSCON_DEVICE_MAX_TTL_MS = 25000
CACTUSCON_DEVICE_MIN_RSSI = -78
BluetoothDevice = __build_class__(<func_0>, 'BluetoothDevice')
BluetoothManager = __build_class__(<func_1>, 'BluetoothManager')
__slots__ = ('addr_type', 'addr', 'name', 'rssi', 'last_seen', 'availability', 'service_uuid_bytes')
__init__ = (None, -100, None, None)
addr_str = <func_1>
update = (None, None, None)
age_ms = <func_3>
is_cactuscon_badge = property(<func_4>)
is_available = <func_5>
get_embedded_mac = <func_6>
__repr__ = <func_7>
0.addr_type = 1
0.addr = 2
0.name = 'Unknown'
0.rssi = 4
0.last_seen = time
0.availability = 5
0.service_uuid_bytes = 6
return 0.addr
0.rssi = 1
0.last_seen = time
5 = 2
0.name = 5
0.availability = 3
0.service_uuid_bytes = 4
return 0.last_seen
return 1
return 0.service_uuid_bytes(6(12))
1 = '?'
return 1
CACTUSCON_UUID_PREFIX = b'\xcc\x14\x00\x01'
CACTUSCON_UUID_SUFFIX = b'\xca\xc7\x1b\x07 &'
format_address = staticmethod(<func_0>)
parse_address = staticmethod(<func_1>)
__init__ = (12, -85, 256, 20)
_irq_handler = <func_3>
_handle_scan_result = <func_4>
_handle_scan_done = <func_5>
_handle_connect = <func_6>
_handle_disconnect = <func_7>
_parse_name = <func_8>
_parse_service_uuids = <func_9>
has_service_uuid = <func_10>
start_scan = (2000, 100000, 50000, None, False)
stop_scan = <func_12>
is_scanning = <func_13>
get_nearby_devices = (None, None, None)
get_cactuscon_badges = (-78, 25000)
get_available_badges = (-78, 25000, None)
get_device_by_addr = <func_17>
clear_devices = <func_18>
uuid_to_bytes = staticmethod(<func_19>)
get_mac_address = staticmethod(<func_20>)
create_device_uuid = staticmethod((None))
extract_mac_from_uuid = staticmethod(<func_22>)
is_cactuscon_uuid = staticmethod(<func_23>)
start_advertising = (None, None, 0, 100000, None, None)
stop_advertising = <func_25>
_restart_advertising = <func_26>
connect = (0, 5000, None)
disconnect = <func_28>
reset_connection_state = <func_29>
is_connected = <func_30>
get_state = <func_31>
write_data = (True)
read_data = <func_33>
set_data_callback = <func_34>
set_disconnect_callback = <func_35>
process_pending = <func_36>
device_count = <func_37>
get_connection_info = <func_38>
deinit = <func_39>
setup_gatt_server = (None)
stop_gatt_server = <func_41>
is_server_running = <func_42>
get_server_connections = <func_43>
server_notify = (None)
set_server_data_callback = <func_45>
_handle_central_connect = <func_46>
_handle_central_disconnect = <func_47>
_handle_gatts_write = <func_48>
return <func_0>(0)
1 = 0
1 = ':'
return bytes(<func_0>(1))
2 = (ValueError, AttributeError)
2 = None
1 = 0
0.logger = Logger(4)
0.ble = bluetooth
5 = (ValueError, OSError)
5 = None
0.max_devices = 1
0.rssi_threshold = 2
0.devices = {}
0.lock = _thread
0.state = 0
0.scan_active = False
0.scan_callback = None
0.adv_active = False
0.adv_params = {}
0.conn_handle = None
0.connected_addr = None
0.connect_callback = None
0.disconnect_callback = None
0.data_callback = None
0._pending_connect = None
0.negotiated_mtu = 23
0.service_uuid = None
0.char_uuid = None
0.char_handle = None
0._service_start_handle = None
0._service_end_handle = None
0.server_running = False
0.server_service_handle = None
0.server_char_handle = None
0.server_connections = {}
0.server_data_callback = None
0._pending_server_data = []
0._pending_client_data = []
0._pending_disconnect = None
0.max_server_connections = 1
3 = 2
4 = 5
5 = 1
6 = ?
7 = ?
8 = 2
3 = 7
4 = 1
8 = 2
3 = 8
4 = 1
8 = 2
9 = 9
10 = 1
11 = 4
0._service_start_handle = 9
0._service_end_handle = 10
8 = 2
12 = 11
13 = 1
14 = 10
11 = 9
15 = bytes(11)
0.char_handle = 13
0.char_handle = 13
8 = 2
13 = 15
8 = 2
13 = 17
8 = 2
13 = 18
8 = 2
0.negotiated_mtu = 21
8 = 2
3 = '[BT-IRQ] CENTRAL_CONNECT'
4 = logger
8 = 2
3 = '[BT-IRQ] CENTRAL_DISCONNECT'
4 = logger
8 = 2
8 = 2
8 = 2
13 = 20
6 = bytes(2)
7 = None
8 = None
9 = None
10 = 4
11 = 0
12 = len(5)
13 = 11
14 = 1
15 = 13
7 = 'utf-8'
7 = 'utf-8'
9 = b'& \x07\x1b\xc7\xca'
8 = 16
11 = 13
return 1.rssi
0.scan_active = False
0.state = 0
4 = bytes(3)
0.conn_handle = 1
0.connected_addr = 4
0.state = 3
0._pending_connect = (1, 2, 4)
4 = bytes(3)
0.conn_handle = None
0.connected_addr = None
0.char_handle = None
0.state = 0
5 = 4
0._pending_disconnect = (1, 2, 4)
2 = 0
3 = 2
4 = 1
5 = 3
return 'utf-8'
2 = 3
return []
2 = []
3 = 0
4 = 3
5 = 1
6 = 4
7 = 0
8 = 0
7 = 0
9 = 7(16)
10 = [8, 10, 9, 10, 16]
3 = 4
return 2
return False
3 = 2
return 3
return False
return False
0.scan_callback = 4
0.scan_active = True
0.state = 1
return True
6 = Exception
0.scan_active = False
0.state = 0
return False
6 = None
return False
0.scan_active = False
0.state = 0
return True
1 = Exception
return False
1 = None
return 0.scan_active
1 = 0.rssi_threshold
4 = list(0.devices)
4 = 2(4)
4 = 1(4)
4 = 3
return 4
2 = 1
return 2
2 = 1
return 2
return 0.rssi
3 = 2
return <func_0>(3)
1 = 0
return 1
1 = -70
4 = 2
5 = <func_0>(4)
5 = 3
return 5
1 = 0
return 1
1 = 1
return 1
1 = str(0)
1 = -2
1 = -2
2 = int(1, 16)
2 = int(1, 16)
return 2
3 = '-'
4 = 3
return bytes(reversed(4))
1 = 0
0 = network.STA_IF
1 = 'mac'
return bytes(1)
1 = BluetoothManager
2 = str(0)
2 = -2
3 = <func_0>(1)
4 = '-'
5 = 4
return 5
1 = 0
return 0(6(12))
1 = str(0)
1 = -2
2 = '-'
3 = 3
return 3
return False
return CACTUSCON_UUID_SUFFIX_LE
1 = 'Badge'
7 = bytearray()
8 = 'utf-8'
9 = min(len(8), 20)
10 = 9
11 = bytearray()
12 = 6
13 = 6
14 = 12
15 = len(13)
15 = len(13)
12 = 2
14 = 12
15 = len(5)
7 = bytearray(b'\x02\x01\x06')
return False
0.adv_active = True
0.adv_params = 'service_data'
return True
return False
return True
0.adv_active = False
return True
1 = Exception
return False
1 = None
1 = 1
return False
0.connect_callback = 4
0.state = 2
5 = 1
return True
6 = Exception
0.state = 0
return False
6 = None
return False
1 = 0.conn_handle
0.state = 4
return True
2 = Exception
0.state = 3
return False
2 = None
0.conn_handle = None
0.connected_addr = None
0.char_handle = None
0._pending_connect = None
0._service_start_handle = None
0._service_end_handle = None
0.negotiated_mtu = 23
0.state = 0
return 0.state
3 = None
4 = None
5 = False
return False
return False
3 = 0.conn_handle
4 = 0.char_handle
6 = 0
7 = 6
return True
8 = OSError
return False
8 = None
8 = Exception
return False
8 = None
return False
1 = 0.conn_handle
2 = 0.char_handle
return True
3 = Exception
return False
3 = None
0.data_callback = 1
0.disconnect_callback = 1
1 = False
2 = len(0._pending_client_data)
3 = len(0._pending_server_data)
4 = None
4 = 0._pending_connect
0._pending_connect = None
1 = True
5 = 4
6 = 0.connect_callback
7 = 4
8 = Exception
8 = None
1 = True
5 = 0
9 = 0._pending_server_data
8 = Exception
8 = None
1 = True
9 = 0
8 = Exception
8 = None
10 = None
10 = 0._pending_disconnect
0._pending_disconnect = None
1 = True
5 = 10
6 = 0.disconnect_callback
7 = 10
8 = Exception
8 = None
return 1
return len(0.devices)
return 'state'
return True
3 = bluetooth.FLAG_NOTIFY
4 = 0.adv_active
5 = 0.scan_active
6 = (1, ((2, 3)))
7 = (6)
0.server_service_handle = 0
0.server_char_handle = 0
0.server_running = True
return True
8 = Exception
return False
8 = None
return True
1 = list(0.server_connections)
0.server_running = False
0.server_char_handle = None
0.server_service_handle = None
return True
return 0.server_running
return list(0.server_connections)
return False
3 = list(0.server_connections)
4 = 3
5 = Exception
5 = None
return True
5 = Exception
return False
5 = None
0.server_data_callback = 1
4 = bytes(3)
5 = 4
6 = Exception
6 = None
0.conn_handle = 1
0.connected_addr = 4
0.state = 3
4 = bytes(3)
5 = 4
0.conn_handle = None
0.connected_addr = None
0.state = 0
0._pending_disconnect = (1, 2, 4)
3 = 2
4 = Exception
4 = None