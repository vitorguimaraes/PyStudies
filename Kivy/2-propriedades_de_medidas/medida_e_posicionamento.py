from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class RootWidget(FloatLayout):
    pass

class medida(App):
    def build(self):
        return RootWidget()

def main():
    medida().run()

if __name__ == "__main__":
	main()