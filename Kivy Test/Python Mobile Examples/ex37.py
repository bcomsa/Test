# ex37.py

from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.app import App

class Ex37(GridLayout):
    pass
        
class Ex37App(App):
    def build(self):
        self.load_sounds()
        return Ex37()

    def load_sounds(self):
        self.sounds = {}
        for i in range(3):
            fname = 'sound' + str(1) + '.wav'
            self.sounds[i] = SoundLoader.load(fname)

    def play_sound1(self):
        sound = self.sounds.get(0)
        if sound is not None:
            sound.volume = 0.5
            sound.play()

    def play_sound2_once(self, *args):
        sound = self.sounds.get(1)
        if sound is not None:
            sound.volume = 0.5
            sound.play()
        
    def play_sound2(self):
        Clock.schedule_once(self.play_sound2_once,0)
        Clock.schedule_once(self.play_sound2_once,1)
        Clock.schedule_once(self.play_sound2_once,2)
        Clock.schedule_once(self.play_sound2_once,3)
        Clock.schedule_once(self.play_sound2_once,4)

    def play_sound3(self):
        sound = self.sounds.get(2)
        if sound is not None:
            sound.volume = 0.5
            sound.loop = True
            sound.play()

    def stop_sound(self,i):
        if i == 1:
            Clock.unschedule(self.play_sound2_once)
        else:
            sound = self.sounds.get(i)
            if sound is not None:
                if sound.state == "play":
                    sound.stop()
            
if __name__=='__main__':
    Ex37App().run()
