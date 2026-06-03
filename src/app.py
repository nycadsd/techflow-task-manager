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
        "titulo": dados["titulo"],
        "status": "Pendente"
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

@app.route("/tarefas/<int:id>", methods=["PUT"])
def editar_tarefa(id):

    dados = request.get_json()

    for tarefa in tarefas:

        if tarefa["id"] == id:

            tarefa["titulo"] = dados["titulo"]

            return jsonify({
                "mensagem": "Tarefa atualizada com sucesso",
                "tarefa": tarefa
            })

    return jsonify({
        "erro": "Tarefa não encontrada"
    }), 404

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir_tarefa(id):

    for tarefa in tarefas:

        if tarefa["id"] == id:

            tarefas.remove(tarefa)

            return jsonify({
                "mensagem": "Tarefa removida com sucesso"
            })

    return jsonify({
        "erro": "Tarefa não encontrada"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)