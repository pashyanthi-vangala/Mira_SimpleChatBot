from textblob import TextBlob   # Used for sentiment analysis for detecting mood.

# Introduction
print("  ")
print("  ")
print("Welcome to the Chatbot with Sentiment Analyzer! My name is Mira🌸")
print("  ")
print("You can ask questions or share how you feel.")
print("Type 'exit' to exit")
print(" ")


#Pre-stored Chats
chats = {
    "hi": "Hello! How are you doing?",
    "what's up": "Not much! Ready to chat with you.",
    "how is it going": "All good things! How about you?",
    "what is chatbot":"A chatbot is a computer program that simulates human conversation with an end user",
    "what is ai": "AI stands for Artificial Intelligence. It's about making computers think like humans.",
    "how are you": "I'm doing great!",
    "how are you doing": "I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "hello":"Hello! nice to meet you",
    "what can you do": "I can chat with you and even analyze your mood if you tell me how you're feeling!",
    "thank you": "You're welcome! Happy to help.",
    "goodbye": "See you later! Take care.",
    "what is your name": "I'm your friendly AI chatbot! My name is Mira",
    "how old are you": "I don't have an age like humans",
    "i am happy": "That's great to hear! Keep smiling! ",
    "i am sad": "I'm sorry to hear that. If you want to talk, I'm here to listen.",
    "i am tired": "Make sure to get some rest! Your health is important.",
    "what is your favorite colour": "I like all colors equally—I feel like each colour has its own speciality!",
    "thank you very much": "You're very welcome!",
    "good morning": "Good morning! Wish you a great day!",
    "good night": "Good night! Sweet Dreams",
    "fine":"good to know",
    "good":"Nice to know.So whats up?",
    "not good":"Sad to know...What happened?",
    "what is machine learning": "Machine learning is a type of AI that allows computers to learn from data and improve over time.",
    "what is deep learning": "Deep learning is a part of machine learning that uses neural networks to model complex patterns in data.",
    "what is python": "Python is a popular programming language that's great for beginners and widely used in AI, web, and data science.",
    "who made you": "I was built using Python and a library called TextBlob to understand your feelings!",
    "what should i do today": "Try learning something new or going for a walk",
    "love it":"That's Great!",
    "i am bored": "Want to hear a fun fact or a joke to cheer you up?",
    "tell me a fun fact": "The oldest living land animal on earth is a 192-year-old tortoise named Jonathan.",
    "tell me a joke":"Why are mountains so funny? They are hill areas.",
    "fun fact": "The oldest living land animal on earth is a 192-year-old tortoise named Jonathan.",
    "joke":"Why are mountains so funny? They are hill areas.",
    "tell me another fun fact": "A group of owls is called a parliament.",
    "tell me another joke":"What's the difference between spring rolls and summer rolls? Their seasoning.",
    "are you real": "Yep!",
    "can you think": "Not totally like humans, but I can try and respond.",
    "can you feel": "I do not have feelings, but I will try to understand yours!",
    "can you learn": "I learn a little with every conversation!",
    "who is your friend": "Oh! you are my friend",
    "are you happy":"Yes! Totally",
    "i feel anxious": "It is okay to feel that way sometimes. Talk to someone you trust.",
    "i am excited": "That is awesome! What is it got you excited?",
    "i am stressed": "Take a deep breath. Maybe a short break will help.",
    "i am confused": "I am  here to help. What is confusing you?",
    }

while True:  #while condition for repetitive chatting
    user_input = input("You: ")   #Taking input from user
    if user_input.lower() == "exit":       #condition for exit
        print("Chatbot: Bye! Take care.It was nice talking to you.See you soon")
        break
    text_blob = TextBlob(user_input)  # Analyze mood of text using TextBlob
    polarity = text_blob.sentiment.polarity
    if user_input.lower() in chats:          #checking whether input is in chats
        print("Chatbot:", chats[user_input.lower()] )
        print("  ")
    else:       # reply for inputs that are not in chats
        print("Chatbot: Hmm... I don't have a response for that yet. But I'm learning every day!")
        print("  ")
        print("Chatbot:But I analyzed your mood on your input")
        # mood analysis as compensation
        if polarity > 0.2:
            print("You are in Positive mood😊")
            print("  ")
            print("Advice :  Keep going! Ride that positive energy.")
        elif polarity < -0.2:
            print("You are in Negative mood😟")
            print("  ")
            print("Advice : Take a short break or talk to a friend. You’ve got this!")
        else:
            print("You are in Neutral mood😐")
            print("  ")
            print("Advice : Stay balanced! Every day is a fresh start.")