import random

#Simple chat program
#Responds randomly with one of four preprogrammed responses

def generate_response(user_input):
  responses = [
    "Wow so cool!",
    "Please don\'t say that!",
    "Very cool!",
    "Programming is fun!"
    'Hi there!',  
    'Hi',  
    'How do you do?',  
    'How are you?',  
    'I\'m cool.',  
    'Always cool.',  
    'I\'m Okay',  
    'Glad to hear that.',  
    'I\'m fine',  
    'I feel awesome',  
    'Excellent, glad to hear that.',  
    'Not so good',  
    'Sorry to hear that.',  
    'What\'s your name?',  
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'X'

  user_input = input("Hello, what\'s your name?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")
  print('Bye')
if __name__ == "__main__":
  init_chat()