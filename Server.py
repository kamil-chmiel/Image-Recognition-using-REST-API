import os
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(f)
    # tutaj chyba cos z kerasem

    return "tu cos co zwracamy" #render_template('index.html')


@app.route('/train', methods=['POST'])
def train_image():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(f)
    # tutaj chyba cos do trenowania w jeden ksiezyc

    return "Image successfully trained" #render_template('index.html')

app.run(port=5000)