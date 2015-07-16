
###########################################################################################################
###########################################################################################################

import time
import sys
from ListenerDirector import ListenerDirector
from PrigogineLexer import PrigogineLexer
from PrigogineParser import PrigogineParser
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

###########################################################################################################
###########################################################################################################

class Prigogine:

    def __init__(self):
        self.model = None

    @staticmethod
    def buildLexer(inputStream):
        return PrigogineLexer(inputStream)

    @staticmethod
    def buildTokenStream(lexer):
        return CommonTokenStream(lexer)

    @staticmethod
    def buildParser(tokenStream):
        return PrigogineParser(tokenStream)

    @staticmethod
    def buildListener(tokenStream):
        return ListenerDirector(tokenStream)

    @staticmethod
    def buildWalker():
        return ParseTreeWalker()

    def buildModel(self, inputStream):
        lexer = self.buildLexer(inputStream)
        tokenStream = self.buildTokenStream(lexer)
        parser = self.buildParser(tokenStream)
        tree = parser.filestart()
        listener = self.buildListener(tokenStream)
        walker = self.buildWalker()
        walker.walk(listener, tree)
        self.model = listener.getModel()

    def runModel(self, numIterations):
        self.model.runModel(numIterations)
        print self.model.populations["households"].attributes["numJobs"]

###########################################################################################################
###########################################################################################################

def main(argv):

    start = time.clock()
    inputStream = FileStream(argv[1])
    prigogine = Prigogine()
    prigogine.buildModel(inputStream)


    prigogine.runModel(100)
    end = time.clock()
    print "time elapsed: " + str(end - start) + "s"

if __name__ == '__main__':

    main(sys.argv)

###########################################################################################################
###########################################################################################################

