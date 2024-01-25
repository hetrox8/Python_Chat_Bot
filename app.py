from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    sorted_tasks = sorted(todo_list, key=lambda x: (x['due_date'] is None, x['due_date']))
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    priority = int(request.form.get('priority'))
    due_date_str = request.form.get('due_date')
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None

    todo_list.append({'task': task, 'priority': priority, 'due_date': due_date})
    return redirect('/')

@app.route('/complete_task', methods=['POST'])
def complete_task():
    task = request.form.get('task')
    todo_list = [t for t in todo_list if t['task'] != task]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
