# import everything needed
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class calculator(Widget): # calculator app widget
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def click(self, event): # function for buttons 0 to 9 and /*-+
        self.ids.outnum.text = self.ids.outnum.text + event

    def clear(self): # clear the text with C button
        self.ids.outnum.text = ""

    def equal(self): # calculate the Equation with = button
        try: self.ids.outnum.text = str(eval(self.ids.outnum.text))
        except: pass


class myapp(App): # create the app
    def build(self):
        return calculator() # return calculator widget


if __name__ == "__main__": # if file is main file run app
    myapp().run()
