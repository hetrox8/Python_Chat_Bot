# user_management.py
import bcrypt

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Example usage:
users = {}

def register_user(username, password):
    if username not in users:
        users[username] = User(username, password)
        print(f"User '{username}' registered successfully.")
    else:
        print(f"User '{username}' already exists.")

def authenticate_user(username, password):
    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username].password_hash):
        print(f"User '{username}' authenticated successfully.")
        return True
    else:
        print(f"Authentication failed for user '{username}'.")
        return False
