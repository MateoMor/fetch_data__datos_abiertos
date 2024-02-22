import pandas as pd
from sodapy import Socrata


def api_request(limite, departamento_nom):
    # Unauthenticated client only works with public data sets.
    client = Socrata("www.datos.gov.co", None)

    # The request is made
    results = client.get("gt2j-8ykr", limit=limite, pais_viajo_1_nom="AFGANISTÁN")

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    # print(results_df)

    #print(results_df.keys())

    #elementos = results_df[["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio", "estado"]]

    #print(elementos)

    return results_df
