from flask import Flask, request, jsonify, make_response
import json

tasks = [
    {
        'id': 1,
        'nome': "Arroz",
        'preco' : 7.00
    },
    {
        "id": 2,
        "nome": "Feijão",
        'preco' : 10.00
    },
    {
        "id": 3,
        "nome": "Macarrão",
        'preco' : 3.50
    }
]

listprodutos = json.dumps(tasks)

class produto_Model:
    def produtos():
        return listprodutos

