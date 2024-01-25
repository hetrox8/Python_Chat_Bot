# main.py
import tkinter as tk
from chatterbot_integration import ToDoListChatbot
from user_management import register_user, authenticate_user
from todo_list_db import ToDoListDB
from datetime import datetime, timedelta
from todo_list_ui import ToDoListUI

def main():
    # Example user registration and authentication
    username = "john_doe"
    password = "secure_password"

    register_user(username, password)
    authenticated = authenticate_user(username, password)

    if authenticated:
        # Initialize ChatterBot
        todo_list_chatbot = ToDoListChatbot()

        # Instance of ToDoListDB
        todo_list_db = ToDoListDB(username)

        # Create and run the Tkinter UI
        root = tk.Tk()
        app = ToDoListUI(root, todo_list_db, todo_list_chatbot)
        root.mainloop()

if __name__ == "__main__":
    main()
