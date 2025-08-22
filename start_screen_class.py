import kivy
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.text import Label as CoreLabel
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen 

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
		

        vert_spacer_layout = BoxLayout(orientation='vertical')
        horiz_spacer_layout = BoxLayout(orientation="horizontal")
        button_layout = BoxLayout(orientation='vertical')
       

        title = CoreLabel(text='Lark\'s Stance Randomizer', font_size=50, color=(1, 0, 0, 1))
        title.refresh()
        title_texture = title.texture
        title_size = list(title.size)


        title_label = Label()
        title_label.canvas.add(Rectangle(texture=title_texture, size=title_size))
        stance_limit_button = Button(text = 'Stance Number')
        stance_limit_button.bind(on_press = self.stanceInputNav)
        time_limit_button = Button(text = 'Timer')
        time_limit_button.bind(on_press = self.timeInputNav)

        button_layout.add_widget(title_label)
        button_layout.add_widget(stance_limit_button)

        button_layout.add_widget(time_limit_button)

        vert_spacer_layout.add_widget(Widget())  # Spacer
        vert_spacer_layout.add_widget(button_layout)
        vert_spacer_layout.add_widget(Widget())  # Spacer

        self.add_widget(vert_spacer_layout)

    def stanceInputNav(self, *args):
        self.manager.current = 'stance_input_screen'

    def timeInputNav(self, *args):
        self.manager.current = 'time_input_screen'

