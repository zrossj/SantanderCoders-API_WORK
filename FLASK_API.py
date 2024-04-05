
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


if __name__ == "__main__":
    app.run(port = 5001, debug=True)



#%%
import pandas as pd
dados = pd.read_csv('~/Downloads/code.csv')
dados.head()

#dados.to_json()
#%%