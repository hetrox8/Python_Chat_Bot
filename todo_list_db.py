# todo_list_db.py
import sqlite3
from datetime import datetime, timedelta

class ToDoListDB:
    def __init__(self, username):
        self.username = username
        self.conn = sqlite3.connect('todo.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                task TEXT,
                due_date TEXT,
                completed BOOLEAN
            )
        ''')
        self.conn.commit()

    def add_task(self, task, due_date=None):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO tasks (username, task, due_date, completed) VALUES (?, ?, ?, ?)',
                       (self.username, task, due_date, False))
        self.conn.commit()
        return f"Task '{task}' added to the to-do list."

    def show_tasks(self):
        # Fetch tasks including due dates
        cursor = self.conn.cursor()
        cursor.execute('SELECT task, due_date FROM tasks WHERE username=? AND completed=?', (self.username, False))
        tasks = cursor.fetchall()

        if not tasks:
            return "Your to-do list is empty."
        else:
            tasks_list = "\n".join([f"{task} (Due: {due_date})" if due_date else f"{task}" for task, due_date in tasks])
            return f"Your to-do list:\n{tasks_list}"
