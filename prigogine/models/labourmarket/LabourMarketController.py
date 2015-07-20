import time
from prigogine.Prigogine import *
import matplotlib.pyplot as plt

start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm")

prigogine.initglobal("reserveWage", [] ) #np.empty((1,1)))
prigogine.initglobal("weeksEmployed", [] ) #np.empty((1,1)))
prigogine.initglobal("minWage", [] ) #np.empty((1,1)))

prigogine.createpop("households", 100)

prigogine.initstates("households", np.random.choice(['employed', 'unemploy'], size=100))
prigogine.initvars("households", "reserveWage", np.random.randint(100, size=100)) #np.random.uniform(1,10,1))
prigogine.initvars("households", "weeksEmployed", np.random.randint(2, size=100))
prigogine.initparams("households", "minWage", np.ones((1,100)) * 60 ) #np.random.uniform(1,5,1))

#print "weeksEmployed: " + str(prigogine.model.populations["households"].attributes["weeksEmployed"])
#print "reserveWages: " + str(prigogine.model.populations["households"].attributes["reserveWages"])
#print "minWage: " + str(prigogine.model.populations["households"].attributes["minWage"])

print "-------- running model --------\n"

for i in range(100):
    #print prigogine.getglobal("weeksEmployed")

    prigogine.setglobal("weeksEmployed", prigogine.getvars("households", "weeksEmployed").mean())
    prigogine.setglobal("reserveWage", prigogine.getvars("households", "reserveWage").mean())
    prigogine.setglobal("minWage", prigogine.getparams("households", "minWage").mean())
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






