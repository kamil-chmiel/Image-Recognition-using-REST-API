import os
from flask import Flask, render_template, request, jsonify
from Network_VGG16 import VGG16Network

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
    result = VGG16Network(file).network_predict()
    label = [result[0][0], result[0][1], result[0][2]] # three most probable results
    print(label)  # show results format

    return '%s %f %s' % (label[0][1], label[0][2]*100, "%")

    # TODO: Add proper JSON Response
    #return jsonify(
#
    #    result1=label[0],
   #     result2=label[1],
   #     result3=label[2]

  #  )


@app.route('/train', methods=['POST'])
def train_image():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(f)
    # TODO: add 'dotrenowywanie w jeden ksiezyc' option

    return "Image successfully trained" #render_template('index.html')


app.run(port=5000)
