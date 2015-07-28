
from numpy import *
import numpy.ma as ma
import numpy.core.defchararray as char
class Population:

    #########################

    def __init__(self, populationSize, parentModel):

        self.popsize = populationSize
        self.variables = {'state': None}
        self.parameters = {}
        self.updateCode = []
        self.stateTransitionCode = []
        self.currentstates = []
        self.model = parentModel
        self.calculateNewArray_vect = vectorize(self.calculateNewArray)
        self.variableNames = []
        self.parameterNames = []
        self.t = 0

    #########################

    # def createAgents(self, numAgents):
    #     self.populationSize = numAgents
    #     for variableName in self.variableNames:
    #         exec "self.%(variable)s = zeros(2, %(numAgents)d)" % \
    #              {"variable" : variableName, "numAgents" : self.populationSize}

    #########################

    def init(self, varName, expression):

        exec "self.%s = zeros((2,self.popsize))" % varName

        code = "self.%(varName)s[0] = %(expression)s" % \
             {"varName" : varName, "expression" : expression}
        exec code in globals(), locals()

        code = "self.%(varName)s[1] = %(expression)s" % \
               {"varName" : varName, "expression" : expression}
        exec code in globals(), locals()

    #########################

    def getglobal(self, variableName):
        return self.model.globals[variableName]

    #########################

    def getfrom(self, populationName, variableName, t):
        readIndex = t
        return self.model.populations[populationName].variables[variableName][readIndex]

    #########################

    def getvars(self, variableName, t):
        readIndex = t
        while readIndex >= self.timeStepMem:
            readIndex -= self.timeStepMem
        return self.variables[variableName][readIndex]
        #return exec "self.%s[readIndex]" % variableName

    #########################

    def getparams(self, parameterName):
        #print self.parameters
        return self.parameters[parameterName][0]

    #########################

    def getstates(self, populationName):
        return self.currentstates

    #########################

    def transition(self, populationName, nextState, maskArray):
        #print "next: " + str(nextState) + ", " + str(maskArray)
        for index in where(maskArray)[0]:
            self.currentstates[index] = nextState
        #print self.currentstates
        #print nextState

    #########################

    def evalUpdateCode(self):
        #t = self.model.t
        update = lambda variableName, value, conditionalCheck, t: self.update(variableName, value, conditionalCheck, self.model.t)
        updateMap = lambda variableName, value, conditionalCheck, t: self.updateMap(variableName, value, conditionalCheck, self.model.t)
        #print "executing code"
        #print self.updateCode
        for code in self.updateCode:
            #print code
            exec code in globals(), locals()

    #########################

    @staticmethod
    def calculateNewArray(oldVals, newVals, trueFalse):
        resultArray = oldVals
        #print "result array 1" + str(resultArray)
        #print "trueFalse: " + str(trueFalse)
        for index in where(trueFalse):
            #print index
            resultArray[index] = newVals[index]
        #print "result array 2" + str(resultArray)
        return resultArray

    #########################

    def update(self, variableName, newValues, conditionalCheck, t):

        readIndex = self.model.readIndex
        writeIndex = self.model.writeIndex

        #print readIndex
        #print writeIndex

        t = readIndex
        oldVals = eval("self.%s[readIndex]" % variableName)
        newVals = eval(newValues)
        trueFalse = eval(conditionalCheck)
        #exec "print self.%s" % variableName

        #print trueFalse
        # maskedVals = ma.masked_array(oldVals, mask=~trueFalse)
        # result = maskedVals + newVals - oldVals
        # result.mask = ma.nomask
        #print result
        result = self.calculateNewArray(oldVals, newVals, trueFalse)
        #print result
        exec "self.%(variableName)s[%(writeIndex)d] = result" % \
             {"variableName" : variableName, "result" : result, "writeIndex" : writeIndex} in locals(), globals()


    #########################

    def updateMap(self, variableName, newValue, conditionalCheck, t):

        readIndex = self.model.readIndex
        writeIndex = self.model.writeIndex

        t = readIndex
        oldVals = eval("self.%s[readIndex]" % variableName)
        newVals = eval("self.%s[readIndex].copy()" % variableName)
        newVals.fill(eval(newValue))
        trueFalse = eval(conditionalCheck)
        #print conditionalCheck
        #exec "print self.%s" % variableName

        # maskedVals = ma.masked_array(oldVals, mask=~trueFalse)
        # print maskedVals
        # result = maskedVals + newVals - oldVals
        # result.mask = ma.nomask
        # print result
        #print oldVals
        #print newVals
        #print trueFalse
        result = self.calculateNewArray(oldVals, newVals, trueFalse)
        #print "-----"
        #print result
        #print "-----"
        exec "self.%(variableName)s[%(writeIndex)d] = result" % \
             {"variableName" : variableName, "result" : result, "writeIndex" : writeIndex} in locals(), globals()

    #########################

    def declareVariable(self, variableName):
        self.variables[variableName] = None

    #########################

    def declareParameter(self, parameterName):
        self.parameters[parameterName] = None

    #########################

    def addState(self, stateName):
        self.currentstates.append(stateName)
        #print self.currentstates

    #########################

    def addUpdateCode(self, codeString):
        self.updateCode.append(codeString)

    #########################

    def addStateTransitionCode(self, codeString):
        self.stateTransitionCode.append(codeString)

    #########################

    def updateStates(self, variables, t):

        getvars = lambda variableName : self.getvars(variableName, t)
        getstates = lambda populationName : self.getstates(populationName)
        transition = lambda populationName, nextState, maskArray : self.transition(populationName, nextState, maskArray)
        getparams = lambda parameterName : self.getparams(parameterName)
        getglobal = lambda variableName : self.getglobal(variableName)

        for codeblock in self.stateTransitionCode:
            #print codeblock
            code = compile(codeblock, "<string>", "exec")
            exec code in globals(), locals()

    #########################

    def updateVariables(self, variables, t):

        update = lambda variableName, value, mask : self.update(variableName, value, mask, t)
        getvars = lambda variableName : self.getvars(variableName, t)
        getparams = lambda parameterName : self.getparams(parameterName)
        getglobal = lambda variableName : self.getglobal(variableName)
        getfrom = lambda populationName, variableName : self.getfrom(populationName, variableName, t)
        getstates = lambda populationName : self.getstates(populationName)
        #updateglobal = lambda globalName, value, mask : self.updateglobal(globalName, value, mask)

        for codeblock in self.updateCode:
            #print codeblock
            code = compile(codeblock, "<string>", "exec")
            exec code in globals(), locals()

    #########################


