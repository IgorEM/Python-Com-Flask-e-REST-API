from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/<int:id>")
def minha_api_pessoa(id):
    return jsonify({'id':id,'nome': 'Igor', 'profissao':'Desenvolvedor'})

@app.route('/sum1/<int:valor1>/<int:valor2>/')
def sum1(valor1, valor2):
    return jsonify({'sum1': valor1 + valor2}) #funciona sem o jsonify

@app.route('/soma', methods=['POST','GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
        print(dados)
    elif request.method == 'GET':
        total = 10 + 32

    return jsonify({'soma':total})

if __name__ == '__main__':
    app.run(debug=True)

#testado no POSTMAN :D
#teste console
""" 
METODO GET

>>> response = requests.get('http://127.0.0.1:5000/soma')
>>> response
<Response [200]>

>>> print(response.text)
{
  "soma": 42
}

>>> print(response.json())
{'soma': 42}


>>> dados = response.json()
>>> print(dados)
{'soma': 42}

>>> print(dados['soma'])
42

METODO POST


"""


