
from Population import Population

class Model:

    #########################

    def __init__(self):
        self.populations = {}
        self.timeStepMem = 2
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
        for population in self.populations:
            attributes = self.populations[population].attributes
            self.populations[population].updateAttributes(attributes, self.t)

    #########################

    def initialiseModel(self):
        for population in self.populations:
            attributes = self.populations[population].attributes
            self.populations[population].initialiseAttributes(attributes, self.t)

    #########################

    def runModel(self, numIterations):
        print "running model"
        itno = 0
        self.initialiseModel()
        for each in range(numIterations):
            itno +=1
            print "------------------\niteration number: " + str(itno) + "\n------------------"
            self.updateModel()
            self.t += 1
            #print "--------------------------------------------"
            if self.t >= self.timeStepMem:
                self.t = 0

    #########################


