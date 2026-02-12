# Decompiled from: fs_image/cactuscon/hw/pixels.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

asyncio = asyncio
time = time
Pin = Pin
NeoPixel = NeoPixel
NeoPixelController = __build_class__(<func_0>, 'NeoPixelController')
__init__ = (18, 8)
fade_in = ((255, 0, 0), 1000)
fade_out = ((255, 0, 0), 1000)
_blink_loop = (500, 500, 3)
_rainbow_loop = (80)
_wheel = <func_5>
start_blink = ((255, 0, 0), 2000, 200, 5)
start_rainbow = (50)
stop_blink = <func_8>
fill = <func_9>
off = <func_10>
_snapshot_mode = <func_11>
_restore_mode = <func_12>
flash_chat_alert = (3, 200)
0.np = NeoPixel(Pin(1), 2)
0.running = False
0._blink_task = None
0._mode = 'off'
0._mode_params = {}
0._last_color = (0, 0, 0)
0._alert_running = False
3 = 20
4 = 0
6 = 3(255)
5 = tuple(6(1))
2 = 1
3 = 20
4 = 3
6 = 3(255)
5 = tuple(6(1))
2 = 1
5 = 0
2 = 0
3 = 255
2 = 256
return (1, 3, 0)
1 = 85
return (3, 1, 3)
1 = 170
return (255, 1, 3)
0.running = True
0._mode = 'blink'
0._mode_params = 'times'
0._last_color = 1
0._blink_task = 4
0.running = False
0._blink_task = None
0._blink_task = None
0.running = True
0._mode = 'rainbow'
0._mode_params = 'pause_ms'
0._blink_task = 1
0.running = False
0._blink_task = None
0.running = False
0._blink_task = None
2 = 0
0._last_color = 1
0._mode = 'off'
0._mode_params = 'color'
0.running = False
0._mode = 'off'
0._mode_params = {}
return 'last_color'
2 = 'off'
3 = {}
0._alert_running = True
3 = 0
0._blink_task = None
0.running = False
4 = 0
0._alert_running = False