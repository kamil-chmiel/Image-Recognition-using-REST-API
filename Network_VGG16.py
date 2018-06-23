from keras.applications import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras_applications.vgg16 import decode_predictions


class VGG16Network:

    def __init__(self, file):
        self.network_model = VGG16()
        self.file = load_img(file, target_size=(224, 224))

    def network_predict(self):
        image = img_to_array(self.file)
        image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
        image = preprocess_input(image)

        prediction = self.network_model.predict(image)
        label = decode_predictions(prediction)

        return label
