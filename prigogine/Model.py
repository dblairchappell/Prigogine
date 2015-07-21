
from Population import Population
from numpy import *
from matplotlib.pyplot import *

class Model:

    #########################

    def __init__(self):

        self.modelName = ""
        self.populations = {}
        self.timeStepMem = 2
        self.t = 0
        self.itno = 0
        self.globals = {}
        self.timeStepCode = ""

    #########################

    def initglobal(self, globalName, globalValue):
        self.globals[globalName] = eval(globalValue)
        #print self.globals

    #########################

    def getglobal(self, variableName):
        return self.globals[variableName]

    #########################

    def evaluateCode(self, codeToEval):
        getglobal = lambda variableName : self.getglobal(variableName)
        code = compile(codeToEval, "<string>", "exec")
        exec code in globals(), locals()

    #########################

    # def initvars(self, populationName, varName, varValue):
    #     self.populations[populationName].variables[varName] = eval(varValue)
    #     print self.populations[populationName].variables

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
        self.populations[populationName].currentstates = eval(states)
        #print self.populations[populationName].currentstates

    ##############################################

    def setglobal(self, variableName, value):
        self.globals[variableName] = append(self.globals[variableName], value)

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

    def addStateTransitionCode(self, populationName, codeString):
        self.populations[populationName].addStateTransitionCode(codeString)

    #########################

    def updateModel(self):
        for population in self.populations:
            variables = self.populations[population].variables
            states = self.populations[population].currentstates
            #print self.populations[population]
            self.populations[population].updateStates(states, self.t)
            self.populations[population].updateVariables(variables, self.t)

    #########################

    def getvars(self, populationName, variableName):
        #return self.model.populations[populationName].variables[variableName][self.model.t]
        #print self.populations
        #print self.populations[populationName].variables
        return self.populations[populationName].getvars(variableName, self.t)

    #########################

    def getparams(self, populationName, parameterName):
        return self.populations[populationName].getparams(parameterName)

    #########################

    def doIterationCode(self, t):

        getvars = lambda populationName, variableName  : self.getvars(populationName, variableName)
        getparams = lambda  populationName, parameterName: self.getparams(populationName, parameterName)
        getglobal = lambda variableName : self.getglobal(variableName)
        setglobal = lambda variableName, value : self.setglobal(variableName, value)

        code = compile(self.timeStepCode, "<string>", "exec")
        exec code in globals(), locals()

    #########################

    def runModel(self, numIterations):
        for each in range(numIterations):
            self.itno +=1
            self.updateModel()
            self.doIterationCode(self.t)
            if self.itno % 25 == 1:
                print ""
            print ".",
            self.t += 1
            if self.t >= self.timeStepMem:
                self.t = 0

    #########################

    def initvars(self, populationName, variableName, value):
        #print self.populations[populationName].populationSize
        self.populations[populationName].variables[variableName] = zeros((self.timeStepMem, self.populations[populationName].populationSize))

        self.populations[populationName].variables[variableName][0] = eval(value)
        #print self.populations[populationName].variables
    #########################

    def initparams(self, populationName, parameterName, value):
        self.populations[populationName].parameters[parameterName] = zeros((1, self.populations[populationName].populationSize))
        self.populations[populationName].parameters[parameterName][0] = eval(value)

    #########################


