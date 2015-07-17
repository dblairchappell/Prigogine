
##############################################
##############################################

from numpy import *
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

    def initglobal(self, attributeName, value):
        self.model.globals[attributeName] = value

    ##############################################

    def create(self, populationName, populationSize):
        self.model.create(populationName, populationSize)

    ##############################################

    def startstate(self, populationName, stateName):
        self.model.startstate(populationName, stateName)

    ##############################################

    def init(self, populationName, attributeName, value):
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






