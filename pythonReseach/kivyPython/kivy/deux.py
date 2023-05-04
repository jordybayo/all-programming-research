from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout 

from kivy.uix.image import Image 
from kivy.properties import ObjectProperty 
from kivy.lang import Builder

Builder.load_string('''


<RootWidget>
    CustomLayout: 
        size_hint: .9, .9 
        pos_hint: {'center_x': .5, 'center_y': .5} 
        rows:1 
        Label: 
            text: "I don't suffer from insanity, I enjoy every minute of it"
            text_size: self.width-20, self.height-20
            valign: 'top'
        Label:
            text: "When I was born I was so surprised; I didn't speak for a year and a half." 
            text_size: self.width-20, self.height-20 
            valign: 'middle' 
            halign: 'center' 
        Label: 
            text: "A consultant is someone who takes a subject you understand andmakes it sound confusing" 
            text_size: self.width-20, self.height-20 
            valign: 'bottom' 
            halign: 'justify'
''')

class RootWidget(FloatLayout): 
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
