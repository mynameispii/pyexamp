import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.switch import Switch
kivy.require('1.9.0')

class SimpleSwitch(GridLayout):
    def __init__(self,**kwargs):
        super(SimpleSwitch,self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text="H.O.W"))
        self.setting_sample=Switch(active=False)
        self.add_widget(self.setting_sample)
    def callback(instance, value):
        print('the switch', instance, 'is', value)
        switch = Switch()
        switch.bind(active=callback)

        

class switchApp(App):
    def build(self):
        return SimpleSwitch()
        return callback()
       
switchApp().run()

        
