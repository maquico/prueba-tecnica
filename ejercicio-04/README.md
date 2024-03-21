Si se quiere aislar las dependencias usando un entorno virtual, primero correr los comandos:

- python -m venv .venv
- ./.venv/Scripts/Activate

Para correr el programa y las pruebas:
- pip install -r requirements.txt (instalar las dependencias del proyecto)
- Agrega el archivo data_customer_classification.csv a la carpeta data
- python main.py (entrena el modelo y lo exporta en un .h5, abrira una ventana con la matriz de confusión, cerrar despues de ver)

## PARA LAS PRUEBAS ##
- python tests/test0x (sustituyendo x por el numero de prueba que se quiere ejecutar (del 1 al 5))

Nota: para salir del entorno virtual usar deactivate


