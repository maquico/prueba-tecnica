from models import Entero
from collections import deque

def validar_rango(valor, minimo, maximo):
    if valor < minimo or valor > maximo:
        return False
    return True

def validar_entrada(objeto, texto):
    while True:
        entrada = input(f"Ingrese el valor de {texto}: ")
        try:
            if not entrada.isdigit():
                raise ValueError
            if not validar_rango(int(entrada), objeto.minimo, objeto.maximo):
                raise ValueError
            objeto.valor = int(entrada)
            break
        except ValueError:
            print("Ingrese un número valido")

def min_saltos(objetivo):
    visitados = set() 
    # En la lista de tupls el primer elemento es el punto y el segundo es la cantidad de saltos
    queue = deque([(0, 0), (-1, 1)]) 

    while queue:
        punto, saltos = queue.popleft()
        if punto == objetivo:
            return saltos
        if punto not in visitados:
            visitados.add(punto)
        queue.append((punto - 1, saltos + 1))
        queue.append((punto + saltos + 1, saltos + 1))

    return -1
    

punto_inicial = 0
casos = Entero("Casos", 0, 1, 1000)
validar_entrada(casos, "casos")

lista_objetivos=[]
for i in range(casos.valor):
    objetivo = Entero("Objetivo", 0, 1, 106)
    validar_entrada(objetivo, "objetivo")
    lista_objetivos.append(objetivo.valor)

for objetivo in lista_objetivos:
    print(f"El objetivo es {objetivo}")
    print("Minimo de saltos: ", min_saltos(objetivo))

