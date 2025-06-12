from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
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

class ChatApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.chat_display = Label(text='\n', size_hint=(1, 0.7))
        self.input_box = TextInput(size_hint=(1, 0.1), multiline=True)
        self.send_button = Button(text='Send', size_hint=(1, 0.1))
        self.send_button.bind(on_press=self.send_message)
        self.layout.add_widget(self.chat_display)
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.send_button)
        return self.layout
    
    def send_message(self, instance):
        user_input = self.input_box.text
        self.chat_display.text += f"You: {user_input}\n"
        response = get_response(user_input)
        self.chat_display.text += f"Bot: {response}\n"
        self.input_box.text = ''

if __name__ == '__main__':
    ChatApp().run()