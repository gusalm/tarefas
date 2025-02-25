from flask import Flask, request

app = Flask(__name__)

tarefas = [
    {
            'id':1,
            'titulo': "Lavar Louca",
            'descricao': "Lavar os pratos",
            'status': "Nao iniciado",
            'duracao': "10 minutos",
            'dificuldade': "Facil",
            'prioridade': "Baixa"
    },
    {
            'id':2,
            'titulo': "Estudar",
            'descricao': "Estudar matematica",
            'status': "Nao iniciado",
            'duracao': "10 minutos",
            'dificuldade': "Facil",
            'prioridade': "Alta"
    }
]

@app.route('/tasks', methods = ['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods = ['GET'])
def get_tasks_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:

            return tarefa

    return 'Tarefa nao encontrada'

@app.route('/tasks', methods = ['POST'])
def create_tasks():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['duracao'] = task_body.get('duracao')
    task_search['dificuldade'] = task_body.get('dificuldade')
    task_search['prioridade'] = task_body.get('prioridade')


    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)

    return 'A tarefa foi escluida'


if __name__ == '__main__':
    app.run(debug=True)