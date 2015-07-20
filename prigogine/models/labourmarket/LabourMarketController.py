import time
from prigogine.Prigogine import *
import matplotlib.pyplot as plt

start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm")

prigogine.initglobal("reserveWage", [] ) #np.empty((1,1)))
prigogine.initglobal("weeksEmployed", [] ) #np.empty((1,1)))
prigogine.initglobal("minWage", [] ) #np.empty((1,1)))

prigogine.createpop("households", 1)

prigogine.initstates("households", np.random.choice(['employed'], size=1))
prigogine.initvars("households", "reserveWage", np.ones((1,1)) * 100 ) #np.random.uniform(1,10,1))
prigogine.initvars("households", "weeksEmployed", np.random.randint(2, size=1))
prigogine.initparams("households", "minWage", np.ones((1,1)) * 60 ) #np.random.uniform(1,5,1))

#print "weeksEmployed: " + str(prigogine.model.populations["households"].attributes["weeksEmployed"])
#print "reserveWages: " + str(prigogine.model.populations["households"].attributes["reserveWages"])
#print "minWage: " + str(prigogine.model.populations["households"].attributes["minWage"])

print "-------- running model --------\n"

for i in range(100):
    #print prigogine.getglobal("weeksEmployed")

    prigogine.setglobal("weeksEmployed", prigogine.getvars("households", "weeksEmployed").sum())
    prigogine.setglobal("reserveWage", prigogine.getvars("households", "reserveWage").sum())
    prigogine.setglobal("minWage", prigogine.getparams("households", "minWage").sum())
    #print "global RW: " + str(prigogine.getglobal("reserveWages"))
    #print "local RW: " + str(prigogine.getvars("households", "reserveWages"))
    prigogine.runmodel(1)

print "\n\n-------- model run complete  --------\n"

#print "weeksEmployed: " + str(prigogine.model.populations["households"].attributes["weeksEmployed"])
#print "reserveWages: " + str(prigogine.model.populations["households"].attributes["reserveWages"])
#print "minWage: " + str(prigogine.model.populations["households"].attributes["minWage"])
#print "--------------------"

end = time.clock()
print "time elapsed: " + str(end - start) + "s"

plt.plot(prigogine.getglobal("reserveWage"), 'r', prigogine.getglobal("weeksEmployed"), 'b-', prigogine.getglobal("minWage"), 'g-')
#plt.ylabel("averageWages")
plt.show()






