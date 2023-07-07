import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class LoginScreen(GridLayout):
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__( **kwargs)
        self.cols = 1
        self.inner_grid = GridLayout()
        self.inner_grid.cols =2
        self.add_widget(self.inner_grid)
        self.inner_grid.add_widget(Label(text = "user name"))
        self.username = TextInput(multiline = False)
        self.inner_grid.add_widget(self.username)

        self.inner_grid.add_widget(Label(text = "password"))
        self.password = TextInput(password = True, multiline = False)        
        self.inner_grid.add_widget(self.password)

        self.wlc = Label(text='welcome')
        self.add_widget(self.wlc)

        self.submit = Button(text='submit')
        self.submit.bind(on_press=self.callback)
        # self.submit.bind(on_press=callback)
        self.add_widget(self.submit)

    def callback(self,instance):
        # self.wlc.text = self.username.text
        self.wlc.text ="Welcome " + self.username.text
       


class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__=="__main__":
    MyApp().run()