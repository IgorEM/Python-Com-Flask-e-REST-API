from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Igor',
     'habilidades': ['Python', 'Django', 'Flask','PostGre']},
    {'nome': 'Eduardo',
     'habilidades': ['HTML5', 'CSS3', 'JavaScript','Node','React','Vue','BootStrap']}

]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            devResponse = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            devResponse = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrados da API'
            devResponse = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(devResponse)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido'})

@app.route('/dev')
def  lista_desenvolvedores():
    if request.method == 'POST':
        dados 

if __name__ == '__main__':
    app.run()