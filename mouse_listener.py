from threading import Thread
from time import sleep
import win32api


class MouseListener:
    def __init__(self, callback):
        self.callback = callback
        self.pressed = False
        thread_run = Thread(target=self.run, daemon=True)
        thread_run.start()

    def run(self):
        while True:
            prev_pressed = self.pressed
            self.pressed = (
                win32api.GetKeyState(0x04) < 0
                or win32api.GetKeyState(0x05) < 0
                or win32api.GetKeyState(0x06) < 0
            )
            if self.pressed != prev_pressed:
                self.callback(self.pressed)

            sleep(0.01)
