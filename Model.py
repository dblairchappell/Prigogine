
from Population import Population

class Model:

    #########################

    def __init__(self):
        self.populations = {}
        self.timeStepMem = 10
        self.t = 0

    #########################

    def incrementTime(self):
        self.t += 1

    #########################

    def addPopulation(self, populationName, populationSize):
        self.populations[populationName] = Population(populationSize)

    #########################

    def addAttribute(self, populationName, attributeName):
        self.populations[populationName].addAttribute(attributeName)

    #########################

    def addState(self, populationName, stateName):
        self.populations[populationName].addState(stateName)

    #########################

    def addUpdateCode(self, populationName, codeString):
        self.populations[populationName].updateCode.append(codeString)

    #########################

    def addInitialisationCode(self, populationName, codeString):
        self.populations[populationName].initialisationCode.append(codeString)

    #########################

    def updateModel(self):
        for population, val in self.populations.items():
            attributes = self.populations[population].attributes
            self.populations[population].updateAttributes(attributes, self.t)

    #########################

    def runModel(self, numIterations):
        print "running model"
        for each in range(numIterations):
            print "------------------\niteration number: " + str(self.t) + "\n------------------"
            self.updateModel()
            self.t += 1

    #########################


