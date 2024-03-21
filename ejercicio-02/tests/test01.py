import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import calcular_puntaje, calcular_ganadores
from models import Caso

casos = []
caso1 = Caso(
        cantidad_sp=3,
        carreras=1,
        pilotos=3,
        resultados=[[3, 2, 1]],
        sistemas_puntaje=[[5, 3, 2], [5, 3, 1], [1, 1, 1]],
)
caso2 = Caso(
        cantidad_sp=2,
        carreras=3,
        pilotos=10,
        resultados=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]],
        sistemas_puntaje=[[5, 4, 3, 2, 1], [10, 5, 1]]
)
caso3 = Caso(
        cantidad_sp=2,
        carreras=2,
        pilotos=4,
        resultados=[[1, 3, 4, 2], [4, 1, 3, 2]],
        sistemas_puntaje=[[3, 2, 1], [5, 4, 2]],
)
casos.append(caso1)
casos.append(caso2)
casos.append(caso3)
# Analizar caso por caso
for caso in casos:
    ganadores_caso = []
    for sistema_puntaje in caso.sistemas_puntaje:
        puntos_sistema=calcular_puntaje(caso.pilotos, caso.resultados, sistema_puntaje)
        ganadores_sistema = calcular_ganadores(puntos_sistema)
        ganadores_caso.append(ganadores_sistema)
    for ganadores in ganadores_caso:
        print(' '.join(map(str, ganadores)))