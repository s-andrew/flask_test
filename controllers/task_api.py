#https://habr.com/post/246699/

from app import app
from data import tasks

from flask import jsonify, abort, request


#from flask import Flask
#app = Flask('qwe')


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    task = tuple(task)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/tasks', methods=['POST'])
def create_task():
    # request очень чувствителен к Content-Type
    if not request.json or not 'title' in request.json:
        abort(400)
    task = dict(
            id = tasks[-1]['id'] + 1,
            title = request.json['title'],
            description = request.json.get('description', ''),
            done = False
            )
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    task = tuple(task)
    if len(task) == 0:
        abort(404)
        
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    
    task = task[0]
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})