from src.api import api_request
from src.ui import print_list, ask_for_options, print_data


def main():

    departamentos = [
        "AMAZONAS", "ANTIOQUIA", "ARAUCA", "ATLANTICO", "BOLIVAR", "BOYACA",
        "CALDAS", "CAQUETA", "CASANARE", "CAUCA", "CESAR", "CHOCO", "CORDOBA", "CUNDINAMARCA",
        "GUAINIA", "GUAVIARE", "HUILA", "GUAJIRA", "MAGDALENA", "META", "NARIÑO", "SANTANDER",
        "NORTE SANTANDER", "PUTUMAYO", "QUINDIO", "RISARALDA", "SAN ANDRES", "SANTANDER", "SUCRE",
        "TOLIMA", "VALLE", "VAUPES", "VICHADA"
    ]

    print_list(departamentos)

    selected_options = ask_for_options(departamentos)
    
    data_to_print = api_request( departamento_nom=selected_options["departament"], limite=selected_options["number_of_elements"])

    print_data(data=data_to_print)

main()
