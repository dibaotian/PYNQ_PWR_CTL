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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/switch_clicked')
def switch_clicked():

    responses = {'code': 1, 'msg': 'failure', 'data': {}}

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
      
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
