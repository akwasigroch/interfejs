from crypt import methods
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/form', methods=['POST'])
def process_image():
    if request.method =='POST':
        print(request)
        return 'ok'

@app.route("/")
def home():
    return render_template('index.html')