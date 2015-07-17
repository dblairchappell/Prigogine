import time
from prigogine.Prigogine import *
import matplotlib.pyplot as plt

start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm")

prigogine.initglobal("averageWages", zeros((1,1)))
prigogine.initglobal("numJobs", zeros((1,1)))
prigogine.initglobal("minWage", zeros((1,1)))

prigogine.create("households", 5000000)
prigogine.startstate("households", "employed")
prigogine.init("households", "reserveWages", random.uniform(1,10,5000000))
prigogine.init("households", "numJobs", random.uniform(1,10,5000000))
prigogine.init("households", "minWage", random.uniform(1,5,5000000))

print prigogine.model.populations["households"].attributes["minWage"]

prigogine.runmodel(100)

print prigogine.model.populations["households"].attributes["minWage"]
print "--------------------"

end = time.clock()
print "time elapsed: " + str(end - start) + "s"

plt.plot(prigogine.getglobal("averageWages"), 'r', prigogine.getglobal("numJobs"), 'b-', prigogine.getglobal("minWage"), 'g-')
plt.ylabel("averageWages")
plt.show()






