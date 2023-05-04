from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider





Builder.load_string("""



<MenuScreen>:
    BoxLayout:
        Button: 
            text: 'Goto settings' 
            on_press: root.manager.current = 'settings'
        Button: 
            text: 'Quit'

<SettingsScreen>:
    BoxLayout: 
        Button: 
            text: 'My settings button' 
        Button:
            on_press: root.manager.current = 'menu'
            text: 'Back to menu' 
""")


class MenuScreen(Screen): 
    pass

class SettingsScreen(Screen): 
    pass

sm = ScreenManager() 
sm.add_widget(MenuScreen(name='menu')) 
sm.add_widget(SettingsScreen(name='settings'))

class SimpleKivy(App):
    def build(self):
        return sm



        
if __name__ == "__main__":
    SimpleKivy().run()
