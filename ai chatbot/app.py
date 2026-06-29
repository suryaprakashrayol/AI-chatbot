def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm doing well. Thanks for asking!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

# Chat loop
while True:
    message = input("You: ")
    response = chatbot(message)
    print("Bot:", response)

    if message.lower() == "bye":
        break