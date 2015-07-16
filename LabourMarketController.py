import time
from Prigogine import *

start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm")

prigogine.create("households", 25000)
prigogine.startstate("households", "employed")
prigogine.init("households", "reserveWages", random.uniform(1,100,25000))
prigogine.init("households", "numJobs", ones(25000))
prigogine.init("households", "minWage", ones(25000) * 5)

prigogine.runmodel(100)

end = time.clock()
print "time elapsed: " + str(end - start) + "s"



