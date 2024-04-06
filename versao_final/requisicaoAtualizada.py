import pandas as pd
import requests
from datetime import datetime
print('FASE1')

apiKey = "df97b6ec3d3148c2a0f34e552e3f53af"
keyWords = "bitcoin+blockchain+web3"

def busca_atualizada():

    url = f'https://newsapi.org/v2/everything?q={keyWords}&from=2024-04-04&to=2024-04-04&language=en&sortBy=published&page=1&apiKey={apiKey}'
    response = requests.get(url)

    if response.status_code == 200:

      results = response.json()
      print("Requisição feita com sucesso!.")
    else:
      return print("Problema na requisição.")

    return results
print('FASE2')
busca_atualizada()

df1 = pd.json_normalize(busca_atualizada()['articles'])

df1
