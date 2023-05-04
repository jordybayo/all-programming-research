#coding:utf-8

from kivy.app import App
#kivy.require("1.10.1")
from kivy.uix.widget import Widget

class TouchInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
    def on_touch_move(self,touch):
        print(touch)
    def on_touch_up(self, touch):
        print("RELEASED", touch)

#mouse input or press or touch input

class mouseKV(App):
    def build(self):
        return TouchInput()



if __name__ == "__main__":
    mouseKV().run()


"""

"""