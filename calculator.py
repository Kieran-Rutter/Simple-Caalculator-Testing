import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem ,QPushButton, QLineEdit, QListWidget, QSizePolicy

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 400)
        self.initUI()

    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.display = QLineEdit(self)
        self.display.setFixedHeight(35)
        vbox.addWidget(self.display)

        #spacer_item = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        #vbox.addItem(spacer_item)

        self.history = QListWidget(self)
        self.history.setFixedHeight(50)
        vbox.addWidget(self.history)

        hbox.addWidget(self.createButton('7'))
        hbox.addWidget(self.createButton('8'))
        hbox.addWidget(self.createButton('9'))
        hbox.addWidget(self.createButton('/'))
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.createButton('4'))
        hbox.addWidget(self.createButton('5'))
        hbox.addWidget(self.createButton('6'))
        hbox.addWidget(self.createButton('*'))
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.createButton('1'))
        hbox.addWidget(self.createButton('2'))
        hbox.addWidget(self.createButton('3'))
        hbox.addWidget(self.createButton('-'))
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.createButton('0'))
        hbox.addWidget(self.createButton('.'))
        hbox.addWidget(self.createButton('='))
        hbox.addWidget(self.createButton('+'))
        vbox.addLayout(hbox)

        centralWidget.setLayout(vbox)

    def createButton(self, text):
        button = QPushButton(text)
        button.setFixedSize(60, 40)
        button.clicked.connect(lambda: self.buttonClicked(text))
        return button

    def buttonClicked(self, text):
        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.history.addItem(self.display.text() + " = " + result)
            except:
                result = 'Error'
            self.display.setText(result)
        elif text == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())