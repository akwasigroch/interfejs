from crypt import methods
from flask import Flask, request, redirect, flash
from flask import render_template
import os
from predict import classify

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = 'static'



@app.route('/form')
def return_to_index():
    return render_template('index.html')


@app.route('/form', methods=['POST'])
def process_image():
    filename = False
    probability = 5
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            state = 'no_file_part'

        file = request.files['image']
        if file.filename == '':
            state = 'no_selected_file'

        if file:
            filename = file.filename
            extension = filename.split('.')[-1]
            filename = f'image.{extension}'
            file_path =  os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            probability = int(classify(file_path) * 100)
            state = 'ok'

        return render_template('classification.html', state=state, filename=filename, probability=probability)


@app.route("/")
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host="0.0.0.0")

