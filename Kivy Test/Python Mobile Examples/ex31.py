# figure.py

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import *
from math import pi,atan

class Figure(RelativeLayout):
    def __init__(self, **kwargs):
        touchPos=100,350.5
        ballPos=200,370.8
        size=50,50
        def lineAng():
            dy = ballPos[1]-touchPos[1]+size[1]/2
            dx = ballPos[0]-touchPos[0]+size[0]/2
            ang=atan(dy/dx)
            ang=ang*180/pi
            return ang
        super(Figure, self).__init__(**kwargs)
        with self.canvas:
            Color(1,1,1)
            Rectangle(pos=(0,0), size=(800,600))
            Color(0,0,1)
            Point(points=(touchPos),pointsize=3)
            Point(points=(ballPos),pointsize=3)
            Point(points=(ballPos[0]+size[0]/2,ballPos[1]+size[1]/2),pointsize=3)
            Line(rectangle=(ballPos+size),width=2)
            Line(points=((ballPos[0]+size[0]/2,
                         ballPos[1]+size[1]/2)+touchPos),width=2)
            ang = lineAng()
            Line(points=(touchPos+(touchPos[0]+25,touchPos[1])),width=2)
            PushMatrix()
            Rotate(angle=2*ang,origin=touchPos)
            Line(points=(touchPos+(touchPos[0]+25,touchPos[1])),width=2)
            PopMatrix()
        b1 = Button(text='touchPos',pos=(touchPos[0]-20,touchPos[1]-40),
                                   size_hint=(.1,.05))
        self.add_widget(b1)
        b2 = Button(text='ballPos',pos=(ballPos[0]-20,ballPos[1]-40),
                                   size_hint=(.1,.05))
        self.add_widget(b2)
        

      
class FigureApp(App):
    def build(self):
        return Figure()

if __name__=='__main__':
    FigureApp().run()