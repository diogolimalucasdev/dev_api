import json

from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, Habilidades2
app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Diogo',
        'hablidades': ['Python', 'Flask', 'Django']
    },
    {
        'id': '1',
        'nome': 'Maria',
        'habilidades': ['Python', 'JavaScript', 'React']

    }
]

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': 'Desenvolvedor de Id{} nao existe'.format(id)}
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrator da Api"
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'register delete'}

# Lista todos os desenvolvedor e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        print(posicao)
        dados['id'] = posicao
        #print(dados['id'])
        desenvolvedores.append(dados)
       # print(desenvolvedores[posicao])
        return desenvolvedores[posicao]


api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Habilidades2, '/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
