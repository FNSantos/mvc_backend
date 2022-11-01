from flask import Flask
from Model.Produto_Model import produto_Model


app = Flask(__name__)

@app.route('/v1/produto/consultar/', methods=["GET"])
def consultar():
    return produto_Model.produtos()


if __name__ == '__main__':
    app.run(debug=True,port=5000)