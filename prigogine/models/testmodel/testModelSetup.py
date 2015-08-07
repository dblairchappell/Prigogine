import time
from prigogine.PrigogineCore import *

start = time.clock()
testmodel = prigogine.loadmodel("testModel.prm")

popsize = 10
testmodel.testpop.create(popsize)
testmodel.testpop.testvar[0] = np.ones(popsize)
print testmodel.testpop.testvar[testmodel.readIndex]
for i in range(5):
    testmodel.runModel(1)
    print testmodel.testpop.testvar[testmodel.readIndex]


end = time.clock()
print "\n\ntime elapsed: " + str(end - start) + "s"

