import json

from flask_restful import Resource, request

lista_habilidades = ['Python', 'Java', 'Flask', 'PHB']


class Habilidades(Resource):

    # mostra todas as habilidades da lista_habilidades
    def get(self):
        return lista_habilidades

    # adicona mais uma hablidade a lista_habilidades
    def post(self):
        dados = json.loads(request.data)
        if dados in lista_habilidades:
            return f"A habilidade {dados} ja esta inserida na lista !"
        else:
            lista_habilidades.append(dados)
            return f"item {dados} adicionado a lista com sucesso  {lista_habilidades}"


# criei mais uma class pois como essa precisa de um id, passo pelo uri
class Habilidades2(Resource):

    # No put ele adiciona uma habilidade no lugar de outra habilidade escolhida atraves do id
    def put(self, id):
        dados = json.loads(request.data)
        if dados in lista_habilidades:
            return f"A habilidade {dados} ja esta inserida na lista !"
        else:
            lista_habilidades[id] = dados
            return f"Item {dados} adicionado a lista {lista_habilidades}"

    # como o método ja diz eu deleto uma habilidade
    def delete(self, id):
        lista_habilidades.pop(id)
        return f"Item deletado com sucesso  {lista_habilidades}"
