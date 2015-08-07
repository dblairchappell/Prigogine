from Population import Population
from numpy import *
import numpy as np
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
        self.updateCode = []
        self.variables = []

    #########################

    def get(self, variableName):
        exec "return self.%s[self.readIndex][0]" % variableName

    #########################

    def evaluateCode(self, codeToEval):
        getglobal = lambda variableName : self.getglobal(variableName)
        getfrom = lambda populationName, variableName : self.getfrom(populationName, variableName)
        code = compile(codeToEval, "<string>", "exec")
        exec code in globals(), locals()

    #########################

    def init(self, varName, expression):

        exec "self.%s = zeros((2,1))" % varName
        code = "self.%(varName)s[0] = %(expression)s" % \
               {"varName" : varName, "expression" : expression}
        exec code in globals(), locals()

        code = "self.%(varName)s[1] = %(expression)s" % \
               {"varName" : varName, "expression" : expression}
        exec code in globals(), locals()

    #########################

    @staticmethod
    def calculateNewVals(oldVals, newVals, trueFalse):
        resultArray = oldVals
        if trueFalse:
            resultArray = newVals
        return resultArray

    #########################

    def update(self, variableName, newValues, conditionalCheck, t):

        readIndex = self.readIndex
        writeIndex = self.writeIndex
        t = readIndex

        for popName, population in self.populations.items():
            codeline = "%(pop)s = self.%(pop)s" % \
                       {"pop" : popName}
            code = compile(codeline, "<string>", "exec")
            exec code in locals()

        for varName in self.variables:
            codeline = "%(variable)s = self.%(variable)s" % \
                       {"variable" : varName}
            code = compile(codeline, "<string>", "exec")
            exec code in locals()

        oldVals = eval("self.%s[readIndex]" % variableName)
        newVals = eval(newValues)
        trueFalse = eval(conditionalCheck)
        result = self.calculateNewVals(oldVals, newVals, trueFalse)
        exec "self.%(variableName)s[%(writeIndex)d] = result" % \
             {"variableName" : variableName, "result" : result, "writeIndex" : writeIndex} in locals(), globals()

    #########################

    def evalUpdateCode(self):
        update = lambda variableName, value, conditionalCheck, t: self.update(variableName, value, conditionalCheck, self.t)
        for code in self.updateCode:
            exec code in globals(), locals()

    #########################

    def updateModel(self):
        self.evalUpdateCode()
        for name, population in self.populations.items():
            population.t = self.t
            population.evalUpdateCode()

    #########################

    def runModel(self, numIterations):

        for each in range(numIterations):

            self.updateModel()
            self.itno +=1

            if self.itno % 25 == 1:
                 print ""
            print ".",

            self.t += 1

            self.writeIndex = self.t + 1
            while self.writeIndex >= self.timeStepMem:
                self.writeIndex -= self.timeStepMem

            self.readIndex = self.t
            while self.readIndex >= self.timeStepMem:
                self.readIndex -= self.timeStepMem

    #########################


