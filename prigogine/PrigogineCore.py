
##############################################
##############################################

from ListenerBuilder import *
from prigogine.parser.PrigogineLexer import PrigogineLexer
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

prigogine = Prigogine()






