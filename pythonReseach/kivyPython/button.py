#coding:utf-8

from kivy.app import App
#kivy.require("1.10.1")
from kivy.uix.label import Label
from kivy.uix.widget import Widget



class widgets(Widget):
    pass

class twoKV(App):
    def build(self):
        return widgets()



if __name__ == "__main__":
    twoKV().run()

    """

"""