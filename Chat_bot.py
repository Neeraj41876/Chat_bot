import random

def chatbot():
    print("Hello! I am an extended dictionary-based chatbot. Type 'exit' to end the conversation.")
    
    responses = {
        "hello": [
            "Hello there! How can I help you today?", 
            "Hi! What can I do for you?", 
            "Hey! Need assistance with something?",
            "Greetings! How can I assist you?",
            "Hello! What would you like to talk about?"
        ],
        "how are you": [
            "I'm just a program, but I'm doing well! How about you?", 
            "Doing great! How are you doing?",
            "I’m here and ready to help! How about you?",
            "I'm functioning well, thank you! What’s on your mind?"
        ],
        "your name": [
            "I'm called Chatbot. What's your name?", 
            "You can call me Chatbot! And you?",
            "I'm known as Chatbot. Nice to meet you!",
            "They call me Chatbot. What should I call you?"
        ],
        "what can you do": [
            "I can chat with you and answer simple questions!", 
            "I'm here to help with any questions you have!",
            "I can assist with information and conversation.",
            "I'm designed to provide answers and engage in discussions!"
        ],
        "goodbye": [
            "Goodbye! Have a great day!", 
            "See you later!", 
            "Take care! Until next time!",
            "Farewell! I'm here whenever you need me."
        ],
        "joke": [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I told my computer I needed a break, and now it won’t stop sending me beach wallpapers!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!"
        ],
        "weather": [
            "I can't check the weather, but it's always sunny in my code!",
            "The weather is a bit cloudy, but I’m here to brighten your day!",
            "I can’t provide real-time weather updates, but I hope it’s nice where you are!",
            "If I could check the weather, I would say it's perfect for a chat!"
        ],
        "favorite color": [
            "I don’t have a favorite color, but I love all colors of the text!",
            "Colors are fascinating! What's your favorite?",
            "I think I’d like all colors equally, since they all represent different things.",
            "I don't see colors, but I appreciate how they make the world vibrant!"
        ],
        "hobbies": [
            "I enjoy chatting with users like you! What are your hobbies?",
            "I don't have hobbies like humans, but I love answering your questions!",
            "My main hobby is learning from our conversations!",
            "I guess you could say my hobby is being helpful!"
        ],
        "music": [
            "I don't listen to music, but I know many people love it!",
            "Music is a wonderful form of art! What’s your favorite genre?",
            "If I could listen, I’d love to know what you enjoy!",
            "I can't play music, but I can help you find songs or artists!"
        ],
        "news": [
            "I can’t browse the web for news, but I’m here to chat about anything!",
            "I don’t have the latest news, but I’d love to hear what interests you!",
            "News can be overwhelming. What topics do you find intriguing?",
            "I’m not up-to-date, but I can discuss general news topics!"
        ],
    }

    keywords = {k: v for k, v in responses.items()}
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        matched_response = None
        for keyword in keywords:
            if keyword in user_input:
                matched_response = random.choice(keywords[keyword])
                break
        
        if matched_response:
            print("Chatbot:", matched_response)
        else:
            print("Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()
