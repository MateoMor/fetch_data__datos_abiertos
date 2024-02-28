import pandas as pd
from sodapy import Socrata


def api_request(departamento_nom, limite ):
    # Unauthenticated client only works with public data sets.
    client = Socrata("www.datos.gov.co", None)

    selected_data = "ciudad_municipio_nom, departamento_nom, edad, fuente_tipo_contagio, estado, pais_viajo_1_nom"
    
    # The request is made
    results = client.get("gt2j-8ykr", limit=limite, departamento_nom=departamento_nom, select=selected_data)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    # If pais_viajo_1_nom is not in the data, fill the columns with an empty string
    if 'pais_viajo_1_nom' not in results_df.columns:
        results_df['pais_viajo_1_nom'] = ''

    return results_df