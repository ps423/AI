'''
Q.2) Write a Python program to implement Simple Chatbot
[20 Marks]
'''

print("Hello! I'm a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    
    if 'hello' in user_input or 'hi' in user_input:
        print("Bot: Hi there!")
    elif 'how are you' in user_input:
        print("Bot: I'm doing well, thank you!")
    elif 'name' in user_input:
        print("Bot: I'm a simple chatbot.")
    elif 'bye' in user_input or 'exit' in user_input:
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: I'm sorry, I don't understand that.")
