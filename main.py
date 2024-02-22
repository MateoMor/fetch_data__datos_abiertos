from api import api_request

def main():
    
    departamentos = [
        "AMAZONAS", "ANTIOQUIA", "ARAUCA", "ATLANTICO", "BARRANQUILLA", "BOGOTA", "BOLIVAR", "BOYACA", 
        "CALDAS", "CAQUETA", "CASANARE", "CAUCA", "CESAR", "CHOCO", "CORDOBA", "CUNDINAMARCA", 
        "GUAINIA", "GUAVIARE", "HUILA", "GUAJIRA", "MAGDALENA", "META", "NARIÑO", "SANTANDER", 
        "NORTE SANTANDER", "PUTUMAYO", "QUINDIO", "RISARALDA", "SAN ANDRES", "SANTANDER", "SUCRE", "TOLIMA", "VALLE", "VAUPES", "VICHADA"
    ]
    
    for departamento in departamentos:
        try:
            print(i)
            i = i + 1
            # Ejecutar la función api_request para cada departamento solicitando 2 datos
            api_request(limite=2, departamento_nom=departamento)["id_de_caso"]
            # print(f"El departamento {departamento} ha sido procesado con exito")
        except Exception as e:
            print(f"Error al procesar el departamento {departamento}: {e}")
        
    """  nombre_departamento = input("Ingrse el departamento que desa consultar: ")
    cantidad_registros = input ("Ingrese la cantidad de registros que desea consultar: ")
    
    resultados = api_request(limite=cantidad_registros, departamento_nom=nombre_departamento)
    
    print("\n")
    
    print(resultados["id_de_caso"]) """
    
    
main()