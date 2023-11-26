from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Daeeee Mundo!'

@app.route('/about')
def about():
    return 'About'