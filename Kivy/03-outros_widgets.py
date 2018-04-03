from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        bt = Button(text="Clique aqui")
        bt.on_press = self.click
        return bt

    def click(self):
        print("O botão foi clicado")

def main():
    MyApp().run()

if __name__ == "__main__":
    main()
