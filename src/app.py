from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []
proximo_id = 1

@app.route("/")
def inicio():
    return "Sistema de Gerenciamento de Tarefas - TechFlow Solutions"


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():

    global proximo_id

    dados = request.get_json()

    tarefa = {
        "id": proximo_id,
        "titulo": dados["titulo"]
    }

    tarefas.append(tarefa)
    proximo_id += 1

    return jsonify({
        "mensagem": "Tarefa criada com sucesso",
        "tarefa": tarefa
    }), 201


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():

    return jsonify(tarefas)


if __name__ == "__main__":
    app.run(debug=True)