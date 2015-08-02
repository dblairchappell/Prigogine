
from Model import Model
from PrigogineCore import *
from prigogine.parser.PrigogineParser import PrigogineParser
from prigogine.parser.PrigogineParser import PrigogineListener
from Population import Population
import numpy as np

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

    def enterModel(self, ctx):

        modelName = ctx.getChild(1).getText().encode("ascii")
        exec "self.%s = Model()" % modelName
        self.currentModel = modelName

        modelVariables = self.getVariableNames(ctx)
        for variableName in modelVariables:

            exec "self.%(modelName)s.variables.append(\"%(variableName)s\")" % \
                 {"modelName" : self.currentModel, "variableName" : variableName}

            exec "self.%(modelName)s.%(variableName)s = None" % \
                 {"modelName" : self.currentModel, "variableName" : variableName}

            exec "self.%(modelName)s.%(variable)s = np.zeros(2)" % \
                 {"modelName" : self.currentModel, "variable" : variableName}

    #########################

    def exitModel(self, ctx):
        exec "self.model = self.%s" % self.currentModel

    #########################

    def enterPopulation(self, ctx):

        populationName = ctx.getChild(1).getText().encode("ascii")
        self.currentPopulation = populationName

        exec "self.%(currentmodel)s.%(population)s = Population(self.%(currentmodel)s)" % \
            {"currentmodel" : self.currentModel, "population" : populationName}

        exec "self.%(currentmodel)s.populations[\"%(population)s\"] = self.%(currentmodel)s.%(population)s" % \
             {"currentmodel" : self.currentModel, "population" : populationName}

        agentVariableNames = self.getVariableNames(ctx)

        for varName in agentVariableNames:
            exec "self.%(currentmodel)s.%(population)s.variables.append(\"%(variable)s\")" % \
                {"currentmodel" : self.currentModel, "population" : populationName, "variable" : varName}

            exec "self.%(currentmodel)s.%(population)s.%(variable)s = None" % \
                 {"currentmodel" : self.currentModel, "population" : populationName, "variable" : varName}

    ########################

    def exitPopulation(self, ctx):
        self.currentPopulation = ""

    ########################

    def enterEquationlist(self, ctx):

        if self.currentPopulation == "": # IF SETTING UP MODEL EQUATIONS

            for equationline in ctx.elementwiseEquation():

                variableName = equationline.getChild(0).getText().encode('ascii') #+ "."
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
                #print codeToPass

        ################################

        if self.currentPopulation != "": # IF SETTING UP POPULATION EQUATIONS

            for equationline in ctx.elementwiseEquation():

                variableName = equationline.getChild(0).getText().encode('ascii') #+ "."
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
                exec "self.%(currentmodel)s.%(population)s.updateCode.append('%(codeToPass)s')" % \
                     {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}
                #print codeToPass

            for equationline in ctx.mapEquation():

                variableName = equationline.getChild(0).getText().encode('ascii')
                equationInterval = equationline.expression().getSourceInterval()
                conditionInterval = equationline.conditional(0).getSourceInterval()

                equationCode = str(self.tokens.getText(equationInterval))
                conditionCode = str(self.tokens.getText(conditionInterval))

                codeToPass = "updateMap(\"" + variableName + "\", \"" + equationCode + "\", \"" + conditionCode + "\", self.t)"
                exec "self.%(currentmodel)s.%(population)s.updateCode.append('%(codeToPass)s')" % \
                     {"currentmodel" : self.currentModel, "population" : self.currentPopulation, "codeToPass" : codeToPass}
                print codeToPass

    #########################

    # def enterIndexedvariable(self, ctx):
    #     print type(ctx.getChild(0))
    #     print ctx.getChild(1).getText()