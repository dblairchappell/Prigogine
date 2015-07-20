
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

    def getglobal(self, attributeName):
        return self.model.globals[attributeName]

    ##############################################

    def get(self, populationName, attributeName):
        #return self.model.populations[populationName].attributes[attributeName][self.model.t]
        return self.model.populations[populationName].get(attributeName, self.model.t)

    ##############################################

    def setglobal(self, attributeName, value):
        self.model.globals[attributeName] = np.append(self.model.globals[attributeName], value)
        #print self.model.globals

    ##############################################

    def initglobal(self, attributeName, value):
        self.model.globals[attributeName] = value

    ##############################################

    def createpop(self, populationName, populationSize):
        self.model.create(populationName, populationSize)

    ##############################################

    def initstates(self, populationName, stateName):
        self.model.setstates(populationName, stateName)

    ##############################################

    def initvars(self, populationName, attributeName, value):
        self.model.init(populationName, attributeName, value)

    ##############################################

    def initparams(self, populationName, attributeName, value):
        self.model.init(populationName, attributeName, value)

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






