from tensorflow.keras.models import load_model
import numpy as np

class CustomerClassifier:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.class_labels = ['low', 'medium', 'high']

    def predict_class(self, client):
        prediction = self.model.predict(np.array([client]))
        predicted_class = np.argmax(prediction, axis=1)
        print(f'El cliente pertenece a la clase: {self.class_labels[predicted_class[0]]}')

