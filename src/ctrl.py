#!../venv/bin/python3
# -*- coding: utf-8 -*-

import time

# from pynq import Overlay
from pynq.overlays.base import BaseOverlay
#AXI GPIO
from pynq.lib import AxiGPIO
# PS GPIO
from pynq import GPIO


start_time = time.time()
print(f'start to program base overlay: {time.strftime("%I:%M:%S")}')
base = BaseOverlay("base.bit")
print(f'program base overlay complete: {time.strftime("%I:%M:%S")}')
end_time = time.time()
prog_time = end_time - start_time
print(f'program the overlay took: {prog_time} seconds')

# 通过AXIGPIO 操作
# btns = base.btns_gpio
# leds = base.leds_gpio

# print(btns.register_map)

# print(leds.register_map)

# leds.register_map.GPIO_DATA.Channel_1_GPIO_DATA = 8
# leds.register_map.GPIO_DATA[2:0] = 5

# pynq.gpio module is a driver for reading and writing PS GPIO pins on a board. PS GPIO pins are not connected to the PL
# gpio = GPIO.get_gpio_base()
# print(gpio)

rgbleds = [base.rgbleds[i] for i in range(4, 6)]
leds = [base.leds[i] for i in range(4)]

# Toggle board LEDs leaving small LEDs lit
for i in range(8):
    [l.off() for l in leds]
    [rgbled.off() for rgbled in rgbleds]
    time.sleep(.2)
    [l.on() for l in leds]
    [rgbled.on(1) for rgbled in rgbleds]
    time.sleep(.2)

[rgbled.off() for rgbled in rgbleds]



