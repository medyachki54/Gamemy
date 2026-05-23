import json
import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

# Функция для определения пути сохранения
def get_save_path():
    # Если мы на Android, сохраняем в папку приложения
    if os.path.exists('/sdcard/'): 
        return "save.json" 
    # В Colab можно использовать путь, если нужно, но для APK лучше проще:
    return "save.json"

class GameScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.dna = 0
        self.click_power = 1
        self.auto_click_power = 0
        
        self.load_game() # Загружаем данные сразу при старте
        
        # --- Твои виджеты ---
        self.dna_label = Label(text=f"ДНК: {self.dna}", font_size='30sp', pos_hint={'center_x': 0.5, 'top': 0.95})
        self.add_widget(self.dna_label)
        
        self.dna_btn = Button(text="Жми на ДНК!", size_hint=(0.4, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.dna_btn.bind(on_press=self.on_dna_click)
        self.add_widget(self.dna_btn)
        
        Clock.schedule_interval(self.update_auto_click, 1.0)

    def save_game(self):
        data = {"dna": self.dna, "power": self.click_power, "auto": self.auto_click_power}
        with open(get_save_path(), "w") as f:
            json.dump(data, f)

    def load_game(self):
        if os.path.exists(get_save_path()):
            with open(get_save_path(), "r") as f:
                data = json.load(f)
                self.dna = data.get("dna", 0)
                self.click_power = data.get("power", 1)
                self.auto_click_power = data.get("auto", 0)

    def on_dna_click(self, instance):
        self.dna += self.click_power
        self.dna_label.text = f"ДНК: {self.dna}"
        self.save_game()

    def update_auto_click(self, dt):
        if self.auto_click_power > 0:
            self.dna += self.auto_click_power
            self.dna_label.text = f"ДНК: {self.dna}"
            self.save_game()

class MyGameApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    MyGameApp().run()
