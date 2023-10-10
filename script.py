import nltk
import random

input_patterns = ["What is your name?", "How are you?", "Tell me a joke", "What is your favorite color?"]
responses = ["My name is Chatbot.", "I'm good.", "Why don't scientists trust atoms? Because they make up everything!", "My favorite color is blue."]


tokenized_patterns = [nltk.word_tokenize(pattern) for pattern in input_patterns]


def generate_response(user_input):
    tokenized_input = nltk.word_tokenize(user_input)
    for i, pattern in enumerate(tokenized_patterns):
        if tokenized_input == pattern:
            return responses[i]
    return "I'm sorry, I don't understand."

while True:
    user_input = input("You: ")
    response = generate_response(user_input)
    print("Chatbot:", response)
