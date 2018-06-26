import keras
import tensorflow as tf
import numpy as np
from keras_applications.vgg16 import VGG16
from keras.preprocessing.image import img_to_array, load_img
from keras.applications.vgg16 import preprocess_input
from keras_applications.vgg16 import decode_predictions


def load_model():
    global network_model
    network_model = VGG16(weights="imagenet")
    global graph
    graph = tf.get_default_graph()


def prepare_image(file):

    image = load_img(file, target_size=(224,224))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    vgg16_input = preprocess_input(image_array)

    return vgg16_input


def network_predict(image):

    image_to_predict = prepare_image(image)

    with graph.as_default():
        prediction = network_model.predict(image_to_predict)

    label = decode_predictions(prediction)

    return label


def train_model(image):

    image_to_train_on = prepare_image(image)



