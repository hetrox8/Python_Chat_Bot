from flask import Flask, render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
bcrypt = Bcrypt(app)

users = {}

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    user_todo_list = users[session['username']]['tasks']
    sorted_tasks = sorted(user_todo_list, key=lambda x: (x['due_date'] is None, x['due_date']))
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username not in users:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            users[username] = {'password': hashed_password, 'tasks': []}
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('register.html', message='Username already exists. Choose another.')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and bcrypt.check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', message='Invalid username or password. Please try again.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/add_task', methods=['POST'])
def add_task():
    if 'username' not in session:
        return redirect(url_for('login'))

    task = request.form.get('task')
    priority = int(request.form.get('priority'))
    due_date_str = request.form.get('due_date')
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None

    user_todo_list = users[session['username']]['tasks']
    user_todo_list.append({'task': task, 'priority': priority, 'due_date': due_date})
    return redirect('/')

@app.route('/complete_task', methods=['POST'])
def complete_task():
    if 'username' not in session:
        return redirect(url_for('login'))

    task = request.form.get('task')
    user_todo_list = users[session['username']]['tasks']
    user_todo_list = [t for t in user_todo_list if t['task'] != task]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
