
###########################################################################################################
###########################################################################################################

import numpy as np

###########################################################################################################
###########################################################################################################


class ModelBuilder:

    def __init__(self):
        self.populations = {}
        self.t = 1

    def updateData(self):
        for populationName,val in self.populations.items():
            for attributeName, val in self.populations[populationName]["attrs"].items():
                print attributeName
                codeToEval = self.populations[populationName]["attrs"][attributeName]["code"]
                for code in codeToEval:
                    exec code

    def runModel(self, numIterations):
        for each in range(numIterations):
            print "------------------\niteration number: " + str(self.t) + "\n------------------"
            self.updateData()
            self.t += 1

    def addPopulation(self, populationName):
        self.populations[populationName] = {}
        self.populations[populationName]["attrs"] = {}
        self.populations[populationName]["states"] = {}


    def createPopulation(self, populationName, numAgents):

        for attributeName, val in self.populations[populationName]["attrs"].items(): # instantiate attributes for all agents
            self.populations[populationName]["attrs"][attributeName]["data"] = np.zeros((1, numAgents))
            #print attributeName

        for stateName, val in self.populations[populationName]["states"].items():
            self.populations[populationName]["states"][stateName] = np.zeros((1, numAgents))

    def addAttribute(self, populationName, attrName): # declare that an attibutes exists
        self.populations[populationName]["attrs"][attrName] = {}
        self.populations[populationName]["attrs"][attrName]["code"] = []
        self.populations[populationName]["attrs"][attrName]["data"] = np.zeros((1, 1))


    def addState(self, populationName, stateName):
        self.populations[populationName]["states"][stateName] = np.zeros((1, 1))

    def initAttrsRand(self, populationName, attrName, min, max):
        for j in range(len(self.populations[populationName]["attrs"][attrName]["data"][0])):
            val = np.random.uniform(min, max)
            self.populations[populationName]["attrs"][attrName]["data"][0][j] = val

    def initAttrsRandInt(self, populationName, attrName, min, max):
        for j in range(len(self.populations[populationName]["attrs"][attrName]["data"][0])):
            val = np.random.randint(min, max)
            self.populations[populationName]["attrs"][attrName]["data"][0][j] = val

    def random(self, args):
        return np.random.uniform(args[0], args[1])


###########################################################################################################
###########################################################################################################

