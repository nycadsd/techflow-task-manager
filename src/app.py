from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []

@app.route("/")
def inicio():
    return "Sistema de Gerenciamento de Tarefas - TechFlow Solutions"


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():

    dados = request.get_json()

    tarefa = {
        "titulo": dados["titulo"]
    }

    tarefas.append(tarefa)

    return jsonify({
        "mensagem": "Tarefa criada com sucesso",
        "tarefa": tarefa
    }), 201


if __name__ == "__main__":
    app.run(debug=True)