import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import pandas as pd



# Create design element class
class MyGrid(GridLayout):
    def __init__(self, **kwargs):   # As manyn as args we can pass now
        super(MyGrid, self).__init__(**kwargs) # calling the default constructor
        self.cols = 1 # Main Grid Layout columns

        # Create a new Grid layout inside the main gridlayout
        self.inside = GridLayout()
        self.inside.cols = 2   # Inside grid layout columns

        self.inside.add_widget(Label(text= "Task Name: "))
        self.task_name = TextInput(multiline= False)
        self.inside.add_widget(self.task_name)

        self.inside.add_widget(Label(text="Est Mins: "))
        self.est_time = TextInput(multiline=False)
        self.inside.add_widget(self.est_time)

        self.inside.add_widget(Label(text="Complete Before Date: "))
        self.comp_before_date = TextInput(multiline=False)
        self.inside.add_widget(self.comp_before_date)


        self.inside.add_widget(Label(text="Complete Before Time: "))
        self.comp_befoe_time = TextInput(multiline=False)
        self.inside.add_widget(self.comp_befoe_time)

        self.inside.add_widget(Label(text="Effort: "))
        self.effort = TextInput(multiline=False)
        self.inside.add_widget(self.effort)

        # Add this inside grid to new grid
        self.add_widget(self.inside)

        self.add = Button(text= "Add Task")
        self.add.bind(on_press= self.add_task)
        self.add_widget(self.add)

    def add_task(self, instance):
        print("Button Pressed")
        task_name = self.task_name.text
        est_time = self.est_time.text
        comp_before_date = self.comp_before_date.text
        comp_before_time = self.comp_befoe_time,text
        effort = self.effort.text




class Task_Priority(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    Task_Priority().run()