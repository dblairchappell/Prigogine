
import numpy as np
from AttributeArray import AttributeArray

class TimeSeries:

    def __init__(self, attributeName, timeSteps):

        self.timestep = np.ones(timeSteps)

        for t in self.timestep:
            self.addAttribute(attributeName)

    def addAttribute(self, attributeName):
        self.timestep.append(AttributeArray())


