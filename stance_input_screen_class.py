import kivy

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput


class StanceInputScreen(Screen):
    stance_input = TextInput(font_size = 50, size_hint_y = None, height = 100, text="-1")
    def __init__(self, **kwargs):
        super(StanceInputScreen, self).__init__(**kwargs)
		

        vert_spacer_layout = BoxLayout(orientation='vertical')
        item_layout = BoxLayout(orientation='vertical')
         
        next_button = Button(text = 'Ready to Start!')
        next_button.bind(on_press = self.stanceNav)
        back_button = Button(text = 'Back')
        back_button.bind(on_press = self.startNav)

        item_layout.add_widget(self.stance_input)
        item_layout.add_widget(next_button)
        item_layout.add_widget(back_button)

        vert_spacer_layout.add_widget(Widget())  # Spacer
        vert_spacer_layout.add_widget(item_layout)
        vert_spacer_layout.add_widget(Widget())  # Spacer

        self.add_widget(vert_spacer_layout)

    def on_enter(self, *args):
        self.stance_input.text = "0"

    def startNav(self, *args):
        self.stance_input.text = -1
        self.manager.current = 'start_screen'

    def stanceNav(self, *args):
        self.manager.current = 'stance_screen'

    
    def getStanceNum(self, *args):
        return self.stance_input