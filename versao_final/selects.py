import re
import pandas as pd
import requests
from datetime import datetime
print('FASE1')
# %%
df_historico = pd.read_csv("code.csv")

df_historico['ano'] = df_historico.publishedAt.apply(lambda x: x.split('-')[0])
df_historico['mes'] = df_historico.publishedAt.apply(lambda x: x.split('-')[1])
df_historico['dia'] = df_historico.publishedAt.apply(lambda x: x.split('-')[2][:2])

df_historico.head()

# %%
# 4.1 - Quantidade de notícias por ano, mês e dia de publicação;

noticias_por_data = df_historico.groupby(['ano', 'mes', 'dia']).count()[['title']]
noticias_por_data.head(3) # apagar o head

#     - 4.2 - Quantidade de notícias por fonte e autor;
noticias_por_fonte_autor = df_historico.groupby(['source.name', 'author']).size().reset_index(name='Quantidade')
noticias_por_fonte_autor



# 4.3 - Quantidade de aparições das 3 palavras-chave por ano, mês e dia de publicação definidas no item 2
palavras_chave = ['bitcoin', 'blockchain', 'web3']
for palavra in palavras_chave:
    df_historico[palavra] = df_historico['title'].str.count(palavra, flags=re.IGNORECASE)

aparicoes_palavras_chave = df_historico.groupby(['ano', 'mes', 'dia'])[palavras_chave].sum().reset_index()

aparicoes_palavras_chave


# Salvando as transformações em arquivo csv
noticias_por_data.to_csv("noticias_por_data.csv",sep=",")
noticias_por_fonte_autor.to_csv("noticias_por_fonte_autor.csv",sep=",",index=False)
aparicoes_palavras_chave.to_csv("aparicoes_palavras_chave.csv",sep=",",index=False)
# %%
