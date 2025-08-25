import kivy
from kivy.app import App


import start_screen_class
from start_screen_class import StartScreen
import stance_input_screen_class
from stance_input_screen_class import StanceInputScreen
import time_input_screen_class
from time_input_screen_class import TimeInputScreen
import stance_screen_class
from stance_screen_class import StanceScreen

from kivy.uix.screenmanager import ScreenManager 

class RandomSwordStances(App):
    def build(self):
        screen_manager = ScreenManager()

        start_screen = StartScreen(name='start_screen')
        stance_input_screen = StanceInputScreen(name='stance_input_screen')
        time_input_screen = TimeInputScreen(name='time_input_screen')
        stance_screen = StanceScreen(name='stance_screen')

        screen_manager.add_widget(start_screen)
        screen_manager.add_widget(stance_input_screen)
        screen_manager.add_widget(time_input_screen)
        screen_manager.add_widget(stance_screen)
        

        return screen_manager
        
if __name__ == '__main__':
    app = RandomSwordStances()
    app.run()