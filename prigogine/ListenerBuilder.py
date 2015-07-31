
from Model import Model
from PrigogineCore import *
from prigogine.parser.PrigogineParser import PrigogineParser
from prigogine.parser.PrigogineParser import PrigogineListener
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

    # @staticmethod
    # def getParameterNames(ctx):
    #     numParams = ctx.parameterlist()[0].getChildCount() - 3
    #     paramList = []
    #     for i in range(numParams):
    #         paramName = ctx.parameterlist()[0].getPayload().getChild(i+2).getText().encode('ascii')
    #         paramName = paramName.replace("\"", "")
    #         paramList.append(paramName)
    #
    #     return paramList

    #########################

    def enterModel(self, ctx):

        modelName = ctx.getChild(1).getText().encode("ascii")
        exec "self.%s = Model()" % modelName
        self.currentModel = modelName

        modelVariables = self.getVariableNames(ctx)
        for variableName in modelVariables:
            exec "self.%(modelName)s.%(variableName)s = None" % \
                 {"modelName" : self.currentModel, "variableName" : variableName}

    #########################

    def exitModel(self, ctx):
        exec "self.model = self.%s" % self.currentModel

    #########################

    def enterPopulation(self, ctx):

        populationName = ctx.getChild(1).getText().encode("ascii")
        self.currentPopulation = populationName

        exec "self.%(currentmodel)s.%(population)s = Population(1, self.%(currentmodel)s)" % \
            {"currentmodel" : self.currentModel, "population" : populationName}

        exec "self.%(currentmodel)s.populations[\"%(population)s\"] = self.%(currentmodel)s.%(population)s" % \
             {"currentmodel" : self.currentModel, "population" : populationName}

        agentVariableNames = self.getVariableNames(ctx)
        for varName in agentVariableNames:
            exec "self.%(currentmodel)s.%(population)s.%(variable)s = None" % \
                 {"currentmodel" : self.currentModel, "population" : populationName, "variable" : varName}

    ########################

    def exitPopulation(self, ctx):
        self.currentPopulation = ""

    ########################

    def enterEquationlist(self, ctx):

        if self.currentPopulation == "": # IF SETTING UP MODEL EQUATIONS

            for equationline in ctx.elementwiseEquation():

                variableName = equationline.getChild(2).getText().encode('ascii') #+ "."
                equationInterval = equationline.expression().getSourceInterval()
                conditionCode = ""

                for child in equationline.children:

                    if type(child) is PrigogineParser.ConditionalContext:
                        conditionInterval = equationline.conditional(0).getSourceInterval()
                        conditionCode = str(self.tokens.getText(conditionInterval))

                    else:
                        conditionCode = "True"

                equationCode = str(self.tokens.getText(equationInterval))
                codeToPass = "update(\"" + variableName + "\", \"" + equationCode + "\", \"" + conditionCode + "\", self.t)"
                exec "self.%(currentmodel)s.updateCode.append('%(codeToPass)s')" % \
                     {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}

        ################################

        if self.currentPopulation != "": # IF SETTING UP POPULATION EQUATIONS

            for equationline in ctx.elementwiseEquation():

                variableName = equationline.getChild(2).getText().encode('ascii') #+ "."
                equationInterval = equationline.expression().getSourceInterval()
                conditionInterval = equationline.conditional(0).getSourceInterval()

                equationCode = str(self.tokens.getText(equationInterval))
                conditionCode = str(self.tokens.getText(conditionInterval))

                codeToPass = "update(\"" + variableName + "\", \"" + equationCode + "\", \"" + conditionCode + "\", self.t)"
                exec "self.%(currentmodel)s.%(population)s.updateCode.append('%(codeToPass)s')" % \
                     {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}

            for equationline in ctx.mapEquation():

                variableName = equationline.getChild(2).getText().encode('ascii')
                equationInterval = equationline.expression().getSourceInterval()
                conditionInterval = equationline.conditional(0).getSourceInterval()

                equationCode = str(self.tokens.getText(equationInterval))
                conditionCode = str(self.tokens.getText(conditionInterval))

                codeToPass = "updateMap(\"" + variableName + "\", \"" + equationCode + "\", \"" + conditionCode + "\", self.t)"
                exec "self.%(currentmodel)s.%(population)s.updateCode.append('%(codeToPass)s')" % \
                     {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}

    #########################
