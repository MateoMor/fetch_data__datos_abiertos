def validate_number():
    numero = input()

    try:
        numero = int(numero)
        return numero
    except ValueError:
        print("Ingrese un número valido: ", end="")
        return validate_number()
