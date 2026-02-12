# Decompiled from: fs_image/cactuscon/hw/power_meter.py
# This is a best-effort reconstruction from MicroPython bytecode.
# Some complex logic may be approximate or incomplete.

Logger = Logger
max1704x = max1704x
config = config
fuel_gauge = max1704x(0, config.PIN_I2C_SDA, config.PIN_I2C_SCL)
logger = Logger(config.LOG_LEVEL)