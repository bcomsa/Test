# ex31.py

from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ListProperty
from kivy.vector import Vector as Vec
from kivy.clock import Clock
import kivy
kivy.require('1.8.0')

class Ball(Widget):
    vel = ListProperty()
    
class Wall(Widget):
    pass

class Ex30(Widget):
      
    def __init__(self, **kwargs):
        super(Ex30, self).__init__(**kwargs)
        self.ball1.pos = self.width/2, self.height/2
        self.ball2.pos = self.width/3, self.height/3

    def on_touch_down(self,touch):
        for ball in [self.ball1,self.ball2]:
            touch_vector = Vec(touch.pos) -  Vec(ball.center)
            touch_vector_mag = touch_vector.length()
            unit_touch_vector = touch_vector/touch_vector_mag
            ball.vel = 5.0*unit_touch_vector
            print touch_vector

    def update(self,dt):
        for ball in [self.ball1,self.ball2]:
            if ball.collide_widget(self.wall_left):
                ball.vel[0] = abs(ball.vel[0])
            elif ball.collide_widget(self.wall_right):
                ball.vel[0] = -abs(ball.vel[0])
            if ball.collide_widget(self.wall_top):
                ball.vel[1] = -abs(ball.vel[1])
            elif ball.collide_widget(self.wall_down):
                ball.vel[1] = abs(ball.vel[1])
            
        if self.ball1.collide_widget(self.ball2):
            col_vector=Vec(self.ball1.pos)-Vec(self.ball2.pos)
            col_vector_mag=col_vector.length()
            self.ball1.vel = 5.0/col_vector_mag*col_vector
            self.ball2.vel = -5.0/col_vector_mag*col_vector
            
        self.ball1.pos = Vec(self.ball1.vel) + Vec(self.ball1.pos)
        self.ball2.pos = Vec(self.ball2.vel) + Vec(self.ball2.pos)
       
class Ex30App(App):
    def build(self):
        self.title = "Two Bouncing Balls with Widget Collisions"
        ex31 = Ex30()
        Clock.schedule_interval(ex31.update, 1.0/60)
        return ex31

if __name__=='__main__':
    Ex30App().run()
