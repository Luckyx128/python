
from unittest import result
from flask import Flask, request, render_template , session, make_response
from req import RequestClass
from sele import seleniumClass
from cp import cp
app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def index():
        if request.method == 'GET':
                results = {'nome':'Lucas','email':'lulu'}
                return render_template('index.html')
        else: return request.form['nome']

@app.route('/')
def index2():
        return render_template('login.html')

@app.route("/autenticar", methods=["POST"])
def autenticar():
        resp = make_response(render_template('index.html',user=request.form["login"]))
        resp.set_cookie('login', request.form["login"])
        return resp


@app.route('/cep')
def cep():
        return RequestClass.ReqClass()

@app.route('/selenium')
def sele():
        return seleniumClass.selens()

@app.route('/cp')
def pg():
        return cp.psyco()
