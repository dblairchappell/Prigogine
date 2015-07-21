
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
    def getVariableNames(ctx):
        numVars = ctx.variablelist().getPayload().getChildCount() - 3
        varList = []
        for i in range(numVars):
            varName = ctx.variablelist().getPayload().getChild(i+2).getText().encode('ascii')
            varName = varName.replace("\"", "")
            varList.append(varName)
        return varList

    #########################

    @staticmethod
    def getParameterNames(ctx):
        numParams = ctx.parameterlist().getPayload().getChildCount() - 3
        paramList = []
        for i in range(numParams):
            paramName = ctx.parameterlist().getPayload().getChild(i+2).getText().encode('ascii')
            paramName = paramName.replace("\"", "")
            paramList.append(paramName)

        return paramList

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
        #populationName = "\"" + str(populationName) + "\""

        self.currentPopulation = populationName
        self.model.declarePopulation(populationName)

        agentVariableNames = self.getVariableNames(ctx)
        for varName in agentVariableNames:
            varName = "\"" + str(varName) + "\""
            self.model.declareVariable(populationName, varName)

        agentParameterNames = self.getParameterNames(ctx)
        for paramName in agentParameterNames:
            #paramName = "\"" + str(paramName) + "\""
            self.model.declareParameter(populationName, paramName)

        agentStateNames = self.getStateNames(ctx)
        for stateName in agentStateNames:
            #stateName = "\"" + str(stateName) + "\""
            #print stateName
            self.model.addState(populationName, stateName)
            #self.model.addState(populationName, stateName, self.currentStateId)
        #    self.currentStateId += 1

    ########################

    def enterStatedef(self, ctx):
        stateName = ctx.getChild(1).getText().encode("ascii")
        self.currentState = stateName

    ########################

    def enterUpdate(self, ctx):


        codeType = type(ctx.getChild(2)) # detect whether code is in a single line or a block
        populationName = self.currentPopulation
        variableName = ctx.getChild(1).getText().encode("ascii")
        variableName = "\"" + str(variableName) + "\""
        if codeType == PrigogineParser.CodelineContext:
            codeline = ctx.codeline()
            expression = codeline.expression()
            tokenInterval = expression.getSourceInterval()
            codeToPass = str(self.tokens.getText(tokenInterval))
            codelineString = "update(" + variableName + ", "
            codelineString = codelineString + codeToPass + ", getstates(\"" + self.currentPopulation + "\") == \"" + self.currentState + "\")"
            #print codelineString
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

    def enterTransition(self, ctx):

        populationName = self.currentPopulation
        currentState = self.currentState
        targetState = ctx.getChild(1).getText().encode("ascii")
        #targetState = "\"" + str(targetState) + "\""
        guardExpression = ctx.conditional() #.getText()
        tokenInterval = guardExpression.getSourceInterval()
        guardExpressionString = str(self.tokens.getText(tokenInterval))

        codelineString = "transition(\"" + populationName + "\", \"" + targetState + "\", (getstates(\"" + self.currentPopulation + "\") == \"" + self.currentState + "\") * " + guardExpressionString + ")"
        #print codelineString

        self.model.addStateTransitionCode(populationName, codelineString)

    #########################

    def enterInitglobal(self, ctx):

        globalName = ctx.getChild(1).getText().encode("ascii")
        #globalName = "\"" + str(globalName) + "\""
        globalValue =  ctx.getChild(2).getText().encode("ascii")
        self.model.initglobal(globalName, globalValue)
        #print self.model.globals

    #########################

    def enterCreate(self, ctx):

        populationName = ctx.getChild(1).getText().encode("ascii")
        #populationName = "\"" + str(populationName) + "\""
        populationSize = int(ctx.getChild(2).getText())
        self.model.create(populationName, populationSize)
        self.currentPopulation = populationName

    #########################

    def enterInitvars(self, ctx):

        varName = ctx.getChild(1).getText().encode("ascii")
        #varName = "\"" + str(varName) + "\""
        varValue =  ctx.getChild(2).getText().encode("ascii")
        self.model.initvars(self.currentPopulation, varName, varValue)

    #########################

    def enterInitparams(self, ctx):

        paramName = ctx.getChild(1).getText().encode("ascii")
        paramValue =  ctx.getChild(2).getText().encode("ascii")
        self.model.initparams(self.currentPopulation, paramName, paramValue)

    #########################

    def enterInitstates(self, ctx):
        populationName = self.currentPopulation
        states = ctx.getChild(1).getText().encode("ascii")
        self.model.setstates(populationName, states)

    #########################

    def enterFinalise(self, ctx):

        codeblock = ctx.getChild(1)
        codeblockString = ""
        blockLen = len(codeblock.children) - 2
        for i in range(blockLen):
            lineNum = i + 1
            codeline = codeblock.children[lineNum]
            expression = codeline.expression()
            tokenInterval = expression.getSourceInterval()
            codelineString = str(self.tokens.getText(tokenInterval))
            codeblockString = codeblockString + codelineString + "\n"
            self.model.evaluateCode(codeblockString)

    #########################

    def enterRunmodel(self, ctx):

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
            self.model.timeStepCode = codeblockString

        numIterations = int(ctx.getChild(1).getText().encode("ascii"))
        self.model.runModel(numIterations)

    #########################
