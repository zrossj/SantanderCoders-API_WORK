import pandas as pd
import re
import numpy as np
import requests
from flask import Flask, jsonify, make_response, request
import csv
import sys
import time
from datetime import datetime



def busca_tema():
    url = 'https://newsapi.org/v2/everything?q=bitcoin+blockchain+web3&from=2024-03-10&to=2024-04-03&language=en&sortBy=published&page=1&apiKey=df97b6ec3d3148c2a0f34e552e3f53af'
    r = requests.get(url)

    if r.status_code == 200:
        results = r.json()
    else:
        print("Problema na requisição.")
        results = None

    return results

def atualizar_csv():
    df_novo = pd.json_normalize(busca_tema()['articles'])
    try:
        df_antigo = pd.read_csv('code.csv', index_col = 0)
        df_atualizado = pd.concat([df_antigo, df_novo]).drop_duplicates(subset=['author', 'title'], keep='last')
        df_atualizado = df_atualizado.reset_index(drop=True)
        df_atualizado.to_csv('code.csv')
        print(f"Arquivo CSV atualizado com sucesso em {datetime.now()}.")
    except FileNotFoundError:
        df_novo.to_csv('code.csv', index=True)
        print(f"Arquivo CSV criado com sucesso em {datetime.now()}.")


while True:
    atualizar_csv()
    time.sleep(10)  # Espera 1 hora (3600 segundos) antes de verificar novamente


df = pd.read_csv("code.csv")

df['ano'] = df.publishedAt.apply(lambda x: x.split('-')[0])
df['mes'] = df.publishedAt.apply(lambda x: x.split('-')[1])
df['dia'] = df.publishedAt.apply(lambda x: x.split('-')[2][:2])




# 4.1 - Quantidade de notícias por ano, mês e dia de publicação;

noticias_por_data = df.groupby(['ano', 'mes', 'dia']).count()[['title']]
noticias_por_data.head(3) # apagar o head

#     - 4.2 - Quantidade de notícias por fonte e autor;
noticias_por_fonte_autor = df.groupby(['source.name', 'author']).size().reset_index(name='Quantidade')
noticias_por_fonte_autor



# 4.3 - Quantidade de aparições das 3 palavras-chave por ano, mês e dia de publicação definidas no item 2
palavras_chave = ['bitcoin', 'blockchain', 'web3']
for palavra in palavras_chave:
    df[palavra] = df['title'].str.count(palavra, flags=re.IGNORECASE)

aparicoes_palavras_chave = df.groupby(['ano', 'mes', 'dia'])[palavras_chave].sum().reset_index()



# Salvando as transformações em arquivo csv
noticias_por_data.to_csv("noticias_por_data.csv",sep=",")
noticias_por_fonte_autor.to_csv("noticias_por_fonte_autor.csv",sep=",",index=False)
aparicoes_palavras_chave.to_csv("aparicoes_palavras_chave.csv",sep=",",index=False)

#%%
import pandas as pd
df = pd.read_csv('~/code.csv', index_col=0)
df.reset_index(drop = True)

# %%
