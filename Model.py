
from Population import Population
from TaskScheduler import TaskScheduler
from numpy import *

class Model:

    #########################

    def __init__(self):

        self.modelName = ""
        #self.initialisationCode = []
        self.taskScheduler = TaskScheduler()
        self.populations = {}
        self.timeStepMem = 2
        self.t = 0

    #########################

    def incrementTime(self):
        self.t += 1

    #########################

    def addModelName(self, modelName):
        self.modelName = modelName

    def getModelName(self):
        return self.modelName

    #########################

    def startstate(self, populationName, stateName):
        self.populations[populationName].startState = stateName

    #########################

    def create(self, populationName, populationSize):
        self.populations[populationName].populationSize = populationSize
        print "population size"
        print self.populations[populationName].populationSize

    #########################

    def declarePopulation(self, populationName):
        self.populations[populationName] = Population(1)

    #########################

    def addAttribute(self, populationName, attributeName):
        self.populations[populationName].addAttribute(attributeName)
        print "adding attributes"

    #########################

    def addState(self, populationName, stateName):
        self.populations[populationName].addState(stateName)

    #########################

    def addUpdateCode(self, populationName, codeString):
        self.populations[populationName].updateCode.append(codeString)

    #########################

    # def addInitialisationCode(self, modelName, codeString):
    #     self.initialisationCode.append(codeString)

    #########################

    def updateModel(self):
        for population in self.populations:
            attributes = self.populations[population].attributes
            self.populations[population].updateAttributes(attributes, self.t)

    #########################

    def runModel(self, numIterations):
        print "running model"
        print self.populations["households"].attributes
        print self.populations["households"].attributes["reserveWages"]
        itno = 0
        #self.initialiseModel()
        for each in range(numIterations):
            itno +=1
            print "------------------\niteration number: " + str(itno) + "\n------------------"
            self.updateModel()
            self.t += 1
            #print "--------------------------------------------"
            if self.t >= self.timeStepMem:
                self.t = 0

    #########################

    # def startstateDef(self, populationName, statename):
    #     self.populations[populationName].startstate = statename
    #
    # #########################
    #
    def init(self, populationName, attributeName, value):
        print "init def"
        print attributeName
        print type(attributeName)
        print self.populations["households"].attributes
        print self.populations[populationName].attributes

        self.populations[populationName].attributes[attributeName] = value
    #
    # #########################
    #
    # def initialiseModel(self):
    #     print "initialiseModel()"
    #     print self.populations["households"].attributes
    #     create = lambda populationName, numAgents : self.addPopulation(populationName, numAgents)
    #     runmodel = lambda numIterations : self.runModel(numIterations)
    #     startstate = lambda populationName, statename : self.startstateDef(populationName, statename)
    #     init = lambda populationName, attributeName, value : self.initDef(populationName, attributeName, value)
    #
    #     for codeblock in self.initialisationCode:
    #         code = compile(codeblock, "<string>", "exec")
    #         exec code in globals(), locals()

        #for population in self.populations:
        #    attributes = self.populations[population].attributes
        #    self.populations[population].initialiseAttributes(attributes, self.t)

    #########################


