import kivy
import os
import random

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.text import Label as CoreLabel
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.clock import Clock



class StanceScreen(Screen):
    stance_num = -1
    time_limit = -1

    stances = []
    titles = []
    i=-1

    cur_stance = None
    cur_title = None
    
    def __init__(self, **kwargs):
        super(StanceScreen, self).__init__(**kwargs)
		

    def on_enter(self):
        self.stances = []
        self.titles = []
            
        self.stance_num = int(self.manager.get_screen('stance_input_screen').stance_input.text)
        self.time_limit = int(self.manager.get_screen('time_input_screen').time_input.text)


        if self.stance_num == -1 and self.time_limit == -1:
            print("ERROR: NEITHER STANCE OR TIME INPUT")
            self.manager.current = 'start_screen'

        elif self.stance_num is not -1:
            self.stance()
            self.stance_num = -1

        elif self.time_limit is not -1:
            self.time()
            self.time_limit = -1

        else:
            print("UNKNOWN ERROR")
            self.manager.current = 'start_screen'

        Clock.schedule_once(self.updateStance)
        Clock.schedule_interval(self.updateStance, 3)



    def startNav(self, *args):
        self.manager.get_screen('stance_input_screen').stance_input.text = "-1"
        self.manager.get_screen('time_input_screen').time_input.text = "-1"
        self.manager.current = 'start_screen'
        self.i = -1
        self.stances = []
        self.titles = []
        self.cur_stance = None
        self.cur_title = None
    

    def stance(self):
        img_dir = './images'
        files = os.listdir(img_dir)

        for f in range(0, self.stance_num):
            random_stance = random.choice(files)
            title = random_stance[:-4]
            self.stances.append(img_dir+'/'+random_stance)
            self.titles.append(title)

    def time(self):
        img_dir = './images'
        files = os.listdir(img_dir)

        num = self.time_limit//3

        for f in range(0, num):
            random_stance = random.choice(files)
            title = random_stance[:-4]
            self.stances.append(img_dir+'/'+random_stance)
            self.titles.append(title)
    
    def updateStance(self, *args):
        self.clear_widgets()

        item_layout = GridLayout(cols = 1, rows = 3)
        back_button = Button(text = 'Back to Start', size_hint_x = 0.5, width=50, size_hint_y = 0.1, height = 90)
        back_button.bind(on_press = self.startNav)

        

        if self.i+1 < len(self.titles):
            self.i += 1
            self.cur_stance = self.stances[self.i]
            self.cur_title = self.titles[self.i]


            title = CoreLabel(text= self.cur_title, font_size=20, color=(1, 0, 0, 1), )
            title.refresh()
            title_texture = title.texture
            title_size = list(title.size)
            title_label = Label()
            title_label.canvas.add(Rectangle(texture=title_texture, pos_hint = {'top' : 1}))
            
            stance_img = Image(source = self.cur_stance, fit_mode = "contain", size_hint_y = 1)

            item_layout.add_widget(title_label)
            item_layout.add_widget(stance_img)
            item_layout.add_widget(back_button)

            self.add_widget(item_layout)
            

        else:
            title = CoreLabel(text= "COMPLETE", font_size=20, color=(1, 0, 0, 1))
            title.refresh()
            title_texture = title.texture
            title_size = list(title.size)
            title_label = Label()
            title_label.canvas.add(Rectangle(texture=title_texture, size=title_size))
            item_layout.add_widget(title_label)
            item_layout.add_widget(back_button)
            self.add_widget(item_layout)
            return False



