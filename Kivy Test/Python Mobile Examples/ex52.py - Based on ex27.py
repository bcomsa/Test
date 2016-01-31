# ex52.py - Based on ex27.py

from kivy.uix.widget import Widget
from kivy.app import App
from kivy.logger import Logger
from time import ctime

def log(func):
    func.count=0
    def decor(*args):
        func.count += 1
        Logger.info('count {}: {}'.
                    format(func.__name__,func.count))
        Logger.debug('time: {}'.format(ctime()))
        func(*args)
    return decor


class Ball(Widget):
    
    @log
    def on_touch_down(self, touch):
        self.center=touch.pos

    @log
    def on_touch_move(self, touch):
        self.center=touch.pos
    
class Ex52(Widget):
    pass
       
class Ex52App(App):
    def build(self):
        return Ex52()

if __name__=='__main__':
    Ex52App().run()