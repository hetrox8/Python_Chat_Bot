# todo_list_ui.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from chatterbot_integration import ToDoListChatbot
from user_management import register_user, authenticate_user
from todo_list_db import ToDoListDB

class ToDoListUI:
      def __init__(self, root, todo_list_db, todo_list_chatbot):
        self.root = root
        self.root.title("To-Do List Application")

        # Initialize ChatterBot
        self.todo_list_db = todo_list_db
        self.todo_list_chatbot = todo_list_chatbot

        # UI Elements
        self.label = tk.Label(root, text="You:")
        self.entry = tk.Entry(root)
        self.button = tk.Button(root, text="Enter", command=self.process_user_input)
        self.text_area = tk.Text(root, height=15, width=50)
        self.scrollbar = tk.Scrollbar(root, command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        # Pack UI Elements
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.text_area.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Example user registration and authentication
        self.username = "john_doe"
        self.password = "secure_password"
        register_user(self.username, self.password)
        authenticated = authenticate_user(self.username, self.password)

        if authenticated:
            # Instance of ToDoListDB
            self.todo_list_db = ToDoListDB(self.username)

    def process_user_input(self):
        user_input = self.entry.get()
        response = self.todo_list_chatbot.get_response(user_input)

        if "add_task" in response.data:
            task = response.data["add_task"]
            self.text_area.insert(tk.END, f"To-Do Bot: {self.todo_list_db.add_task(task)}\n")
        elif "show_tasks" in response.data:
            tasks = self.todo_list_db.show_tasks()
            self.text_area.insert(tk.END, f"To-Do Bot: {tasks}\n")
        elif "exit" in response.data:
            self.text_area.insert(tk.END, "To-Do Bot: Exiting the to-do list application. Goodbye!\n")
            self.root.destroy()
        else:
            self.text_area.insert(tk.END, f"To-Do Bot: {response}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListUI(root)
    root.mainloop()
