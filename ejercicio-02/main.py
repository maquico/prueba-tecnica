from models import Entero

def validar_rango(valor, minimo, maximo):
    if valor < minimo or valor > maximo:
        return False
    return True

def solicitar_enteros(lista_enteros):
    while True:
        try:
            # Solicitar la entrada y dividirla en componentes
            entradas = input("Ingrese los números separados por un espacio: ").split()
            if len(entradas) != len(lista_enteros):
                raise ValueError
            
            # Convertir las entradas en enteros y validarlas
            for i in range(len(lista_enteros)):
                if not entradas[i].isdigit():
                    raise ValueError
                if not validar_rango(int(entradas[i]), lista_enteros[i].minimo, lista_enteros[i].maximo):
                    raise ValueError
                lista_enteros[i].valor = int(entradas[i])
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
        entradas = input("Introduce los numeros separados por espacios: ").split()
        for i in range(len(entradas)):
            if not validar_rango(entradas[i], 1, pilotos):
                pass
            
if __name__ == "__main__":
    carreras = Entero("Carreras", 0, 1, 100)
    pilotos = Entero("Pilotos", 0, 1, 100)

    carreras, pilotos = solicitar_enteros([carreras, pilotos])
    print(carreras.valor, pilotos.valor) 

    resultados = solicitar_resultados(carreras, pilotos)
    print(resultados)

    # sp = sistemas de puntajes
    cantidad_sp = Entero("Sistemas de puntajes", 0, 1, 10)
    cantidad_sp = solicitar_enteros([cantidad_sp])
    print(cantidad_sp[0].valor)

    