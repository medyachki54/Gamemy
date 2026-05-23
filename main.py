from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle

class ClickerGame(App):
    def build(self):
        self.count = 0
        # Используем FloatLayout для размещения элементов поверх фона
        self.layout = FloatLayout()

        # Задний фон (темно-синий)
        with self.layout.canvas.before:
            Color(0.1, 0.1, 0.2, 1)
            self.rect = Rectangle(size=(2000, 2000), pos=self.layout.pos)

        # Настройки (в правом верхнем углу)
        settings_btn = Button(text='⚙️', size_hint=(0.15, 0.1), pos_hint={'right': 1, 'top': 1})
        self.layout.add_widget(settings_btn)

        # Счетчик
        self.label = Label(text='Счет: 0', font_size=50, pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.layout.add_widget(self.label)
        
        # Кнопка клика
        self.btn = Button(text='Жми на ДНК!', size_hint=(0.4, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.btn.bind(on_press=self.animate_click)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def animate_click(self, instance):
        self.count += 1
        self.label.text = f'Счет: {self.count}'
        
        # Анимация: кнопка увеличивается и возвращается
        anim = Animation(size_hint=(0.45, 0.25), duration=0.1) + Animation(size_hint=(0.4, 0.2), duration=0.1)
        anim.start(instance)

if __name__ == '__main__':
    ClickerGame().run()
