# CodeAlpha - Basic Chatbot

def chatbot():
    print("Simple Chatbot Started! (Type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi there!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("Bot: I am CodeAlpha Bot.")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()