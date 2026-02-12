# Decompiled from: fs_image/cactiotpad/storage.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

esp32 = esp32
ujson = ujson
StorageError = StorageError
SecureStorage = __build_class__(<func_0>, 'SecureStorage')
NAMESPACE = 'cactiotpad'
API_KEY_KEY = 'api_key'
DEVICE_ID_KEY = 'device_id'
CHAT_SESSIONS_KEY = 'chat_sessions'
__init__ = (None, False)
_acquire_lock = <func_1>
_release_lock = <func_2>
store_api_key = <func_3>
retrieve_api_key = <func_4>
delete_api_key = <func_5>
has_api_key = <func_6>
store_device_id = <func_7>
retrieve_device_id = <func_8>
delete_device_id = <func_9>
_read_json_blob = <func_10>
_write_json_blob = <func_11>
get_chat_sessions = <func_12>
set_chat_sessions = <func_13>
update_chat_session = <func_14>
0.lock = 1
0.debug = 2
0.nvs = None
0.nvs = 0.NAMESPACE
3 = Exception
3 = None
2 = 'utf-8'
return True
3 = Exception
3 = None
1 = bytearray(256)
2 = 1
3 = 'utf-8'
return 3
4 = Exception
4 = None
return True
1 = Exception
1 = None
1 = 0
return 0
return False
2 = 'utf-8'
return True
3 = Exception
3 = None
1 = bytearray(256)
2 = 1
3 = 'utf-8'
return 3
4 = Exception
4 = None
return True
1 = Exception
1 = None
3 = bytearray(4096)
4 = 3
return 2
5 = 'utf-8'
return 5
return 2
6 = Exception
6 = None
3 = 2
return True
4 = Exception
4 = None
return 'sessions'
return 1
3 = 0
return 3