from mapview_build.lib.kivy_garden.mapview import MapView
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from plyer import notification
from kivy.clock import Clock
import asyncio
from kivy.app import async_runTouchApp
from kivy.uix.label import Label

# from plyer_build.lib.plyer import notification
import os

kv_path = os.path.join(os.path.dirname(__file__), 'main.kv')
print(kv_path)
# exit()
# kv = Builder.load_file("main.kv")


class Places_Mapview(MapView):
    pass


class MyLayout(Widget):
    def press(self):
        notification.notify(
            title="Hello",
            message="100m od Ciebie jest Piękny Domek",
            timeout=10
        )


class MyApp(App):
    lol = 1

    def build(self):
        return MyLayout()

    def on_pause(self):
        print("PAUSED")
        self.pause_event = Clock.schedule_interval(self.noti_pause, 10)
        print("PAUSED 2")
        return True

    def noti_pause(self, dt):
        print("PAUSED LOOP ", self.lol)
        notification.notify(
            title="PAUSE",
            message="Paused {0}".format(self.lol)
        )
        self.lol = self.lol + 1

    def on_resume(self):
        try:
            self.pause_event.cancel()
        except:
            notification.notify(
                title="NO CANSEL",
                message="Resumed CANSEL"
            )
        notification.notify(
            title="RESUME",
            message="Resumed"
        )
        print("XD HELLO")

    def on_stop(self):
        print("STOPED")
        notification.notify(
            title="STOP",
            message="Stoped",
            timeout=1
        )



# Uruchomienie pętli zdarzeń asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(
    async_runTouchApp(MyApp.run(), async_lib='asyncio'))
loop.close()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(
#     async_runTouchApp(myApp(), async_lib='asyncio'))
# loop.close()

# loop = asyncio.get_event_loop()
# loop.call_soon(myApp().run)
# loop.run_forever()
# loop.close()
