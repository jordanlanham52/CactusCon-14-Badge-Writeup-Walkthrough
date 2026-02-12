# Decompiled from: fs_image/cactiotpad/auth.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

urequests = urequests
ujson = ujson
RegistrationResponse = RegistrationResponse
AuthenticationError = AuthenticationError
NetworkError = NetworkError
APIError = APIError
compute_registration_pin = compute_registration_pin
build_url = build_url
safe_debug_print = safe_debug_print
DeviceAuth = __build_class__(<func_0>, 'DeviceAuth')
__init__ = <func_0>
request_nonce = (None)
complete_registration = (None)
register_device = (None)
get_api_key = <func_4>
has_api_key = <func_5>
get_device_id = <func_6>
delete_api_key = <func_7>
0.base_url = 1
0.storage = 2
0.config = 3
0.debug = 3.debug
6 = build_url(0.base_url, 'devices', 'register')
7 = 'handle'
8 = 0.config.timeout
9 = 8.status_code
10 = 8
11 = 10
return 11.nonce
12 = 8.text
13 = OSError
13 = None
13 = Exception
13 = None
7 = compute_registration_pin(1, 5)
8 = build_url(0.base_url, 'devices', 'register')
9 = 'pin'
10 = 0.config.timeout
11 = 10.status_code
12 = 10
13 = 12
return 13.api_key
14 = 10.text
15 = OSError
15 = None
15 = Exception
15 = None
6 = 5
7 = 5
return 7
return 0.storage
return 0.storage
return 0.storage
return True