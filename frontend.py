import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="What is your current location?"))
        self.location = TextInput(multiline = False)
        self.inside.add_widget(self.location)

        self.inside.add_widget(Label(text="How much time would you like to spend?"))
        self.time = TextInput(multiline=False)
        self.inside.add_widget(self.time)

        self.inside.add_widget(Label(text="How much location recommendations would you like to receive?"))
        self.amount = TextInput(multiline=False)
        self.inside.add_widget(self.amount)

        self.add_widget(self.inside)
        self.submit = Button(text="Recommend me", font_size=40)
        self.add_widget(self.submit)

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()