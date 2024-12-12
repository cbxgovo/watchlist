from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'

@app.route('/test')
def hello1():
    return 'Test!'

@app.route('/test1')
def hello2():
    return 'Test1!'