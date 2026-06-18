def chatbot():
    print("🤖 ChatBot Started")
    print("Type 'bye' to exit")

    while True:
        msg = input("You: ").lower()

        if msg == "hello":
            print("Bot: Hi! How can I help you?")
        elif msg == "how are you":
            print("Bot: I'm fine, thank you!")
        elif msg == "what is your name":
            print("Bot: I am a Python ChatBot.")
        elif msg == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()