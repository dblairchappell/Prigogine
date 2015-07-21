## Overview of the Project:

Prigogine is a domain-specific language and development environment for scientists wanting to develop large-scale agent-based models but lacking the knowledge neccessary to take advantage of high-performance computing technology.

By utilising Python's multiprocessing module and the NumPy package for n-dimensional arrays, it is hoped that the performance capabilities of modelling frameworks like Repast HPC and FLAME, and the productiveness of a high-level language like NetLogo, can be brought together in one convenient package.

The project is at a relatively early stage and is presently focussed on getting single-core functionality up and running. The target timeframe for getting the first version released is mid-september 2015.

#### Example of Proposed Syntax:

    ##### Model Definition

    population households [
        parameters [
            minwage
        ]
        variables [
            reserveWage
            weeksEmployed
            minWage
        ]
        state employed [
            transition unemploy where getvars('reserveWage') > (getparams('minWage') + 100)
            update reserveWage getvars('reserveWage') * 1.1
            update weeksEmployed getvars('weeksEmployed') + 1
        ]
        state unemploy [
            transition employed where getvars('reserveWage') <= getparams('minWage')
            update reserveWage maximum(getvars('reserveWage') * 0.9, getparams('minWage'))
            update weeksEmployed getvars('weeksEmployed')
        ]
    ]

    ##### Model Simulation

    initglobal sumReserveWages []
    initglobal sumWeeksEmployed []
    initglobal sumMinWages []

    create households 100 [
        initvars reserveWage random.randint(100, size=100)
        initvars minWage ones((1,100)) * 60
        initvars weeksEmployed ones((1,100))
        initstates random.choice(["employed", "unemploy"], size=100)
    ]

    runmodel 100 [
        print "-"
    ]

    finalise [
        plot(getglobal("reserveWage"), 'r', getglobal("weeksEmployed"), 'b-', getglobal("minWage"), 'g-')
    ]


