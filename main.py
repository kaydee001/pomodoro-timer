from PySide6.QtWidgets import QApplication
from ui import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
