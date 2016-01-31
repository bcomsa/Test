# ex47.py

from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.app import App
from kivy.animation import Animation
from kivy.properties import (StringProperty, NumericProperty,
                             BooleanProperty)
from kivy.core.window import Window
from kivy.clock import Clock
import string

LETTERS={}
LETT_TEMPLATE = ('Letter_Blocks_01/'
                 'Letter_Blocks_01_Set_4_{}_64x64.png')
for letter in string.ascii_uppercase:
    LETTERS[letter] = LETT_TEMPLATE.format(letter)

POSITIONS={}
POSITIONS[0]=100,Window.height-100
POSITIONS[1]=Window.width/3,Window.height-50
POSITIONS[2]=2*Window.width/3,Window.height-50
POSITIONS[3]=Window.width - 100, Window.height - 100
POSITIONS[4]=100,100
POSITIONS[5]=Window.width/2,50
POSITIONS[6]=Window.width-100,100

FPOSITIONS={}
_X,_Y = Window.width/2,Window.height/2
FPOSITIONS[0]=_X-64,_Y+32
FPOSITIONS[1]=_X,_Y+32
FPOSITIONS[2]=_X+64,_Y+32
FPOSITIONS[3]=_X+128,_Y+32
FPOSITIONS[4]=_X-32,_Y-32
FPOSITIONS[5]=_X+32,_Y-32
FPOSITIONS[6]=_X+96,_Y-32

class Letter(Image):
    fname = StringProperty()
    counter = NumericProperty()
    pos = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Letter, self).__init__(**kwargs)
        Clock.schedule_once(self.start_anim,.1)

    def start_anim(self,dt):
        i=self.counter
        Animation.cancel_all(self)
        anim = Animation(center_x = FPOSITIONS[i][0],
                         center_y = FPOSITIONS[i][1],
                         t='out_bounce',
                         d = 5)
        anim.start(self)
        self.pos = True
        
    def on_touch_down(self,touch):
        if self.pos == True:
            Clock.schedule_once(self.rev_anim,.1)
        else:
            Clock.schedule_once(self.start_anim,.1)

    def rev_anim(self,dt):
        i=self.counter
        Animation.cancel_all(self)
        anim = Animation(center_x = POSITIONS[i][0],
                         center_y = POSITIONS[i][1],
                         t='in_bounce',
                         d = 5)
        anim.start(self)
        self.pos = False

class Ex47(Widget):
    def initial_positions(self,dt):
        for i,lett in enumerate(list('NGOCANH')):
            letter = Letter()
            letter.fname = LETTERS[lett.upper()]
            letter.center = POSITIONS[i]
            letter.counter = i
            self.add_widget(letter)

       
class Ex47App(App):
    def build(self):
        ex47=Ex47()
        Clock.schedule_once(ex47.initial_positions,.5)
        return ex47

if __name__=='__main__':
    Ex47App().run()