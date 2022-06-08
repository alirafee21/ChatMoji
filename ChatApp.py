import kivy

from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App 
textinput = TextInput(text='Hello world')
kivy.require("2.1.0")

class ChatApp(App):
    def build(self):
        b = BoxLayout(orientation ='vertical')
        b.add_widget(Label(text="IP:"))
        b.port = TextInput(multiline=False, focus=True)
        b.add_widget(b.port)
        
        return b

if __name__ == "__main__":
    ChatApp().run()