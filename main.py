from mapview_build.lib.kivy_garden.mapview import MapView
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from plyer import notification
from kivy.clock import Clock
# import asyncio
# from kivy.app import async_runTouchApp
# from kivy.uix.label import Label
import threading
import time
# from plyer_build.lib.plyer import notification
import os

kv_path = os.path.join(os.path.dirname(__file__), 'main.kv')
print(kv_path)


# exit()
kv = Builder.load_file(kv_path)


class Places_Mapview(MapView):
    pass


class MyLayout(Widget):
    def press(self):
        notification.notify(
            title="Hello",
            message="100m od Ciebie jest Piękny Domek",
            timeout=2
        )


class MyApp(App):
    lol = 1
    itsgo=0

    def build(self):
        return MyLayout()

    def on_start(self):
        # Zadanie, które będzie uruchamiane w tle
        class HelloWorldPrinter:
            def __init__(self):
                self.stop_printing = threading.Event()

            def print_hello_world(self):
                while not self.stop_printing.is_set():
                    print('Background!')
                    notification.notify(
                        title="BACKGROUND",
                        message="XD BG"
                    )
                    time.sleep(5)

            def stop(self):
                self.stop_printing.set()

        self.printer = HelloWorldPrinter()

        # Clock.schedule_interval(, 0)

    def letsgo(self):
        print(self.itsgo)
        if self.itsgo==1:
            return
        self.itsgo = 1
        self.background_thread = threading.Thread(target=self.printer.print_hello_world)
        self.background_thread.start()
    def dontgo(self):
        if self.itsgo == 1:
            self.printer.stop()
            self.itsgo = 0

    def on_pause(self):
        print("PAUSED")
        # self.pause_event = Clock.schedule_interval(self.noti_pause, 10)
        notification.notify(
            title="PAUSE",
            message="Paused {0}".format(self.lol)
        )
        self.lol = self.lol + 1
        print("PAUSED 2")
        return True

    # def noti_pause(self, dt):
    #     print("PAUSED LOOP ", self.lol)
    #     notification.notify(
    #         title="PAUSE",
    #         message="Paused {0}".format(self.lol)
    #     )
    #     self.lol = self.lol + 1

    def on_resume(self):
        # try:
        #     self.pause_event.cancel()
        # except:
        #     notification.notify(
        #         title="NO CANSEL",
        #         message="Resumed CANSEL"
        #     )
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
        self.printer.stop()


# async def print_hello_world():
#     while True:
#         print("Hello, world")
#         await asyncio.sleep(1)  # Czeka na 1 sekundę

# Utworzenie nowej pętli zdarzeń asyncio i dodanie do niej zadania
# loop = asyncio.new_event_loop()
# loop.create_task(print_hello_world())
#
# # Synchronizacja pętli zdarzeń asyncio z zegarem Kivy
# loop.run_forever()

# async def main():
#     await MyApp().async_run(async_lib="asyncio")
#
# # Uruchomienie pętli zdarzeń asyncio
#
# loop = asyncio.new_event_loop()
# loop.create_task(main())
#
# # Synchronizacja pętli zdarzeń asyncio z zegarem Kivy
# loop.run_forever()
# print("LOL XD")


MyApp().run()





# Uruchomienie pętli zdarzeń asyncio
# MyApp().run()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(
#     async_runTouchApp(MyApp.run(), async_lib='asyncio'))
# loop.close()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(
#     async_runTouchApp(myApp(), async_lib='asyncio'))
# loop.close()

# loop = asyncio.get_event_loop()
# loop.call_soon(myApp().run)
# loop.run_forever()
# loop.close()
