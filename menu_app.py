import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,\
QPushButton, QAction
from PyQt5.QtGui import QIcon
class example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("example")
        self.setGeometry(40,40,640,400)
        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu('File')
        editMenu=mainMenu.addMenu('Edit')
        viewMenu=mainMenu.addMenu('View')
        searchMenu=mainMenu.addMenu('Search')
        toolsMenu=mainMenu.addMenu('Tools')
        helpMenu=mainMenu.addMenu('Help')
        exitButton=QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        self.show()
app=QApplication(sys.argv)
ex=example()
sys.exit(app.exec_())
