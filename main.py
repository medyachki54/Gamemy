from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.audio import SoundLoader

class GameLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lang = 'ru'
        self.sound_on = True
        
        # Фон и ДНК
        self.add_widget(Image(source='lab_bg.jpg', allow_stretch=True, keep_ratio=False))
        
        self.dna_btn = Button(background_normal='dna_purple.png', size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.dna_btn.bind(on_press=self.on_dna_click)
        self.add_widget(self.dna_btn)
        
        # Меню настроек (изначально пустое)
        self.settings_menu = FloatLayout(size_hint=(1, 1))
        
        # Кнопка открытия настроек
        self.settings_btn = Button(text="⚙️", size_hint=(0.1, 0.1), pos_hint={'right': 1, 'top': 1})
        self.settings_btn.bind(on_press=self.open_settings)
        self.add_widget(self.settings_btn)

    def open_settings(self, instance):
        # Очищаем меню перед показом
        self.settings_menu.clear_widgets()
        
        # Фон меню
        self.settings_menu.add_widget(Button(background_color=(0,0,0,0.8))) 
        
        # Кнопки настроек
        btn_sound = Button(text="Звук ВКЛ/ВЫКЛ", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'top': 0.7})
        btn_sound.bind(on_press=self.toggle_sound)
        
        btn_lang = Button(text="Язык RU/EN", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'top': 0.5})
        btn_lang.bind(on_press=self.toggle_lang)
        
        btn_close = Button(text="Назад", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'top': 0.3})
        btn_close.bind(on_press=lambda x: self.remove_widget(self.settings_menu))
        
        self.settings_menu.add_widget(btn_sound)
        self.settings_menu.add_widget(btn_lang)
        self.settings_menu.add_widget(btn_close)
        
        self.add_widget(self.settings_menu)

    def on_dna_click(self, instance):
        # Анимация клика
        anim = Animation(size_hint=(0.35, 0.35), duration=0.05) + Animation(size_hint=(0.4, 0.4), duration=0.05)
        anim.start(instance)

    def toggle_sound(self, instance):
        self.sound_on = not self.sound_on
        # Здесь будет логика управления звуком
        
    def toggle_lang(self, instance):
        self.lang = 'en' if self.lang == 'ru' else 'ru'

class DnaGame(App):
    def build(self):
        return GameLayout()

if __name__ == '__main__':
    DnaGame().run()
