# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by PrigogineParser.

class PrigogineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrigogineParser#filestart.
    def visitFilestart(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#model.
    def visitModel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#simulation.
    def visitSimulation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#codeinsert.
    def visitCodeinsert(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#equationlist.
    def visitEquationlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#elementwiseEquation.
    def visitElementwiseEquation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#mapEquation.
    def visitMapEquation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#assignment.
    def visitAssignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#population.
    def visitPopulation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#parameterlist.
    def visitParameterlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#variablelist.
    def visitVariablelist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#listcomp.
    def visitListcomp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#listdef.
    def visitListdef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#tupledef.
    def visitTupledef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#variable.
    def visitVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#indexedvariable.
    def visitIndexedvariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#parameter.
    def visitParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#timeindex.
    def visitTimeindex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#timevar.
    def visitTimevar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#dictindex.
    def visitDictindex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#codeblock.
    def visitCodeblock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#codeline.
    def visitCodeline(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#pyforloop.
    def visitPyforloop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#string.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#conditional.
    def visitConditional(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#lparen.
    def visitLparen(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#rparen.
    def visitRparen(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#func.
    def visitFunc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrigogineParser#number.
    def visitNumber(self, ctx):
        return self.visitChildren(ctx)


