from flask import flash, json, request
from flask_admin.contrib.sqla import ModelView

from app import app, db, admin
from .models import Task

admin.add_view(ModelView(Task, db.session))


class TaskEncoder(json.JSONEncoder):
    '''
		JSON encoder for Tasks
	'''

    def default(self, obj):
        if isinstance(obj, Task):
            return {'id': obj.id, 'title': obj.title, 'task': obj.task, 'completed': obj.completed, 'owner': obj.owner}
        return json.JSONEncoder.default(self, obj)


@app.route('/tasks', methods=['GET'])
def getTasks():
    '''
	Exposes route: /tasks
	Method: GET
	Returns: A list of tasks in the database
	'''
    tasks = Task.query.filter_by().all()
    return json.dumps(tasks, cls=TaskEncoder)


@app.route('/tasks/completed', methods=['GET'])
def getCompletedTasks():
    '''
	Exposes route: /tasks/completed
	Method: GET
	Returns: A list of completed tasks is the database
	'''
    tasks = Task.query.filter_by(completed=True).all()
    return json.dumps(tasks, cls=TaskEncoder)


@app.route('/tasks/uncompleted', methods=['GET'])
def getUncompletedTasks():
    '''
	Exposes route: /tasks/uncompleted
	Method: GET
	Returns: A list of uncompleted tasks is the database
	'''
    tasks = Task.query.filter_by(completed=False).all()
    return json.dumps(tasks, cls=TaskEncoder)


@app.route('/task/<int:id>', methods=['GET'])
def getTask(id):
    '''
	Exposes route: /task/<id>
	Method: GET
	Returns: The task with the specified id or 404 if no task with that id exsists
	'''
    task = Task.query.filter_by(id=id).all()
    if len(task) == 1:
        return json.dumps(task, cls=TaskEncoder), 200, {'ContentType': 'application/json'}
    else:
        return "", 404, {'ContentType': 'application/json'}
