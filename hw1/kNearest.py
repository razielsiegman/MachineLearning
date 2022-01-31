import numpy as np
from math import sqrt


def expectedVal(x, y, k, xVals, yVals, zVals):
    allDistances = list()
    for i in range(400):
        distance = sqrt(((xVals[i] - x)**2) + ((yVals[i] - y)**2))
        allDistances.append((i, distance, zVals[i]))
    allDistances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(k):
        neighbors.append((allDistances[i][0], allDistances[i][2]))
    out = [i[1] for i in neighbors]
    res = max(set(out), key=out.count)
    return res

#Add 100 random data points in each of the 4 quadrants
xVals = np.concatenate([np.random.uniform(0, 100, 100), np.random.uniform(-100, 0, 100), np.random.uniform(0, 100, 100), np.random.uniform(-100, 0, 100)])
yVals = np.concatenate([np.random.uniform(-100, 0, 100), np.random.uniform(0, 100, 100), np.random.uniform(0, 100, 100), np.random.uniform(-100, 0, 100)])
zVals = np.concatenate([[1]*200, [0]*200])

#Test using 1 data point from each quadrant
prediction1 = expectedVal(25.0,25.0,5, xVals, yVals, zVals)
print('For data point: "25,25".  Expected %d, Got %d.' % (0, prediction1))
prediction2 = expectedVal(-25.0,-25.0,5, xVals, yVals, zVals)
print('For data point: "-25,-25".  Expected %d, Got %d.' % (0, prediction2))
prediction3 = expectedVal(-25.0,25.0,5, xVals, yVals, zVals)
print('For data point: "-25,25".  Expected %d, Got %d.' % (1, prediction3))
prediction4 = expectedVal(25.0,-25.0,5, xVals, yVals, zVals)
print('For data point: "25,-25".  Expected %d, Got %d.' % (1, prediction4))
prediction5 = expectedVal(25.0,0,5, xVals, yVals, zVals)
print('For data point: "25,0".  Expected value can vary, Got %d.' % prediction5)


