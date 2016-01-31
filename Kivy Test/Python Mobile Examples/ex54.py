# ex54.py
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Line, Color, Rectangle
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

class Ex54App(App):
    def build(self):
        store = JsonStore('ex54.json')
        store['p1'] = {'name':'Mercury', 'mass':0.055}
        store['p2'] = {'name':'Venus', 'mass':0.815}
        store['p3'] = {'name':'Earth', 'mass':1}
        store['p4'] = {'name':'Mars', 'mass':0.107}

        store['p5'] = {'name':'Jupiter','mass':317.8}
        store['p6'] = {'name':'Saturn','mass':95.152}
        store['p7'] = {'name':'Uranus','mass':14.536}
        store['p8'] = {'name':'Neptune','mass':17.147}
              
        y0 = Window.height/(len(store)+1)
        y = Window.height
        gl = GridLayout(cols = 2)
        Str = '[size=32][color=FF4488]{}[/color][/size]'
        Str1 = '[size=44][color=2222FF]{}[/color][/size]'
        with gl.canvas:
            Color(1,.95,.95,1)
            Rectangle(size = Window.size)
        y = y - y0
        Strin = Str1.format('Planet')
        lbl = Label(text=Strin, markup = True)
        gl.add_widget(lbl)
        Strin = Str1.format('Relative Mass')
        lbl = Label(text=Strin, markup = True)
        gl.add_widget(lbl)
        with gl.canvas:
            Color(0,1,0,1)
            Line(points=(0,y,Window.width,y))
        for key in sorted(store):
            y = y - y0
            Strin = Str.format(store[key]['name'])
            lbl = Label(text=Strin, markup = True)
            gl.add_widget(lbl)
            Strin = Str.format(store[key]['mass'])
            lbl = Label(text=Strin, markup = True)
            gl.add_widget(lbl)
            with gl.canvas:
                Color(0,1,0,1)
                Line(points=(0,y,Window.width,y))
        return gl
        
if __name__=='__main__':
    Ex54App().run()