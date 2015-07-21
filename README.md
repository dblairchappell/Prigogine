## Overview of the Project:

Prigogine is a domain-specific language and development environment for scientists wanting to develop large-scale agent-based models but lacking the knowledge neccessary to take advantage of high-performance computing technology.

By utilising Python's multiprocessing module and the NumPy package for n-dimensional arrays, it is hoped that the performance capabilities of modelling frameworks like Repast HPC and FLAME, and the productiveness of a high-level language like NetLogo, can be brought together in one convenient package.

The project is at a relatively early stage and is presently focussed on getting single-core functionality up and running. The target timeframe for getting the first version released is mid-september 2015.

#### Example of Working Model:

##### Model Definition Script

    population households [
        parameters [
            minWage
        ]
        variables [
            reserveWage
            weeksEmployed
            minWage
        ]
        state employed [
            transition unemploy where getvars("reserveWage") > (getparams("minWage") + 100)
            update reserveWage getvars("reserveWage") * 1.1
            update weeksEmployed getvars("weeksEmployed") + 1
        ]
        state unemploy [
            transition employed where getvars("reserveWage") <= getparams("minWage")
            update reserveWage maximum(getvars("reserveWage") * 0.9, getparams("minWage"))
            update weeksEmployed getvars("weeksEmployed")
        ]
    ]

##### Model Simulation Script

    initglobal sumReserveWages []
    initglobal sumWeeksEmployed []
    initglobal sumMinWages []

    create households 10000 [
        initvars reserveWage random.randint(100, size=10000)
        initvars minWage ones((1,10000)) * 60
        initvars weeksEmployed ones((1,10000))
        initparams minWage ones((1,10000)) * 60
        initstates random.choice(["employed", "unemploy"], size=10000)
    ]

    runmodel 200 [
        setglobal("sumWeeksEmployed", getvars("households", "weeksEmployed").mean())
        setglobal("sumReserveWages", getvars("households", "reserveWage").mean())
        setglobal("sumMinWages", getparams("households", "minWage").mean())
    ]

    finalise [
        plot(getglobal("sumReserveWages"), 'r', getglobal("sumWeeksEmployed"), 'b-', getglobal("sumMinWages"), 'g-')
        show()
    ]

##### Model Output

![Model Output](https://raw.githubusercontent.com/dblairchappell/Prigogine/master/prigogine/models/labourmarket/figure_1.png)

