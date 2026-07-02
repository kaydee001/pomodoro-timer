from PySide6.QtCore import QTimer, QObject, Signal


class PomodoroTimer(QObject):
    tick_signal = Signal(int, int)

    def __init__(self):
        super().__init__()

        self.state = "IDLE"
        self.work_duration = 25
        self.break_duration = 5
        self.timer = QTimer()
        self.seconds = 0
        self.minutes = self.work_duration

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
        self.tick_signal.emit(self.minutes, self.seconds)
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds = 59
            self.minutes -= 1
        if self.minutes == -1:
            self.state = "BREAK" if self.state == "WORKING" else "IDLE"
            self.minutes = self.work_duration
            self.seconds = 0
