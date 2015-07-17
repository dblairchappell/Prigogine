
##############################################
##############################################

from numpy import *
from ListenerBuilder import ListenerBuilder
from PrigogineLexer import PrigogineLexer
from PrigogineParser import PrigogineParser
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
        print self.model.populations["households"].attributes["numJobs"]


##############################################
##############################################

prigogine = Prigogine()

##############################################
##############################################






