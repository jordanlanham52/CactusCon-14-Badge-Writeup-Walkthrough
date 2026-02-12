# Decompiled from: fs_image/cactuscon/registration.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

Logger = Logger
config = config
logger = Logger(config.LOG_LEVEL)
RegistrationState = __build_class__(<func_0>, 'RegistrationState')
STATE_INIT = 'init'
STATE_HANDLE_INPUT = 'handle_input'
STATE_REGISTERING = 'registering'
STATE_SUCCESS = 'success'
STATE_ERROR = 'error'
COLOR_YELLOW = 65504
COLOR_GREEN = 2016
COLOR_RED = 63488
COLOR_WHITE = 65535
__init__ = <func_0>
start = <func_1>
update = <func_2>
submit_handle = <func_3>
_register_device = <func_4>
is_complete = <func_5>
is_success = <func_6>
cleanup = <func_7>
0.api_client = 1
0.screen = 2
0.device_id = 3
0.state = 0.STATE_INIT
0.handle = None
0.error_message = None
0.state = 0.STATE_HANDLE_INPUT
0.screen.keyboard_active = True
return True
return True
return False
1 = 0.screen.keyboard
0.handle = 1
0.state = 0.STATE_REGISTERING
1 = 0.handle
0.state = 0.STATE_SUCCESS
2 = Exception
0.error_message = str(2)
0.state = 0.STATE_ERROR
2 = None
return (0.STATE_SUCCESS, 0.STATE_ERROR)
return 0.STATE_SUCCESS
0.screen.keyboard.locked = False
0.screen.keyboard.waiting = False
0.screen.keyboard_active = False