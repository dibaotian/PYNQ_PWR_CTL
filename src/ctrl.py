#!/usr/bin/python3
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

pin = GPIO.get_gpio_pin(0)
print ('pin', pin)
path = GPIO.get_gpio_base_path()
print ('path', path)
npins = GPIO.get_gpio_npins()
print ('npins', npins)

# def get_gpio_info():
#     pin = GPIO.get_gpio_pin(0)
#     print ('pin', pin)
#     pah = GPIO.get_gpio_base_path()
#     print ('path', path)
#     npins = GPIO.get_gpio_npins()
#     print ('npins', npins)




# print(btns.register_map)

# print(leds.register_map)

# leds.register_map.GPIO_DATA.Channel_1_GPIO_DATA = 8
# leds.register_map.GPIO_DATA[2:0] = 5

# pynq.gpio module is a driver for reading and writing PS GPIO pins on a board. PS GPIO pins are not connected to the PL
# gpio = GPIO.get_gpio_base()
# print(gpio)

def power_on():

    rgbleds = [base.rgbleds[i] for i in range(4, 6)]
    leds = [base.leds[i] for i in range(4)]

    # Toggle board LEDs leaving small LEDs lit
    for i in range(3):
        # [l.off() for l in leds]
        [rgbled.off() for rgbled in rgbleds]
        time.sleep(.2)
        # [l.on() for l in leds]
        [rgbled.on(1) for rgbled in rgbleds]
        time.sleep(.2)

    [rgbled.on(2) for rgbled in rgbleds]
    [l.on() for l in leds]

def power_off():

    rgbleds = [base.rgbleds[i] for i in range(4, 6)]
    leds = [base.leds[i] for i in range(4)]

    # Toggle board LEDs leaving small LEDs lit
    for i in range(3):
        [l.off() for l in leds]
        # [rgbled.off() for rgbled in rgbleds]
        time.sleep(.2)
        [l.on() for l in leds]
        # [rgbled.on(1) for rgbled in rgbleds]
        time.sleep(.2)

    [rgbled.off() for rgbled in rgbleds]
    [l.off() for l in leds]


