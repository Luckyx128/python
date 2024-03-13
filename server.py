import flask
from req import RequestClass
from sele import seleniumClass
from cp import cp
app = flask.Flask(__name__)

@app.route('/')
def index():
        return flask.render_template('index.html')
        

@app.route('/cep')
def cep():
        return RequestClass.ReqClass()

@app.route('/selenium')
def sele():
        return seleniumClass.selens()

@app.route('/cp')
def pg():
        return cp.psyco()


app.run(port='5555',debug=True)