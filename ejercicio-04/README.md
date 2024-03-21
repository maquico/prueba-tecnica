Si se quiere aislar las dependencias usando un entorno virtual, primero correr los comandos:

- python -m venv .venv
- ./.venv/Scripts/Activate

Para correr el programa y las pruebas:
- pip install -r requirements.txt (instalar las dependencias del proyecto)
- python main.py (por si se quiere volver a entrenar el modelo, si se quiere ir directo a las pruebas ignorar pues el modelo esta exportado en un archivo .h5)
- python tests/test0x (sustituyendo x por el numero de prueba que se quiere ejecutar (del 1 al 5))

Nota: para salir del entorno virtual usar deactivate


