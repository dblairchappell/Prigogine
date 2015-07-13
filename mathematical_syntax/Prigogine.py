
##########################################

import sys
import numpy as np
from antlr4 import *
from antlr4.InputStream import InputStream
from PrigogineParser import PrigogineParser
from PrigogineLexer import PrigogineLexer
from PrigogineListener import PrigogineListener

##########################################

class Model:
    def __init__(self):
        self.attributes = {}
    def add_attribute(self, name):
        self.attributes[name] = np.zeros((1, 1))

##########################################

class PrigogineListener(PrigogineListener):

    def __init__(self):
        self.model = Model()

    def enterFilestart(self, ctx):
        print "enter file"

    def exitFilestart(self, ctx):
        print "exit file"
        print self.model.attributes

    def enterCommand(self, ctx):
        print "enter command"

    def exitCommand(self, ctx):
        print "exit command"

    def enterExpression(self, ctx):
        print "enter expression"

    def exitExpression(self, ctx):
        print "exit expression"

    def enterInitvar(self, ctx):
        print "enter initvar"

    def exitInitvar(self, ctx):
        print "exit initvar"

    def enterGetvar(self, ctx):
        print "enter getvar"

    def exitGetvar(self, ctx):
        print "exit getvar"

    def enterListcomp(self, ctx):
        print "enter listcomp"

    def exitListcomp(self, ctx):
        print "exit listcomp"

    def enterEquation(self, ctx):
        print "enter equation"
        varName = str(ctx.ID())
        self.model.add_attribute(varName)

    def exitEquation(self, ctx):
        print "exit equation"

    def enterTimestep(self, ctx):
        print "enter timestep"

    def exitTimestep(self, ctx):
        print "exit timestep"

    def enterFunc(self, ctx):
        print "enter func"

    def exitFunc(self, ctx):
        print "exit func"

    def enterNumber(self, ctx):
        print "enter number"

    def exitNumber(self, ctx):
        print "exit number"

    def enterDeflist(self, ctx):
        print "enter deflist"

    def exitDeflist(self, ctx):
        print "exit deflist"

##########################################

if __name__ == '__main__':


    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = PrigogineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = PrigogineParser(token_stream)
    tree = parser.filestart()

    listener = PrigogineListener()
    walker = ParseTreeWalker()

    filestart = PrigogineListener()
    walker.walk(filestart, tree)

##########################################




