#ex53.py
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.properties import DictProperty
from ex53json import json_data
# Uncomment, next 2 lines to remove warning
#from kivy.clock import Clock
#Clock.max_iteration = 15

class Ex53(RelativeLayout):
    pass

class Ex53App(App):
    use_kivy_settings = False
    Val = DictProperty({'circle':0,'square':0,'up_triangle':0,
                        'down_triangle':0,'pixels':0})

    def build_config(self, config):
        config.add_section('shape')
        for val in ['circle','square','up_triangle','down_triangle']:
            config.setdefault('shape', val, '1')
        config.add_section('size')
        config.setdefault('size', 'pixels', '50')

    def build(self):
        for val in ['circle','square','up_triangle','down_triangle']:
            self.Val[val]=self.config.getint('shape',val)
        self.Val['pixels']=self.config.getint('size','pixels')
        return Ex53()
    
    def build_settings(self, settings):
        settings.add_json_panel('Settings',
                                self.config, data='data.json')
        with settings.canvas.before:
            Color(.2,.25,.25,1)
            Rectangle(pos=(0,0),size=Window.size)
            
    def on_config_change(self, config, section, key, value):
        self.Val[key] = value
        config.set(section,key,value)
        config.write()

if __name__ == '__main__':
    Ex53App().run()