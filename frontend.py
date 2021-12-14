from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from database_func import Database
from mybackend import get_recommendations, is_legal_input
from kivy.config import Config

Window.clearcolor = (.6, .5, .4, .3)
Window.size = (900, 600)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class MyGrid(GridLayout):

    location = ObjectProperty(None)
    time = ObjectProperty(None)
    amount = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_recommendations(self):
        location = self.location.text
        time = self.time.text
        amount = self.amount.text
        line = ""
        size = (400, 600)
        title = ''
        errors = is_legal_input(location, time, amount)

        if len(errors) is not 0:
            for rec in errors:
                line += '\n' + str(rec)
            title='Errors:'
            size=(500,200)
        else:
            title = 'Recommendations:'
            recommendations = get_recommendations(location, time, amount)
            for rec in recommendations:
                line +='\n' +str(rec)

        popup = Popup(title=title, content=Label(text=line),size_hint=(None, None), size=size)
        popup.open()

        self.location.text = ''
        self.time.text = ''
        self.amount.text = ''


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    db = Database()
    db.test()
    MyApp().run()