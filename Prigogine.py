
###########################################################################################################
###########################################################################################################

import sys
from PrigogineDirector import PrigogineDirector
from PrigogineLexer import PrigogineLexer
from PrigogineParser import PrigogineParser
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

###########################################################################################################
###########################################################################################################

class Prigogine():

    def __init__(self, inputStream):

        self.model = self.buildModel(inputStream)

    def buildModel(self, inputStream):

        lexer = PrigogineLexer(inputStream)
        tokenStream = CommonTokenStream(lexer)
        parser = PrigogineParser(tokenStream)
        tree = parser.filestart()

        listener = PrigogineDirector(tokenStream)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        model = listener.getModel()

        return model

    def runModel(self, numIterations):

        self.model.runModel(numIterations)

###########################################################################################################
###########################################################################################################

def main(argv):

    inputStream = FileStream(argv[1])
    prigogine = Prigogine(inputStream)
    prigogine.runModel(50)

if __name__ == '__main__':

    main(sys.argv)

###########################################################################################################
###########################################################################################################

