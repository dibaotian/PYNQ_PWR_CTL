#!../venv/bin/python3
# -*- coding: utf-8 -*-

# from pynq import Overlay
from pynq.overlays.base import BaseOverlay
from pynq.lib import AxiGPIO

ol = BaseOverlay("base.bit")

led_ip = ol.ip_dict['gpio_leds']
switches_ip = ol.ip_dict['gpio_switches']
leds = AxiGPIO(led_ip).channel1
switches = AxiGPIO(switches_ip).channel1

