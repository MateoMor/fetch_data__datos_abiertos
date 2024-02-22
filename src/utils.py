def pedir_numero(final, inicio=0):
    numero = input()

    try:
        numero = int(numero)
        if (numero > final or numero < inicio):
            print("Ingrese una opción valida")
            return pedir_numero()

        return numero
    except ValueError:
        print("Tipo de dato invalido, por favor ingrese un número entero")
        return pedir_numero()
