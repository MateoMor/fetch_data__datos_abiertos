def pedir_numero(maximo, minimo=0):
    numero = input()

    try:
        numero = int(numero)
        if (numero > maximo or numero < minimo):
            print("Ingrese un valor valido: ", end="")
            return pedir_numero(maximo, minimo)
        return numero
    
    except ValueError:
        print("Tipo de dato invalido, por favor ingrese un número entero: ", end="")
        return pedir_numero(maximo, minimo)
