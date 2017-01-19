import sys
from myinterface import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.my_func)
        self.ui.lineEdit.returnPressed.connect(self.my_func)

    def my_func(self):
        s = self.ui.lineEdit.text()
        counter_space = len([ch for ch in s if ch.isspace()])
        text = 'Length of your string is: {}/{}'
        self.ui.label.setText(text.format(len(s) - counter_space, counter_space))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
