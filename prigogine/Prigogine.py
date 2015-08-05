from prigogine.PrigogineCore import *
from PyQt4 import QtCore, uic
from PyQt4.QtGui import *
import sys
import json
import ast

form_class = uic.loadUiType("Prigogine.ui")[0]
popname_class = uic.loadUiType("namePopulationPopup.ui")[0]
varname_class = uic.loadUiType("nameVariablePopup.ui")[0]
loader_class = uic.loadUiType("PrigogineLoader.ui")[0]

########################################

class NamePopulationPopup(QDialog, popname_class):

    def __init__(self, parent):
        self.mainWindow = parent
        QDialog.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.popNameButtonBox.accepted.connect(self.addPop)

    def addPop(self):
        popName = self.popNameLineEdit.text()
        if popName != "":
            self.mainWindow.addPopulation(self.mainWindow.modelRoot, popName)

########################################

class NameVariablePopup(QDialog, varname_class):

    def __init__(self, parent):
        self.mainWindow = parent
        QDialog.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.varNameButtonBox.accepted.connect(self.addVar)

    def addVar(self):
        varName = self.varNameLineEdit.text()
        if varName != "":
            self.mainWindow.addVariable(self.mainWindow.modelRoot, varName)

########################################

class LoaderPopup(QDialog, loader_class):

    def __init__(self, parent):
        QDialog.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.white)
        self.setPalette(p)
        myPixmap = QPixmap('PrigogineLogo.png')
        myScaledPixmap = myPixmap.scaled(self.imageLabel.size(), QtCore.Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(myScaledPixmap)

########################################

class MyWindowClass(QMainWindow, form_class):

    #######################################

    def __init__(self, parent=None):

        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten) # Install the custom output stream
        sys.stderr = EmittingStream(textWritten=self.errorOutputWritten)

        self.currentProject = None
        self.workingData = {"model" : {"populations" : {}, "variables" : [], "equations" : "", "modelName" : ""}, "simulationCode" : "", "analysisCode" : "", "notes" : ""}

        self.selectedPopulation = ""
        self.modelRoot = None

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
        self.equationTextEdit.textChanged.connect(self.equationTextEdit_Changed)

        self.simulationTextEdit.textChanged.connect(self.simulationTextEdit_Changed)
        self.analysisTextEdit.textChanged.connect(self.analysisTextEdit_Changed)
        self.notesTextEdit.textChanged.connect(self.notesTextEdit_Changed)

        self.clearTerminalPushButton.clicked.connect(self.actionClearTerminalPushButton_clicked)
        self.actionAboutPrigogine.triggered.connect(self.showLoaderPopup)

        self.addPopAction = QAction("Add Population", self)
        self.addVarAction = QAction("Add Variable", self)
        self.delAction = QAction("Delete", self)

        self.populationTreeWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.populationTreeWidget.addAction(self.addPopAction)
        self.populationTreeWidget.addAction(self.addVarAction)
        self.populationTreeWidget.addAction(self.delAction)

        self.addPopAction.triggered.connect(self.showAddPopName)
        self.addVarAction.triggered.connect(self.showAddVarName)
        self.delAction.triggered.connect(self.deleteFromTree)

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

    def showAddVarName(self):
        self.w = NameVariablePopup(self)
        self.w.show()

    #######################################

    def deleteFromTree(self):
        item = self.populationTreeWidget.currentItem()
        if self.populationTreeWidget.currentItem().parent() is not None:
            #self.workingData
            #del self.workingData[str(item.text(0))]
            #self.populationTreeWidget.currentItem().parent().removeChild(item)
            print self.workingData

    #######################################

    def addRoot(self, name):

        item = QTreeWidgetItem(self.populationTreeWidget)
        item.setText(0, name)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setIcon(0, QIcon(QtCore.QString.fromUtf8("model_icon.png")))
        self.populationTreeWidget.addTopLevelItem(item)
        #self.workingData[name] = {}
        self.populationTreeWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        return item

    #######################################

    def addPopulation(self, parent, name):
        item = QTreeWidgetItem()
        item.setText(0, name)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setIcon(0, QIcon(QtCore.QString.fromUtf8("population_icon.png")))
        parent.addChild(item)
        parent.text(0)
        self.workingData["model"]["populations"][str(name)] = {"variables" : [], "equations" : ""}

    #######################################

    def addVariable(self, parent, name):
        item = QTreeWidgetItem()
        item.setText(0, name)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setIcon(0, QIcon(QtCore.QString.fromUtf8("variable_icon.png")))
        parent.addChild(item)
        parent.text(0)
        self.workingData["model"]["variables"].append(str(name))

    #######################################

    def actionClearTerminalPushButton_clicked(self):
        self.terminalOutTextEdit.clear()

    #######################################

    def newFileButton_Clicked(self):
        self.showNewFileDialog()

    #######################################

    def showNewFileDialog(self):

        fileDialog = QFileDialog()
        fileName = str(fileDialog.getSaveFileName(self, 'New File', '.','*.pr'))

        with open(fileName, 'w') as outfile:
           with open(fileName) as infile:
                for line in infile:
                    outfile.write(line)

        windowTitle = "Prigogine - " + str(fileName)
        self.setWindowTitle(windowTitle)
        self.currentProject = fileName

        self.populationTreeWidget.clear()
        self.equationTextEdit.clear()
        self.simulationTextEdit.clear()
        self.analysisTextEdit.clear()
        self.notesTextEdit.clear()

        self.modelRoot = self.addRoot("model")

        self.workingData["model"] = {"populations" : {}, "variables" : [], "equations" : "", "modelName" : "model"}
        self.workingData["simulationCode"] = ""
        self.workingData["analysisCode"] = ""
        self.workingData["notes"] = ""

        with open(fileName, 'w') as outfile:
            json.dump(self.workingData, outfile)

    #######################################

    def openFileButton_Clicked(self):
        self.showOpenFileDialog()

    #######################################

    def showOpenFileDialog(self):

        fileDialog = QFileDialog()
        filename = str(QFileDialog.getOpenFileName(fileDialog, 'Open Project', '.','*.pr'))
        self.currentProject = filename

        self.populationTreeWidget.clear()
        self.equationTextEdit.clear()
        self.simulationTextEdit.clear()
        self.analysisTextEdit.clear()
        self.notesTextEdit.clear()

        with open(filename, 'r') as inData:

            dataToLoad = ast.literal_eval(inData.read())
            self.modelRoot = self.addRoot(dataToLoad["model"]["modelName"])

            for varName in dataToLoad["model"]["variables"]:
                self.addVariable(self.modelRoot, varName)

            for popName, value in dataToLoad["model"]["populations"].items():
                self.addPopulation(self.modelRoot, popName)

            self.simulationTextEdit.insertPlainText(dataToLoad["simulationCode"])
            self.analysisTextEdit.insertPlainText(dataToLoad["analysisCode"])
            self.notesTextEdit.insertPlainText(dataToLoad["notes"])
            self.workingData = dataToLoad

        windowTitle = "Prigogine - " + str(filename)
        self.setWindowTitle(windowTitle)

    #######################################

    def saveAsButton_Clicked(self):
        self.showSaveAsDialog()

    #######################################

    def showSaveAsDialog(self):

        fileDialog = QFileDialog()
        filename = QFileDialog.getSaveFileName(fileDialog, 'Save Project', '.','*.pr')
        self.currentProject = filename
        with open(filename, 'w') as outfile:
            outfile.write(str(self.workingData))

    #######################################

    def saveButton_Clicked(self):

        filename = self.currentProject
        with open(filename, 'w') as outfile:
            outfile.write(str(self.workingData))

    #######################################

    def simulationRunPushButton_Clicked(self):
        # codeToParse = self.workingData["modelCode"] #+ "\n\n" + self.workingData["simulationScript"]
        # prigogine.loadModelFromGUI(codeToParse)
        # code = compile(self.workingData["simulationScript"], "<string>", "exec")
        # exec code in globals(), locals()
        print "running simulation"

    #######################################

    def equationTextEdit_Changed(self):
        #self.workingData["modelCode"] = str(self.equationTextEdit.toPlainText())
        print "editing equations"

    #######################################

    def simulationTextEdit_Changed(self):
        self.workingData["simulationCode"] = str(self.simulationTextEdit.toPlainText())

    #######################################

    def analysisTextEdit_Changed(self):
        self.workingData["analysisCode"] = str(self.analysisTextEdit.toPlainText())

    #######################################

    def notesTextEdit_Changed(self):
        self.workingData["notes"] = str(self.analysisTextEdit.toPlainText())

    #######################################

    def __del__(self):
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

