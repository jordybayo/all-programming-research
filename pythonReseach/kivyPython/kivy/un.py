from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
from quatre import SettingsScreen


Builder.load_string("""
<UnScreen>:
    name:"BE PRESENT"
    Button:
        on_press: root.manager.current = 'settings'
        text: "Next screen"
        font_size: 50
""")

class UnScreen(Screen): 
    pass

sm = ScreenManager() 
sm.add_widget(UnScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))


class SimpleKivy(App):
    def build(self):
        return sm


 
if __name__ == "__main__":
    SimpleKivy().run()
