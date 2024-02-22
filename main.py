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
    numero_departamento = pedir_numero(maximo=(len(departamentos) - 1))

    print("Ingrese la cantidad de registros a obtener (maximo 500): ", end="")
    cantidad_registros = pedir_numero(maximo=500)

    datos_departamento = api_request(
        limite=cantidad_registros, departamento_nom=departamentos[numero_departamento])

    print_data(datos_obtenidos_pandas=datos_departamento)


main()
