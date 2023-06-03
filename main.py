from kivy.garden.mapview import MapView
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
# import os

# kv_path = os.path.join(os.path.dirname(__file__), 'main.kv')
# print(kv_path)
# exit()
kv = Builder.load_file("main.kv")

class Places_Mapview(MapView):
    pass

class MyLayout(Widget):
    def press(self):
        pass
    #     notification.notify(
    #         title="Hello",
    #         message="100m od Ciebie jest Piękny Domek"
    #     )
    # def on_pause(self):
    #     notification.notify(
    #         title="PAUSE",
    #         message="Paused"
    #     )
    #
    # def on_resume(self):
    #     notification.notify(
    #         title="RESUME",
    #         message="Resumed"
    #     )
    #
    # def on_stop(self):
    #     notification.notify(
    #         title="STOP",
    #         message="Stoped"
    #     )

class myApp(App):
    def build(self):
        return MyLayout()

myApp().run()
