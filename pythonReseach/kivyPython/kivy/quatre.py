from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider



Builder.load_string("""
<SettingsScreen>:
    BoxLayout: 
        Button: 
            text: 'My settings button' 
        Button:
            on_press: root.manager.current = 'menu'
            text: 'Back to menu' 
""")



class SettingsScreen(Screen): 
    pass


sm = ScreenManager() 
sm.add_widget(SettingsScreen(name='settings'))

