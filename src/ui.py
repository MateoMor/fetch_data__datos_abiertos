from tabulate import tabulate
from src.utils import validate_number

def print_list(lista):
    for i, elemento in enumerate(lista):
        print(f"{i}: {elemento}")

def ask_for_options(departments):
    selected_options = {"departament": "", "number_of_elements": 0}
    
    while True:
        selected_options["departament"] = input("\nIngrese el nombre del departamento: ").upper()
        if selected_options["departament"] in departments:
            break
        else:
            print("El departamento ingresado no se encuentra en la lista.")

    user_answer = "n" 
    while(user_answer.lower() == "n"):
        print("Ingrese la cantidad de elementos a consultar: ", end="")
        selected_options["number_of_elements"] = validate_number()
        if(selected_options["number_of_elements"] > 1000):
            user_answer = input("La cantidad de elementos es superior a 1000. ¿Continuar?: [S/n]: ")
        else:
            break
        
    return selected_options
    
def print_data(data):
    headers = ["Municipio", "Departamento", "Edad", "Tipo de contagio", "Estado", "País de Procedencia"]
    
    print()
    print(tabulate(data, headers=headers, tablefmt = "double_grid"))
