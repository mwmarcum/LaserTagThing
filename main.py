import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        #loading image
        self.pixmap = QPixmap('logo.jpg')
        self.pixmap = self.pixmap.scaled(1000, 1000, Qt.KeepAspectRatio)

        #creating label
        self.label = QLabel(self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)

        #adding image to label
        self.label.setPixmap(self.pixmap)

        self.layout = QGridLayout()

        #adding label to screen
        self.layout.addWidget(self.label, 0, 0)
        self.setStyleSheet("background-color: black;")

        self.setLayout(self.layout)
        self.show()

        #after 3 seconds, it hides the image label
        def on_timeout():
            self.label.hide()

        #setting timer
        QTimer.singleShot(3000, on_timeout)

app = QApplication(sys.argv)
win = Window()
win.showMaximized()
sys.exit(app.exec_())