
from ModelBuilder import ModelBuilder
from PrigogineParser import PrigogineParser
from PrigogineListener import PrigogineListener

class ListenerDirector(PrigogineListener):

    #########################

    def __init__(self, tokens):

        self.modelBuilder = ModelBuilder()
        self.tokens = tokens
        self.currentPopulation = ""

    #########################

    def getModel(self):
        self.modelBuilder.assembleModelPieces()
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

    ########################

    def enterAction(self, ctx):

        codeType = type(ctx.getChild(1)) # detect whether code is in a single line or a block
        populationName = self.currentPopulation

        if codeType == PrigogineParser.CodelineContext:

            attributeName = str(ctx.getChild(1).getText())
            codeline = ctx.codeline() # getChild(2)
            expression = codeline.expression() # getChild(0)
            tokenInterval = expression.getSourceInterval()
            codelineString = str(self.tokens.getText(tokenInterval))
            #self.model.populations[populationName]["attrs"][attributeName]["code"].append(codelineString)
            self.modelBuilder.populationData[populationName]["attributeUpdateData"].append(codelineString)
            #print self.model.populations[populationName]["attrs"][attributeName]["code"]
            #print "line update " + attributeName + ": " + codelineString
            #print codelineString
            #print "----------"

        if codeType == PrigogineParser.CodeblockContext:
            attributeName = str(ctx.getChild(1).getText())
            codeblock = ctx.getChild(1) #.children
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

            self.modelBuilder.populationData[populationName]["attributeUpdateData"].append(codeblockString)
            #print self.modelBuilder.populationData[populationName]["attributeUpdateData"]
            #print "----------"

    #########################

    def enterCreatepopulation(self, ctx):

        # create data necessary to instantiate populations

        populationName = str(ctx.getPayload().ID())
        self.currentPopulation = populationName
        numAgents = int(ctx.getPayload().INT().getText())
        self.modelBuilder.setPopulationSize(populationName, numAgents)
        #print "creating " + str(numAgents) + " " + populationName + " agents"

        # create data neccessary to initialise attribute values

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
        #print codeblockString
        #print "----------"

    #########################

    #def assembleModelPieces(self):
    #    self.modelBuilder.assembleModelPieces()

    #########################




