
from Population import Population
import numpy as np
import dask.array as da

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

    def addState(self, populationName, stateName, stateId):
        self.populations[populationName].addState(stateName, stateId)

    #########################

    # def addUpdateCode(self, populationName, codeString):
    #     self.populations[populationName].addUpdateCode(codeString)

    def addUpdateCode(self, populationName, stateName, codeString):
        self.populations[populationName].addUpdateCode(stateName, codeString)

    #########################

    def updateModel(self):
        for population in self.populations:

            # check for state transition triggers


            # update attributes
            attributes = self.populations[population].attributes
            self.populations[population].updateAttributes(attributes, self.t)

    #########################

    def runModel(self, numIterations):
        print "-------- running model --------\n"
        itno = 0
        for each in range(numIterations):
            itno +=1
            print ".",
            self.updateModel()
            self.t += 1
            if self.t >= self.timeStepMem:
                self.t = 0
        print "\n\n-------- model run complete  --------\n"

    #########################

    def init(self, populationName, attributeName, value):
        self.populations[populationName].attributes[attributeName] = np.zeros((self.timeStepMem, self.populations[populationName].populationSize))
        #x = np.zeros((self.timeStepMem, self.populations[populationName].populationSize))
        #print x
        #a = da.from_array(x, chunks=(1000, 1000))
        #print a
        #self.populations[populationName].attributes[attributeName] = a
        self.populations[populationName].attributes[attributeName][0] = value

    #########################


