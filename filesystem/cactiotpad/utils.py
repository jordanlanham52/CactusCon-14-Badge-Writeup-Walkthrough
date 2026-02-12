# Decompiled from: fs_image/cactiotpad/utils.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

time = time
ujson = ujson
ValidationError = ValidationError
MAX_APPDATA_SIZE = 4096
MAX_USERDATA_SIZE = 1024
default_device_id_generator = <func_0>
compute_registration_pin = <func_1>
validate_json_size = ('data')
validate_appdata = <func_3>
validate_userdata = <func_4>
build_url = <func_5>
exponential_backoff = (30)
retry_with_backoff = (False)
safe_debug_print = <func_8>
0 = network
1 = ubinascii
2 = 0.STA_IF
3 = 'mac'
4 = 'utf-8'
return 4
5 = Exception
5 = None
2 = uhashlib
3 = 1
4 = 2
5 = 4
6 = ubinascii
7 = 'utf-8'
return 8
8 = Exception
8 = None
3 = 0
4 = 3('utf-8')
return 3
5 = Exception
5 = None
return validate_json_size(0, MAX_APPDATA_SIZE, 'appdata')
return validate_json_size(0, MAX_USERDATA_SIZE, 'userdata')
2 = '/'
3 = 1
3 = '/'
2 = 3
return 2
3 = 0
return min(3, 2)
4 = None
5 = 0
return 0()
6 = Exception
4 = 6
7 = exponential_backoff(5, 2)
6 = None