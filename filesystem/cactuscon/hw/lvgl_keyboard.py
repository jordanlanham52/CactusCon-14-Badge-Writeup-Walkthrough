# Decompiled from: fs_image/cactuscon/hw/lvgl_keyboard.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

Logger = Logger
config = config
logger = Logger(config.LOG_LEVEL)
lv = lvgl
LVGLKeyboard = __build_class__(<func_0>, 'LVGLKeyboard')
TouchKeyboard = LVGLKeyboard
__init__ = (None, None, False)
_warn_once = <func_1>
_ensure_ui = <func_2>
_obj_show = <func_3>
_obj_hide = <func_4>
_keyboard_is_visible = <func_5>
_on_kb_ready = <func_6>
_on_kb_cancel = <func_7>
_submit = <func_8>
_show = <func_9>
_hide = <func_10>
open = (?, None)
close = <func_12>
get_value = <func_13>
clear_text = <func_14>
set_state = <func_15>
show_message = (None)
load_keyboard = <func_17>
unload_keyboard = <func_18>
handle_keypress = (False)
ensure_preloaded = <func_20>
_show_loading = ('Loading...')
_hide_loading = <func_22>
0.active = False
0._on_submit = None
0._container = None
0._textarea = None
0._keyboard = None
0._initialized = False
0._keyboard_hidden = True
0.waiting = False
0.locked = False
0.kb_text = ?
0._warned = set()
1 = lv
2 = 1
3 = 1
0._container = 1
0._textarea = 0._container
4 = 0._container
4 = lv
4 = 0._container
0._keyboard = 4
5 = Exception
0._keyboard = None
5 = None
0._keyboard_hidden = True
0._initialized = True
return False
return False
2 = Exception
return False
2 = None
return True
return False
return False
2 = Exception
return False
2 = None
return True
return False
return lv.obj.FLAG.HIDDEN
return 0._keyboard_hidden
0._on_submit = None
1 = 0
2 = 0._on_submit
0._on_submit = None
3 = Exception
3 = None
0._keyboard_hidden = False
0.active = True
0._keyboard_hidden = True
0.active = False
0._on_submit = 2
0.kb_text = 1
0._on_submit = None
1 = 0._textarea
0.kb_text = 1
return 1
return 1
return 0.kb_text
return 0.kb_text
0.kb_text = ?
return False