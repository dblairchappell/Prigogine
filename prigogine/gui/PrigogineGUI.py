
from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
import sys

form_class = uic.loadUiType("Prigogine.ui")[0]

class MyWindowClass(QMainWindow, form_class):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.addPopulationButton.clicked.connect(self.actionAddPopulationButton_clicked)

    def actionAddPopulationButton_clicked(self):
        populationName = self.addPopulationLineEdit.text()
        population = QListWidgetItem(populationName)
        self.populationListWidget.addItem(population)

app = QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()




