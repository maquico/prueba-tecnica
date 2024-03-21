import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from models import CustomerClassifier

classifier = CustomerClassifier('customer_classification_model.h5')
client = [-1.31, -0.36, -0.05]  
classifier.predict_class(client)