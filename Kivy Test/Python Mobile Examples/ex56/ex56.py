# ex56.py
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.clock import Clock

class Ex56(Carousel):
    def update(self, dt):
        self.load_next()

class Ex56App(App):
    def build(self):
        self.title = 'Carousel Example'
        ex56 = Ex56()
        #Clock.schedule_interval(ex56.update, 1)
        return ex56

if __name__ == '__main__':
    Ex56App().run()