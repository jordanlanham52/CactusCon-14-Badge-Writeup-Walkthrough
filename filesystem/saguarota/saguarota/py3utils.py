# Decompiled from: fs_image/saguarota/saguarota/py3utils.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

os = os
json = json
hashlib = hashlib
Path = Path
HTTPServer = HTTPServer
BaseHTTPRequestHandler = BaseHTTPRequestHandler
unquote = unquote
threading = threading
Optional = Optional
OTAManifestBuilder = __build_class__(<func_0>, 'OTAManifestBuilder')
OTAManifestServer = __build_class__(<func_1>, 'OTAManifestServer')
__init__ = <func_0>
calculate_md5 = <func_1>
get_file_version = <func_2>
generate_manifest = <func_3>
0.src_dir = Path(1)
2 = hashlib
4 = open(1, 'rb')
3 = iter(4, b'')
return 2
return 4096
return int(1.st_mtime)
1 = '.c'
2 = 'test_'
3 = 'tests'
4 = []
15 = True
5 = 'followlinks'
6 = 0.src_dir
16 = 6
7 = Path(16).suffix
8 = 16
9 = 0.src_dir
10 = '/'
11 = 8
12 = 8
13 = ?(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '.py', '.mpy', '.raw', '.rgb565', '__pycache__', 'examples', 'docs', os, 7, 1(any(2)), any(15(3)), Path(15), 8, str(9), '\\', {0, 0, 4}, 10, 'path', 12, 'version', 11, 'md5', max, <func_2>(4), 'default', 0)
14 = 'files'
return 2
2 = 1
2 = 1
1 = 0
__init__ = ('localhost', 8000)
_Handler = __build_class__(<func_1>, '_Handler', BaseHTTPRequestHandler)
start = (False)
stop = <func_3>
0.src_dir = Path(1)
0.host = 2
0.port = 3
0.builder = OTAManifestBuilder(0.src_dir)
0.httpd = None
0._thread = None
do_GET = <func_0>
log_message = <func_1>
1 = unquote(0.path)
2 = 0.server.builder
3 = None
4 = 3
5 = open(4, 'rb')
6 = 5
7 = 'application/octet-stream'
7 = 'text/plain'
7 = 'application/json'
0.httpd = HTTPServer((0.host, 0.port), 0._Handler)
0.httpd.src_dir = 0.src_dir
0.httpd.builder = 0.builder
0._thread = True