import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QTextEdit,\
QGridLayout,QLabel,QPushButton,\
QTabWidget,QFormLayout,QHBoxLayout,QRadioButton,\
QLabel,QCheckBox
class example(QTabWidget):
    def __init__(self,parent=None):
        super(example,self).__init__(parent)
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.addTab(self.tab1,"Tab1")
        self.addTab(self.tab2,"Tab2")
        self.addTab(self.tab3,"Tab3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.setWindowTitle("Contact Saver")

    def tab1UI(self):
        layout=QFormLayout()
        layout.addRow("Name",QLineEdit())
        layout.addRow("Address",QLineEdit())
        self.setTabText(0,"contact details")
        self.tab1.setLayout(layout)
    def tab2UI(self):
        layout=QFormLayout()
        s=QHBoxLayout()
        s.addWidget(QRadioButton("Male"))
        s.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("sex"),s)
        layout.addRow("Date of Birth",QLineEdit())
        self.setTabText(1,"personal ditails")
        self.tab2.setLayout(layout)
    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("subject"))
        layout.addWidget(QCheckBox("physics"))
        layout.addWidget(QCheckBox("math"))
        self.setTabText(2,"Education Details")
        self.tab3.setLayout(layout)
app=QApplication(sys.argv)
ex=example()
ex.show()
sys.exit(app.exec_())
