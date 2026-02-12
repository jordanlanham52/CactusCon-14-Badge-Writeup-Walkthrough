# Decompiled from: fs_image/cactuscon/game/engine/deterministic_random.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

struct = struct
const = const
DeterministicRNG = __build_class__(<func_0>, 'DeterministicRNG')
create_turn_seed = <func_1>
verify_rng_state = <func_2>
__slots__ = ('_state', '_initial_seed')
_MULTIPLIER = 1664525
_INCREMENT = 1013904223
_MODULUS = 4294967296
__init__ = (None)
_hash_seed = <func_1>
_next = <func_2>
random = <func_3>
uniform = <func_4>
randint = <func_5>
choice = <func_6>
get_state = <func_7>
get_seed = <func_8>
0._state = 0
0._initial_seed = b'\x00\x00\x00\x00'
0._initial_seed = 1
0._state = 1
0._state = 4294967295
0._initial_seed = 0._state
2 = 5381
3 = 1
2 = 4294967295
return 2
0._state = 4294967295
return 0._state
return 0._MODULUS
return 0
1 = 1
2 = 2
return 1
return len(1)
return 0._state
return 0._initial_seed
4 = min(2, 3)
5 = max(2, 3)
6 = 5
7 = 5381
8 = 5387
9 = enumerate(6)
10 = 4
7 = 4294967295
8 = 4294967295
return 8
return 1