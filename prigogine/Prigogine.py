
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

    def getvars(self, populationName, variableName):
        #return self.model.populations[populationName].variables[variableName][self.model.t]
        return self.model.populations[populationName].getvars(variableName, self.model.t)

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

    def loadmodel(self, *filenames):
        with open('__workingmodel.prm', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)

        inputStream = FileStream('__workingmodel.prm')
        self.model = self.buildModel(inputStream)
        print self.model
        return self.model

    def getmodel(self):
        return self.model

    ##############################################

    def loadModelFromGUI(self, codeToParse):
        with open('__workingmodel.prm', 'w') as outfile:
            for line in codeToParse:
                outfile.write(line)

        inputStream = FileStream('__workingmodel.prm')
        self.model = self.buildModel(inputStream)

    ##############################################

    def runmodel(self, numIterations):
        self.model.runModel(numIterations)

    ##############################################

    def init(self):
        print "test"

prigogine = Prigogine()






