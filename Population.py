
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

    # def get(self, attributeName, timestamp):
    #     print self.timeStepMem - 1
    #     if timestamp >= self.timeStepMem - 1:
    #         timestamp = timestamp - self.timeStepMem
    #     print timestamp
    #     return self.attributes[str(attributeName)][timestamp]

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
        get = lambda attributeName, timeStamp : attributes[str(attributeName)][timeStamp]
        for codeblock in self.updateCode:
            #print codeblock
            code = compile(codeblock, "<string>", "exec")
            exec code in globals(), locals()
            #print "====="

    #########################

    def initialiseAttributes(self, attributes, t):
        for codeblock in self.initialisationCode:
            exec codeblock

    #########################


