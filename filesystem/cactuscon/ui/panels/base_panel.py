# Decompiled from: fs_image/cactuscon/ui/panels/base_panel.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

lv = lvgl
gc = gc
time = time
Logger = Logger
config = config
GameUI = GameUI
get_cached_sprite = get_cached_sprite
put_cached_sprite = put_cached_sprite
load_rgb565_file = load_rgb565_file
create_image_descriptor = create_image_descriptor
ListContainer = __build_class__(<func_0>, 'ListContainer')
BasePanel = __build_class__(<func_1>, 'BasePanel')
__init__ = (None, None)
add_btn = <func_1>
clean = <func_2>
set_align = <func_3>
set_x = <func_4>
set_y = <func_5>
set_size = <func_6>
set_style_bg_color = <func_7>
0.obj = 1
0._items = []
3 = 0.obj
4 = 3
return 3
1 = 0._items
0._items = []
return 1
return 1
return 1
return 1
return 1
__init__ = (None, None, None, config.LOG_LEVEL, True)
load = <func_1>
unload = <func_2>
show = <func_3>
hide = <func_4>
update = <func_5>
create_ui = <func_6>
on_show = <func_7>
on_hide = <func_8>
on_cleanup = <func_9>
on_back_pressed = (None)
_ensure_spinner_overlay = <func_11>
show_spinner = ('Loading...')
hide_spinner = <func_13>
is_spinner_visible = <func_14>
create_button = (None, None, None)
create_label = (lv.ALIGN.CENTER)
create_list = (None, None)
_load_icon_descriptor = (None, 32, None)
_set_icon_on_container = (None, None, None, None, None, None, None, False)
show_error = (3000)
0.logger = Logger(4)
0.tft = 1
0.display = None
0.game_ui = 2
0.battle_manager = 3
0.memory_efficient = 5
0.screen = None
0.ui_elements = {}
0.loaded = False
0.visible = False
0._spinner_visible = False
0._spinner_last_message = None
0._auto_spinner_active = False
0._icon_images = {}
0._icon_img_dsc = {}
0._icon_img_data = {}
return True
0.screen = lv
0.loaded = True
return True
1 = Exception
0.loaded = False
return False
1 = None
0._spinner_visible = False
1 = Exception
1 = None
0.screen = None
0.loaded = False
2 = Exception
2 = None
return False
0.visible = True
1 = 'Loading...'
2 = False
2 = True
2 = False
0._auto_spinner_active = 2
return True
3 = Exception
return False
3 = None
0.visible = False
return True
return False
1 = 'spinner_overlay'
return 1
1 = 0.screen
2 = 48
3 = 1
4 = 3
5 = 1
return 1
2 = 0
3 = 'spinner_label'
0._spinner_last_message = 1
4 = 'spinner'
0._spinner_visible = True
1 = 'spinner_overlay'
0._spinner_visible = False
0._spinner_last_message = None
return bool(0._spinner_visible)
6 = 1
7 = 6
return 6
4 = 1
return 4
return ListContainer(1, 2, 3)
return (None, None, None)
5 = {}
6 = 'frame_width'
7 = 'frame_height'
8 = get_cached_sprite(1)
8 = ?(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, 2, 5, 5, 8, 0.logger, '[CACHE MISS] {} - loading from disk', 1, load_rgb565_file, 1, 'do_swap', 4, None, 4, False)
return (None, None, None)
9 = 2
10 = 9(0.5)
6 = 10
7 = 0
6 = 32
7 = 10
11 = create_image_descriptor(8, 6, 7)
12 = 6
return (11, 8, 12)
13 = Exception
return (None, None, None)
13 = None
11 = 0
12 = 0
13 = 0
13 = 0
14 = 32
14 = min(4, 13)
14 = 1
15 = 9
return 14
3 = 0.screen