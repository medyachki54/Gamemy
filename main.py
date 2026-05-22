from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ClickerGame(App):
    def build(self):
        self.count = 0
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text='Счет: 0', font_size=40)
        self.layout.add_widget(self.label)
        
        btn = Button(text='Жми на ДНК!', font_size=30)
        btn.bind(on_press=self.increment)
        self.layout.add_widget(btn)
        
        return self.layout

    def increment(self, instance):
        self.count += 1
        self.label.text = f'Счет: {self.count}'

if __name__ == '__main__':
    ClickerGame().run()
