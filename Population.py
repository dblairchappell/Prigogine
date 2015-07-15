
from numpy import *

class Population:

    #########################

    def __init__(self, populationSize):

        self.populationSize = populationSize
        self.timeStepMem = 10
        self.attributes = {}
        self.stateMasks = {}
        self.updateCode = []
        self.initialisationCode= []
        self.startstate = ""

    #########################

    def startstateDef(self, statename):
        print statename

    def getDef(self, attributeName, t):
        return self.attributes[attributeName][t]

    def updateDef(self, attributeName, newValue, t):
        self.attributes[attributeName][t] = newValue

    def initDef(self, attributeName, value):
        self.attributes[attributeName][0] = value

    #########################

    def addAttribute(self, attributeName):
        self.attributes[attributeName] = zeros((self.timeStepMem, self.populationSize))
        #self.attributes[attributeName] = zeros((self.populationSize + 1, self.populationSize))

    #########################

    def addState(self, stateName):
        self.stateMasks[stateName] = zeros((self.timeStepMem, self.populationSize))
        #self.stateMasks[stateName] = zeros((self.populationSize + 1, self.populationSize))

    #########################

    def addUpdateCode(self, codeString):
        self.updateCode.append(codeString)

    #########################

    def addInitialisationCode(self, codeString):
        self.initialisationCode.append(codeString)

    #########################

    def updateAttributes(self, attributes, t):
        update = lambda attributeName, value : self.updateDef(attributeName, value, t)
        get = lambda attributeName : self.getDef(attributeName, t)
        for codeblock in self.updateCode:
            #print codeblock
            code = compile(codeblock, "<string>", "exec")
            exec code in globals(), locals()
            #print "====="

    #########################

    def initialiseAttributes(self, attributes, t):
        startstate = lambda statename : self.startstateDef(statename)
        init = lambda attributeName, value : self.initDef(attributeName, value)
        for codeblock in self.initialisationCode:
            code = compile(codeblock, "<string>", "exec")
            exec code in globals(), locals()

    #########################


