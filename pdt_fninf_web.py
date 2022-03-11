#!/usr/bin/python
#-*- encoding:utf-8 -*-
import numpy as np

from pdt_fninf import pdt_fninf

from flask import *
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

@app.route('/', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        k_type = request.form.get('k_type')
        sel_condition = request.form.getlist('mod')
        jsontext = pdt_fninf(k_type, sel_condition)
        print(k_type, sel_condition)
    else:
        jsontext = ''
    return jsontext

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        k_type = request.form.get('k_type')
        sel_condition = request.form.getlist('mod')
        jsontext = pdt_fninf(k_type, sel_condition)
    else:
        jsontext = 'please search you need data'   
    return render_template('index_backup.html', content=jsontext)

if __name__=="__main__":
    
    app.run(host='127.0.0.1', port=8080, debug = True)
    #app.after_request(after_request)
    k_type = 'Database'
    sel_condition = ['AD']
    result = pdt_fninf(k_type, sel_condition)
    print(result)