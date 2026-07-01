from PySide6.QtCore import QTimer


class PomodoroTimer():
    def __init__(self):
        self.seconds = 0
        self.minutes = self.work_duration
        self.state = "IDLE"
        self.work_duration = 25
        self.break_duration = 5
        self.timer = QTimer()

        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tick)

    def start(self):
        self.state = "WORKING"
        self.timer.start()

    def pause(self):
        self.state = "PAUSED"
        self.timer.stop()

    def resume(self):
        self.state = "WORKING"
        self.timer.start()

    def reset(self):
        self.state = "IDLE"
        self.timer.stop()
        self.minutes = self.work_duration
        self.seconds = 0

    def tick(self):
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds = 59
            self.minutes -= 1
        if self.minutes == -1:
            self.state = "BREAK" if self.state == "WORKING" else "IDLE"
            self.minutes = self.work_duration
            self.seconds = 0
