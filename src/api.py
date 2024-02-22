import pandas as pd
from sodapy import Socrata


def api_request(limite, departamento_nom):
    # Unauthenticated client only works with public data sets.
    client = Socrata("www.datos.gov.co", None)

    # The request is made
    results = client.get("gt2j-8ykr", limit=limite, departamento_nom=departamento_nom)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    return results_df