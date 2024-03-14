from unittest import result
from flask import Flask, request, render_template , session
from req import RequestClass
from sele import seleniumClass
from cp import cp
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'GET':
                results = {'nome':'Lucas','email':'lulu'}
                return render_template('index.html',content=[results],nome="Emily")
        else: return request.form['nome']

@app.route('/cep')
def cep():
        return RequestClass.ReqClass()

@app.route('/selenium')
def sele():
        return seleniumClass.selens()

@app.route('/cp')
def pg():
        return cp.psyco()


app.run(port='5555',debug=True, host='0.0.0.0')