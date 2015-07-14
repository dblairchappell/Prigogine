
from AttributeArray import AttributeArray

class TimeSeries:

    def __init__(self, attributeName, timeSteps):
        self.attributes = []

    def addAttribute(self, attributeName):
        self.attributes.append(AttributeArray())