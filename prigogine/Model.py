
from Population import Population
import numpy as np

class Model:

    #########################

    def __init__(self):

        self.modelName = ""
        self.populations = {}
        self.timeStepMem = 2
        self.t = 0
        self.itno = 0
        self.globals = {}

    #########################

    # def incrementTime(self):
    #     self.t += 1

    #########################

    def addModelName(self, modelName):
        self.modelName = modelName

    #########################

    def getModelName(self):
        return self.modelName

    #########################

    def convertStateNameToId(self, populationName, stateName):
        return self.populations[populationName].stateData[stateName]["stateId"]

    #########################

    def setstates(self, populationName, states):
        self.populations[populationName].currentstates = states
        print self.populations[populationName].currentstates

    #########################

    def create(self, populationName, populationSize):
        self.populations[populationName].populationSize = populationSize
        #self.populations[populationName].currentStates = None

    #########################

    def declarePopulation(self, populationName):
        self.populations[populationName] = Population(1, self)

    #########################

    def declareVariable(self, populationName, variableName):
        self.populations[populationName].declareVariable(variableName)

    #########################

    def declareParameter(self, populationName, parameterName):
        self.populations[populationName].declareParameter(parameterName)

    #########################

    # def addState(self, populationName, stateName, stateId):
    #     self.populations[populationName].addState(stateName, stateId)

    def addState(self, populationName, stateName):
        self.populations[populationName].addState(stateName)

    #########################

    def addUpdateCode(self, populationName, codeString):
        self.populations[populationName].addUpdateCode(codeString)

    #########################

    def updateModel(self):
        for population in self.populations:
            variables = self.populations[population].variables
            self.populations[population].updateVariables(variables, self.t)

    #########################

    def runModel(self, numIterations):
        for each in range(numIterations):
            self.itno +=1
            self.updateModel()
            if self.itno % 25 == 1:
                print "" #self.itno
            print ".",
            self.t += 1
            if self.t >= self.timeStepMem:
                self.t = 0

    #########################

    def initvars(self, populationName, variableName, value):
        self.populations[populationName].variables[variableName] = np.zeros((self.timeStepMem, self.populations[populationName].populationSize))
        self.populations[populationName].variables[variableName][0] = value

    #########################

    def initparams(self, populationName, parameterName, value):
        self.populations[populationName].parameters[parameterName] = np.zeros((1, self.populations[populationName].populationSize))
        self.populations[populationName].parameters[parameterName][0] = value

    #########################


