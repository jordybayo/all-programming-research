from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
from quatre import SettingsScreen



Builder.load_string("""

<MenuScreen>:
    BoxLayout:
        Button: 
            text: 'Goto settings' 
            on_press: root.manager.current = 'settings'
        Button: 
            text: 'Quit'
""")


class MenuScreen(Screen): 
    pass


sm = ScreenManager() 
sm.add_widget(MenuScreen(name='menu')) 
sm.add_widget(SettingsScreen(name='settings'))

class SimpleKivy(App):
    def build(self):
        return sm



        
if __name__ == "__main__":
    SimpleKivy().run()
