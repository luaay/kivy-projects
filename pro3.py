import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
# import kivy.properties as kyprops

class LoginScreen(Widget):

    username = ObjectProperty(None)
    password = ObjectProperty(None)
    welcome = ObjectProperty(None)

    def btn(self):
        self.welcome.text = "Welcome " + self.username.text

class MyApp(App):
    def build(self):
        return LoginScreen()
    

if __name__ == '__main__':
    MyApp().run()
