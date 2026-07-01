from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel
from timer import PomodoroTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pomodoro")
        self.resize(800, 600)
        self.timer = PomodoroTimer()

        self.start_button = QPushButton("start")
        self.pause_button = QPushButton("pause")
        self.reset_button = QPushButton("reset")

        self.timer_displayer = QLabel()
        self.state_toggle_button = QPushButton("working")
        self.session_counter = QLabel()
