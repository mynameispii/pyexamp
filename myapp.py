import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.switch import Switch
kivy.require('1.9.0')



class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=1
        self.inside=GridLayout()
        self.inside.cols=2
        self.inside.add_widget(Label(text="First Name :"))
        self.name=TextInput(multiline=False)
        self.inside.add_widget(self.name)
        self.inside.add_widget(Label(text="Last Name :"))
        self.lastname=TextInput(multiline=False)
        self.inside.add_widget(self.lastname)
        self.inside.add_widget(Label(text="ID Number :"))
        self.idnumber=TextInput(multiline=True)
        self.inside.add_widget(self.idnumber)
        self.inside.add_widget(Label(text="Phone Number :"))
        self.phonenumber=TextInput(multiline=False)
        self.inside.add_widget(self.phonenumber)

        self.add_widget(self.inside)

        self.submit=Button(text="Submit",font_size=40)
        self.submit.bind(on_press=self.pressed)

        self.add_widget(self.submit)
        
    def pressed(self,instance):
        name=self.name.text
        last=self.lastname.text
        idnum=self.idnumber.text
        pnum=self.phonenumber.text
        

        print("Name :",name,"Last Name : ",last,"ID number :",idnum,"Phone number :",pnum)
        self.name.text=""
        self.lastname.text=""
        self.idnumber.text=""
        self.phonenumber.text=""

    


class MyApp(App):
    def build(self):
        return MyGrid()
MyApp().run()        
        
        
        
