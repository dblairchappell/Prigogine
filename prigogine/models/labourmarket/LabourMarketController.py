
import time
from prigogine.Prigogine import *
from numpy import *
from matplotlib.pyplot import *

start = time.clock()

labourmarket = prigogine.loadmodel("LabourMarketNew.prm")
labourmarket.households.popsize = 10

labourmarket.households.init("states", "random.choice([1, 0], size=self.popsize, p=[1.0,0.0])")
labourmarket.households.init("reserveWages", "ones(self.popsize) * 30")
labourmarket.households.init("weeksEmployed", "ones(self.popsize)")
labourmarket.households.init("minWages", "ones(self.popsize) * 35")

labourmarket.init("sumWeeksEmployed", "zeros(1)")
labourmarket.init("sumReserveWages", "zeros(1)")
labourmarket.init("sumMinWages", "zeros(1)")

print labourmarket.households.reserveWages
print labourmarket.sumReserveWages
labourmarket.runModel(10)
print labourmarket.households.reserveWages
print labourmarket.sumReserveWages

end = time.clock()
print "time elapsed: " + str(end - start) + "s"


