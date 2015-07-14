
###########################################################################################################
###########################################################################################################

from ModelBuilder import ModelBuilder
from PrigogineParser import PrigogineParser
from PrigogineListener import PrigogineListener

###########################################################################################################
###########################################################################################################

class ListenerDirector(PrigogineListener):

    #########################

    def __init__(self, tokens):

        self.modelBuilder = ModelBuilder()
        self.tokens = tokens
        self.currentPopulation = ""

    #########################

    def getModel(self):
        return self.modelBuilder.getModel()
    #########################

    @staticmethod
    def getAttributeNames(ctx):
        numAttrs = ctx.attributelist().getPayload().getChildCount() - 2
        attrList = []
        for i in range(numAttrs):
            attrList.append(str(ctx.attributelist().getPayload().getChild(i+1).getText()))
        return attrList

    #########################

    @staticmethod
    def getStateNames(ctx):
        stateList = []
        for state in ctx.statedef():
            stateList.append(str(state.getPayload().getChild(1)))
        return stateList

    #########################

    def enterPopulation(self, ctx):

        populationName = str(ctx.ID())
        self.currentPopulation = populationName
        self.modelBuilder.declarePopulation(populationName)

        agentAttributeNames = self.getAttributeNames(ctx)
        for attrName in agentAttributeNames:
            self.modelBuilder.declareAttribute(populationName, attrName)

        agentStateNames = self.getStateNames(ctx)
        for stateName in agentStateNames:
             self.modelBuilder.declareState(populationName, stateName)

    #########################

    def enterStatedef(self, ctx):
        pass

    #########################
    #
    # def enterUpdate(self, ctx):
    #
    #     codeType = type(ctx.getChild(2))
    #     populationName = self.currentPopulation
    #
    #     if codeType == PrigogineParser.CodelineContext:
    #
    #         attributeName = str(ctx.getChild(1).getText())
    #         codeline = ctx.codeline() # getChild(2)
    #         expression = codeline.expression() # getChild(0)
    #         tokenInterval = expression.getSourceInterval()
    #         codelineString = str(self.tokens.getText(tokenInterval))
    #         self.model.populations[populationName]["attrs"][attributeName]["code"].append(codelineString)
    #         #print self.model.populations[populationName]["attrs"][attributeName]["code"]
    #         #print "line update " + attributeName + ": " + codelineString
    #         #print codelineString
    #         #print "----------"
    #
    #     if codeType == PrigogineParser.CodeblockContext:
    #         attributeName = str(ctx.getChild(1).getText())
    #         codeblock = ctx.getChild(2) #.children
    #         #tokenInterval = codeblock.getSourceInterval()
    #         #tokenInterval = (tokenInterval[0] + 1, tokenInterval[1] -1) # get rid of 'begin' and 'end' tokens
    #         #codeblockString = str(self.tokens.getText(tokenInterval))
    #         #self.model.populations[populationName]["attrs"][attributeName]["code"].append(codeblockString)
    #
    #         codeblockString = ""
    #         blockLen = len(codeblock.children) - 2
    #
    #         for i in range(blockLen):
    #             lineNum = i + 1
    #             codeline = codeblock.children[lineNum]
    #             expression = codeline.expression()
    #             #print type(codeblock)
    #             tokenInterval = expression.getSourceInterval()
    #
    #             codelineString = str(self.tokens.getText(tokenInterval))
    #             codeblockString = codeblockString + codelineString + "\n"
    #             self.model.populations[populationName]["attrs"][attributeName]["code"].append(codelineString)
    #         #print "block update " + attributeName + ":\n" + codeblockString
    #         print codeblockString
    #         #print self.model.populations[populationName]["attrs"][attributeName]["code"]
    #         print "----------"

    #########################

    # def enterInitvar(self, ctx):
    #
    #     interval = ctx.getSourceInterval()
    #     print interval
    #     print ctx.start.getInputStream().getText(interval[0], interval[1])
    #
    #     codeType = type(ctx.getChild(2))
    #
    #     if codeType == PrigogineParser.CodelineContext:
    #         # interval = ctx.getSourceInterval()
    #         # print interval
    #         # for child in ctx.children:
    #         #    interval = child.getSourceInterval()
    #         #    print ctx.getInputStream().getText(interval[0], interval[1])
    #         code = ctx.getChild(2).getText()
    #         # print "init code line: " + str(code)
    #
    #     if codeType == PrigogineParser.CodeblockContext:
    #         code = ctx.getChild(2).getChild(1).getText()
    #         # print "init code block: " + str(code)

    #########################

    def enterCreatepopulation(self, ctx):

        populationName = str(ctx.getPayload().ID())
        self.currentPopulation = populationName
        numAgents = int(ctx.getPayload().INT().getText())
        self.modelBuilder.setPopulationSize(populationName, numAgents)
        print "creating " + str(numAgents) + " " + populationName + " agents"

        attributeName = str(ctx.getChild(1).getText())
        codeblock = ctx.getChild(3) #.children
        codeblockString = ""
        blockLen = len(codeblock.children) - 2

        for i in range(blockLen):
            lineNum = i + 1
            codeline = codeblock.children[lineNum]
            expression = codeline.expression()
            tokenInterval = expression.getSourceInterval()

            codelineString = str(self.tokens.getText(tokenInterval))
            codeblockString = codeblockString + codelineString + "\n"
            self.modelBuilder.populationData[populationName]["initialisationData"].append(codelineString)
        print codeblockString
        print "----------"


    #########################

    # def enterInitvar(self, ctx):
    #
    #     codeType = type(ctx.getChild(2))
    #     populationName = self.currentPopulation
    #
    #     if codeType == PrigogineParser.CodelineContext:
    #
    #         attributeName = str(ctx.getChild(1).getText())
    #         codeline = ctx.codeline() # getChild(2)
    #         expression = codeline.expression() # getChild(0)
    #         tokenInterval = expression.getSourceInterval()
    #         codelineString = str(self.tokens.getText(tokenInterval))
    #         self.modelBuilder.populationData[populationName]["attributeData"][attributeName]["code"].append(codelineString)
    #         #print self.model.populations[populationName]["attrs"][attributeName]["code"]
    #         #print "line update " + attributeName + ": " + codelineString
    #         #print codelineString
    #         #print "----------"
    #
    #     if codeType == PrigogineParser.CodeblockContext:
    #         attributeName = str(ctx.getChild(1).getText())
    #         codeblock = ctx.getChild(2) #.children
    #         #tokenInterval = codeblock.getSourceInterval()
    #         #tokenInterval = (tokenInterval[0] + 1, tokenInterval[1] -1) # get rid of 'begin' and 'end' tokens
    #         #codeblockString = str(self.tokens.getText(tokenInterval))
    #         #self.model.populations[populationName]["attrs"][attributeName]["code"].append(codeblockString)
    #
    #         codeblockString = ""
    #         blockLen = len(codeblock.children) - 2
    #
    #         for i in range(blockLen):
    #             lineNum = i + 1
    #             codeline = codeblock.children[lineNum]
    #             expression = codeline.expression()
    #             #print type(codeblock)
    #             tokenInterval = expression.getSourceInterval()
    #
    #             codelineString = str(self.tokens.getText(tokenInterval))
    #             codeblockString = codeblockString + codelineString + "\n"
    #             self.model.populations[populationName]["attrs"][attributeName]["code"].append(codelineString)
    #         #print "block update " + attributeName + ":\n" + codeblockString
    #         print codeblockString
    #         #print self.model.populations[populationName]["attrs"][attributeName]["code"]
    #         print "----------"



###########################################################################################################
###########################################################################################################





