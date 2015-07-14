
from TimeSeries import TimeSeries

class Population:

    def __init__(self, populationSize):
        
        self.populationSize = populationSize
        self.timeSteps = 2
        self.timeSeries = {}
        self.t = 1

    def addAttribute(self, attributeName):
        self.timeSeries[attributeName] = TimeSeries(attributeName, self.timeSteps)


