from tabulate import tabulate

def print_list_with_index(lista, elementos_por_linea=3, longitud_elemento=22):
    # Función para imprimir los elementos de un arreglo numerados por su indice y con formato de bloque

    contador = 0 
    cadena_a_imprimir = "" 

    for i, elementeo in enumerate(lista):
        # Se crea la cadena a mostrar y se guarda su longitud
        cadena = f"{i}. {elementeo}"
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


def print_data(datos_obtenidos_pandas):
    print()
    
    # Añade pais_viajo_1_nom a las columnas si no se encuentra
    if "pais_viajo_1_nom" not in datos_obtenidos_pandas.columns:
        datos_obtenidos_pandas.loc[:, "pais_viajo_1_nom"] = ""
    
    # Se copian los elementos a imprimir
    elementos_a_imprimir = datos_obtenidos_pandas[["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio", "estado", "pais_viajo_1_nom"]].copy()
    
    # Encabezados de las columnas
    headers = ["Municipio", "departamento", "edad", "Tipo de contagio", "Estado", "País de Procedencia"]
    
    print(tabulate(elementos_a_imprimir, headers=headers, tablefmt = "double_grid"))
