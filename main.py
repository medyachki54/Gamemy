from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import json
import os

# Путь к файлу сохранения
SAVE_PATH = "save.json"

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dna_count = 0
        
        # Фон
        self.add_widget(Image(source='assets/dna_bg.jpg', allow_stretch=True, keep_ratio=False))
        
        # Счётчик
        self.dna_label = Label(text="ДНК: 0", font_size='40sp', pos_hint={'center_x': 0.5, 'top': 0.9})
        self.add_widget(self.dna_label)
        
        # Кнопка ДНК
        btn = Button(text="ЖМИ", size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn.bind(on_press=self.increment_dna)
        self.add_widget(btn)
        
        # Кнопка магазина
        shop_btn = Button(text="Маг", size_hint=(0.1, 0.1), pos_hint={'right': 1, 'top': 1})
        shop_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'shop'))
        self.add_widget(shop_btn)
        
        # Кнопка настроек
        set_btn = Button(text="Настр", size_hint=(0.1, 0.1), pos_hint={'right': 0.9, 'top': 1})
        set_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'settings'))
        self.add_widget(set_btn)

    def increment_dna(self, instance):
        self.dna_count += 1
        self.dna_label.text = f"ДНК: {self.dna_count}"
        self.save_game()

    def save_game(self):
        with open(SAVE_PATH, "w") as f:
            json.dump({"dna": self.dna_count}, f)

class ShopScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Это Магазин"))
        back_btn = Button(text="Назад", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'y': 0.1})
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'game'))
        self.add_widget(back_btn)

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Это Настройки"))
        back_btn = Button(text="Назад", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'y': 0.1})
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'game'))
        self.add_widget(back_btn)

class MyGameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(ShopScreen(name='shop'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    MyGameApp().run()
