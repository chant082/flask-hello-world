from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! from YOUR NAME in 3308'
