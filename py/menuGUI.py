from PyQt5 import QtWidgets, uic
import sys


class menuGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(menuGUI, self).__init__()
        uic.loadUi('..\\ui\menu.ui', self)
        self.show()

        self.manualButton.clicked.connect(self.showManualGUI)
        self.fileButton.clicked.connect(self.showQualiGUI)
        self.randomButton.clicked.connect(self.showRandomGUI)

    def showManualGUI(self):
        from manualGUI import manualGUI
        self.manual = manualGUI()
        self.manual.show()

    def showQualiGUI(self):
        from qualiGUI import qualiGUI
        self.quali = qualiGUI()
        self.quali.show()

    def showRandomGUI(self):
        from randomGUI import randomGUI
        self.random = randomGUI()
        self.random.show()

app = QtWidgets.QApplication(sys.argv)
window = menuGUI()
app.exec_()