
from Model import Model
from parser.PrigogineParser import PrigogineParser
from parser.PrigogineListener import PrigogineListener

class ListenerBuilder(PrigogineListener):

    #########################

    def __init__(self, tokens):
        self.model = Model()
        self.tokens = tokens
        self.currentPopulation = ""
        self.currentModel = ""
        self.currentState = ""
        self.currentStateId = 0

    #########################

    def getModel(self):
        return self.model

    #########################

    @staticmethod
    def getAttributeNames(ctx):
        numAttrs = ctx.attributelist().getPayload().getChildCount() - 3
        attrList = []
        for i in range(numAttrs):
            attrName = ctx.attributelist().getPayload().getChild(i+2).getText().encode('ascii')
            attrName = attrName.replace("\"", "")
            attrList.append(attrName)
        return attrList

    #########################

    @staticmethod
    def getStateNames(ctx):
        stateList = []
        for state in ctx.statedef():
            #print state.getPayload().getChild(1).getText()
            stateNameString = state.getPayload().getChild(1).getText().encode('ascii')
            stateNameString = stateNameString.replace("\"", "")
            stateList.append(stateNameString)
        #print "states: ",
        #print stateList
        return stateList

    #########################

    def enterPopulation(self, ctx):

        populationName = ctx.getChild(1).getText().encode("ascii")
        populationName = populationName.replace("\"", "")
        self.currentPopulation = populationName
        self.model.declarePopulation(populationName)

        agentAttributeNames = self.getAttributeNames(ctx)
        for attrName in agentAttributeNames:
            self.model.declareAttribute(populationName, attrName)

        agentStateNames = self.getStateNames(ctx)
        for stateName in agentStateNames:
            self.model.addState(populationName, stateName, self.currentStateId)
            self.currentStateId += 1

    ########################

    def enterStatedef(self, ctx):
        stateNameString = ctx.getChild(1).getText().encode("ascii")
        stateNameString = stateNameString.replace("\"", "")
        self.currentState = stateNameString

        #print "current state: " + self.currentState

        # for child in ctx.children:
        #     print type(child.getChild(0))
        #     print child.getText()
        #     print "---------------------"

    ########################

    def enterAction(self, ctx):

        #print "current state: " + self.currentState
        codeType = type(ctx.getChild(1)) # detect whether code is in a single line or a block
        populationName = self.currentPopulation

        if codeType == PrigogineParser.CodelineContext:
            #attributeName = str(ctx.getChild(1).getText())
            codeline = ctx.codeline() # getChild(2)
            expression = codeline.expression() # getChild(0)
            tokenInterval = expression.getSourceInterval()
            codelineString = str(self.tokens.getText(tokenInterval))
            #self.model.addUpdateCode(populationName, codelineString)
            self.model.addUpdateCode(populationName, self.currentState, codelineString)


        if codeType == PrigogineParser.CodeblockContext:

            codeblock = ctx.getChild(1) #.children
            codeblockString = ""
            blockLen = len(codeblock.children) - 2

            for i in range(blockLen):
                lineNum = i + 1
                codeline = codeblock.children[lineNum]
                expression = codeline.expression()
                tokenInterval = expression.getSourceInterval()
                codelineString = str(self.tokens.getText(tokenInterval))
                codeblockString = codeblockString + codelineString + "\n"

            #self.model.addUpdateCode(populationName, codeblockString)
            self.model.addUpdateCode(populationName, self.currentState, codeblockString)

    #########################





