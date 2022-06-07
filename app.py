from flask import Flask

app = Flask(__name__)
@app.route('/index')
def index():
    return "hello world"

app = Flask(__name__)
@app.route('/home')
def home():
    return "Home page"

if __name__ == '_main_':
    app.run(debug=True)