import time
from prigogine.Prigogine import *
import matplotlib.pyplot as plt

start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm")

prigogine.initglobal("averageWages", zeros((1,1)))
prigogine.initglobal("numJobs", zeros((1,1)))
prigogine.initglobal("minWage", zeros((1,1)))

prigogine.createpop("households", 10)
prigogine.setstates("households", random.choice(["unemployed", "employed"],10))
prigogine.initattrs("households", "reserveWages", random.uniform(1,10,10))
prigogine.initattrs("households", "numJobs", random.uniform(1,10,10))
prigogine.initattrs("households", "minWage", random.uniform(1,5,10))

print prigogine.model.populations["households"].attributes["numJobs"]

prigogine.runmodel(100)

print prigogine.model.populations["households"].attributes["numJobs"]
print "--------------------"

end = time.clock()
print "time elapsed: " + str(end - start) + "s"

plt.plot(prigogine.getglobal("averageWages"), 'r', prigogine.getglobal("numJobs"), 'b-', prigogine.getglobal("minWage"), 'g-')
plt.ylabel("averageWages")
plt.show()






