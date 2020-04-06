
# IMPORTS
import pandas as pd
import numpy as np
import csv


# VARIABLES

# Fiber Type
# PR, OX
fiberType = [0, 1]

# Dispersing Agent
# No, Yes
dispersingAgent = [0, 1]

# Mixing
# SO, HS, SO+HS
mixing = [0, 1, 2]

# Fiber Weight
# 0-1 in .05 increments
w = 0
fiberWeight = []
while w <= 1.05:
    fiberWeight.append(round(w, 3))
    w += 0.001

# WRITE EACH COMBINATION TO CSV

number = 1

for fibT in fiberType:
    for dispA in dispersingAgent:
        for mix in mixing:
            with open(f"{number}.csv", 'w', newline='') as file:
                writ = csv.writer(file)
                writ.writerow(['Fiber Type', 'Fiber Weight', 'Dispersing Agent', 'Mixing'])
                for fibW in fiberWeight:
                    writ.writerow([fibT, fibW, dispA, mix])
            number += 1


