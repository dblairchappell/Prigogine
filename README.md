## Overview of the Project:

Prigogine is a domain-specific language and development environment for scientists wanting to develop large-scale agent-based models but lacking the knowledge neccessary to take advantage of high-performance computing technology.

By utilising Python's multiprocessing module and the NumPy package for n-dimensional arrays, it is hoped that the performance capabilities of modelling frameworks like Repast HPC and FLAME, and the productiveness of a high-level language like NetLogo, can be brought together in one convenient package.

The project is at a relatively early stage and is presently focussed on getting single-core functionality up and running. The target timeframe for getting the first version released is mid-september 2015.

#### Example of Proposed Syntax:

    population "households" [

        attributes [
            "reserveWages"
            "weeksEmployed"
            "minWage"
        ]

        state "employed" [
            transition "unemployed" if get("reserveWages") < 50
            update "reserveWages" get("reserveWages") * 1.1
            update "weeksEmployed" get("weeksEmployed") + 1

        ]

        state "unemployed" [
            transition "employed" if get("reserveWages") > 100
            update "reserveWages" maximum(get("reserveWages") * 0.9, get("minWage"))
            update "minWage" get("minWage") + (random.random_sample() -0.5) * 10
        ]
    
    ]


