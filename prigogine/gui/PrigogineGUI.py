
from prigogine.Prigogine import *
from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
import sys
import json

form_class = uic.loadUiType("Prigogine.ui")[0]

class MyWindowClass(QMainWindow, form_class):

    #######################################

    def __init__(self, parent=None):

        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten) # Install the custom output stream
        self.currentProject = None
        self.workingData = {"populationCode": "", "simulationScript": ""}
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.showMaximized()
        self.addPopulationButton.clicked.connect(self.actionAddPopulationButton_clicked)
        self.actionQuit.triggered.connect(app.quit)
        self.actionNew.triggered.connect(self.newFileButton_Clicked)
        self.actionOpen.triggered.connect(self.openFileButton_Clicked)
        self.actionSave_As.triggered.connect(self.saveAsButton_Clicked)
        self.actionSave.triggered.connect(self.saveButton_Clicked)
        self.simulationRunPushButton.clicked.connect(self.simulationRunPushButton_Clicked)
        self.modelCodeTextEdit.textChanged.connect(self.modelCodeTextEdit_Changed)
        self.simulationScriptTextEdit.textChanged.connect(self.simulationScriptTextEdit_Changed)

        self.clearTerminalPushButton.clicked.connect(self.actionClearTerminalPushButton_clicked)

    #######################################

    def actionClearTerminalPushButton_clicked(self):
        self.terminalOutTextEdit.clear()

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
        self.currentProject = filename
        with open(filename, 'r') as inData:
            data = json.load(inData)
            self.modelCodeTextEdit.insertPlainText(data["populationCode"])
            self.workingData["populationCode"] = data["populationCode"]
            self.simulationScriptTextEdit.insertPlainText(data["simulationScript"])
            self.workingData["simulationScript"] = data["simulationScript"]


    #######################################

    def saveAsButton_Clicked(self):
        self.showSaveAsDialog()

    def showSaveAsDialog(self):

        fileDialog = QFileDialog()
        filename = QFileDialog.getSaveFileName(fileDialog, 'Save Project', '/home/','*.pr')
        self.currentProject = filename

        popCode = str(self.modelCodeTextEdit.toPlainText())
        self.workingData["populationCode"] = popCode

        simCode = str(self.simulationScriptTextEdit.toPlainText())
        self.workingData["simulationScript"] = simCode

        with open(filename, 'w') as outfile:
            json.dump(self.workingData, outfile)

    #######################################

    def saveButton_Clicked(self):

        filename = self.currentProject
        popCode = str(self.modelCodeTextEdit.toPlainText())
        self.workingData["populationCode"] = popCode

        simCode = str(self.simulationScriptTextEdit.toPlainText())
        self.workingData["simulationScript"] = simCode

        with open(filename, 'w') as outfile:
            json.dump(self.workingData, outfile)

    #######################################

    def simulationRunPushButton_Clicked(self):
        codeToParse = self.workingData["populationCode"] + "\n\n" + self.workingData["simulationScript"]
        prigogine.loadModelFromGUI(codeToParse)

    #######################################

    def modelCodeTextEdit_Changed(self):
        self.workingData["populationCode"] = str(self.modelCodeTextEdit.toPlainText())

    #######################################

    def simulationScriptTextEdit_Changed(self):
        self.workingData["simulationScript"] = str(self.simulationScriptTextEdit.toPlainText())

    #######################################

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    #######################################

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.terminalOutTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.terminalOutTextEdit.setTextCursor(cursor)
        self.terminalOutTextEdit.ensureCursorVisible()

    #######################################

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

app = QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()




