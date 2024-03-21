import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 1. Leer el archivo CSV
    df = pd.read_csv('data/data_customer_classification.csv')

    # 2. Agrupar los datos por customer_id
    grouped = df.groupby('customer_id')['tran_amount']

    # Calcular la frecuencia de compra, los hábitos de gasto y la cantidad máxima
    df['purchase_frequency'] = grouped.transform('count')
    df['spending_habit'] = grouped.transform('mean')
    df['max_spending'] = grouped.transform('max')

    # 3. Normalizar los datos
    scaler = StandardScaler()
    df[['purchase_frequency', 'spending_habit', 'max_spending']] = scaler.fit_transform(df[['purchase_frequency', 'spending_habit', 'max_spending']])

    # 4. Codificar las etiquetas de las clases en números
    # Calcular el gasto total como la frecuencia de compra multiplicada por los hábitos de gasto
    df['total_spent'] = df['purchase_frequency'] * df['spending_habit']

    # Definir los límites para las clases
    low_limit = df['total_spent'].quantile(0.33)
    high_limit = df['total_spent'].quantile(0.66)

    # Crear la columna de clases
    df['class_label'] = pd.cut(df['total_spent'], bins=[-float('inf'), low_limit, high_limit, float('inf')], labels=['low', 'medium', 'high'])

    # Codificar las etiquetas de las clases en números
    encoder = LabelEncoder()
    df['class_label'] = encoder.fit_transform(df['class_label'])

    print(df.head())
    # Escribir en un archivo CSV
    df.to_csv('data/data_customer_classification_processed.csv', index=False)

    # 5. Dividir los datos en conjuntos de entrenamiento y prueba
    X = df[['purchase_frequency', 'spending_habit', 'max_spending']].values
    y = to_categorical(df['class_label'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 6. Construir el modelo de clasificación con Keras
    model = Sequential()
    model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(y_train.shape[1], activation='softmax'))

    # Compilar el modelo
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # 7. Entrenar el modelo
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    # 8. Evaluar el modelo
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test loss: {loss}, Test accuracy: {accuracy}')

    # Predecir los valores del conjunto de prueba
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1) 
    y_true = np.argmax(y_test, axis=1) 

    # Calcular la matriz de confusión
    confusion_mtx = confusion_matrix(y_true, y_pred_classes) 

    #  Visualizar la matriz de confusión
    sns.heatmap(confusion_mtx, annot=True, fmt='d')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()

    # Guardar el modelo
    model.save('customer_classification_model.h5')
    

