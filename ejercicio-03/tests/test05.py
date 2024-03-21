import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import min_saltos

lista_objetivos = [100]
for objetivo in lista_objetivos:
        print(min_saltos(objetivo))