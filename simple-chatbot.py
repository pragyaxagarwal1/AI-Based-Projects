import random

responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm fine!", "Doing well, thanks!", "All good!"],
    "bye": ["Goodbye!", "See you!", "Take care!"]
}

def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            break
        for key in responses:
            if key in user_input:
                print("Bot:", random.choice(responses[key]))
                break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
