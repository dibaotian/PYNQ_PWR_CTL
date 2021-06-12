#!../venv/bin/python3
# -*- coding: utf-8 -*-

import time


from flask import Flask, render_template

# from pynq import Overlay
from pynq.overlays.base import BaseOverlay
#AXI GPIO
from pynq.lib import AxiGPIO
# PS GPIO
from pynq import GPIO

app = Flask(__name__)

base = BaseOverlay("base.bit")

POWER_STATUS="OFF"


@app.route('/')
def index():
    return render_template('index.html', power_status = POWER_STATUS)

@app.route('/switch_on')
def switch_on():

    responses = {'code': 1, 'msg': 'failure', 'data': {}}

    POWER_STATUS = 'ON'
    print('POWER_STATUS %s',POWER_STATUS)

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

    responses['code'] = 0
    responses['msg'] = 'success'

    return responses

@app.route('/switch_off')
def switch_off():
    responses = {'code': 1, 'msg': 'failure', 'data': {}}

    POWER_STATUS = 'OFF'
    print('POWER_STATUS %s',POWER_STATUS)

    rgbleds = [base.rgbleds[i] for i in range(4, 6)]
    leds = [base.leds[i] for i in range(4)]

    # Toggle board LEDs leaving small LEDs lit
    for i in range(8):
        [rgbled.off() for rgbled in rgbleds]
        time.sleep(.2)
        [rgbled.on(1) for rgbled in rgbleds]
        time.sleep(.2)

    [rgbled.off() for rgbled in rgbleds]

    responses['code'] = 0
    responses['msg'] = 'success'
    return responses
      
if __name__ == '__main__':
    print("PYNQ Need about 15s to initalize the system. please wait...")
    app.debug = True
    app.run(host='0.0.0.0')
