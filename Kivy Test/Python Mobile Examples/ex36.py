# ex36.py

from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.properties import (NumericProperty,
                             StringProperty)
from kivy.graphics import Line

class ColorEllipse(Widget):
    pass

class ColorRectangle(Widget):
    pass

class ColorUpTriangle(Widget):
    pass

class ColorDownTriangle(Widget):
    pass

class ToolBox(Widget):
    w = NumericProperty(20)
    h = NumericProperty(20)
    shape = StringProperty('down:0')

    def on_w(self,*args):
        self.drawing.box_resize(*args)

    def on_h(self,*args):
        self.drawing.box_resize(*args)
    
class Drawing(Widget):
    sel = NumericProperty(0)
    def common(self,touch):
        if touch.x>150:
            if self.toolbox.shape=='down:0':
                ce = ColorEllipse()
                ce.center = touch.pos
                self.add_widget(ce)
            elif self.toolbox.shape=='down:1':
                cr = ColorRectangle()
                cr.center = touch.pos
                self.add_widget(cr)
            elif self.toolbox.shape=='down:2':
                cut = ColorUpTriangle()
                cut.center = touch.pos
                self.add_widget(cut)
            elif self.toolbox.shape=='down:3':
                cdt = ColorDownTriangle()
                cdt.center = touch.pos
                self.add_widget(cdt)
        
    def on_touch_down(self,touch):
        self.common(touch)

    def on_touch_move(self,touch):
        self.common(touch)

    def clear(self,*args):
        self.clear_widgets()

    def undo(self,*args):
        try: self.remove_widget(self.children[0])
        except: pass

    def box(self,*args):
        ch = self.children
        if len(ch) == 0: return
        if self.sel==0:
            with self.canvas:
                self.select=Line(rectangle=(ch[0].x-5,ch[0].y-5,
                                ch[0].width+10,ch[0].height+10),width=2)
                self.sel=1
        else:
            self.canvas.remove(self.select)
            self.sel = 0

    def box_resize(self,*args):
        if self.sel==1:
            self.canvas.remove(self.select)
            self.sel = 0
       
class Ex36(RelativeLayout):
    pass
        
class Ex36App(App):
    def build(self):
        self.title = 'Drawing Application 2'
        return Ex36()

if __name__=='__main__':
    Ex36App().run()
