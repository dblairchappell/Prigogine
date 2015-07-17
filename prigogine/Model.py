
from Population import Population
from numpy import *

class Model:

    #########################

    def __init__(self):

        self.modelName = ""
        self.populations = {}
        self.timeStepMem = 2
        self.t = 0
        self.globals = {}

    #########################

    def incrementTime(self):
        self.t += 1

    #########################

    def addModelName(self, modelName):
        self.modelName = modelName

    #########################

    def getModelName(self):
        return self.modelName

    #########################

    def startstate(self, populationName, stateName):
        self.populations[populationName].startState = stateName

    #########################

    def create(self, populationName, populationSize):
        self.populations[populationName].populationSize = populationSize

    #########################

    def declarePopulation(self, populationName):
        self.populations[populationName] = Population(1, self)

    #########################

    def declareAttribute(self, populationName, attributeName):
        self.populations[populationName].declareAttribute(attributeName)

    #########################

    def addState(self, populationName, stateName):
        self.populations[populationName].addState(stateName)

    #########################

    def addUpdateCode(self, populationName, codeString):
        self.populations[populationName].updateCode.append(codeString)

    #########################

    def updateModel(self):
        for population in self.populations:
            attributes = self.populations[population].attributes
            self.populations[population].updateAttributes(attributes, self.t)

    #########################

    def runModel(self, numIterations):
        print "-------- running model --------\n"
        itno = 0
        for each in range(numIterations):
            itno +=1
            #print "------------------\niteration number: " + str(itno) + "\n------------------"
            print str(itno) + ", ",
            self.updateModel()
            self.t += 1
            if self.t >= self.timeStepMem:
                self.t = 0
        print "\n\n-------- model run complete  --------\n"

    #########################

    def init(self, populationName, attributeName, value):
        self.populations[populationName].attributes[attributeName] = value

    #########################


