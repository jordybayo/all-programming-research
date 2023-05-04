import kivy
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.config import Config
from kivy.lang import Builder

Config.set("graphics", "width", "640")
Config.set("graphics", "height", "480")


class Mi_cam(RelativeLayout):
    def __init__(self, **kargs):
        super(Mi_cam, self).__init__(**kargs)

    def Captural(self):
        self.Cam0 = Camera()
        self.Cam0.resolution=640,480
        self.Cam0.play=True
        self.add_widget(self.Cam0)


class CameraApp(App):
    def build(self):
        return Mi_cam()
 
if __name__ == "__main__":
    CameraApp().run()

