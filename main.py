from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from backend import get_response

class ChatApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.chat_container = BoxLayout(orientation='vertical', size_hint_y=None)
        self.chat_container.bind(minimum_height=self.chat_container.setter('height'))
        self.scroll_view = ScrollView(size_hint=(1, 0.7))
        self.scroll_view.add_widget(self.chat_container)
        self.input_box = TextInput(size_hint=(1, 0.1), multiline=True)
        self.send_button = Button(text='Send', size_hint=(1, 0.1))
        self.send_button.bind(on_press=self.send_message)
        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.send_button)
        return self.layout
    
    def send_message(self, instance):
        user_input = self.input_box.text
        if not user_input:
            return
        
        user_label = Label(
            text=f"{user_input}",
            size_hint_y=None,
            height=dp(40),
            text_size=(self.chat_container.width, None),
            halign='right',
            valign='middle',
            padding_x=0,
            color=(1, 1, 1, 1)
        )

        self.chat_container.add_widget(user_label)

        response = get_response(user_input)
        ai_label = Label(
            text=f"{response}",
            size_hint_y=None,
            height=dp(40),
            text_size=(self.chat_container.width, None),
            halign='left',
            valign='middle',
            padding_x=0,
            color=(1, 1, 1, 1)
        )

        self.chat_container.add_widget(ai_label)

        self.input_box.text = ''

        self.scroll_view.scroll_y = 0

if __name__ == '__main__':
    ChatApp().run()