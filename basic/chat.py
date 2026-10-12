# Simple Two-Way Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "name" in user_input:
        return "I am a simple Python chatbot."

    elif "how are you" in user_input:
        return "I am doing great! Thanks for asking."

    elif "python" in user_input:
        return "Python is a popular programming language used for AI, web development, and automation."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand. Can you ask something else?"


print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")

    response = chatbot_response(user)
    print("Chatbot:", response)

    if "bye" in user.lower():
        break