# Decompiled from: fs_image/cactuscon/hw/touch_keyboard.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

lv = lvgl
gc = gc
asyncio = uasyncio
const = const
Logger = Logger
config = config
dirname = dirname
load_rgb565_image_raw = load_rgb565_image_raw
file_exists = file_exists
create_image_descriptor = create_image_descriptor
time = utime
time = time
logger = Logger(config.LOG_LEVEL)
get_image_path = <func_0>
_load_keyboard_image = <func_1>
KB_TEXT_AREA_HEIGHT = 48
KB_HEIGHT = 192
KB_WIDTH = 320
KB_ROW_HEIGHT = 48
TouchKeyboard = __build_class__(<func_2>, 'TouchKeyboard', object)
1 = 0
return 1
1 = get_image_path(0)
return (None, None, None)
return load_rgb565_image_raw(1, KB_WIDTH)
2 = Exception
return (None, None, None)
2 = None
YELLOW = 65504
GREEN = 2016
KEYS = ((('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'), ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'), ('\t', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '\x08', '\x08'), ('\n', ' ', '\r')), (('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'), ('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'), ('\t', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '\x08', '\x08'), ('\n', ' ', '\r')), (('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'), ('@', '#', '$', '%', '^', '&', '*', '(', ')'), ('\x0c', '+', ',', '.', '-', '_', '!', '?', '\x08', '\x08'), ('\x07', ' ', '\r')), (('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'), ('<', '>', '|', '\\', '/', '{', '}', '[', ']'), ('\x0c', '=', '"', "'", ';', ':', '`', '~', '\x08', '\x08'), ('\x07', ' ', '\r')))
__init__ = <func_0>
_show_loading = ('Loading...')
_hide_loading = <func_2>
open = (?, None)
close = <func_4>
get_value = <func_5>
clear_text = <func_6>
handle_keypress = (False)
_update_display = <func_8>
_scroll_to_cursor = <func_9>
_handle_text_area_touch = (False)
_activate = <func_11>
_load_initial_layer = <func_12>
_preload_remaining_layers_async = <func_13>
_preload_all_layers = <func_14>
_wait_and_show_layer = (2000)
_show_keyboard_layer = <func_16>
_show_keyboard_layer_sync = <func_17>
load_keyboard = <func_18>
_set_keyboard_placeholder = <func_19>
_ensure_ui = <func_20>
set_state = <func_21>
unload_keyboard = <func_22>
show_message = <func_23>
0.active = 3
0.display = 1
0.kb_screen = 0
0.cursor_char = '_'
0.kb_text = ?
0.cursor_pos = 0
0._text_scroll_x = 0
0.container = None
0.text_area = None
0.label_obj = None
0.placeholder_obj = None
0.kb_layers = {}
0._preloaded = False
0._loading_overlay = None
0._loading_spinner = None
0._loading_label = None
0._preload_task = None
0._on_submit = None
0.waiting = False
0.locked = False
2 = 0.container
3 = 2
4 = 3
5 = 2
0._loading_overlay = 2
0._loading_spinner = 4
0._loading_label = 5
0._on_submit = 2
0.kb_text = 1
0.cursor_pos = len(0.kb_text)
0._text_scroll_x = 0
0.active = True
0.locked = True
0._on_submit = None
0.active = False
return 0.kb_text
return 0.kb_text
0.kb_text = ?
0.cursor_pos = 0
0._text_scroll_x = 0
return False
0.waiting = False
return False
4 = 1
5 = 2
return False
6 = 48
6 = min(6, 3)
7 = 32
7 = min(7, 9)
7 = 4(16, 32)
7 = min(7, 8)
7 = 4(16, 32)
7 = min(7, 9)
7 = 0
7 = 2
7 = 1
8 = 7
return False
1.kb_screen = 0.kb_screen
0.kb_screen = 0
0.kb_screen = 2
0.kb_text = None
1.cursor_pos = 0.cursor_pos
9 = 0
10 = 0._on_submit
0._on_submit = None
0.active = False
return True
0.active = False
return True
0.kb_text = None
1.cursor_pos = 0.cursor_pos
return False
1 = None
1 = 8
2 = 5
3 = 0.text_area
4 = 0.text_area
5 = 0(2, 30)
5 = 50
3 = 0.text_area
4 = 8
5 = 4
0.cursor_pos = max(0, min(5, len(0.kb_text)))
0._preload_task = 0
1 = _load_keyboard_image('kb0.raw')
2 = 0
3 = 0.kb_layers
4 = 0.container
5 = Exception
5 = None
1 = 1
2 = 'kb{}.raw'(1)
3 = _load_keyboard_image
4 = None
5 = 0.container
6 = Exception
6 = None
0._preloaded = True
0._preload_task = None
0.locked = False
1 = 1
2 = 'kb{}.raw'(1)
3 = _load_keyboard_image
4 = 0.kb_layers
5 = 0.container
6 = Exception
6 = None
0._preloaded = True
3 = time
1 = 0.kb_layers
2 = print('  Showing kb0+kb1 overlay')
1 = 0.kb_layers
2 = lv.obj.FLAG.HIDDEN
1 = 0.kb_layers
0.placeholder_obj = 0.container
2 = 0.placeholder_obj
1 = lv
2 = 1
3 = 1
0.container = 1
0.text_area = 0.container
0.label_obj = 0.text_area
0.active = 1
1 = list(0.kb_layers)
2 = 1
0._preloaded = False