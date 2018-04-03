from kivy.app import App
from kivy.uix.label import Label 

class MyApp(App):
	def build(self):
		lb = Label()
		lb.text = "Python e Kivy"
		lb.italic = True
		lb.font_size = 50
		
		return lb

def main():
	MyApp().run()

if __name__ == "__main__":
	main()
