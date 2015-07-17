import time
from Prigogine import *
import matplotlib.pyplot as plt

start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm")

prigogine.initglobal("averageWages", zeros((1,1)))

prigogine.create("households", 1000000)
prigogine.startstate("households", "employed")
prigogine.init("households", "reserveWages", random.uniform(1,10,1000000))
prigogine.init("households", "numJobs", ones(1000000) * 1.5)
prigogine.init("households", "minWage", ones(1000000) * 5)

print prigogine.model.populations["households"].attributes

prigogine.runmodel(10)

print prigogine.model.populations["households"].attributes
print "--------------------"

end = time.clock()
print "time elapsed: " + str(end - start) + "s"

plt.plot(prigogine.getglobal("averageWages"))
plt.ylabel("averageWages")
plt.show()






