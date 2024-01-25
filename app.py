from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    todo_list.append(task)
    return redirect('/')

@app.route('/complete_task', methods=['POST'])
def complete_task():
    task = request.form.get('task')
    if task in todo_list:
        todo_list.remove(task)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
