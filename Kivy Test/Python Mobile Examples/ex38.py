# ex38.py

from kivy.uix.widget import Widget
from kivy.app import App
from kivy.animation import Animation
from kivy.properties import StringProperty

class Ball(Widget):
    anim_choice = StringProperty('touch_down to animate ball')
    counter = 0
    def on_touch_down(self, touch):
        Animation.cancel_all(self)
        anim_choices = ['in_back','in_bounce','in_circ',
                        'in_cubic','in_elastic','in_expo',
                        'in_out_back','in_out_bounce','in_out_circ',
                        'in_out_cubic','in_out_elastic','in_out_expo',
                        'in_out_quad','in_out_quart','in_out_quint',
                        'in_out_sine','in_quad','in_quart',
                        'in_quint','in_sine','linear',
                        'out_back','out_bounce','out_circ',
                        'out_cubic','out_elastic','out_expo',
                        'out_quad','out_quart','out_quint',
                        'out_sine']
        self.anim_choice = anim_choices [self.counter]
        anim = Animation(center_x = touch.x,
                         center_y = touch.y,
                         t = self.anim_choice)
        anim.start(self)
        self.counter = (self.counter+1) % len(anim_choices)
    
class Ex38(Widget):
    pass
       
class Ex38App(App):
    def build(self):
        return Ex38()

if __name__=='__main__':
    Ex38App().run()
