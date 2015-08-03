from prigogine.PrigogineCore import *
from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
import sys
import json

form_class = uic.loadUiType("Prigogine.ui")[0]
popname_class = uic.loadUiType("namePopulationPopup.ui")[0]
loader_class = uic.loadUiType("PrigogineLoader.ui")[0]

########################################

class NamePopulationPopup(QDialog, popname_class):

    def __init__(self, parent):
        self.mainWindow = parent
        QDialog.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.popNameButtonBox.accepted.connect(self.addPopulation)

    def addPopulation(self):
        popName = self.popNameLineEdit.text()
        if popName != "":
            self.mainWindow.addChild(self.mainWindow.modelRoot, popName)

########################################

class LoaderPopup(QDialog, loader_class):

    def __init__(self, parent):
        QDialog.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(p)
        myPixmap = QPixmap('Prigogine Logo.png')
        myScaledPixmap = myPixmap.scaled(self.imageLabel.size(), QtCore.Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(myScaledPixmap)

########################################

class MyWindowClass(QMainWindow, form_class):

    #######################################

    def __init__(self, parent=None):

        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten) # Install the custom output stream
        sys.stderr = EmittingStream(textWritten=self.errorOutputWritten)
        self.currentProject = None
        self.workingData = {"modelCode" : "", "simulationScript" : ""}
        self.selectedPopulation = ""

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.showMaximized()
        self.showLoaderPopup()

        self.actionQuit.triggered.connect(app.quit)
        self.actionNew.triggered.connect(self.newFileButton_Clicked)
        self.actionOpen.triggered.connect(self.openFileButton_Clicked)
        self.actionSave_As.triggered.connect(self.saveAsButton_Clicked)
        self.actionSave.triggered.connect(self.saveButton_Clicked)
        self.simulationRunPushButton.clicked.connect(self.simulationRunPushButton_Clicked)
        self.modelCodeTextEdit.textChanged.connect(self.modelCodeTextEdit_Changed)

        self.initialisationTextEdit.textChanged.connect(self.initialisationTextEdit_Changed)
        self.simulationTextEdit.textChanged.connect(self.simulationTextEdit_Changed)
        self.analysisTextEdit.textChanged.connect(self.analysisTextEdit_Changed)

        self.clearTerminalPushButton.clicked.connect(self.actionClearTerminalPushButton_clicked)
        self.actionAboutPrigogine.triggered.connect(self.showLoaderPopup)

        self.modelRoot = self.addRoot("ModelName")
        self.populationTreeWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        self.addPopAction = QAction("Add Population", self)
        self.delPopAction = QAction("Delete Population", self)
        self.populationTreeWidget.addAction(self.addPopAction)
        self.populationTreeWidget.addAction(self.delPopAction)

        self.populationTreeWidget.itemChanged.connect(self.treeWidgetChanged)

        #self.variableListWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        #self.addVarAction = QAction("Add Variable", self)
        #self.delVarAction = QAction("Delete Variable", self)
        #self.variableListWidget.addAction(self.addVarAction)
        #self.variableListWidget.addAction(self.delVarAction)

        self.addPopAction.triggered.connect(self.showAddPopName)
        self.delPopAction.triggered.connect(self.delPopulation)
        #self.addPopAction.triggered.connect(self.btn1, SIGNAL("clicked()"), self.doit)

    #######################################

    def treeWidgetChanged(self, item, column):
        if item.parent() is not None:
            print "changed"
        else:
            self.workingData[str(item.text(0))] ={}

    #######################################

    def showLoaderPopup(self):
        self.w = LoaderPopup(self)
        self.w.show()

    #######################################

    def showAddPopName(self):
        self.w = NamePopulationPopup(self)
        self.w.show()

    #######################################

    def delPopulation(self):
        item = self.populationTreeWidget.currentItem()
        if self.populationTreeWidget.currentItem().parent() is not None:
            self.workingData
            del self.workingData[str(item.text(0))]
            self.populationTreeWidget.currentItem().parent().removeChild(item)
            print self.workingData

    #######################################

    def addRoot(self, name):
        item = QTreeWidgetItem(self.populationTreeWidget)
        item.setText(0, name)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        self.populationTreeWidget.addTopLevelItem(item)
        self.workingData[name] = {}
        return item

    #######################################

    def addChild(self, parent, name):
        item = QTreeWidgetItem()
        item.setText(0, name)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        parent.addChild(item)
        parent.text(0)
        self.workingData[str(parent.text(0))][name] = {}
        #print self.workingData

    #######################################

    def actionClearTerminalPushButton_clicked(self):
        self.terminalOutTextEdit.clear()

    # def actionAddPopulationButton_clicked(self):
    #     populationName = self.addPopulationLineEdit.text()
    #     populationName = populationName.replace(" ", "")
    #     if populationName != "":
    #         self.workingData["populationCode"][populationName] = ""
    #         population = QListWidgetItem(populationName)
    #         self.populationListWidget.addItem(population)

    #######################################

    def newFileButton_Clicked(self):
        self.showNewFileDialog()

    def showNewFileDialog(self):
        fileDialog = QFileDialog()
        fileName = fileDialog.getSaveFileName(self, 'New File', '.','*.pr')
        with open(fileName, 'w') as outfile:
           with open(fileName) as infile:
                for line in infile:
                    outfile.write(line)
        #self.addRoot("Model")

    #######################################

    def openFileButton_Clicked(self):
        self.showOpenFileDialog()

    def showOpenFileDialog(self):

        fileDialog = QFileDialog()
        filename = QFileDialog.getOpenFileName(fileDialog, 'Open Project', '.','*.pr')
        self.currentProject = filename

        with open(filename, 'r') as inData:

            self.modelCodeTextEdit.clear()
            self.simulationScriptTextEdit.clear()
            data = json.load(inData)

            self.initialisationTextEdit.insertPlainText(data["initialisationCode"])
            self.simulationTextEdit.insertPlainText(data["simulationCode"])
            self.analysisTextEdit.insertPlainText(data["analysisCode"])

            self.workingData["initialisationCode"] = data["initialisationCode"]
            self.workingData["simulationCode"] = data["simulationCode"]
            self.workingData["analysisCode"] = data["analysisCode"]

    #######################################

    def saveAsButton_Clicked(self):
        self.showSaveAsDialog()

    def showSaveAsDialog(self):

        fileDialog = QFileDialog()
        filename = QFileDialog.getSaveFileName(fileDialog, 'Save Project', '.','*.pr')
        self.currentProject = filename

        initCode = str(self.initialisationTextEdit.toPlainText())
        self.workingData["initialisationCode"] = initCode

        simCode = str(self.simulationTextEdit.toPlainText())
        self.workingData["simulationCode"] = simCode

        analysisCode = str(self.analysisTextEdit.toPlainText())
        self.workingData["analysisCode"] = analysisCode

        with open(filename, 'w') as outfile:
            json.dump(self.workingData, outfile)

    #######################################

    def saveButton_Clicked(self):

        filename = self.currentProject

        initCode = str(self.initialisationTextEdit.toPlainText())
        self.workingData["initialisationCode"] = initCode

        simCode = str(self.simulationTextEdit.toPlainText())
        self.workingData["simulationCode"] = simCode

        analysisCode = str(self.analysisTextEdit.toPlainText())
        self.workingData["analysisCode"] = analysisCode

        with open(filename, 'w') as outfile:
            json.dump(self.workingData, outfile)

    #######################################

    def simulationRunPushButton_Clicked(self):
        # codeToParse = self.workingData["modelCode"] #+ "\n\n" + self.workingData["simulationScript"]
        # prigogine.loadModelFromGUI(codeToParse)
        # code = compile(self.workingData["simulationScript"], "<string>", "exec")
        # exec code in globals(), locals()
        print "running simulation"
    #######################################

    def modelCodeTextEdit_Changed(self):
        self.workingData["modelCode"] = str(self.modelCodeTextEdit.toPlainText())

    #######################################

    def simulationTextEdit_Changed(self):
        self.workingData["simulationCode"] = str(self.simulationTextEdit.toPlainText())

    #######################################

    def initialisationTextEdit_Changed(self):
        self.workingData["initialisationCode"] = str(self.initialisationTextEdit.toPlainText())

    #######################################

    def analysisTextEdit_Changed(self):
        self.workingData["analysisCode"] = str(self.analysisTextEdit.toPlainText())

    #######################################

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    #######################################

    def normalOutputWritten(self, text):
        cursor = self.terminalOutTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.terminalOutTextEdit.setTextCursor(cursor)
        self.terminalOutTextEdit.ensureCursorVisible()

    #######################################

    def errorOutputWritten(self, text):
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

#######################################

app = QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()

#######################################

