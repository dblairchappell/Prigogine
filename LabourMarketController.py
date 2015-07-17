import time
from Prigogine import *

start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm")

prigogine.create("households", 90000000)
prigogine.startstate("households", "employed")
prigogine.init("households", "reserveWages", random.uniform(1,10,90000000))
prigogine.init("households", "numJobs", ones(90000000) * 1.5)
prigogine.init("households", "minWage", ones(90000000) * 5)

print prigogine.model.populations["households"].attributes

prigogine.runmodel(100)

print prigogine.model.populations["households"].attributes
print ""

end = time.clock()
print "time elapsed: " + str(end - start) + "s"



