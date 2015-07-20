import time
from prigogine.Prigogine import *
import matplotlib.pyplot as plt

start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm")

prigogine.initglobal("reserveWages", [] ) #np.empty((1,1)))
prigogine.initglobal("weeksEmployed", [] ) #np.empty((1,1)))
prigogine.initglobal("minWage", [] ) #np.empty((1,1)))

prigogine.createpop("households", 100000)

prigogine.initstates("households", np.random.choice(['employed'], size=100000))
prigogine.initvars("households", "reserveWages", np.ones((1,100000)) * 100 ) #np.random.uniform(1,10,1))
prigogine.initvars("households", "weeksEmployed", np.random.randint(2, size=100000))
prigogine.initparams("households", "minWage", np.ones((1,100000)) * 60 ) #np.random.uniform(1,5,1))

#print "weeksEmployed: " + str(prigogine.model.populations["households"].attributes["weeksEmployed"])
#print "reserveWages: " + str(prigogine.model.populations["households"].attributes["reserveWages"])
#print "minWage: " + str(prigogine.model.populations["households"].attributes["minWage"])

print "-------- running model --------\n"

for i in range(100):
    #print prigogine.getglobal("weeksEmployed")

    prigogine.setglobal("weeksEmployed", prigogine.get("households", "weeksEmployed").sum())
    prigogine.setglobal("reserveWages", prigogine.get("households", "reserveWages").sum())
    prigogine.setglobal("minWage", prigogine.getparams("households", "minWage").sum())
    #print "global RW: " + str(prigogine.getglobal("reserveWages"))
    #print "local RW: " + str(prigogine.get("households", "reserveWages"))
    prigogine.runmodel(1)

print "\n\n-------- model run complete  --------\n"

#print "weeksEmployed: " + str(prigogine.model.populations["households"].attributes["weeksEmployed"])
#print "reserveWages: " + str(prigogine.model.populations["households"].attributes["reserveWages"])
#print "minWage: " + str(prigogine.model.populations["households"].attributes["minWage"])
#print "--------------------"

end = time.clock()
print "time elapsed: " + str(end - start) + "s"

plt.plot(prigogine.getglobal("reserveWages"), 'r', prigogine.getglobal("weeksEmployed"), 'b-', prigogine.getglobal("minWage"), 'g-')
#plt.ylabel("averageWages")
plt.show()






