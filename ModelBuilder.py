
from Model import Model
import numpy as np

class ModelBuilder:

    #########################

    def __init__(self):

        self.populationData = {}
        self.model = Model()

    #########################

    @staticmethod
    def buildModel():
        return 0

    #########################

    def getModel(self):
        #for each in self.populationData["households"]["attributeUpdateData"]:
        #    print each
        #    print "---------"

        #print self.populationData["households"]["initialisationData"]
        return self.model

    #########################

    def assembleModelPieces(self):

        for populationName, data in self.populationData.items():
            self.model.addPopulation(populationName, data["populationSize"])

            for attributeName in data["attributeNames"]:
                self.model.addAttribute(populationName, attributeName)

            for codeString in data["initialisationData"]:
                self.model.addInitialisationCode(populationName, codeString)

            for codeString in data["attributeUpdateData"]:
                self.model.addUpdateCode(populationName, codeString)

    #########################

    def declarePopulation(self, populationName):
        self.populationData[populationName] = {}
        self.populationData[populationName]["attributeNames"] = []
        self.populationData[populationName]["stateData"] = []
        self.populationData[populationName]["populationSize"] = 0
        self.populationData[populationName]["initialisationData"] = []
        self.populationData[populationName]["attributeUpdateData"] = []

    #########################

    def declareAttribute(self, populationName, attributeName): # declare that an attibutes exists
         self.populationData[populationName]["attributeNames"].append(attributeName)
         #print self.populationData[populationName]["attributeNames"]
         #self.populationData[populationName]["attributeData"][attrName]["code"] = []

    #########################

    def declareState(self, populationName, stateName):
         self.populationData[populationName]["stateData"].append(stateName)

    #########################

    def setPopulationSize(self, populationName, populationSize):
        self.populationData[populationName]["populationSize"] = populationSize

    #########################

    #def setState(self, populationName, stateName):
    #    self.populationData[populationName]["stateData"].append(stateName)

    #########################

    # def createPopulation(self, populationName, numAgents):
    #
    #     for attributeName, val in self.populations[populationName]["attrs"].items(): # instantiate attributes for all agents
    #         self.populations[populationName]["attrs"][attributeName]["data"] = np.zeros((1, numAgents))
    #         #print attributeName
    #
    #     for stateName, val in self.populations[populationName]["states"].items():
    #         self.populations[populationName]["states"][stateName] = np.zeros((1, numAgents))
    #

    #########################

    # def initAttrsRand(self, populationName, attrName, min, max):
    #     for j in range(len(self.populations[populationName]["attrs"][attrName]["data"][0])):
    #         val = np.random.uniform(min, max)
    #         self.populations[populationName]["attrs"][attrName]["data"][0][j] = val
    #
    # def initAttrsRandInt(self, populationName, attrName, min, max):
    #     for j in range(len(self.populations[populationName]["attrs"][attrName]["data"][0])):
    #         val = np.random.randint(min, max)
    #         self.populations[populationName]["attrs"][attrName]["data"][0][j] = val
    #
    # def random(self, args):
    #     return np.random.uniform(args[0], args[1])

    #########################
