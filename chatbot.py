print("🤖 AI Chatbot Started!")

while True:
    user_input = input("You: ").lower()

    # Greeting responses
    if user_input == "hello":
        print("Bot: Hello! How can I help you?")

    elif user_input == "hi":
        print("Bot: Hi there!")

    elif user_input == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    # Basic questions
    elif user_input == "your name":
        print("Bot: I am DecodeLabs AI Bot.")

    elif user_input == "what are you doing":
        print("Bot: I am chatting with you.")

    # Exit condition
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand.")