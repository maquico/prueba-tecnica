import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import calcular_puntaje, calcular_ganadores
from models import Caso

casos = []
caso1 = Caso(
        cantidad_sp=2,
        carreras=2,
        pilotos=3,
        resultados=[[3, 2, 1], [3, 2, 1]],
        sistemas_puntaje=[[10, 5, 1], [10, 5, 2]],
)

casos.append(caso1)

# Analizar caso por caso
for caso in casos:
    ganadores_caso = []
    for sistema_puntaje in caso.sistemas_puntaje:
        puntos_sistema=calcular_puntaje(caso.pilotos, caso.resultados, sistema_puntaje)
        ganadores_sistema = calcular_ganadores(puntos_sistema)
        ganadores_caso.append(ganadores_sistema)
    for ganadores in ganadores_caso:
        print(' '.join(map(str, ganadores)))