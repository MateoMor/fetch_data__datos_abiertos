from src.api import api_request
from src.ui import ask_for_department, print_data
from src.utils import pedir_numero


def main():

    departamentos = [
        "AMAZONAS", "ANTIOQUIA", "ARAUCA", "ATLANTICO", "BARRANQUILLA", "BOGOTA", "BOLIVAR", "BOYACA",
        "CALDAS", "CAQUETA", "CASANARE", "CAUCA", "CESAR", "CHOCO", "CORDOBA", "CUNDINAMARCA",
        "GUAINIA", "GUAVIARE", "HUILA", "GUAJIRA", "MAGDALENA", "META", "NARIÑO", "SANTANDER",
        "NORTE SANTANDER", "PUTUMAYO", "QUINDIO", "RISARALDA", "SAN ANDRES", "SANTANDER", "SUCRE",
        "TOLIMA", "VALLE", "VAUPES", "VICHADA"
    ]

    ask_for_department(departamentos)

    print("\nIngrese el numero del departamento: ", end="")
    numero_departamento = pedir_numero(final=len(departamentos))

    print("Ingrese la cantidad de registros a obtener (maximo 100): ", end="")
    cantidad_registros = pedir_numero(final=100)

    datos_departamento = api_request(
        limite=cantidad_registros, departamento_nom=departamentos[numero_departamento])

    print_data(datos_departamento)

    """ for departamento in departamentos:
        try:
            # Ejecutar la función api_request para cada departamento solicitando 2 datos
            print(api_request(limite=2, departamento_nom=departamento).keys())
            # print(f"El departamento {departamento} ha sido procesado con exito")
        except Exception as e:
            print(f"Error al procesar el departamento {departamento}: {e}") """

    """  nombre_departamento = input("Ingrse el departamento que desa consultar: ")
    cantidad_registros = input ("Ingrese la cantidad de registros que desea consultar: ")

    resultados = api_request(limite=cantidad_registros, departamento_nom=nombre_departamento)

    print("\n")

    print(resultados["id_de_caso"]) """


main()
