from _typeshed import Self
from PyQt5.QtWidgets import *
from _init import *

class app(QWidget):
    def __init__(self):
        super().__init__()
        self.title = WinTitle
        self.width = WinWidth
        self.height = WinHeight
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle = WinTitle(self.title)
        self.geometry(self.width, self.height)
        self.show()

    