
import pandas as pd
#import pyspark.pandas as ps 
from flask import Flask, jsonify, make_response, request


#app.config["JSON_SORT_KEYS"] = False

app = Flask(
    __name__
)  # instância o método Flask com o nome do app igual ao nome do arquivo.py



dados = pd.read_csv('~/Downloads/code.csv')

@app.route("/", methods=["GET"])  # define o endpoint da página e qual método ela aceita
def homepage():

    return jsonify(
        dados.to_json())


@app.route("/dados", methods=["GET"])  # define o endpoint da página e qual método ela aceita
def todos_dados():

    return jsonify({"mensagem": "olá, você está na página principal", "pagina": 1})

@app.route("/dados/<int:id>", methods = ["GET"])
def retorna_id(id):

    try:
        df_id = dados.loc[[id]].to_json()
        return jsonify(
            df_id)
    except:
        print("id não encontrado")
        return jsonify(
            dados.to_json())




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





if __name__ == "__main__":
    app.run(port = 5002, debug=True)



#%%
import pandas as pd
dados = pd.read_csv('~/Downloads/code.csv')
dados.head()

#dados.to_json()
#%%