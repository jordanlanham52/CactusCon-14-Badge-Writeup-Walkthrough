# Decompiled from: fs_image/thirdparty/uFT6336U.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

__version__ = '0.1.1'
const = const
I2C_ADDRESS = 56
REG_MODE_SWITCH = 0
REG_TD_STATUS = 2
REG_P1_XH = 3
REG_P1_XL = 4
REG_P1_YH = 5
REG_P1_YL = 6
REG_P1_WEIGHT = 7
REG_P1_MISC = 8
REG_P2_XH = 9
REG_P2_XL = 10
REG_P2_YH = 11
REG_P2_YL = 12
REG_P2_WEIGHT = 13
REG_P2_MISC = 14
REG_ID_G_THGROUP = 128
REG_ID_G_THDIFF = 133
REG_ID_G_CTRL = 134
REG_ID_G_TIMEENTERMONITOR = 135
REG_ID_G_PERIODACTIVE = 136
REG_ID_G_PERIODMONITOR = 137
REG_ID_G_FREQ_HOPPING_EN = 139
REG_ID_G_TEST_MODE_FILTER = 150
REG_ID_G_CIPHER_MID = 159
REG_ID_G_CIPHER_LOW = 160
REG_ID_G_LIB_VERSION_H = 161
REG_ID_G_LIB_VERSION_L = 162
REG_ID_G_CIPHER_HIGH = 163
REG_ID_G_MODE = 164
REG_ID_G_PMODE = 165
REG_ID_G_FIRMID = 166
REG_ID_G_FOCALTECH_ID = 168
REG_ID_G_VIRTUAL_KEY_THRES = 169
REG_ID_G_IS_CALLING = 173
REG_ID_G_FACTORY_MODE = 174
REG_ID_G_RELEASE_CODE_ID = 175
REG_ID_G_FACE_DEC_MODE = 176
REG_ID_G_STATE = 188
DEVICE_MODE_WORKING = 0
DEVICE_MODE_FACTORY = 64
CHIP_CODE_FT6336U = 2
FT6336U = __build_class__(<func_0>, 'FT6336U')
read_buffer = bytearray(2)
write_buffer = bytearray(1)
__init__ = (None)
_readfrom_mem = (1)
_writeto_mem = <func_2>
set_mode_working = <func_3>
set_mode_factory = <func_4>
get_points = <func_5>
get_p1_x = <func_6>
get_p1_y = <func_7>
get_p2_x = <func_8>
get_p2_y = <func_9>
get_positions = <func_10>
0.i2c = 1
0.rst = 2
return 8
return 'large'
return 2
return 4095
return 4095
return 4095
return 4095
1 = []
2 = 0
return 1