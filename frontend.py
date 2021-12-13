import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from kivy.core.window import Window

from mybackend import get_recommendations

Window.clearcolor = (.6, .5, .4, .3)
Window.size = (900, 600)
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class MyPopup(Popup):
    def __init__(self):
        grid = GridLayout(cols=1)
        super().__init__(content=grid, size_hint=(.40, .40))
        self.msg = Label(halign="center")
        btn = Button(text="close")
        btn.bind(on_press=lambda x: self.dismiss())
        grid.add_widget(self.msg)
        grid.add_widget(btn)

    def set_msg(self, text):
        self.msg.text = text

    def set_title(self, title):
        self.title = title


class MyGrid(GridLayout):

    location = ObjectProperty(None)
    time = ObjectProperty(None)
    amount = ObjectProperty(None)

    def __init__(self, **kwargs):


        super().__init__(**kwargs)
        # self.cols=1
        #
        # self.inside = GridLayout()
        # self.inside.cols = 2
        #
        # self.inside.add_widget(Label(text="What is your current location?"))
        # self.location = TextInput(multiline = False)
        # self.inside.add_widget(self.location)
        #
        # self.inside.add_widget(Label(text="How much time would you like to spend?"))
        # self.time = TextInput(multiline=False)
        # self.inside.add_widget(self.time)
        #
        # self.inside.add_widget(Label(text="How much location recommendations would you like to receive?"))
        # self.amount = TextInput(multiline=False)
        # self.inside.add_widget(self.amount)
        #
        # self.add_widget(self.inside)
        # self.submit = Button(text="Recommend me", font_size=40)
        # self.add_widget(self.submit)

    def show_recommendations(self):
        location = self.location.text
        time = self.time.text
        amount = self.amount.text
        recommendations = get_recommendations(location, time, amount)
        line = ""
        for rec in recommendations:
            line +='\n' +str(rec)

        popup = Popup(title='Recommendations:',
                      content=Label(text=line),
                      size_hint=(None, None), size=(400, 600))

        popup.open()
        self.location.text = ''
        self.time.text = ''
        self.amount.text = ''


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()