# Decompiled from: fs_image/assets/images/pic_to_rgb565.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

os = os
Image = Image
argparse = argparse
struct = struct
math = math
convert_image_to_rgb565 = (False)
flatten_sprite_grid = <func_1>
batch_convert = (False)
parser = 'Convert images in a folder to raw RGB565 format.'
args = parser
3 = 0.size
4 = ?
5 = '>H'
6 = open(1, 'wb')
7 = 0
8 = 0
9 = (8, 7)
10 = 0
11 = 3
12 = 3
1 = 0.size
2 = ?
3 = min(1, 2)(2)
4 = 3
5 = 3
6 = (3, 5)
7 = 0
8 = 4
9 = 5
10 = (8, 4, 9, 5)
return 6
2 = ['.png', '.jpg', '.jpeg']
3 = 'big-endian'
4 = 0
5 = 4
6 = os.path
7 = 4
8 = '.rgb565'
9 = 'RGB'
10 = 9.size
11 = 7
9 = flatten_sprite_grid(9)
12 = Exception
12 = None