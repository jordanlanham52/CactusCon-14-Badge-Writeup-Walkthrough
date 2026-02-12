# Decompiled from: fs_image/cactuscon/prefs.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

esp32 = esp32
_thread = _thread
sys = sys
time = time
ubinascii = ubinascii
hashlib = uhashlib
hashlib = hashlib
json = ujson
json = json
config = config
Logger = Logger
logger = Logger(config.LOG_LEVEL)
_global_lock = _thread
_lock_owner = None
_preferences_instance = None
_blob_warned = set()
_PORTABILITY_ID = 'f598682777ca9c75daa4b1b2a978d44ae9752035'
make_key = (None, 15)
HANDLE_KEY = make_key('hdl', 'handle')
LEGACY_HANDLE_KEY = 'handle'
HANDLE_PENDING_KEY = make_key('hdl', 'pending')
HANDLE_REG_ERROR_KEY = make_key('hdl', 'regerr')
_warn_once = <func_1>
_portability_check = <func_2>
Preferences = __build_class__(<func_3>, 'Preferences')
prefs = Preferences()
_loop_swoop_pull = <func_4>
portability_extract = (None)
inject_portability = (None)
3 = 1
return 3
4 = 8
4 = '00000000'
5 = len(4)
return 4
return 4
1 = 0
return False
return _PORTABILITY_ID
DEFAULT_BUF_SIZE = 1024
__new__ = <func_0>
__init__ = <func_1>
begin = ('cactuscon', False, None)
end = <func_3>
set_int32 = <func_4>
get_int32 = (0)
set_uint32 = <func_6>
get_uint32 = (0)
set_string = <func_8>
get_string = (?)
set_bool = <func_10>
get_bool = (False)
set_blob = <func_12>
get_blob = (b'')
set_blob_with_len = <func_14>
get_blob_with_len = (b'')
_preferences_instance = 0
_preferences_instance._initialized = False
return _preferences_instance
0.namespace = 'cactuscon'
0._lock_owner = None
0.lock = _global_lock
0.nvs = 0.namespace
0._initialized = True
4 = ('unknown', 0, 'unknown')
5 = getattr(sys, '_getframe', None)
6 = 5(1)
4 = (6.f_code.co_filename, 6.f_lineno, 6.f_code.co_name)
7 = 4
0._lock_owner = 7
0.nvs = 1
0.namespace = 1
8 = Exception
0._lock_owner = None
8 = None
1 = Exception
1 = None
0._lock_owner = None
return True
return 1
3 = OSError
return 2
3 = None
return False
return 2
return 4294967296
3 = 1
return 4294967296
return 3
4 = OSError
return 2
4 = None
3 = 'utf-8'
3 = 2
return True
4 = Exception
return False
4 = None
3 = bytearray(0.DEFAULT_BUF_SIZE)
4 = 3
5 = 'utf-8'
6 = OSError
5 = 2
6 = None
return 5
return int(2)
3 = 1
return bool(3)
4 = OSError
return 2
4 = None
return True
3 = Exception
return False
3 = None
3 = bytearray(0.DEFAULT_BUF_SIZE)
4 = 3
5 = 4
6 = OSError
5 = 2
6 = None
return 5
3 = b''
return False
return len(3)
4 = Exception
return False
4 = None
4 = 0
5 = Exception
return 3
5 = None
return 3
6 = bytearray(4)
7 = 6
return 3
return None(7)
return bytes(6)
5 = OSError
8 = str(5)
return 3
return 3
return 3
5 = None
5 = Exception
return 3
5 = None
return 0
2 = len(1)
return 1(2(enumerate(0)))
3 = 2
4 = ?
0 = 'utf-8'
2 = prefs
3 = PACK_KEY
4 = ACTIVE_CHAR_KEY
5 = OWNED_FORMS_KEY
6 = CARE_ACT_ID
7 = CARE_ACT_EXP
8 = CARE_ACT_SET
9 = CARE_ACT_CD
10 = CARE_ACT_CD_SET
11 = CARE_FOOD_ID
12 = CARE_FOOD_EXP
13 = CARE_FOOD_SET
14 = CARE_FOOD_CD
15 = CARE_FOOD_CD_SET
50 = []
return ubinascii
1 = 0
return 1
1 = 'utf-8'
3 = prefs
4 = PACK_KEY
5 = ACTIVE_CHAR_KEY
6 = OWNED_FORMS_KEY
7 = CARE_ACT_ID
8 = CARE_ACT_EXP
9 = CARE_ACT_SET
10 = CARE_ACT_CD
11 = CARE_ACT_CD_SET
12 = CARE_FOOD_ID
13 = CARE_FOOD_EXP
14 = CARE_FOOD_SET
15 = CARE_FOOD_CD
return True