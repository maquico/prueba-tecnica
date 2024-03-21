from models import Entero, Caso
import itertools

def validar_rango(valor, minimo, maximo):
    if valor < minimo or valor > maximo:
        return False
    return True

def solicitar_enteros(lista_enteros, nombres_enteros):
    while True:
        try:
            # Solicitar la entrada y dividirla en componentes
            entradas = input(f"{nombres_enteros}: \nIngrese los números separados por un espacio: ").split()
            if len(entradas) != len(lista_enteros):
                raise ValueError
            
            # Convertir las entradas en enteros y validarlas
            for i in range(len(lista_enteros)):
                if not entradas[i].isdigit():
                    raise ValueError
                valor = int(entradas[i])
                if valor == 0 and all(int(e) == 0 for e in entradas) and nombres_enteros == "Carreras y Pilotos":  # Condición especial para manejar el caso cuando los valores son 0
                    lista_enteros[i].valor = valor
                    break
                if not validar_rango(valor, lista_enteros[i].minimo, lista_enteros[i].maximo):
                    raise ValueError
                lista_enteros[i].valor = valor
            break
        except ValueError:
            print("Por favor, ingrese solo números enteros en el rango correcto para cada variable.")

    return lista_enteros

def solicitar_resultados(carreras, pilotos):
    resultados = []
    for x in range(carreras.valor):
        while True:
            try:
                # Solicitar la entrada y dividirla en componentes
                entradas = input(f"Ingrese los resultados de la carrera {x + 1}, separados por un espacio: ").split()
                if len(entradas) != pilotos.valor:
                    raise ValueError
                
                # Convertir las entradas en enteros y validarlas
                orden_llegada = []
                for i in range(len(entradas)):
                    if not entradas[i].isdigit():
                        raise ValueError
                    # Validar que si solo hay 3 pilotos, un piloto no puede llegar en la posición 4
                    if not validar_rango(int(entradas[i]), 1, pilotos.valor):
                        raise ValueError    
                    orden_llegada.append(int(entradas[i]))
                resultados.append(orden_llegada)
                break
            except ValueError:
                print("Por favor, ingrese solo números enteros para cada piloto.")
    return resultados

def solicitar_sistemas(cantidad_sp, pilotos):
    sistemas_puntaje = []
    for x in range(cantidad_sp):
        while True:
            try:
                entradas = input(f"Introduce los numeros separados por espacios para el Sistema de puntaje {x + 1}: ").split()
                sistema = []
                puestos_con_puntaje = 0
                for i in range(len(entradas)):
                    if not entradas[i].isdigit():
                        raise ValueError
                    if i == 0:
                        # Validar que la ultima posicion en recibir puntos este entre 1 y el numero de pilotos
                        if not validar_rango(int(entradas[i]), 1, pilotos.valor):
                            raise ValueError
                        puestos_con_puntaje = pilotos.valor - (pilotos.valor - int(entradas[i]))
                        # Revisar que la longitud de la entrada sea la cantidad de puestos que llevan puntaje + 1 por el valor K (ultimo puesto en recibir puntos)
                        if len(entradas) != puestos_con_puntaje + 1:
                            raise ValueError
                    else:
                        if not validar_rango(int(entradas[i]), 1, 100):
                            raise ValueError
                        sistema.append(int(entradas[i]))
                sistemas_puntaje.append(sistema)
                break  
            except ValueError:
                print("Por favor, ingrese solo números enteros para cada piloto.")
    return sistemas_puntaje

def calcular_puntaje(pilotos, resultados, sistema_puntaje):
    sp_extendido = [0] * pilotos
    sp_extendido = [a + b for a, b in itertools.zip_longest(sp_extendido, sistema_puntaje, fillvalue=0)]
    
    puntos_finales = [0] * pilotos
    for carrera in resultados:
        for i in range(len(carrera)):
            puntos_finales[i] += sp_extendido[carrera[i] - 1]

    return puntos_finales

def calcular_ganadores(puntos_sistema):
    max_puntos = max(puntos_sistema)
    ganadores = [i + 1 for i, puntos in enumerate(puntos_sistema) if puntos == max_puntos]
    return ganadores

def main():
    casos = []
    while True:
        caso = Caso(
            cantidad_sp=0,
            carreras=0,
            pilotos=0,
            resultados=[],
            sistemas_puntaje=[],
        )
        carreras = Entero("Carreras", 0, 1, 100)
        pilotos = Entero("Pilotos", 0, 1, 100)

        carreras, pilotos = solicitar_enteros([carreras, pilotos], "Carreras y Pilotos")
        if carreras.valor == 0 and pilotos.valor == 0:
            break
        caso.carreras = carreras.valor
        caso.pilotos = pilotos.valor
        print(carreras.valor, pilotos.valor) 

        resultados = solicitar_resultados(carreras, pilotos)
        caso.resultados = resultados
        print(resultados)

        # sp = sistemas de puntajes
        cantidad_sp = Entero("Sistemas de puntajes", 0, 1, 10)
        cantidad_sp = solicitar_enteros([cantidad_sp], "Cantidad Sistemas de Puntaje")[0].valor
        caso.cantidad_sp = cantidad_sp
        print(cantidad_sp)

        sistemas_puntaje = solicitar_sistemas(cantidad_sp, pilotos)
        caso.sistemas_puntaje = sistemas_puntaje
        print(sistemas_puntaje)

        casos.append(caso)
    
    # Analizar caso por caso
    for caso in casos:
        ganadores_caso = []
        for sistema_puntaje in caso.sistemas_puntaje:
            puntos_sistema=calcular_puntaje(caso.pilotos, caso.resultados, sistema_puntaje)
            ganadores_sistema = calcular_ganadores(puntos_sistema)
            ganadores_caso.append(ganadores_sistema)
        for ganadores in ganadores_caso:
            print(' '.join(map(str, ganadores)))
    
if __name__ == "__main__":
    main()


        

    