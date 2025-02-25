"""
This code was created with the help of ChatGPT.
The goal is to make a lighter executable file using the tkinter library,
since the original version with PySide6 takes several seconds to open.
This version has not been fully reviewed and may contain bugs.
There might not be future updates for it.
"""

import time
import random
from threading import Thread
import tkinter as tk
from pynput.mouse import Button, Controller
from mouse_listener import MouseListener


class Window:
    def __init__(self, master):
        self.master = master
        self.speed = {"min": 10, "max": 20}
        self.base_timeout = {"min": 0.35, "max": 0.65}
        self.mouse = Controller()
        self.click = False
        self.hold_to_click = True

        self.setup_window()
        self.update_speed(self.slider.get())

        MouseListener(self.on_hotkey_click)
        thread_update = Thread(target=self.update, daemon=True)
        thread_update.start()

    def setup_window(self):
        self.master.title("Ghost Autoclicker")
        self.master.resizable(False, False)
        self.master.geometry("360x240")

        self.frame = tk.Frame(self.master, padx=32, pady=32)
        self.frame.pack(expand=True, fill="both")

        self.label_speed = tk.Label(self.frame, text="", font=("Segoe UI", 20))
        self.label_speed.pack(pady=(0, 18))

        self.slider = tk.Scale(
            self.frame,
            from_=self.speed["min"],
            to=self.speed["max"],
            orient="horizontal",
            command=self.update_speed,
            showvalue=False,
            length=296,
        )
        self.slider.set(self.speed["min"])
        self.slider.pack(pady=(0, 18))

        self.hold_var = tk.BooleanVar(value=True)
        self.hold_checkbox = tk.Checkbutton(
            self.frame,
            text="Hold to click",
            variable=self.hold_var,
            command=self.update_listener_type,
            font=("Segoe UI", 9),
        )
        self.hold_checkbox.pack(pady=(0, 18))

        self.label_buttons = tk.Label(
            self.frame,
            text="Use buttons: Middle, Forward or Back",
            font=("Segoe UI", 10),
        )
        self.label_buttons.pack(pady=(0, 18))

    def on_hotkey_click(self, pressed):
        if self.hold_to_click or pressed:
            self.click = not self.click

    def update_speed(self, value):
        speed = int(value)
        self.label_speed.config(text=f"{speed} cps")
        self.timeout = {
            "min": self.base_timeout["min"] / speed,
            "max": self.base_timeout["max"] / speed,
        }

    def update_listener_type(self):
        self.hold_to_click = self.hold_var.get()

    def wait_timeout(self):
        timeout = random.uniform(self.timeout["min"], self.timeout["max"])
        time.sleep(timeout)

    def update(self):
        while True:
            if self.click:
                self.mouse.press(Button.left)
                self.wait_timeout()
                self.mouse.release(Button.left)
                self.wait_timeout()
            else:
                time.sleep(0.01)


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
