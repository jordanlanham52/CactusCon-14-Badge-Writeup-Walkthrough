# Decompiled from: fs_image/thirdparty/xglcd_font.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

ceil = ceil
floor = floor
XglcdFont = __build_class__(<func_0>, 'XglcdFont', object)
BIT_POS = 256
__init__ = (32, 96)
__load_xglcd_font = <func_1>
lit_bits = <func_2>
get_letter = (0, False)
measure_text = (1)
0.width = 2
0.height = max(3, 8)
0.start_letter = 4
0.letter_count = 5
0.bytes_per_letter = 1
2 = 0.bytes_per_letter
0.letters = 2(0.letter_count)
3 = memoryview(0.letters)
4 = 0
5 = open(1, 'r')
6 = 5
6 = 6
7 = '//'
6 = 7
6 = 1
4 = 2
1 = 0
2 = 1
1 = 2
5 = 0.start_letter
return (b'', 0, 0)
6 = 0.bytes_per_letter
7 = 6
8 = 7(6)
9 = 0
10 = 0.height
11 = 9
12 = 'big'(11)
12 = 11(2)
13 = 'big'
14 = 2
15 = 2
15 = 16
15 = 2
6 = 10(8)
15 = 2
15 = 1
return (12, 9, 10)
3 = 0
4 = 1
5 = 0.start_letter
6 = 0.bytes_per_letter
3 = 2
return 3