
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
        numAttrs = ctx.variablelist().getPayload().getChildCount() - 3
        attrList = []
        for i in range(numAttrs):
            attrName = ctx.variablelist().getPayload().getChild(i+2).getText().encode('ascii')
            attrName = attrName.replace("\"", "")
            attrList.append(attrName)
        return attrList

    #########################

    @staticmethod
    def getStateNames(ctx):
        stateList = []
        for state in ctx.statedef():
            stateNameString = state.getPayload().getChild(1).getText().encode('ascii')
            stateNameString = stateNameString.replace("\"", "")
            stateList.append(stateNameString)
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
            self.model.addState(populationName, stateName)
            #self.model.addState(populationName, stateName, self.currentStateId)
        #    self.currentStateId += 1

    ########################

    def enterStatedef(self, ctx):
        stateName = ctx.getChild(1).getText().encode("ascii")
        stateName = stateName.replace("\"", "")
        self.currentState = stateName

    ########################

    def enterUpdate(self, ctx):


        codeType = type(ctx.getChild(2)) # detect whether code is in a single line or a block
        populationName = self.currentPopulation
        attributeName = ctx.getChild(1).getText().encode("ascii")

        if codeType == PrigogineParser.CodelineContext:
            codeline = ctx.codeline()
            expression = codeline.expression()
            tokenInterval = expression.getSourceInterval()
            codeToPass = str(self.tokens.getText(tokenInterval))
            codelineString = "update(" + attributeName + ", "
            codelineString = codelineString + codeToPass + ", getstates(\"" + self.currentPopulation + "\") == \"" + self.currentState + "\")"
            self.model.addUpdateCode(populationName, codelineString)


        if codeType == PrigogineParser.CodeblockContext:

            codeblock = ctx.getChild(2)
            codeblockString = ""
            blockLen = len(codeblock.children) - 2
            for i in range(blockLen):
                lineNum = i + 1
                codeline = codeblock.children[lineNum]
                expression = codeline.expression()
                tokenInterval = expression.getSourceInterval()
                codelineString = str(self.tokens.getText(tokenInterval))
                codeblockString = codeblockString + codelineString + "\n"
            self.model.addUpdateCode(populationName, self.currentState, codeblockString)

    #########################





