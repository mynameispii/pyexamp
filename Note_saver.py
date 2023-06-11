import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QTextEdit,QGridLayout,QLabel,QPushButton
class example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        title=QLabel("title")
        author=QLabel("author")
        review=QLabel("review")
        titleEdit=QLineEdit()
        authorEdit=QLineEdit()
        reviewEdit=QTextEdit()
        button=QPushButton("submit")
        action=QAction(button, self)
        button.addAction(action)
        action.triggered.connect(lambda: label.setText(print(title,author,review)))
        grid=QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)
        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)
        grid.addWidget(button,9,1)
        self.setLayout(grid)
        self.setWindowTitle("Review")
        self.show()
app=QApplication(sys.argv)
ex=example()
sys.exit(app.exec_())
#    .-----.
#   .' -   - '.
#  /  .-. .-.  \
#  |  | | | |  |
#   \ \o/ \o/ /
#  _/    ^    \_
# | \  '---'  / |
#/ /`--. .--`\ \
#/ /'---` `---'\ \
#'.__.       .__.'
#    `|     |`
#     |     \
#     \      '--.
#      '.        `\
#        `'---.   |
#              ) /
#              \/
