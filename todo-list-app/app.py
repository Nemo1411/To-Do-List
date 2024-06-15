from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'POST':
        new_task = Task(title=request.json['title'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.id), 201
    
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'title': task.title, 'completed': task.completed} for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def handle_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'PUT':
        task.completed = request.json.get('completed', task.completed)
        db.session.commit()
        return '', 204
    
    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
