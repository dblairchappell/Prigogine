
from numpy import *
import numpy.ma as ma

class Population:

    #########################

    def __init__(self, populationSize, parentModel):

        self.populationSize = populationSize
        self.timeStepMem = 2
        self.variables = {'state': None}
        self.parameters = {}
        self.updateCode = []
        self.currentstates = []
        self.model = parentModel
        self.calculateNewArray_vect = vectorize(self.calculateNewArray)

    #########################

    def setglobal(self, variableName, value):
        self.model.globals[variableName] = value

    #########################

    def getglobal(self, variableName):
        return self.model.globals[variableName]

    #########################

    def getfrom(self, populationName, variableName, t):
        readIndex = t
        return self.model.populations[populationName].variables[variableName][readIndex]

    #########################

    def getvars(self, variableName, t):
        readIndex = t
        while readIndex >= self.timeStepMem:
            readIndex -= self.timeStepMem
        return self.variables[variableName][readIndex]

    #########################

    def getparams(self, parameterName):
        return self.parameters[parameterName][0]

    #########################

    def getstates(self, populationName):
        return self.currentstates

    #########################

    @staticmethod
    def calculateNewArray(trueFalseMask, newValues, oldValues):
        resultArray = oldValues
        for index in where(trueFalseMask)[0]:
            resultArray[index] = newValues[index]
        return resultArray

    #########################

    def update(self, variableName, newValues, trueFalseMask, t):
        writeIndex = t + 1
        oldValues = self.getvars(variableName, t)
        while writeIndex >= self.timeStepMem:
            writeIndex -= self.timeStepMem
        result = self.calculateNewArray(trueFalseMask, newValues, oldValues)
        self.variables[variableName][writeIndex] = result

    #########################

    def declareVariable(self, variableName):
        self.variables[variableName] = None

    #########################

    def declareParameter(self, parameterName):
        self.parameters[parameterName] = None

    #########################

    def addState(self, stateName):
        self.currentstates.append(stateName)

    #########################

    def addUpdateCode(self, codeString):
        self.updateCode.append(codeString)

    #########################

    def updateVariables(self, variables, t):

        setglobal = lambda variableName, value : self.setglobal(variableName, value)
        update = lambda variableName, value, mask : self.update(variableName, value, mask, t)
        getvars = lambda variableName : self.getvars(variableName, t)
        getparams = lambda parameterName : self.getparams(parameterName)
        getglobal = lambda variableName : self.getglobal(variableName)
        getfrom = lambda populationName, variableName : self.getfrom(populationName, variableName, t)
        getstates = lambda populationName : self.getstates(populationName)

        for codeblock in self.updateCode:
            code = compile(codeblock, "<string>", "exec")
            exec code in globals(), locals()

        # for stateKey, data in self.stateData.items():
        #     for codeblock in data["updateCode"]:
        #         code = compile(codeblock, "<string>", "exec")
        #         exec code in globals(), locals()

    #########################


