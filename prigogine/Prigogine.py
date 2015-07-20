
##############################################
##############################################

import numpy as np
from ListenerBuilder import ListenerBuilder
from parser.PrigogineLexer import PrigogineLexer
from parser.PrigogineParser import PrigogineParser
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

##############################################
##############################################

class Prigogine:

    ##############################################

    def __init__(self):
        self.model = None

    ##############################################

    @staticmethod
    def buildModel(inputStream):
        lexer = PrigogineLexer(inputStream)
        tokenStream = CommonTokenStream(lexer)
        parser = PrigogineParser(tokenStream)
        walker = ParseTreeWalker()
        listener = ListenerBuilder(tokenStream)
        tree = parser.filestart()
        walker.walk(listener, tree)

        return listener.getModel()

    ##############################################

    def getglobal(self, variableName):
        return self.model.globals[variableName]

    ##############################################

    def get(self, populationName, variableName):
        #return self.model.populations[populationName].variables[variableName][self.model.t]
        return self.model.populations[populationName].get(variableName, self.model.t)

    ##############################################

    def getparams(self, populationName, parameterName):
        return self.model.populations[populationName].getparams(parameterName)

    ##############################################

    def setglobal(self, variableName, value):
        self.model.globals[variableName] = np.append(self.model.globals[variableName], value)
        #print self.model.globals

    ##############################################

    def initglobal(self, variableName, value):
        self.model.globals[variableName] = value

    ##############################################

    def createpop(self, populationName, populationSize):
        self.model.create(populationName, populationSize)

    ##############################################

    def initstates(self, populationName, stateName):
        self.model.setstates(populationName, stateName)

    ##############################################

    def initvars(self, populationName, variableName, value):
        self.model.initvars(populationName, variableName, value)

    ##############################################

    def initparams(self, populationName, parameterName, value):
        self.model.initparams(populationName, parameterName, value)

    ##############################################

    def loadmodel(self, modelName):
        inputStream = FileStream(modelName)
        self.model = self.buildModel(inputStream)

    ##############################################

    def runmodel(self, numIterations):
        self.model.runModel(numIterations)

##############################################
##############################################

prigogine = Prigogine()

##############################################
##############################################






