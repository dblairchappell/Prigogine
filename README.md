## Overview of the Project:

Prigogine is a domain-specific language and development environment for researchers wanting to develop large-scale multi-agent and discrete-time models but lacking the knowledge necessary to take advantage of high performance computing technology.

By utilising Python's NumPy package for n-dimensional arrays, it is hoped that the performance capabilities of modelling frameworks like Repast HPC and FLAME, and the productiveness associated with Python's high-level syntax, can be brought together in one convenient package.

The project is at a relatively early stage and is presently focussed on getting single-core functionality up and running. The target timeframe for getting the first version released is mid-September 2015.

#### Example of Working Model:

##### Model Definition Script

    model labourmarket [
        messageboards [
            householdIds (1,1)
        ]
        variables [
            meanWeeksEmployed
            meanReserveWages
            meanMinWages
        ]
        equations [
            self.meanWeeksEmployed[t+1] = self.households.weeksEmployed[t].mean()
            self.meanReserveWages[t+1] = self.households.reserveWages[t].mean()
            self.meanMinWages[t+1] = self.households.minWages[t].mean()
        ]
        population households [
            variables [
                states
                reserveWages
                weeksEmployed
                minWages
            ]
            equations [
                self.states[t+1][:] = 0, where (self.reserveWages[t] >= (self.minWages[t] + 100)) & (self.states[t] == 1)
                self.reserveWages[t+1] = self.reserveWages[t] * 1.1, where self.states[t] == 1
                self.weeksEmployed[t+1] = self.weeksEmployed[t] + 1, where self.states[t] == 1
                self.states[t+1][:] = 1, where (self.reserveWages[t] < self.minWages[t]) & (self.states[t] == 0)
                self.reserveWages[t+1] = self.reserveWages[t] * 0.9, where self.states[t] == 0
                self.weeksEmployed[t+1] = self.weeksEmployed[t], where self.states[t] == 0
            ]
        ]
    ]

##### Model Simulation Script

    from prigogine.PrigogineCore import *
    from numpy import *
    from matplotlib.pyplot import *

    start = time.clock()

    meanReserveWages = []
    meanWeeksEmployed = []
    meanMinWages = []

    labourmarket = prigogine.loadmodel("LabourMarketModel.prm")
    labourmarket.households.popsize = 10000

    labourmarket.households.init("states", "random.choice([1, 0], size=self.popsize, p=[0.5,0.5])")
    labourmarket.households.init("reserveWages", "random.randint(100, size=self.popsize)")
    labourmarket.households.init("weeksEmployed", "ones(self.popsize)")
    labourmarket.households.init("minWages", "ones(self.popsize) * 60")

    labourmarket.init("meanWeeksEmployed", "zeros(1)")
    labourmarket.init("meanReserveWages", "zeros(1)")
    labourmarket.init("meanMinWages", "zeros(1)")

    for i in range(100):
        labourmarket.runModel(1)
        meanWeeksEmployed.append(labourmarket.meanWeeksEmployed[labourmarket.readIndex][0])
        meanReserveWages.append(labourmarket.meanReserveWages[labourmarket.readIndex][0])
        meanMinWages.append(labourmarket.meanMinWages[labourmarket.readIndex][0])

    plot(meanReserveWages,'r-', meanWeeksEmployed, 'b-', meanMinWages, 'g-')
    show()

##### Model Output

![Model Output](https://raw.githubusercontent.com/dblairchappell/Prigogine/master/prigogine/models/labourmarket/figure_1.png)

