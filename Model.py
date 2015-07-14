
from Population import Population

class Model:

    def __init__(self):
        self.populations = {}
        self.t = 1

    def addPopulation(self, populationName, populationSize):
        self.populations[populationName] = Population(populationSize)

    def addAttribute(self, populationName, attributeName):
        self.populations[populationName].addAttribute(attributeName)


