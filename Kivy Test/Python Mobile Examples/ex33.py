#ex33.py

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
class Ex33(GridLayout):
    Num = NumericProperty(10)
    str0 = '[color=224422][size=64]Number: '
    str1 = '.[/color][/size]'
    NumSel = 11*[None]
    for i in range(11):
        NumSel[i]=str0 + str(i) + str1

class Ex33App(App):
    def build(self):
        return Ex33()

if __name__ == '__main__':
    Ex33App().run()
