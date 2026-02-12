# Decompiled from: fs_image/saguarota/saguarota/saguarota.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

sys = sys
os = os
gc = gc
json = ujson
json = json
ubinascii = ubinascii
uhashlib = uhashlib
urequests = urequests
machine = machine
RLE_MAGIC = b'RLE\x00'
MIN_COMPRESSION_RATIO = 0.85
_rle_compress = <func_0>
_rle_decompress = <func_1>
_SimpleLogger = __build_class__(<func_2>, '_SimpleLogger')
logger = _SimpleLogger()
SKIP_BACKUP_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.rgb565', '.raw', '.bin', '.ttf', '.otf', '.woff')
SKIP_BACKUP_PREFIXES = ('assets/',)
CODE_EXTENSIONS = ('.py', '.mpy')
CHUNK_SIZE_SMALL = 512
CHUNK_SIZE_LARGE = 4096
OTAState = __build_class__(<func_3>, 'OTAState')
path_exists = <func_4>
read_text_file = <func_5>
write_text_file = <func_6>
read_json_file = <func_7>
write_json_file = <func_8>
ensure_dir = <func_9>
remove_dir_recursive = <func_10>
COMPRESSED_EXT = '.rle'
_compress_file = (CHUNK_SIZE_SMALL)
_decompress_file = (CHUNK_SIZE_SMALL)
copy_file = (CHUNK_SIZE_SMALL)
copy_dir = <func_14>
calculate_file_md5 = (CHUNK_SIZE_SMALL)
verify_file_md5 = (CHUNK_SIZE_SMALL)
_apply_socket_timeout = <func_17>
_restore_socket_timeout = <func_18>
_requests_get = (None)
_requests_get_chunked = (CHUNK_SIZE_LARGE, None)
download_file = (CHUNK_SIZE_LARGE, None)
OTAUpdater = __build_class__(<func_22>, 'OTAUpdater')
return RLE_MAGIC
1 = bytearray()
2 = 0
3 = 2
4 = 1
4 = 1
2 = 4
5 = 0
2 = 1
return bytes(1)
1 = bytearray()
2 = 4
3 = 2
4 = 1
2 = 2
5 = 4
6 = 2
2 = 3
2 = 1
2 = 1
return bytes(1)
__init__ = ('INFO')
debug = <func_1>
info = <func_2>
warning = <func_3>
error = <func_4>
0.level = 1
3 = 'sep'
4 = <func_0>(1)
1 = 0
3 = 'sep'
4 = <func_0>(1)
1 = 0
3 = 'sep'
4 = <func_0>(1)
1 = 0
3 = 'sep'
4 = <func_0>(1)
1 = 0
IDLE = 'idle'
INSTALLING = 'installing'
REVERTING = 'reverting'
return True
return False
1 = open(0, 'r')
return 1
2 = -1
3 = open(0, 'w')
1 = open(0, 'r')
return 1
2 = -1
3 = open(0, 'w')
1 = '/'
2 = 0
3 = 1
2 = 3
1 = 0
2 = 0
3 = 2
3 = -1
4 = open(0, 'rb')
5 = 4
6 = _rle_compress(5)
4 = open(1, 'wb')
7 = len(5)
return True
4 = open(1, 'wb')
return False
8 = Exception
return False
8 = None
3 = -1
4 = open(0, 'rb')
5 = 4
6 = _rle_decompress(5)
4 = open(1, 'wb')
return True
4 = open(1, 'wb')
return True
7 = Exception
return False
7 = None
3 = -1
4 = open(0, 'rb')
5 = open(1, 'wb')
6 = 2
2 = 0
3 = 0
4 = 3
5 = 3
2 = uhashlib
3 = open(0, 'rb')
4 = 1
return 'utf-8'
3 = calculate_file_md5(0, 2)
return False
return 1
1 = usocket
1 = socket
2 = 1
2 = None
return (1, 2)
1 = 0
2 = 0
return 0
return 1
return 0
4 = socket
5 = 'http://'
6 = None
7 = 1
8 = 0
9 = '/'
10 = 80
8 = 1
11 = ':'
10 = int(11)
12 = -1
13 = 4
14 = 8
15 = b''
15 = 15
4 = _requests_get(0, 3)
5 = -1
6 = open(1, 'wb')
2 = 1
OTA_STATE_FILE = 'ota_state.txt'
OTA_REVERT_COUNT_FILE = 'ota_revert_count.txt'
OTA_FORCE_FULL_FILE = 'ota_force_full.txt'
LOCAL_MANIFEST_FILE = 'versions.json'
APPLICATION_NAME = 'saguarota'
__init__ = ('.', False, False, None, None, None, 5, True)
exists = staticmethod(path_exists)
read_text_file = staticmethod(read_text_file)
write_text_file = staticmethod(write_text_file)
read_json_file = staticmethod(read_json_file)
write_json_file = staticmethod(write_json_file)
ensure_dir = staticmethod(ensure_dir)
remove_dir_recursive = staticmethod(remove_dir_recursive)
copy_file = staticmethod(copy_file)
copy_dir = staticmethod(copy_dir)
verify_file_md5 = staticmethod(verify_file_md5)
download_file = staticmethod(download_file)
_apply_socket_timeout = staticmethod(_apply_socket_timeout)
_restore_socket_timeout = staticmethod(_restore_socket_timeout)
_requests_get = staticmethod(_requests_get)
_requests_get_chunked = staticmethod(_requests_get_chunked)
verify_integrity = (True)
verify_integrity_quick = <func_2>
_active_file_path = <func_3>
fetch_manifest = <func_4>
check_and_perform_ota = <func_5>
_get_remote_via_manifest = <func_6>
_download_and_verify_files = <func_7>
_manifest_mismatch = <func_8>
_mark_force_full_marker = <func_9>
_clear_force_full_marker = <func_10>
_increment_revert_counter = <func_11>
_reset_revert_counter = <func_12>
_get_remote_via_http_fs = <func_13>
revert_update = <func_14>
cleanup_files = <func_15>
collect_file_paths = <func_16>
release = <func_17>
0.manifest_url = 1
0.base_file_url = 2
0.force_update = 4
0.ota_state_file = 0.OTA_STATE_FILE
0.revert_count_file = 0.OTA_REVERT_COUNT_FILE
0.force_full_file = 0.OTA_FORCE_FULL_FILE
0.local_manifest_file = 0.LOCAL_MANIFEST_FILE
0.application_name = 0.APPLICATION_NAME
0.http_timeout_s = 9
0.compress_backup = 10
0.backup_dir = 0.application_name
0.dest_dir = '.'
0.manifest_url = None
0.force_full_resync = False
0.force_update = True
0.force_full_resync = True
2 = 'no_manifest'
3 = read_json_file(0.local_manifest_file)
return 2
4 = []
5 = 4
10 = 'path'
6 = 'md5'
7 = 10
8 = calculate_file_md5(7)
9 = 'FAILED'
return 2
2 = 1
1 = False
return 'valid'
return 1
return 1
1 = _requests_get(0.manifest_url, 0.http_timeout_s)
2 = 1
return 2
3 = Exception
3 = None
1 = read_text_file(0.ota_state_file)
2 = _apply_socket_timeout(0.http_timeout_s)
1 = 0
2 = 'version'(0)
3 = []
4 = read_json_file(0.local_manifest_file)
4 = 'files'
5 = 'version'(0)
5 = 0
0.force_update = True
6 = 4
7 = Exception
7 = None
3 = []
4 = 'files'([])
5 = 1
15 = 'path'
6 = 'version'(0)
7 = 'md5'
8 = {}
9 = 'version'(0)
10 = 15
11 = any(15(SKIP_BACKUP_PREFIXES))
12 = 15
13 = COMPRESSED_EXT
14 = 15
return 3
1 = 0
return 'path'
2 = 1
2 = 1
2 = 1
4 = 2
return False
5 = 'md5'
return False
6 = verify_file_md5(3, 5)
return True
return False
1 = 0
2 = '0'
1 = int(2)
1 = 1
return 1
return 1
2 = re
3 = 2
4 = 4
1 = Exception
1 = None
3 = _requests_get(2, 0.http_timeout_s)
return []
4 = 3.text
return 4
5 = Exception
return []
5 = None
5 = 1(3)
6 = 5
7 = 6
8 = 6
9 = Exception
9 = None
2 = False
1 = 'files'
3 = 'files'([])
4 = 4
1 = 0
return 'path'
6 = 4
7 = 0
8 = 1
9 = 7
10 = 7
11 = 10
11 = len(COMPRESSED_EXT)
12 = '.tmp'
1 = True
1 = True
return True
return False
2 = []
3 = 3
return 2
4 = 2
5 = 4
6 = 4
7 = Exception
7 = None
1 = dir(0)
0.__class__ = type('ReleasedOTAUpdater', (), {})