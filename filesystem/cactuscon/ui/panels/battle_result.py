# Decompiled from: fs_image/cactuscon/ui/panels/battle_result.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

lv = lvgl
BasePanel = BasePanel
BattleResultPanel = __build_class__(<func_0>, 'BattleResultPanel', BasePanel)
__init__ = 0
create_ui = <func_1>
set_result = (0, 0, 0)
_update_ui = <func_3>
on_show = <func_4>
return 0
1.winner = 0
1.exp_gained = 0
1.wins = 0
1.losses = 0
1.voided = False
1.error = None
1.can_evolve_now = False
1.creature_name = 0
1 = 'Defeat!'
2 = 1
3 = '* * *'
4 = 0.exp_gained
5 = 0.losses
6 = 0.screen
7 = 50
0.winner = 1
0.exp_gained = 2
0.wins = 3
0.losses = 4
1 = 'Battle Void'
1 = 'Defeat!'
1 = 0.battle_manager.last_battle_result
0.winner = 0
0.exp_gained = 0
0.wins = 0
0.losses = 0
0.voided = False
0.error = None
0.can_evolve_now = False
0.creature_name = 'creature_name'
0.voided = False
0.error = None
0.can_evolve_now = False
0.creature_name = 'No battle result data available'