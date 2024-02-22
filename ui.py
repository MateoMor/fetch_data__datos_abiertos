
def ask_for_department(departamentos, elementos_por_linea=3, longitud_elemento=22):
    # Función para imprimi los departamentos disponibles para consultar

    contador = 0  # Cuenta la cantidad de elementos que se han impreso en una linea
    cadena_a_imprimir = ""  # En esta cadena se irá guardando el string final que se imprimirá

    print("\nINGRESE EL NUMERO DE DEPARTAMENTO A CONSULTAR\n")

    for i, departamento in enumerate(departamentos):
        # Se crea la cadena con su indice y se guarda su longitud
        cadena = f"{i}. {departamento}"
        longitud_cadena = len(cadena)

        # diferencia_longitud es lo que le falta a cadena para tener longitud_elemento caracteres
        diferencia_longitud = longitud_elemento - longitud_cadena

        # Se añade la cadena a cadena a imprimir con algunos ajustes de formato
        cadena_a_imprimir = cadena_a_imprimir + cadena + " " * diferencia_longitud

        # Se suma 1 al contador y se verifica si el numero de elementos en linea a sido alcanzado, si es asi se hace un salto de linea
        contador += 1
        if (contador == elementos_por_linea):
            cadena_a_imprimir = cadena_a_imprimir + "\n"
            contador = 0

    print(cadena_a_imprimir)  # Se imprime la cadena
