
###########################################################################################################
###########################################################################################################

import sys
import numpy as np
import numpy.ma as ma
from antlr4 import *
from antlr4.InputStream import InputStream
from PrigogineParser import PrigogineParser
from PrigogineLexer import PrigogineLexer
from PrigogineListener import PrigogineListener

###########################################################################################################
###########################################################################################################



###########################################################################################################
###########################################################################################################

class Model:

    def __init__(self):
        self.populations = {}
        self.t = 1

    def updateData(self):
        for populationName,val in self.populations.items():
            for attributeName, val in self.populations[populationName]["attrs"].items():
                codeToEval = self.populations[populationName]["attrs"][attributeName]["code"]
                for code in codeToEval:
                    exec code

    def runModel(self, numIterations):
        for each in range(numIterations):
            print "------------------\niteration number: " + str(self.t) + "\n------------------"
            self.updateData()
            self.t += 1

    def addPopulation(self, populationName):
        self.populations[populationName] = {}
        self.populations[populationName]["attrs"] = {}
        self.populations[populationName]["states"] = {}


    def createPopulation(self, populationName, numAgents):

        for attributeName, val in self.populations[populationName]["attrs"].items(): # instantiate attributes for all agents
            self.populations[populationName]["attrs"][attributeName]["data"] = np.zeros((1, numAgents))
            #print attributeName

        for stateName, val in self.populations[populationName]["states"].items():
            self.populations[populationName]["states"][stateName] = np.zeros((1, numAgents))

    def addAttribute(self, populationName, attrName): # declare that an attibutes exists
        self.populations[populationName]["attrs"][attrName] = {}
        self.populations[populationName]["attrs"][attrName]["code"] = []
        self.populations[populationName]["attrs"][attrName]["data"] = np.zeros((1, 1))


    def addState(self, populationName, stateName):
        self.populations[populationName]["states"][stateName] = np.zeros((1, 1))

    def initAttrsRand(self, populationName, attrName, min, max):
        for j in range(len(self.populations[populationName]["attrs"][attrName]["data"][0])):
            val = np.random.uniform(min, max)
            self.populations[populationName]["attrs"][attrName]["data"][0][j] = val

    def initAttrsRandInt(self, populationName, attrName, min, max):
        for j in range(len(self.populations[populationName]["attrs"][attrName]["data"][0])):
            val = np.random.randint(min, max)
            self.populations[populationName]["attrs"][attrName]["data"][0][j] = val

    def random(self, args):
        return np.random.uniform(args[0], args[1])

###########################################################################################################
###########################################################################################################

