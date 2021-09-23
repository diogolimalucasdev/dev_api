import json

from flask_restful import Resource, request

lista_habilidades = ['Python', 'Java', 'Flask', 'PHB']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados)
        return f"item {dados} adicionado a lista com sucesso \n {lista_habilidades}"


class Habilidades2(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return f"Item {dados} adicionado a lista\n {lista_habilidades}"

    def delete(self, id):
        lista_habilidades.pop(id)
        return f"Item deletado com sucesso \n {lista_habilidades}"
