import time
from prigogine.Prigogine import *
from numpy import *
import matplotlib.pyplot as plt

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

labourmarket.init("meanWeeksEmployed", "zeros(1)")
labourmarket.init("meanReserveWages", "zeros(1)")
labourmarket.init("meanMinWages", "zeros(1)")

for i in range(100):
    labourmarket.runModel(1)
    meanWeeksEmployed.append(labourmarket.meanWeeksEmployed[labourmarket.readIndex][0])
    meanReserveWages.append(labourmarket.meanReserveWages[labourmarket.readIndex][0])
    meanMinWages.append(labourmarket.meanMinWages[labourmarket.readIndex][0])

end = time.clock()
print "\n\ntime elapsed: " + str(end - start) + "s"
print meanReserveWages
plt.plot(meanReserveWages,'r-', meanWeeksEmployed, 'b-', meanMinWages, 'g-')
plt.show()