class Prigogine(PrigogineListener):

    #########################

    def __init__(self, tokens):
        self.model = Model()
        self.tokens = tokens
        self.currentPopulation = ""

    #########################

    def getAttributeNames(self, ctx):
        numAttrs = ctx.attributelist().getPayload().getChildCount() - 2
        attrList = []
        for i in range(numAttrs):
            attrList.append(str(ctx.attributelist().getPayload().getChild(i+1).getText()))
        #print attrList
        return attrList

    #########################

    def getStateNames(self, ctx):
        stateList = []
        for state in ctx.statedef():
            stateList.append(str(state.getPayload().getChild(1)))
        return stateList

    #########################

    def getModel(self):
        return self.model

    #########################

    def enterPopulation(self, ctx):

        populationName = str(ctx.ID())
        self.currentPopulation = populationName
        self.model.addPopulation(populationName)

        agentAttributeNames = self.getAttributeNames(ctx)
        for attrName in agentAttributeNames:
            #print attrName
            self.model.addAttribute(populationName, attrName)

        agentStateNames = self.getStateNames(ctx)
        for stateName in agentStateNames:
            self.model.addState(populationName, stateName)

    #########################

    def enterStatedef(self, ctx):
        pass

    #########################

    def getOderedTokens(self, expression):
        orderedTokenList = []
        for node in expression.children:
            #orderedTokenList.append(node)
            if node.getChildCount() > 0:
                self.getOderedTokens(node)
            else:
                print node

    #########################

    def enterUpdate(self, ctx):

        codeType = type(ctx.getChild(2))
        populationName = self.currentPopulation

        if codeType == PrigogineParser.CodelineContext:

            attributeName = str(ctx.getChild(1).getText())
            codeline = ctx.codeline() # getChild(2)
            expression = codeline.expression() # getChild(0)
            tokenInterval = expression.getSourceInterval()
            codelineString = str(self.tokens.getText(tokenInterval))
            self.model.populations[populationName]["attrs"][attributeName]["code"].append(codelineString)
            #print self.model.populations[populationName]["attrs"][attributeName]["code"]
            #print "line update " + attributeName + ": " + codelineString
            #print codelineString
            #print "----------"

        if codeType == PrigogineParser.CodeblockContext:
            attributeName = str(ctx.getChild(1).getText())
            codeblock = ctx.getChild(2) #.children
            #tokenInterval = codeblock.getSourceInterval()
            #tokenInterval = (tokenInterval[0] + 1, tokenInterval[1] -1) # get rid of 'begin' and 'end' tokens
            #codeblockString = str(self.tokens.getText(tokenInterval))
            #self.model.populations[populationName]["attrs"][attributeName]["code"].append(codeblockString)

            codeblockString = ""
            blockLen = len(codeblock.children) - 2

            for i in range(blockLen):
                lineNum = i + 1
                codeline = codeblock.children[lineNum]
                expression = codeline.expression()
                #print type(codeblock)
                tokenInterval = expression.getSourceInterval()

                codelineString = str(self.tokens.getText(tokenInterval))
                codeblockString = codeblockString + codelineString + "\n"
                self.model.populations[populationName]["attrs"][attributeName]["code"].append(codelineString)
            #print "block update " + attributeName + ":\n" + codeblockString
            print codeblockString
            #print self.model.populations[populationName]["attrs"][attributeName]["code"]
            print "----------"

    #########################

    def enterInitvar(self, ctx):

        # interval = ctx.getSourceInterval()
        # print interval
        # print ctx.start.getInputStream().getText(interval[0], interval[1])

        codeType = type(ctx.getChild(2))

        if codeType == PrigogineParser.CodelineContext:
            # interval = ctx.getSourceInterval()
            # print interval
            # for child in ctx.children:
            #    interval = child.getSourceInterval()
            #    print ctx.getInputStream().getText(interval[0], interval[1])
            code = ctx.getChild(2).getText()
            # print "init code line: " + str(code)

        if codeType == PrigogineParser.CodeblockContext:
            code = ctx.getChild(2).getChild(1).getText()
            # print "init code block: " + str(code)

    #########################

    def enterCreatepopulation(self, ctx):

        populationName = str(ctx.getPayload().ID())
        numAgents = int(ctx.getPayload().INT().getText())
        self.model.createPopulation(populationName, numAgents)

        # for attr in ctx.initvar():
        #    print attr.getPayload().attrsget()
            # print attr.getPayload().expression().getPayload().getText()
            # print attr.getPayload().expression().getPayload().getChild(0).ID()
            # print attr.getPayload().expression().getPayload().getChild(0).children[1].getText()
            # print attr.getPayload().expression().getPayload().getChild(0).children[2].getText()
            # print attr.getPayload().expression().getPayload().getChild(0).getChildCount()

    #########################

###########################################################################################################
###########################################################################################################

def loadModel(modelFileName, setupFileName):

    filenames = [modelFileName, setupFileName]

    with open('tmpmodel.prt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

    #print open('tmpmodel.prt', "r").read()
    input_stream = FileStream('tmpmodel.prt')
    lexer = PrigogineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PrigogineParser(token_stream)
    tree = parser.filestart()

    listener = Prigogine(token_stream)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    model = listener.getModel()

    return model

###########################################################################################################
###########################################################################################################





