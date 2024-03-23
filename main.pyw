import sys
import time
import random
from threading import Thread
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QSlider,
    QVBoxLayout,
    QWidget,
    QCheckBox,
    QHBoxLayout,
)
from pynput.mouse import Button, Controller
from mouse_listener import MouseListener


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.speed = {"min": 10, "max": 20}
        self.base_timeout = {"min": 0.35, "max": 0.65}
        self.mouse = Controller()
        self.click = False
        self.hold_to_click = True
        self.setup_window()
        self.update_speed()
        MouseListener(self.on_hotkey_click)
        thread_update = Thread(target=self.update, daemon=True)
        thread_update.start()

    def setup_window(self):
        self.setWindowTitle("Ghost Autoclicker")
        self.setFixedSize(360, 240)

        widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)

        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(18)

        self.label_speed = QLabel()
        self.label_speed.setAlignment(Qt.AlignCenter)
        self.label_speed.setFont(QFont("Segoe UI", 20))

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.speed["min"])
        self.slider.setMaximum(self.speed["max"])
        self.slider.valueChanged.connect(self.update_speed)

        self.hold_checkbox = QCheckBox("Hold to click")
        self.hold_checkbox.setChecked(True)
        self.hold_checkbox.stateChanged.connect(self.update_listener_type)

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(self.hold_checkbox, alignment=Qt.AlignCenter)

        self.label_buttons = QLabel("Use buttons: Middle, Forward or Back")
        self.label_buttons.setAlignment(Qt.AlignCenter)
        self.label_buttons.setFont(QFont("Segoe UI", 10))

        layout.addWidget(self.label_speed)
        layout.addWidget(self.slider)
        layout.addLayout(checkbox_layout)
        layout.addWidget(self.label_buttons)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_hotkey_click(self, pressed):
        if self.hold_to_click or pressed:
            self.click = not self.click

    def update_speed(self):
        speed = self.slider.value()
        self.label_speed.setText(f"{speed} cps")
        self.timeout = {
            "min": self.base_timeout["min"] / speed,
            "max": self.base_timeout["max"] / speed,
        }

    def update_listener_type(self):
        self.hold_to_click = self.hold_checkbox.isChecked()

    def wait_timeout(self):
        # The sleep function seems accurate now, let's try it out!
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
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
