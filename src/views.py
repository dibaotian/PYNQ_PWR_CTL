#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
from flask import Flask, render_template

import ctrl
import psql

app = Flask(__name__)

# global varilable to keep the Powre status
POWER_STATUS="OFF"


@app.route('/')
def index():
    return render_template('index.html', power_status = POWER_STATUS)

@app.route('/switch_on')
def switch_on():

    responses = {'code': 1, 'msg': 'failure', 'data': {}}

    global  POWER_STATUS
    POWER_STATUS = 'ON'
    print('POWER_STATUS',POWER_STATUS)
    ctrl.power_on()

    # 数据库记录
    psql.update_power_status(True)
    psql.recoder_power_process(True)

    responses['code'] = 0
    responses['msg'] = 'success'

    return responses

@app.route('/switch_off')
def switch_off():
    responses = {'code': 1, 'msg': 'failure', 'data': {}}

    global  POWER_STATUS
    POWER_STATUS = 'OFF'
    print('POWER_STATUS',POWER_STATUS)
    ctrl.power_off()

    # 数据库记录
    psql.update_power_status(True)
    psql.recoder_power_process(True)

    responses['code'] = 0
    responses['msg'] = 'success'
    return responses

@app.route('/switch_status')
def switch_status():
    responses = {'code': 1, 'msg': 'failure', 'data': {'status':False}}

    global  POWER_STATUS
    print('current POWER_STATUS',POWER_STATUS)

    responses['code'] = 0
    responses['msg'] = 'success'
    if POWER_STATUS is 'ON':
        responses['data']['status'] = True
    else:
         responses['data']['status'] = False
    return responses
      
if __name__ == '__main__':
    print("PYNQ Need about 15s to initalize the system. please wait...")
    app.debug = True
    app.run(host='0.0.0.0')
