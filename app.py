from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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


# Put deixa com eu altere os dados
# GET eu recebo esses dados no navegador

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': 'Desenvolvedor de Id{} nao existe'.format(id)}
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrator da Api"
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucess', 'mensagem': 'register delete'})


# Lista todos os desenvolvedor e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
