import random
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.app import App

class Player(Image):
    pass
class EnemyTop(Image):
    pass
class EnemyBottom(Image):
    pass
class Land(Image):
    pass
class FlappyMinion(FloatLayout):
    INTERVAL= 1.0 / 30.0
    gap = Window.height / 2.5
    enemy_width = Window.width / 10
    enemy_speed = 10
    player_size = Window.width / 12, Window.width / 12
    player_velocity = 10
    player_jump = 80
    score = NumericProperty()
    score_label = ObjectProperty()
    def __init__(self, **kwargs):
        super(FlappyMinion, self).__init__(**kwargs)
        self.AllEnemy = []
        self.playgame = True
        self.startgame = False
        self.startgamelabel = Label(center = Window.center, 
                                    text = 'Tap Anywhere To Play',
                                    font_size = 30,
                                    color = (1, .5, .5, 1),
                                    size_hint = (None, None))
        self.add_widget(self.startgamelabel)
        Clock.schedule_interval(self.update, self.INTERVAL)
    def makeEnemy(self):
        enemy_height1 = random.randint(int((self.height * 4 / 5)/10), int((self.height * 4 / 5)/2))
        enemy_height2 = self.height - self.gap - enemy_height1 - self.height / 5
        enemy1 = EnemyBottom(x = Window.width ,y = self.y + self.height / 5,size = (self.enemy_width, enemy_height1))
        enemy2 = EnemyTop(x = Window.width ,y = self.top - enemy_height2,size = (self.enemy_width, enemy_height2))
        return enemy1,enemy2
    def update(self, time):
        if self.startgame == False : return
        self.player.y -= self.player_velocity
        if self.player.y < self.y + self.height / 5:
            self.restart()
        if self.score == 10:
            return
        for enemy in self.AllEnemy:
        	enemy.x -= self.enemy_speed
        	if enemy.collide_widget(self.player):
        		self.restart()
        for enemy in self.AllEnemy:
            if enemy.x < -self.enemy_width:
                self.score += 0.5
                self.remove_widget(enemy)
                self.AllEnemy.remove(enemy)
        
        if len(self.AllEnemy) < 4:
        	enemy1, enemy2 = self.makeEnemy()
        	self.AllEnemy.append(enemy1)
        	self.AllEnemy.append(enemy2)
        	self.add_widget(enemy1)
        	self.add_widget(enemy2)
        
    def restart(self):
        Clock.unschedule(self.update)
        self.playgame = False
        self.clear_widgets()
        def _restart(*args):
            Clock.schedule_interval(self.update, self.INTERVAL)
            self.playgame = True
            self.clear_widgets()
            self._init_game()
        button = Button(center_y = Window.height / 2,
                        x = Window.width / 2 - Window.width * 2 / 10, 
                        text = '   Your Score : %d\nTap To Play Again'%(self.score), 
                        background_color = (.4, .8, .2, .5),
                        size_hint = (.4,.1))
        button.bind(on_press = _restart)
        self.add_widget(button)
    def _init_game(self):
        self.add_widget(self.score_label)
        enemy_height1 = random.randint(int((self.height * 4 / 5)/10), int((self.height * 4 / 5)/2))
        enemy_height2 = self.height - self.gap - enemy_height1 - self.height / 5
        enemy1 = EnemyBottom(x = Window.width * 3 / 2 + self.enemy_width * 2 / 3,
                             y = self.y + self.height / 5,
                             size = (self.enemy_width, enemy_height1))
        enemy2 = EnemyTop(x = Window.width * 3 / 2 + self.enemy_width * 2 / 3,
                          y = self.top - enemy_height2,
                          size = (self.enemy_width, enemy_height2))
        self.AllEnemy = [enemy1,enemy2]
        self.add_widget(enemy1)
        self.add_widget(enemy2)
        self.score = 0
        self.startgame = True
        self.remove_widget(self.startgamelabel)
        self.player = Player(center = (self.width / 4, self.y + self.height * 2 / 3), size = self.player_size)
        self.add_widget(self.player)
    def on_touch_down(self, touch):
        if self.startgame == False:
            enemy_height1 = random.randint(int((self.height * 4 / 5)/10), int((self.height * 4 / 5)/2))
            enemy_height2 = self.height - self.gap - enemy_height1 - self.height / 5
            enemy1 = EnemyBottom(x = Window.width * 3 / 2 + self.enemy_width * 2 / 3,
                                 y = self.y + self.height / 5,
                                 size = (self.enemy_width, enemy_height1))
            enemy2 = EnemyTop(x = Window.width * 3 / 2 + self.enemy_width * 2 / 3,
                              y = self.top - enemy_height2,
                              size = (self.enemy_width, enemy_height2))
            self.AllEnemy = [enemy1,enemy2]
            self.add_widget(enemy1)
            self.add_widget(enemy2)
            self.score = 0
            self.startgame = True
            self.remove_widget(self.startgamelabel)
            self.player = Player(center = (self.width / 4, self.y + self.height * 2 / 3), size = self.player_size)
            self.add_widget(self.player)
            return
        if self.collide_point(*touch.pos) and self.playgame:
            self.player.y += self.player_jump
            self.player.top = min(self.top,self.player.top)
        else:
            super(FlappyMinion,self).on_touch_down(touch)
class MenuInstruction(Popup):
    pass
class Menu(BoxLayout):
    def _playgame(self):
        self.clear_widgets()
        self.add_widget(FlappyMinion(size = self.size))
    def _instruction(self):
        MenuInstruction().open()
if __name__ == '__main__':
    class FlappyMinionApp(App):
        def build(self): 
            Window.size = (480, 960)
            return Menu()#FlappyMinion()
    FlappyMinionApp().run()
