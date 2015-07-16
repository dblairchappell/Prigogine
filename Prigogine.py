
##############################################

from numpy import *
from OverriddenListener import OverriddenListener
from PrigogineLexer import PrigogineLexer
from PrigogineParser import PrigogineParser
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

##############################################


class Prigogine:

    def __init__(self):
        self.model = None

    def buildModel(self, inputStream):

        lexer = PrigogineLexer(inputStream)
        tokenStream = CommonTokenStream(lexer)
        parser = PrigogineParser(tokenStream)
        walker = ParseTreeWalker()
        listener = OverriddenListener(tokenStream)
        tree = parser.filestart()
        walker.walk(listener, tree)

        return listener.getModel()

    ##############################################

    def create(self, populationName, populationSize):
        return

    ##############################################

    def startstate(self, populationName, stateName):
        return

    ##############################################

    def init(self, populationName, attributeName, value):
        return

    ##############################################

    def loadmodel(self, modelName):
        inputStream = FileStream(modelName)
        self.model = self.buildModel(inputStream)

    ##############################################

    def runmodel(self, numIterations):
        self.model.runModel(numIterations)
        print self.model.populations["households"].attributes["numJobs"]

    ##############################################

prigogine = Prigogine()