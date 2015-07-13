

from Prigogine import loadModel

model = loadModel("LabourMarketModel.prm", "LabourMarketSetup.prs")
model.runModel(50)

#results = model.run(100)

#plot(mean(results["household"]["reserveWage"]))

# model.initAttrsRand("household", "reserveWage", 1, 100)
# model.initAttrsRandInt("household", "numJobs", 1, 10)
#
# model.initState("household", "employed")
# model.initStateRandChoice("household", ["employed","unemployed"])

print model.populations




