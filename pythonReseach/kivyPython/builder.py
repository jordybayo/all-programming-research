#coding:utf-8

from kivy.app import App
#kivy.require("1.10.1")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class MainScreen(Screen):
    pass



class AnotherScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass



presentation = Builder.load_file("builder.kv")

class MainApp(App):
    def build(self):
        return presentation



if __name__ == "__main__":
    MainApp().run()
