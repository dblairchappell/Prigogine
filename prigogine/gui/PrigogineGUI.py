
from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
import sys
import json

form_class = uic.loadUiType("Prigogine.ui")[0]

class MyWindowClass(QMainWindow, form_class):

    #######################################

    def __init__(self, parent=None):

        self.workingData = {"populationCode": "", "simulationScript": ""}
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.showMaximized()
        self.addPopulationButton.clicked.connect(self.actionAddPopulationButton_clicked)
        self.actionQuit.triggered.connect(app.quit)
        self.actionNew.triggered.connect(self.newFileButton_Clicked)
        self.actionOpen.triggered.connect(self.openFileButton_Clicked)
        self.actionSave_As.triggered.connect(self.saveAsButton_Clicked)

    #######################################

    def actionAddPopulationButton_clicked(self):
        populationName = self.addPopulationLineEdit.text()
        populationName = populationName.replace(" ", "")
        if populationName != "":
            population = QListWidgetItem(populationName)
            self.populationListWidget.addItem(population)

    #######################################

    def newFileButton_Clicked(self):
        self.showNewFileDialog()

    def showNewFileDialog(self):
        fileDialog = QFileDialog()
        fileName = fileDialog.getSaveFileName(self, 'New File', '/home/','*.pr')
        with open(fileName, 'w') as outfile:
           with open(fileName) as infile:
                for line in infile:
                    outfile.write(line)

    #######################################

    def openFileButton_Clicked(self):
        self.showOpenFileDialog()

    def showOpenFileDialog(self):

        fileDialog = QFileDialog()
        filename = QFileDialog.getOpenFileName(fileDialog, 'Open Project', '/home/','*.pr')
        with open(filename, 'r') as inData:
            data = json.load(inData)
            self.modelCodeTextEdit.insertPlainText(data["populationCode"])
            self.simulationScriptTextEdit.insertPlainText(data["simulationScript"])

    #######################################

    def saveAsButton_Clicked(self):
        self.showSaveAsDialog()

    def showSaveAsDialog(self):

        fileDialog = QFileDialog()
        filename = QFileDialog.getOpenFileName(fileDialog, 'Open Project', '/home/','*.pr')

        popCode = str(self.modelCodeTextEdit.toPlainText())
        self.workingData["populationCode"] = popCode

        simCode = str(self.simulationScriptTextEdit.toPlainText())
        self.workingData["simulationScript"] = simCode

        with open(filename, 'w') as outfile:
            json.dump(self.workingData, outfile)

    #######################################

app = QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()




