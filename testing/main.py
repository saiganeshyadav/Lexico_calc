import kivy
from kivy.config import Config
Config.set('graphics','resizable',True)
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.text import LabelBase
import json
from difflib import get_close_matches
import math
from math import sin
from math import cos
from math import tan
from math import log

LabelBase.register(name='Pacifico',fn_regular='Pacifico.ttf')


kv=Builder.load_file('testlex.kv')

class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class ThirdWindow(Screen):
    def bt1(self):
        self.lbl.text=''
    def bt2(self):
        self.lbl.text = self.lbl.text[:-1]
    def bt3(self):
        self.lbl.text = self.lbl.text+self.btn3.text
    def bt4(self):
        self.lbl.text = self.lbl.text+self.btn4.text
    def bt5(self):
        self.lbl.text = self.lbl.text+'sin('
    def bt6(self):
        self.lbl.text = self.lbl.text+self.btn6.text
    def bt7(self):
        self.lbl.text = self.lbl.text+self.btn7.text
    def bt8(self):
        self.lbl.text = self.lbl.text+self.btn8.text
    def bt9(self):
        self.lbl.text = self.lbl.text+self.btn9.text
    def bt10(self):
        self.lbl.text = self.lbl.text+'cos('
    def bt11(self):
        self.lbl.text = self.lbl.text+self.btn11.text
    def bt12(self):
        self.lbl.text = self.lbl.text+self.btn12.text
    def bt13(self):
        self.lbl.text = self.lbl.text+self.btn13.text
    def bt14(self):
        self.lbl.text = self.lbl.text+self.btn14.text
    def bt15(self):
        self.lbl.text = self.lbl.text+'tan('
    def bt16(self):
        self.lbl.text = self.lbl.text+self.btn16.text
    def bt17(self):
        self.lbl.text = self.lbl.text+self.btn17.text
    def bt18(self):
        self.lbl.text = self.lbl.text+self.btn18.text
    def bt19(self):
        self.lbl.text = self.lbl.text+self.btn19.text
    def bt20(self):
        self.lbl.text = self.lbl.text+'log('
    def bt21(self):
        self.lbl.text = self.lbl.text+self.btn21.text
    def bt22(self):
        self.lbl.text = self.lbl.text+self.btn22.text
    def bt23(self):
        self.lbl.text = self.lbl.text+self.btn23.text
    def bt24(self):
        self.lbl.text = self.lbl.text+'**'
    def bt25(self):
        try:
            ans = str(eval(self.lbl.text))
            self.lbl.text = ans
        except:
            self.lbl.text = 'Error'

class FourthWindow(Screen):
    def dic(self):
        data = json.load(open("dictionary.json"))
        self.lbl1.text = ''
        self.lbl2.text = ''

        def translate(w):
            w = w.lower()
            if w in data:
                return data[w]
            elif len(get_close_matches(w, data.keys())) > 0:
                self.lbl1.text=self.lbl1.text+"Closest word :" + get_close_matches(w, data.keys())[0].upper()
                return data[get_close_matches(w, data.keys())[0]]
            else:
                return 'word not found'

        word = self.tip.text
        output = translate(word)
        deflist=output.split(';')
        if output!='word not found':
            self.lbl2.text=self.lbl2.text+'Definition:\n'
        k=0
        for i in range(1):
            for j in deflist[i]:
                if k<39:
                    self.lbl2.text=self.lbl2.text+j
                    k+=1
                else:
                    self.lbl2.text = self.lbl2.text+'\n'+j
                    k=0

class FifthWindow(Screen):
    pass
screen_manager=ScreenManager()

screen_manager.add_widget(MainWindow(name='main'))
screen_manager.add_widget(SecondWindow(name='second'))
screen_manager.add_widget(ThirdWindow(name='third'))
screen_manager.add_widget(FourthWindow(name='fourth'))
screen_manager.add_widget(FifthWindow(name='fifth'))


class MyApp(App):
    def build(self):
        return screen_manager
running=MyApp()
running.run()