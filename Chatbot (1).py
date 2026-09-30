# CodeAlpha Task 4 - Basic Chatbot

def chatbot():

    print("================================")
    print("       BASIC CHATBOT")
    print("================================")
    print("Hello! I am your chatbot.")
    print("You can say: hello, how are you, bye")
    print("Type 'bye' to exit.")

    while True:

        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: My name is CodeAlpha Bot.")

        elif user_input == "what can you do":
            print("Bot: I can have a simple conversation with you.")

        elif user_input == "bye" or user_input == "exit":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")



chatbot()