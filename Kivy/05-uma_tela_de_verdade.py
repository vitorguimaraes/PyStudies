from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class MyApp(App):
    def build(self):
        layout = FloatLayout()
        self.ed = TextInput(text = "eXcript")
        self.ed.size_hint = None, None
        self.ed.height = 300
        self.ed.width = 400
        self.ed.x = 60
        self.ed.y = 250

        self.bt = Button(text = "Clique aqui")
        self.bt.size_hint = None, None
        self.bt.height = 50
        self.bt.width = 200
        self.bt.x = 170
        self.bt.y = 150
        
        layout.add_widget(self.ed) 
        layout.add_widget(self.bt)

        self.bt.on_press = self.click

        return layout
    
    def click(self):
        print(self.ed.text)

def main():
    Window.size = 600, 600 
        
    root = MyApp()
    root.title = "eXcript"
    root.run()

if __name__ == "__main__":
    main()