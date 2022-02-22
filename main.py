from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import *
import sys
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.acceptDrops()
        # set the title
        self.setWindowTitle("Image")
 
        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)
 
        # creating label
        self.label = QLabel(self)
         
        # loading image
        self.pixmap = QPixmap('logo.jpg')
        self.pixmap = self.pixmap.scaled(1000, 1000, Qt.KeepAspectRatio)

        # adding image to label
        self.label.setPixmap(self.pixmap)
 
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
 
        # show all the widgets
        self.show()
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
window.showMaximized()
# start the app
sys.exit(App.exec())