import random
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('flappyminion.kv')

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
    player_size = Window.width / 10, Window.width / 10
    player_velocity = 8
    player_jump = 80
    score = NumericProperty()

    def __init__(self, **kwargs):
        super(FlappyMinion, self).__init__(**kwargs)
        #self.minion_sound = SoundLoader.load('Sound/flappy-hehe.wav')
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
        enemy_height1 = random.randint(int(self.height/10), int(self.height/2))
        enemy_height2 = self.height - self.gap - enemy_height1 - self.height / 5
        enemy1 = EnemyBottom(x = Window.width ,y = self.y + self.height / 5,size = (self.enemy_width, enemy_height1))
        enemy2 = EnemyTop(x = Window.width ,y = self.top - enemy_height2,size = (self.enemy_width, enemy_height2))
        return enemy1,enemy2
    def update(self, time):
        if self.startgame == False : return
        if self.player.y < self.y:
            pass#self.restart()
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
        self.player.y -= self.player_velocity

    def restart(self):
        Clock.unschedule(self.update)
        self.playgame = False
        self.clear_widgets()
        label = Label(center = Window.center, text = 'Your Score : %d'%(self.score), font_size = 30, color = (1, .5, .5, 1),size_hint = (None, None))
        self.add_widget(label)

    def on_touch_down(self, touch):
        if self.startgame == False:
            enemy_height1 = random.randint(int(self.height/10), int(self.height/2))
            enemy_height2 = self.height - self.gap - enemy_height1
            enemy1 = EnemyBottom(x = Window.width * 3 / 2 + self.enemy_width,y = self.y,size = (self.enemy_width, enemy_height1))
            enemy2 = EnemyTop(x = Window.width * 3 / 2 + self.enemy_width,y = self.top - enemy_height2,size = (self.enemy_width, enemy_height2))
            self.AllEnemy = [enemy1,enemy2]
            self.add_widget(enemy1)
            self.add_widget(enemy2)
            self.startgame = True
            self.remove_widget(self.startgamelabel)
            self.player = Player(center = (self.width / 4, self.y + self.height * 2 / 3), size = self.player_size)
            self.add_widget(self.player)
            return
        if self.collide_point(*touch.pos) and self.playgame:
            #if self.minion_sound.state == 'play': self.minion_sound.stop()
            #self.minion_sound.play()
            self.player.y += self.player_jump
            self.player.top = min(self.top,self.player.top)

if __name__ == '__main__':
    class FlappyMinionApp(App):
        def build(self): 
            Window.size = (480, 960)
            return FlappyMinion()
    FlappyMinionApp().run()
