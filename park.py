#!/usr/bin/env python3
from bottle import get, post, run, request
from bottle import TEMPLATE_PATH, jinja2_template as template
from os.path import dirname, abspath
import json

# テンプレートの場所
BASE_DIR = dirname(abspath(__file__))
TEMPLATE_PATH.append(BASE_DIR + "/views")

# 駐車場の状態
status = {}
x = 1

@get("/")
def index():
    return template('index', status = status, keys = sorted(status.keys()))

@post("/v1/update")
def update():
    ct = request.get_header("Content-Type")
    if ct == "application/json":
        data = request.json
#        print(data)
        if data == {}:
            return("status not updated")
        parkno = int(data['parkno'])
        stat = data['status']
        if stat:
            status[parkno] = stat
        else:
            status.pop(parkno)
    return("status updated")

if __name__ == "__main__":
    status[1] = False
    run(host="0.0.0.0", port=8080, quiet=True)