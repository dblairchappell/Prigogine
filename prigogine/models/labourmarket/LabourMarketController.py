import time
from prigogine.Prigogine import *
from numpy import *
from matplotlib.pyplot import *

start = time.clock()

meanReserveWages = []
meanWeeksEmployed = []
meanMinWages = []

labourmarket = prigogine.loadmodel("LabourMarketNew.prm")
labourmarket.households.popsize = 10000

labourmarket.households.init("states", "random.choice([1, 0], size=self.popsize, p=[0.5,0.5])")
labourmarket.households.init("reserveWages", "random.randint(100, size=self.popsize)")
labourmarket.households.init("weeksEmployed", "ones(self.popsize)")
labourmarket.households.init("minWages", "ones(self.popsize) * 60")

labourmarket.init("sumWeeksEmployed", "zeros(1)")
labourmarket.init("sumReserveWages", "zeros(1)")
labourmarket.init("sumMinWages", "zeros(1)")

for i in range(200):

    meanReserveWages.append(labourmarket.households.reserveWages[labourmarket.readIndex].mean())
    meanWeeksEmployed.append(labourmarket.households.weeksEmployed[labourmarket.readIndex].mean())
    meanMinWages.append(labourmarket.households.minWages[labourmarket.readIndex].mean())

    # meanReserveWages.append(labourmarket.sumWeeksEmployed[labourmarket.readIndex])
    # meanWeeksEmployed.append(labourmarket.sumReserveWages[labourmarket.readIndex])
    # meanMinWages.append(labourmarket.sumMinWages[labourmarket.readIndex])

    labourmarket.runModel(1)

end = time.clock()
print "time elapsed: " + str(end - start) + "s"

plot(meanReserveWages,'r-', meanWeeksEmployed, 'b-', meanMinWages, 'g-')
show()

