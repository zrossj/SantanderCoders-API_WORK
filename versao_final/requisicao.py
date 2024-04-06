import pandas as pd
import requests
from datetime import datetime
print('FASE1')

apiKey = "df97b6ec3d3148c2a0f34e552e3f53af"
keyWords = "bitcoin+blockchain+web3"

def busca_tema():

    url = f'https://newsapi.org/v2/everything?q={keyWords}&from=2024-03-10&to=2024-04-03&language=en&sortBy=published&page=1&apiKey={apiKey}'
    response = requests.get(url)

    if response.status_code == 200:

      results = response.json()
      print("Requisição feita com sucesso!.")
    else:
      return print("Problema na requisição.")

    return results
print('FASE2')

busca_tema()

def atualizar_csv():
    df_novo = pd.json_normalize(busca_tema()['articles'])

    try:
        df_antigo = pd.read_csv('code.csv', index_col=0)
        df_atualizado = pd.concat([df_antigo, df_novo]).drop_duplicates(subset=['publishedAt'], keep='last').reset_index(drop=True)
        df_atualizado.to_csv('code.csv', index=True)
        print(f"Arquivo CSV atualizado com sucesso em {datetime.now()}.")

    except FileNotFoundError:
        df_novo.to_csv('code.csv', index=True)
        print(f"Arquivo CSV criado com sucesso em {datetime.now()}.")

atualizar_csv()
print('FASE3')

import pandas as pd

df2 = pd.read_csv('code.csv',index_col=0)
# df2.rename(columns={0: "index"}, inplace=True)

df2.head()
