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
            meanWeeksEmployed[t+1] = households.weeksEmployed[t].mean()
            meanReserveWages[t+1] = households.reserveWages[t].mean()
            meanMinWages[t+1] = households.minWages[t].mean()
        ]
        population households [
            variables [
                states
                reserveWages
                weeksEmployed
                minWages
            ]
            equations [
                states[t+1][:] = 0, where (reserveWages[t] >= (minWages[t] + 100)) & (states[t] == 1)
                reserveWages[t+1] = reserveWages[t] * 1.1, where states[t] == 1
                weeksEmployed[t+1] = weeksEmployed[t] + 1, where states[t] == 1
                minWages[t+1] = minWages[t]

                states[t+1][:] = 1, where (reserveWages[t] < minWages[t]) & (states[t] == 0)
                reserveWages[t+1] = reserveWages[t] * 0.9, where states[t] == 0
                weeksEmployed[t+1] = weeksEmployed[t], where states[t] == 0
                minWages[t+1] = minWages[t]
            ]
        ]
    ]

##### Model Simulation Script

    from prigogine.PrigogineCore import *

    labourmarket = prigogine.loadmodel("LabourMarketModel.prm")
    numHouseholds = 10000
    labourmarket.households.create(numHouseholds)

    labourmarket.households.states[0] = np.random.choice([1, 0], numHouseholds, [0.5,0.5])
    labourmarket.households.reserveWages[0] = np.random.randint(100, size=numHouseholds)
    labourmarket.households.weeksEmployed[0] = np.ones(numHouseholds)
    labourmarket.households.minWages[0] = np.ones(numHouseholds) * 60

    labourmarket.meanWeeksEmployed[0] = 0
    labourmarket.meanReserveWages[0] = 0
    labourmarket.meanMinWages[0] = 0

    meanReserveWages = []
    meanWeeksEmployed = []
    meanMinWages = []

    for i in range(100):
        labourmarket.runModel(1)
        meanWeeksEmployed.append(labourmarket.meanWeeksEmployed[labourmarket.readIndex])
        meanReserveWages.append(labourmarket.meanReserveWages[labourmarket.readIndex])
        meanMinWages.append(labourmarket.meanMinWages[labourmarket.readIndex])

    plt.plot(meanReserveWages,'r-', meanWeeksEmployed, 'b-', meanMinWages, 'g-')
    plt.show()

##### Model Output

![Model Output](https://raw.githubusercontent.com/dblairchappell/Prigogine/master/prigogine/models/labourmarket/figure_1.png)

