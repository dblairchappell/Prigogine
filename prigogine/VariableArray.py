__author__ = 'David'

import numpy as np

class VariableArray:

    #########################

    def __init__(self):

        self.variableName = ""
        self.data = None
        self.popsize = 0

    def init_choice(self, choiceArray, probabilityArray):

        code = "self.data[0] = np.random.choice(%(choiceArray)s, %(popsize)s, p=%(probabilityArray)s)" % \
               {"choiceArray" : choiceArray, "probabilityArray" : probabilityArray, "popsize" : self.popsize}
        exec code in globals(), locals()

        code = "self.data[1] = np.random.choice(%(choiceArray)s, %(popsize)s, p=%(probabilityArray)s)" % \
               {"choiceArray" : choiceArray, "probabilityArray" : probabilityArray, "popsize" : self.popsize}
        exec code in globals(), locals()

    def init_randint(self, range):

        code = "self.data[0] = np.random.randint(%(range)s, size=%(popsize)s)" % \
               {"range" : range, "popsize" : self.popsize}
        exec code in globals(), locals()

        code = "self.data[1] = np.random.randint(%(range)s, size=%(popsize)s)" % \
               {"range" : range, "popsize" : self.popsize}
        exec code in globals(), locals()

    def init(self, value):

        code = "self.data[0] = np.ones(%(popsize)s) * %(value)s" % \
               {"value" : value, "popsize" : self.popsize}
        exec code in globals(), locals()

        code = "self.data[1] = np.ones(%(popsize)s) * %(value)s" % \
               {"value" : value, "popsize" : self.popsize}
        exec code in globals(), locals()