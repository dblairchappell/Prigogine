
from numpy import *

class Population:

    def __init__(self, populationSize):

        self.populationSize = populationSize
        self.timeStepMem = 10
        self.attributes = {}
        self.stateMasks = {}
        self.codeToEval = []

    def addAttribute(self, attributeName):
        self.attributes[attributeName] = zeros((self.timeStepMem, self.populationSize))

    def addState(self, stateName):
        self.stateMasks[stateName] = zeros((self.timeStepMem, self.populationSize))

    def updateAttributes(self, attributes, t):
        for codeline in self.codeToEval:
            exec codeline



