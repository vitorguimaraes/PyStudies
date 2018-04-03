from kivy.app import App
from kivy.uix.textinput import TextInput


class MyApp(App):
    def build(self):
        return TextInput(text = "Insira o texto aqui")

def main():
    MyApp().run()

if __name__ == "__main__":
    main()