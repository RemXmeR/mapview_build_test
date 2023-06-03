from build.lib.kivy_garden.mapview import MapView
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
kv = Builder.load_file("main.kv")

class Places_Mapview(MapView):
    pass

class MyLayout(Widget):
    def press(self):
        pass

class myApp(App):
    def build(self):
        return MyLayout()

myApp().run()
