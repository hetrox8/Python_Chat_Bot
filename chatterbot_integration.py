# chatterbot_integration.py
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class ToDoListChatbot:
    def __init__(self):
        self.chatbot = ChatBot("To-Do Bot")
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.trainer.train("chatterbot.corpus.english")

    def get_response(self, user_input):
        return self.chatbot.get_response(user_input)
