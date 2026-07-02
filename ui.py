from PySide6.QtWidgets import QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from timer import PomodoroTimer


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pomodoro")
        self.resize(800, 600)
        self.timer = PomodoroTimer()

        self.start_button = QPushButton("start")
        self.pause_button = QPushButton("pause")
        self.reset_button = QPushButton("reset")

        self.timer_display = QLabel(f"{self.timer.work_duration} : 00")
        self.state_toggle_button = QPushButton("working")
        self.session_counter = QLabel("1")

        row1 = QHBoxLayout()
        row1.addWidget(self.state_toggle_button)
        row1.addWidget(self.session_counter)
        row2 = QVBoxLayout()
        row2.addWidget(self.timer_display)
        row3 = QHBoxLayout()
        row3.addWidget(self.start_button)
        row3.addWidget(self.pause_button)
        row3.addWidget(self.reset_button)

        self.start_button.clicked.connect(self.timer.start)
        self.pause_button.clicked.connect(self.timer.pause)
        self.reset_button.clicked.connect(self.timer.reset)

        self.timer.tick_signal.connect(self.update_timer)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(row1)
        mainLayout.addLayout(row2)
        mainLayout.addLayout(row3)

        self.setLayout(mainLayout)

    def update_timer(self, minutes, seconds):
        self.timer_display.setText(f"{minutes:02} : {seconds:02}")
