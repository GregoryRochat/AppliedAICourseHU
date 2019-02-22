import math


def vectorsize(vector):
    return len(vector)


def distancecalc(vector1, vector2):
    x = vectorsize(vector1)
    squareoutput = 0
    if x != vectorsize(vector2):
        return 0
    for l in range(0, x):
        squareoutput += math.pow((vector1[l] - vector2[l]), 2)
    return math.sqrt(squareoutput)


vectora = [2, 3, 4,2]
vectorb = [1, -2, 1, 3]

print(distancecalc(vectora, vectorb))
