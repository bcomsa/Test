# -*- coding: utf8 -*-
import random
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.app import App

class Snow(BoxLayout):
    FLAKE_SIZE = 5 
    NUM_FLAKES = 200
    FLAKE_AREA = FLAKE_SIZE * NUM_FLAKES
    FLAKE_INTERVAL = 1.0 / 30.0

    def __init__(self, **kwargs):
        super(Snow, self).__init__(**kwargs)
        self.flakes = [[x * self.FLAKE_SIZE, 0]
            for x in range(self.NUM_FLAKES)] 

        Clock.schedule_interval(self.update_flakes, self.FLAKE_INTERVAL)

    def update_flakes(self, time):
        for f in self.flakes:
            f[0] += random.choice([-1, 1])
            f[1] -= random.randint(0, self.FLAKE_SIZE)
            if f[1] <= 0:
                f[1] = random.randint(0, int(self.height))

        self.canvas.clear()
        with self.canvas:
            widget_x = self.center_x - self. FLAKE_AREA / 2 
            widget_y = self.pos[1]
            for x_flake, y_flake in self.flakes:
                x = widget_x + x_flake  
                y = widget_y + y_flake
                Color(0.9, 0.9, 1.0) 
                Ellipse(pos=(x, y), size=(self.FLAKE_SIZE, self.FLAKE_SIZE))

class mitchanlai(BoxLayout):
    game_id = ObjectProperty()
    title = StringProperty('Mít Chằn Lai - Flappy Minon For Nguyễn Ngọc Ánh')
    title_temp = 'Mít Chằn Lai - Flappy Minon For Nguyễn Ngọc Ánh'
    sound = [
                SoundLoader.load('Sound/Anh Thuy Chi - Thuy Chi.mp3'),
                SoundLoader.load('Sound/Nho Nhung - Bao Anh.mp3')
            ]
    def show_snow(self): 
        self.game_id.clear_widgets()
        self.game_id.add_widget(Snow())
        self.play_music_2()
    def show_game(self):
        self.game_id.clear_widgets()
        self.game_id.add_widget(tamthegame.TamTheGame())#flappyminion.FlappyMinion())
    def play_music_2(self):
        self.stop_all_sound() 
        if self.sound[1].state == 'play' : 
            self.sound[1].stop()
            self.title = self.title_temp
        else: 
            self.sound[1].play()        
            self.title = 'Bạn Đang Nghe Ca Khúc : Nhớ Nhung - Bảo Anh'
    def play_sound(self): 
        self.stop_all_sound()
        if self.sound[0].state == 'play' : 
            self.sound[0].stop()
            self.title = self.title_temp
        else: 
            self.sound[0].play()        
            self.title = 'Bạn Đang Nghe Ca Khúc : Anh - Thùy Chi ft Anh Vũ'
    def stop_all_sound(self):
        for sound in self.sound:
            sound.stop()

class mitchanlaiApp(App):
    def build(self):
        Window.size = (1024,600)
        self.sound = None
        return mitchanlai()

if __name__ == '__main__':
    mitchanlaiApp().run()
