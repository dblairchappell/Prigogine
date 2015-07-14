
from Population import Population

class Model:

    def __init__(self):
        self.populations = {}
        self.t = 1

    def incrementTime(self):
        self.t += 1

    def addPopulation(self, populationName, populationSize):
        self.populations[populationName] = Population(populationSize)

    def addAttribute(self, populationName, attributeName):
        self.populations[populationName].addAttribute(attributeName)

    def addState(self, populationName, stateName):
        self.populations[populationName].addState(stateName)

    def updateModel(self):
        for population, val in self.populations:
            attributeArrays = self.populations[population].attributes
            self.populations[population].updateAttributes(attributeArrays, self.t)

    def runModel(self, numIteration):
        print "running model"