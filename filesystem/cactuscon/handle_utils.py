# Decompiled from: fs_image/cactuscon/handle_utils.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

re = re
HANDLE_MIN_LEN = 3
HANDLE_MAX_LEN = 18
HANDLE_PATTERN = '^[a-zA-Z0-9]+[-_\\sa-zA-Z0-9]*[a-zA-Z0-9]+$'
normalize_handle = <func_0>
validate_handle = <func_1>
0 = 'utf-8'
0 = str(0)
return Exception
return 0
1 = normalize_handle(0)
return (False, 1, 'Please enter a handle')
2 = len(1)
return (1, 'Handle must be %d+ characters', HANDLE_MIN_LEN)
return (1, 'Handle must be %d or fewer chars', HANDLE_MAX_LEN)
return (False, 1, "Letters/numbers only; '-', '_', spaces in middle")
return (1, True, 1)