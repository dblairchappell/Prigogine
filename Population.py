
from numpy import *

class Population:

    #########################

    def __init__(self, populationSize):

        self.populationSize = populationSize
        self.timeStepMem = 100
        self.attributes = {}
        self.stateMasks = {}
        self.updateCode = []
        self.initialisationCode= []
        self.startstate = ""

    #########################

    def addAttribute(self, attributeName):
        self.attributes[attributeName] = zeros((self.timeStepMem, self.populationSize))

    #########################

    def addState(self, stateName):
        self.stateMasks[stateName] = zeros((self.timeStepMem, self.populationSize))

    #########################

    def addUpdateCode(self, codeString):
        self.updateCode.append(codeString)

    #########################

    def addInitialisationCode(self, codeString):
        self.initialisationCode.append(codeString)

    #########################

    def updateAttributes(self, attributes, t):
        for codeline in self.updateCode:
            exec codeline


    #########################

    def initialiseAttributes(self, attributes, t):
        for codeblock in self.initialisationCode:
            exec codeblock

    #########################


