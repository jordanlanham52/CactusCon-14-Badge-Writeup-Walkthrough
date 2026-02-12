# Decompiled from: fs_image/cactuscon/ui/panels/main_menu.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

lv = lvgl
BasePanel = BasePanel
MainMenuPanel = __build_class__(<func_0>, 'MainMenuPanel', BasePanel)
create_ui = <func_0>
_create_menu_button = <func_1>
on_show = <func_2>
on_hide = <func_3>
_on_close_clicked = <func_4>
_on_battle_clicked = <func_5>
_on_settings_clicked = <func_6>
_on_extras_clicked = <func_7>
_on_info_clicked = <func_8>
_on_chat_clicked = <func_9>
_update_chat_badge = <func_10>
1 = 0.screen
2 = 1
3 = 0.screen
4 = 0.screen
5 = 65
6 = 115
7 = 75
8 = 5
9 = 5
10 = 6
11 = 6
12 = 50
4 = 0.screen
5 = 4
return 4
0.game_ui.chat_has_unread = False
1 = 'btn_chat'
2 = bool(getattr(0.game_ui, 'chat_has_unread', False))
3 = 65280
4 = 65280
5 = 0