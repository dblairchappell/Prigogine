
from Model import Model
from parser.PrigogineParser import PrigogineParser
from parser.PrigogineListener import PrigogineListener
from Population import Population
from numpy import *

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
        numParams = ctx.parameterlist()[0].getChildCount() - 3
        paramList = []
        for i in range(numParams):
            paramName = ctx.parameterlist()[0].getPayload().getChild(i+2).getText().encode('ascii')
            paramName = paramName.replace("\"", "")
            paramList.append(paramName)

        return paramList

    #########################

    def enterModel(self, ctx):

        modelName = ctx.getChild(1).getText().encode("ascii")
        exec "self.%s = Model()" % modelName
        #self.model.modelName = modelName
        self.currentModel = modelName

        modelVariables = self.getVariableNames(ctx)
        for variableName in modelVariables:

            # exec "self.%(currentmodel)s.variableNames.append("+ variableName +" )" % \
            #      {"currentmodel" : self.currentModel}

            exec "self.%(modelName)s.%(variableName)s = None" % \
                 {"modelName" : self.currentModel, "variableName" : variableName}
            #print variableName

        modelParameters = self.getParameterNames(ctx)
        for parameter in modelParameters:

            # exec "self.%(currentmodel)s.parameterNames.append(%(parameter)s)" % \
            #      {"currentmodel" : self.currentModel, "parameter" : parameter}

            exec "self.%(modelName)s.%(parameterName)s = None" % \
                 {"modelName" : self.currentModel, "parameterName" : parameter}
            #print parameter

    def exitModel(self, ctx):
        exec "self.model = self.%s" % self.currentModel

    #########################

    # def exitModel(self, ctx):
    #     print self.labourmarket.households.reserveWages

    #########################

    def enterPopulation(self, ctx):

        populationName = ctx.getChild(1).getText().encode("ascii")
        #print populationName
        self.currentPopulation = populationName
        exec "self.%(currentmodel)s.%(population)s = Population(1, self.%(currentmodel)s)" % \
            {"currentmodel" : self.currentModel, "population" : populationName}

        exec "self.%(currentmodel)s.populations[\"%(population)s\"] = self.%(currentmodel)s.%(population)s" % \
             {"currentmodel" : self.currentModel, "population" : populationName}

        agentParameterNames = self.getParameterNames(ctx)
        for paramName in agentParameterNames:

            # exec "self.%(currentmodel)s.%(population)s.parameterNames.append(%(parameter)s)" % \
            #     {"currentmodel" : self.currentModel, "population" : populationName, "parameter" : paramName}

            exec "self.%(currentmodel)s.%(population)s.%(parameter)s = None" % \
                {"currentmodel" : self.currentModel, "population" : populationName, "parameter" : paramName}

        agentVariableNames = self.getVariableNames(ctx)
        for varName in agentVariableNames:

            # exec "self.%(currentmodel)s.%(population)s.variableNames.append(%(variable)s)" % \
            #      {"currentmodel" : self.currentModel, "population" : populationName, "variable" : varName}

            exec "self.%(currentmodel)s.%(population)s.%(variable)s = None" % \
                 {"currentmodel" : self.currentModel, "population" : populationName, "variable" : varName}

    ########################

    def exitPopulation(self, ctx):
        self.currentPopulation = ""

    ########################

    def enterEquationlist(self, ctx):

        #print self.currentModel
        #print self.currentPopulation

        if self.currentPopulation != "": # IF SETTING UP POPULATION EQUATIONS

            for equationline in ctx.elementwiseEquation():
                #print "EW equation"
                variableName = equationline.getChild(2).getText().encode('ascii') #+ "."
                equationInterval = equationline.expression().getSourceInterval()
                conditionInterval = equationline.conditional(0).getSourceInterval()

                equationCode = str(self.tokens.getText(equationInterval))
                conditionCode = str(self.tokens.getText(conditionInterval))

                codeToPass = "update(\"" + variableName + "\", \"" + equationCode + "\", \"" + conditionCode + "\", self.t)"
                exec "self.%(currentmodel)s.%(population)s.updateCode.append('%(codeToPass)s')" % \
                     {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}

            for equationline in ctx.mapEquation():
                #print "map equation"

                variableName = equationline.getChild(2).getText().encode('ascii')
                equationInterval = equationline.expression().getSourceInterval()
                conditionInterval = equationline.conditional(0).getSourceInterval()

                equationCode = str(self.tokens.getText(equationInterval))
                conditionCode = str(self.tokens.getText(conditionInterval))

                codeToPass = "updateMap(\"" + variableName + "\", \"" + equationCode + "\", \"" + conditionCode + "\", self.t)"
                #print codeToPass
                exec "self.%(currentmodel)s.%(population)s.updateCode.append('%(codeToPass)s')" % \
                     {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}

        ################################

        if self.currentPopulation == "": # IF SETTING UP MODEL EQUATIONS

            for equationline in ctx.elementwiseEquation():

                #print "MODEL BASED EQUATION"
                variableName = equationline.getChild(2).getText().encode('ascii') #+ "."
                equationInterval = equationline.expression().getSourceInterval()

                for child in equationline.children:

                    if type(child) is PrigogineParser.ConditionalContext:

                        conditionInterval = equationline.conditional(0).getSourceInterval()

                        equationCode = str(self.tokens.getText(equationInterval))
                        conditionCode = str(self.tokens.getText(conditionInterval))

                    else:
                        conditionCode = "True"

                equationCode = str(self.tokens.getText(equationInterval))
                codeToPass = "update(\"" + variableName + "\", \"" + equationCode + "\", \"" + conditionCode + "\", self.t)"
                exec "self.%(currentmodel)s.updateCode.append('%(codeToPass)s')" % \
                        {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}


                # codeToPass = "update(\"" + variableName + "\", \"" + equationCode + "\", \"True\", self.model.t)"
                # print codeToPass
                # exec "self.%(currentmodel)s.updateCode.append('%(codeToPass)s')" % \
                #         {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}

            # for equationline in ctx.mapEquation():
            #     print "map equation"
            #
            #     variableName = equationline.getChild(2).getText().encode('ascii')
            #     equationInterval = equationline.expression().getSourceInterval()
            #     conditionInterval = equationline.conditional(0).getSourceInterval()
            #
            #     equationCode = str(self.tokens.getText(equationInterval))
            #     conditionCode = str(self.tokens.getText(conditionInterval))
            #
            #     codeToPass = "updateMap(\"" + variableName + "\", \"" + equationCode + "\", \"" + conditionCode + "\", self.model.t)"
            #     print codeToPass
            #     exec "self.%(currentmodel)s.%(population)s.updateCode.append('%(codeToPass)s')" % \
            #          {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}

    ########################

    # def enterStatedef(self, ctx):
    #     stateName = ctx.getChild(1).getText().encode("ascii")
    #     self.currentState = stateName

    ########################

    # def enterUpdate(self, ctx):
    #
    #     codeType = type(ctx.getChild(2)) # detect whether code is in a single line or a block
    #     populationName = self.currentPopulation
    #     variableName = ctx.getChild(1).getText().encode("ascii")
    #     variableName = "\"" + str(variableName) + "\""
    #     if codeType == PrigogineParser.CodelineContext:
    #         codeline = ctx.codeline()
    #         expression = codeline.expression()
    #         tokenInterval = expression.getSourceInterval()
    #         codeToPass = str(self.tokens.getText(tokenInterval))
    #         codelineString = "update(" + variableName + ", "
    #         codelineString = codelineString + codeToPass + ", getstates(\"" + self.currentPopulation + "\") == \"" + self.currentState + "\")"
    #         #print codelineString
    #         self.model.addUpdateCode(populationName, codelineString)
    #
    #
    #     if codeType == PrigogineParser.CodeblockContext:
    #
    #         codeblock = ctx.getChild(2)
    #         codeblockString = ""
    #         blockLen = len(codeblock.children) - 2
    #         for i in range(blockLen):
    #             lineNum = i + 1
    #             codeline = codeblock.children[lineNum]
    #             expression = codeline.expression()
    #             tokenInterval = expression.getSourceInterval()
    #             codelineString = str(self.tokens.getText(tokenInterval))
    #             codeblockString = codeblockString + codelineString + "\n"
    #         self.model.addUpdateCode(populationName, self.currentState, codeblockString)

    #########################

    # def enterTransition(self, ctx):
    #
    #     populationName = self.currentPopulation
    #     currentState = self.currentState
    #     targetState = ctx.getChild(1).getText().encode("ascii")
    #     #targetState = "\"" + str(targetState) + "\""
    #     guardExpression = ctx.conditional() #.getText()
    #     tokenInterval = guardExpression.getSourceInterval()
    #     guardExpressionString = str(self.tokens.getText(tokenInterval))
    #
    #     codelineString = "transition(\"" + populationName + "\", \"" + targetState + "\", (getstates(\"" + self.currentPopulation + "\") == \"" + self.currentState + "\") * " + guardExpressionString + ")"
    #     #print codelineString
    #
    #     self.model.addStateTransitionCode(populationName, codelineString)

    #########################

    # def enterInitglobal(self, ctx):
    #
    #     globalName = ctx.getChild(1).getText().encode("ascii")
    #     #globalName = "\"" + str(globalName) + "\""
    #     globalValue =  ctx.getChild(2).getText().encode("ascii")
    #     self.model.initglobal(globalName, globalValue)
        #print self.model.globals

    #########################

    # def enterCreate(self, ctx):
    #     #print "entering create"
    #     populationName = ctx.getChild(1).getText().encode("ascii")
    #     #populationName = "\"" + str(populationName) + "\""
    #     populationSize = int(ctx.getChild(2).getText())
    #     self.model.create(populationName, populationSize)
    #     self.currentPopulation = populationName
    #
    # #########################
    #
    # def enterInitvars(self, ctx):
    #
    #     varName = ctx.getChild(1).getText().encode("ascii")
    #     #varName = "\"" + str(varName) + "\""
    #     varValue =  ctx.getChild(2).getText().encode("ascii")
    #     self.model.initvars(self.currentPopulation, varName, varValue)
    #
    # #########################
    #
    # def enterInitparams(self, ctx):
    #
    #     paramName = ctx.getChild(1).getText().encode("ascii")
    #     paramValue =  ctx.getChild(2).getText().encode("ascii")
    #     self.model.initparams(self.currentPopulation, paramName, paramValue)

    #########################

    # def enterInitglobal(self, ctx):
    #
    #     globalName = ctx.getChild(1).getText().encode("ascii")
    #     #varName = "\"" + str(varName) + "\""
    #     globalValue =  ctx.getChild(2).getText().encode("ascii")
    #     self.model.initglobal(globalName, globalValue)

    #########################

    # def enterUpdateglobal(self, ctx):
    #
    #     codeType = type(ctx.getChild(2)) # detect whether code is in a single line or a block
    #     populationName = self.currentPopulation
    #     globalName = ctx.getChild(1).getText().encode("ascii")
    #     globalName = "\"" + str(globalName) + "\""
    #
    #     if codeType == PrigogineParser.CodelineContext:
    #         codeline = ctx.codeline()
    #         expression = codeline.expression()
    #         tokenInterval = expression.getSourceInterval()
    #         codeToPass = str(self.tokens.getText(tokenInterval))
    #         codelineString = "updateglobal(" + globalName + ", " + codeToPass + ", getstates(\"" + self.currentPopulation + "\") == \"" + self.currentState + "\")"
    #         #print codelineString
    #         self.model.addUpdateCode(populationName, codelineString)
    #
    #
    #     if codeType == PrigogineParser.CodeblockContext:
    #
    #         codeblock = ctx.getChild(2)
    #         codeblockString = ""
    #         blockLen = len(codeblock.children) - 2
    #         for i in range(blockLen):
    #             lineNum = i + 1
    #             codeline = codeblock.children[lineNum]
    #             expression = codeline.expression()
    #             tokenInterval = expression.getSourceInterval()
    #             codelineString = str(self.tokens.getText(tokenInterval))
    #             codeblockString = codeblockString + codelineString + "\n"
    #         self.model.addUpdateCode(populationName, self.currentState, codeblockString)
    #
    # #########################
    #
    # def enterInitstates(self, ctx):
    #     populationName = self.currentPopulation
    #     states = ctx.getChild(1).getText().encode("ascii")
    #     self.model.setstates(populationName, states)
    #
    # #########################
    #
    # def enterFinalise(self, ctx):
    #
    #     codeblock = ctx.getChild(1)
    #     codeblockString = ""
    #     blockLen = len(codeblock.children) - 2
    #     for i in range(blockLen):
    #         lineNum = i + 1
    #         codeline = codeblock.children[lineNum]
    #         expression = codeline.expression()
    #         tokenInterval = expression.getSourceInterval()
    #         codelineString = str(self.tokens.getText(tokenInterval))
    #         codeblockString = codeblockString + codelineString + "\n"
    #         self.model.evaluateCode(codeblockString)
    #
    # #########################
    #
    # def exitRunmodel(self, ctx):
    #
    #     # codeblock = ctx.getChild(2)
    #     # codeblockString = ""
    #     # blockLen = len(codeblock.children) - 2
    #     # for i in range(blockLen):
    #     #     lineNum = i + 1
    #     #     codeline = codeblock.children[lineNum]
    #     #     expression = codeline.expression()
    #     #     tokenInterval = expression.getSourceInterval()
    #     #     codelineString = str(self.tokens.getText(tokenInterval))
    #     #     codeblockString = codeblockString + codelineString + "\n"
    #     #     self.model.timeStepCode = codeblockString
    #     #print "running..."
    #     numIterations = int(ctx.getChild(1).getText().encode("ascii"))
    #     self.model.runModel(numIterations)

    #########################
