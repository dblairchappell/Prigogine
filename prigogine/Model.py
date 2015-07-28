
from Population import Population
from numpy import *
from matplotlib.pyplot import *
import time

class Model:

    #########################

    def __init__(self):

        self.modelName = ""
        self.populations = {}
        self.timeStepMem = 2
        self.t = 0
        self.itno = 0
        self.readIndex = 0
        self.writeIndex = 1
        self.globals = {}
        self.timeStepCode = ""
        self.variableNames = []
        self.parameterName = []
        self.updateCode = []

    #########################

    def getfrom(self, populationName, variableName):
        #return self.model.populations[populationName].variables[variableName][self.model.t]
        #print self.populations
        #print self.populations[populationName].variables
        return self.populations[populationName].getvars(variableName, self.t)

    #########################

    def initglobal(self, globalName, globalValue):
        self.globals[globalName] = eval(globalValue)
        #print self.globals

    #########################

    def setglobal(self, globalName, globalValue):
        self.globals[globalName] = eval(globalValue)
        #print self.globals

    #########################

    def getglobal(self, variableName):
        return self.globals[variableName]

    ##############################################

    def appendglobal(self, variableName, value):
        self.globals[variableName] = append(self.globals[variableName], value)

    #########################

    def evaluateCode(self, codeToEval):
        getglobal = lambda variableName : self.getglobal(variableName)
        getfrom = lambda populationName, variableName : self.getfrom(populationName, variableName)
        code = compile(codeToEval, "<string>", "exec")
        exec code in globals(), locals()

    #########################

    # def initvars(self, populationName, varName, varValue):
    #     self.populations[populationName].variables[varName] = eval(varValue)
    #     print self.populations[populationName].variables

    #########################

    # def init(self, varName, varValue):
    #     exec "self.%(varName)s[0] = %(varValue)s" % \
    #          {"varName" : varName, "varValue" : varValue}

    def init(self, varName, expression):

        exec "self.%s = zeros((2,1))" % varName
        #exec "print self.%s" % varName
        code = "self.%(varName)s[0] = %(expression)s" % \
               {"varName" : varName, "expression" : expression}
        exec code in globals(), locals()

        code = "self.%(varName)s[1] = %(expression)s" % \
               {"varName" : varName, "expression" : expression}
        exec code in globals(), locals()
        #exec "print self.%s" % varName

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

    @staticmethod
    def calculateNewVals(oldVals, newVals, trueFalse):
        resultArray = oldVals
        #print "result array 1: " + str(resultArray)
        #print "trueFalse: " + str(trueFalse)
        #for index in where(trueFalse):
        if trueFalse:
            resultArray = newVals
        #print "result array 2: " + str(resultArray)
        return resultArray

    #########################

    def update(self, variableName, newValues, conditionalCheck, t):

        readIndex = self.readIndex
        writeIndex = self.writeIndex

        #print readIndex
        #print writeIndex

        t = readIndex
        oldVals = eval("self.%s[readIndex]" % variableName)
        newVals = eval(newValues)
        trueFalse = eval(conditionalCheck)
        #exec "print self.%s" % variableName

        #print trueFalse
        # maskedVals = ma.masked_array(oldVals, mask=~trueFalse)
        # result = maskedVals + newVals - oldVals
        # result.mask = ma.nomask
        #print result
        result = self.calculateNewVals(oldVals, newVals, trueFalse)
        #print result
        exec "self.%(variableName)s[%(writeIndex)d] = result" % \
             {"variableName" : variableName, "result" : result, "writeIndex" : writeIndex} in locals(), globals()

    #########################

    def evalUpdateCode(self):
        #print self.updateCode
        update = lambda variableName, value, mask, t: self.update(variableName, value, mask, self.t)
        for code in self.updateCode:
            exec code in globals(), locals()

    #########################

    def updateModel(self):
        #print self.populations
        for name, population in self.populations.items():
            population.t = self.t
            #print name
            #print population.updateCode
            population.evalUpdateCode()
            self.evalUpdateCode()

            #variables = self.populations[population].variables
            #states = self.populations[population].currentstates
            #print self.populations[population]
            #self.populations[population].updateStates(states, self.t)
            #self.populations[population].updateVariables(variables, self.t)

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
        getfrom = lambda populationName, variableName  : self.getvars(populationName, variableName)
        code = compile(self.timeStepCode, "<string>", "exec")
        exec code in globals(), locals()

    #########################

    def runModel(self, numIterations):

        print "\n-------- running model for " + str(numIterations) + " timesteps --------"
        start = time.clock()

        for each in range(numIterations):

            self.writeIndex = self.t + 1
            while self.writeIndex >= self.timeStepMem:
                self.writeIndex -= self.timeStepMem

            self.readIndex = self.t
            while self.readIndex >= self.timeStepMem:
                self.readIndex -= self.timeStepMem

            self.updateModel()
            self.itno +=1

            if self.itno % 25 == 1:
                 print ""
            print ".",

            self.t += 1

        end = time.clock()
        print "\n--------- completed run in %.5f secs ---------" % round((end - start),5)

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


