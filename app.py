from crypt import methods
from flask import Flask, request, redirect, flash
from flask import render_template
import os

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = 'upload'


@app.route('/form', methods=['POST'])
def process_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['image']
        if file.filename == '':
            return "No selected file"
        
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "File loaded"




@app.route("/")
def home():
    return render_template('index.html')
