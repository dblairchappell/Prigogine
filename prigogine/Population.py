
from numpy import *

class Population:

    #########################

    def __init__(self, populationSize, parentModel):

        self.populationSize = populationSize
        self.timeStepMem = 2
        self.attributes = {'state': None}
        #self.stateData = {}
        self.updateCode = []
        self.currentstates = []
        self.model = parentModel

    #########################

    def setglobal(self, attributeName, value):
        self.model.globals[attributeName] = value

    #########################

    def getglobal(self, attributeName):
        return self.model.globals[attributeName]

    #########################

    def getfrom(self, populationName, attributeName, t):
        readIndex = t
        return self.model.populations[populationName].attributes[attributeName][readIndex]

    #########################

    def get(self, attributeName, t):
        readIndex = t
        while readIndex >= self.timeStepMem:
            readIndex -= self.timeStepMem
        return self.attributes[attributeName][readIndex]

    #########################

    def getstates(self, populationName):
        return self.currentStates

    #########################

    def update(self, attributeName, newValue, mask, t):
        writeIndex = t + 1
        while writeIndex >= self.timeStepMem:
            writeIndex -= self.timeStepMem
        #print attributeName + ": " + str(mask) + " " + str(newValue)
        self.attributes[attributeName][writeIndex] = newValue

    #########################

    def declareAttribute(self, attributeName):
        self.attributes[attributeName] = None

    #########################

    # def addState(self, stateName, stateId):
    #     self.stateData[stateName] = {}
    #     self.stateData[stateName]["updateCode"] = []
    #     self.stateData[stateName]["stateId"] = stateId

    def addState(self, stateName):
        self.currentstates.append(stateName)

    #########################

    def addUpdateCode(self, stateName, codeString):
        #self.stateData[stateName]["updateCode"].append(codeString)
        self.updateCode.append(codeString)

    #########################

    def updateAttributes(self, attributes, t):

        setglobal = lambda attributeName, value : self.setglobal(attributeName, value)
        update = lambda attributeName, value, mask : self.update(attributeName, value, mask, t)
        get = lambda attributeName : self.get(attributeName, t)
        getglobal = lambda attributeName : self.getglobal(attributeName)
        getfrom = lambda populationName, attributeName : self.getfrom(populationName, attributeName, t)
        getstates = lambda populationName : self.getstates(populationName)

        for codeblock in self.updateCode:
            code = compile(codeblock, "<string>", "exec")
            exec code in globals(), locals()

        # for stateKey, data in self.stateData.items():
        #     for codeblock in data["updateCode"]:
        #         code = compile(codeblock, "<string>", "exec")
        #         exec code in globals(), locals()

    #########################


