import time
from prigogine.Prigogine import *
import matplotlib.pyplot as plt

start = time.clock()

prigogine.loadmodel("LabourMarketModel.prm")

prigogine.initglobal("reserveWages", np.zeros((1,1)))
prigogine.initglobal("weeksEmployed", np.zeros((1,1)))
prigogine.initglobal("minWage", np.zeros((1,1)))

prigogine.createpop("households", 5)

prigogine.setstates("households", np.random.choice(['employed', 'unemployed'], size=5,))
prigogine.initattrs("households", "reserveWages", np.random.uniform(1,10,5))
prigogine.initattrs("households", "weeksEmployed", np.random.randint(2, size=5))
prigogine.initattrs("households", "minWage", np.random.uniform(1,5,5))

#print "weeksEmployed: " + str(prigogine.model.populations["households"].attributes["weeksEmployed"])
#print "reserveWages: " + str(prigogine.model.populations["households"].attributes["reserveWages"])
#print "minWage: " + str(prigogine.model.populations["households"].attributes["minWage"])

print "-------- running model --------\n"

for i in range(100):

    prigogine.setglobal("weeksEmployed", prigogine.get("households", "weeksEmployed").mean())
    prigogine.setglobal("reserveWages", prigogine.get("households", "reserveWages").mean())
    prigogine.setglobal("minWage", prigogine.get("households", "minWage").mean())

    #print prigogine.getglobal("weeksEmployed")
    prigogine.runmodel(1)

print "\n\n-------- model run complete  --------\n"

#print "weeksEmployed: " + str(prigogine.model.populations["households"].attributes["weeksEmployed"])
#print "reserveWages: " + str(prigogine.model.populations["households"].attributes["reserveWages"])
#print "minWage: " + str(prigogine.model.populations["households"].attributes["minWage"])
#print "--------------------"

end = time.clock()
print "time elapsed: " + str(end - start) + "s"

plt.plot(prigogine.getglobal("reserveWages"), 'r', prigogine.getglobal("weeksEmployed"), 'b-', prigogine.getglobal("minWage"), 'g-')
plt.ylabel("averageWages")
plt.show()






