import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from models import CustomerClassifier

classifier = CustomerClassifier('customer_classification_model.h5')
client = [0.86, 1.28, 0.72]  
classifier.predict_class(client)