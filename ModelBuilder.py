
###########################################################################################################
###########################################################################################################

from Model import Model
import numpy as np

###########################################################################################################
###########################################################################################################


class ModelBuilder:

    def __init__(self):
        self.populationData = {}
        self.model = Model()

    @staticmethod
    def buildModel():
        return 0

    def getModel(self):
        print self.populationData
        return self.model

    # def runModel(self, numIterations):
    #     for each in range(numIterations):
    #         print "------------------\niteration number: " + str(self.t) + "\n------------------"
    #         self.updateData()
    #         self.t += 1

    def declarePopulation(self, populationName):
        self.populationData[populationName] = {}
        self.populationData[populationName]["attributeData"] = {}
        self.populationData[populationName]["stateData"] = []
        self.populationData[populationName]["populationSize"] = 0
        self.populationData[populationName]["initialisationData"] = []

    # def createPopulation(self, populationName, numAgents):
    #
    #     for attributeName, val in self.populations[populationName]["attrs"].items(): # instantiate attributes for all agents
    #         self.populations[populationName]["attrs"][attributeName]["data"] = np.zeros((1, numAgents))
    #         #print attributeName
    #
    #     for stateName, val in self.populations[populationName]["states"].items():
    #         self.populations[populationName]["states"][stateName] = np.zeros((1, numAgents))
    #

    def declareAttribute(self, populationName, attrName): # declare that an attibutes exists
         self.populationData[populationName]["attributeData"][attrName] = {}
         self.populationData[populationName]["attributeData"][attrName]["code"] = []

    def declareState(self, populationName, stateName):
         self.populationData[populationName]["stateData"].append(stateName)

    def setPopulationSize(self, populationName, populationSize):
        self.populationData[populationName]["populationSize"] = populationSize

    #def setState(self, populationName, stateName):
    #    self.populationData[populationName]["stateData"].append(stateName)

    #
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


###########################################################################################################
###########################################################################################################

