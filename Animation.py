from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen


class AnimatedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        start_background_color = self.background_color
        start_size_hint = self.size_hint
        start_pos_hint = self.pos_hint
        Animation_1 = Animation(size_hint = (1,1), background_color=(1,1,0,1), pos_hint ={'x':0, 'y':0})
        Animation_2 = Animation(size_hint = (0.5,0.5), background_color=(0,1,0,1), pos_hint ={'x':.25, 'y':.25})
        Animation_3 = Animation(size_hint = (0.25,0.25), background_color=(0,1,1,1), pos_hint ={'x':.75, 'y':.75})
        Animation_4 = Animation(size_hint = (0.5,0.5), background_color=(0,0,1,1), pos_hint ={'x':.25, 'y':.25})
        Animation_5 = Animation(size_hint = (0.25,0.25), background_color=(1,0,1,1), pos_hint ={'x':0, 'y':0})
        Animacion_Vuelta = Animation(background_color = start_background_color, size_hint = (0.5,0.5), pos_hint = start_pos_hint)
        self.animate = Animation_1 + Animation_2 + Animation_3 + Animation_4 + Animation_5 + Animacion_Vuelta

class AnimatedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        start_font_size = self.font_size
        Animation_1 = Animation(font_size=0.5)
        Animation_2 = Animation(font_size=30)
        Animation_Vuelta = Animation(font_size=start_font_size)
        self.animate = Animation_1 + Animation_2 + Animation_Vuelta

class MyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(spacing = 10, orientation = 'vertical')
        self.texto = AnimatedLabel(text = 'Un texto')
        self.boton = AnimatedButton(background_color = (1,0,0,1), text = 'Boton', size_hint=(0.5,0.5), pos_hint ={'x':.25, 'y':.25})
        self.boton.on_press = self.animate_screen
        layout.add_widget(self.texto)
        layout.add_widget(self.boton)
        self.add_widget(layout)

    def animate_screen(self):
        self.boton.animate.start(self.boton)
        self.texto.animate.start(self.texto)
 
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyScreen(name = 'inicio'))
        return sm
 
MyApp().run()