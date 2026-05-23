from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class GameScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Переменные игры
        self.dna = 0
        self.click_power = 1
        self.auto_click_power = 0
        
        # 1. Фон
        self.add_widget(Image(source='lab_bg.jpg', allow_stretch=True, keep_ratio=False))
        
        # 2. Счетчик ДНК
        self.dna_label = Label(text="ДНК: 0", font_size='30sp', pos_hint={'center_x': 0.5, 'top': 0.95})
        self.add_widget(self.dna_label)
        
        # 3. Кнопка настроек (правый верхний угол)
        self.add_widget(Button(text="⚙️", size_hint=(0.1, 0.08), pos_hint={'top': 1, 'right': 1}))
        
        # 4. Кнопка ДНК (центр)
        self.dna_btn = Button(background_normal='dna_purple.png', size_hint=(0.4, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.dna_btn.bind(on_press=self.on_dna_click)
        self.add_widget(self.dna_btn)
        
        # 5. Кнопки магазина
        self.btn_power = Button(text="Сила клика (250)", size_hint=(0.4, 0.1), pos_hint={'x': 0.05, 'y': 0.05})
        self.btn_power.bind(on_press=self.buy_click_power)
        self.add_widget(self.btn_power)
        
        self.btn_auto = Button(text="Автоклик (450)", size_hint=(0.4, 0.1), pos_hint={'right': 0.95, 'y': 0.05})
        self.btn_auto.bind(on_press=self.buy_auto_click)
        self.add_widget(self.btn_auto)
        
        # Запуск автоклика
        Clock.schedule_interval(self.update_auto_click, 1.0)

    def on_dna_click(self, instance):
        self.dna += self.click_power
        self.update_label()

    def buy_click_power(self, instance):
        if self.dna >= 250:
            self.dna -= 250
            self.click_power += 1
            self.update_label()

    def buy_auto_click(self, instance):
        if self.dna >= 450:
            self.dna -= 450
            self.auto_click_power += 1
            self.update_label()

    def update_auto_click(self, dt):
        if self.auto_click_power > 0:
            self.dna += self.auto_click_power
            self.update_label()

    def update_label(self):
        self.dna_label.text = f"ДНК: {self.dna}"

class MyGameApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    MyGameApp().run()
