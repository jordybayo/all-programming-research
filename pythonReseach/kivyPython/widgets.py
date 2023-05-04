#include:utf-8
#kivy.require("1.10.1")

"""import packages place"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


 

class firstkv(App):
    def build(self):
        return Label()


if __name__ == '__main__':
    firstkv().run()