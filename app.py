from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks',methods=['POST'])
def create_task():
    global task_id_control
    dados = request.get_json()
    new_task = Task(id=task_id_control,title=dados['title'],description=dados.get('description'))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message":"Cadastrado com sucesso"})

@app.route('/tasks', methods = ['GET'])
def read_tasks():
    print(tasks)
    task_list = [task.to_dict() for task in tasks]
    
    output = {
                "tasks": task_list, 
                "total_tasks": len(task_list)
            }

    return jsonify(output)

@app.route('/tasks/<int:id>',methods=['GET'])
def read_task(id):
    for t in tasks:
        if t.getId() == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message":"Não foi possível encontrar esse id"}), 404

@app.route('/tasks/<int:id>',methods=['PUT'])
def update_task(id):
    for t in tasks:
        if t.getId() == id:
            dados = request.get_json()
            t.setTitle(dados['title'])
            t.setDescription(dados['description'])
            t.setCompleted(dados['completed'])
            return jsonify({"message":"Tarefa atualizada com sucesso"})
    return jsonify({"message":"Não foi possível encontrar esse id"}), 404

@app.route('/tasks/<int:id>',methods=['DELETE'])
def remove_task(id):
    for t in tasks:
        if t.getId() == id:
            tasks.remove(t)
            return jsonify({"message":"Tarefa deletada com sucesso"})
    
    return jsonify({"message":"Não foi possível encontrar esse id"}), 404

if __name__ == "__main__":
    app.run(debug=True)