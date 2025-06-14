import random

responses = {
    "hi": ["Hello!", "Hey there!", "Hi! how can help?"],
    "how are you!": ["I'm doing great, thanks!", "Just chilling!", "Good how about you?"],
    "bye": ["see ya!", "Goodbye!", "Take care!"],
    "default": ["Hmm", "Can you repeat that?", "What's up?"]
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])