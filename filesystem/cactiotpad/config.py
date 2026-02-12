# Decompiled from: fs_image/cactiotpad/config.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

ConfigurationError = ConfigurationError
ClientConfig = __build_class__(<func_0>, 'ClientConfig')
DEFAULT_TIMEOUT = 10
DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_BACKOFF = 2.0
DEFAULT_DEVICE_TYPE = 'badge'
DEFAULT_DEVICE_VERSION = '1.0.0'
DEFAULT_VERIFY_SSL = True
DEFAULT_DEBUG = False
MAX_TIMEOUT = 60
MAX_RETRIES = 10
MIN_RETRY_BACKOFF = 1.0
MAX_RETRY_BACKOFF = 10.0
__init__ = (None, None, None, None, None, None, None, None, None, None, None)
_validate_url = <func_1>
_validate_timeout = <func_2>
_validate_max_retries = <func_3>
_validate_retry_backoff = <func_4>
__repr__ = <func_5>
0.base_url = 1
0.device_id = 2
0.device_id_generator = 3
0.device_type = 0.DEFAULT_DEVICE_TYPE
0.device_version = 0.DEFAULT_DEVICE_VERSION
0.nvs_lock = 6
0.verify_ssl = 0.DEFAULT_VERIFY_SSL
0.ca_cert = 8
0.timeout = 9
0.max_retries = 10
0.retry_backoff = 11
0.debug = 0.DEFAULT_DEBUG
1 = '/'
return 1
return 0.DEFAULT_TIMEOUT
1 = float(1)
return 1
return 0.DEFAULT_MAX_RETRIES
1 = int(1)
return 1
return 0.DEFAULT_RETRY_BACKOFF
1 = float(1)
return 1
return 0.debug