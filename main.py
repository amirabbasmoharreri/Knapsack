import math
import operator
import time
import matplotlib.pyplot as plt
import numpy as np
from random import randint


class Coromozom():
    weight = 0
    value = 0

    def __init__(self):
        self.array = None
        self.weight = None
        self.value = None

    def __setitem__(self, array, weight, value):
        self.weight = weight
        self.value = value
        self.array = array


class Object():

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def population(n ,populationSize):
    p = []
    counterpop = 0
    while counterpop < populationSize:
        history = []
        counter = 0
        while counter < n:
            adad = randint(0, 1)
            history.append(adad)
            counter += 1
        crom = Coromozom()
        crom.array = history
        p.append(crom)
        counterpop += 1
        print(history)
    return p


def fitnessFunction(lists, objects):
    croms = computingTotalValue(lists, objects)
    croms.sort(key=operator.attrgetter('value'), reverse=True)
    return croms


def fetchBestCrom(lists, maxWeight):
    best = lists[0]
    for i in range(0, len(lists)):
        if lists[i].weight <= maxWeight:
            best.array = lists[i].array
            best.weight = lists[i].weight
            best.value = lists[i].value
            break
    return best


###      Correct

def crossover(n):
    ra = []
    for i in range(2):
        a = randint(0, n - 1)
        if not (a in ra):
            ra.append(a)
    rand = (min(ra), max(ra))

    return rand


###   Correct

def parentSelection(allpop, rate):
    p = []
    history = []
    popsize = len(allpop)
    pecent = (rate / 100)
    crosssize = int(popsize * pecent)

    parents = []
    i = 0
    while i < 2:
        fmparent = []
        counter = 0
        while counter < (int(crosssize/2)):
            num = randint(0, popsize - 1)
            if not (num in history):
                history.append(num)
                fmparent.append(num)
                counter += 1
        parents.append(fmparent)
        i += 1
    j = 0
    while j < 2:
        c = []
        for i in range(0, (int(crosssize/2))):
            c.append(allpop[parents[j][i]])
        p.append(c)
        j += 1

    return p


def surviveSelection(allpop, n):
    allpop.sort(key=operator.attrgetter('value'), reverse=True)
    num = n
    percent = (20 / 100)
    popsize = int(len(allpop) * percent)
    best = []

    for i in range(0, len(allpop)):
        if allpop[i].weight <= maxWeight:
            best.append(allpop[i])
        if len(best) == popsize:
            break

    while len(best) < num:
        rand = randint(0, len(allpop) - 1)
        if not (allpop[rand] in best):
            best.append(allpop[rand])
    return best


###   Correct

def mutation(childs, rate):
    popsize = len(childs)
    lens = len(childs[0].array)
    randcrom = []
    randindex = []
    pecent = (rate / 100)
    musize = int(popsize * pecent)
    # random coromozoms for mutation
    for i in range(musize):
        randcrom.append(randint(0, popsize - 1))

    for i in randcrom:
        a = randint(0, lens - 1)
        if childs[i].array[a] == 0:
            childs[i].array[a] = 1
        else:
            childs[i].array[a] = 0

    return childs


###   Correct

def computingTotalValue(croms, objects):
    sumWeight = 0
    sumvalue = 0
    popsize = len(croms)
    lens = len(croms[0].array)
    for j in range(0, popsize):
        for i in range(0, lens):
            if croms[j].array[i] == 1:
                sumWeight += objects[i].weight
                sumvalue += objects[i].value
        croms[j].weight = sumWeight
        croms[j].value = sumvalue

    return croms


def recombination(allpop, parent):
    lens = len(parent[0][0].array)
    recomsize = len(parent[0])
    childs = []
    for j in range(0, recomsize):
        cross = crossover(lens)
        child1 = []
        child2 = []
        for i in range(0, lens):
            child1.append(-1)
            child2.append(-1)
        p1 = parent[0][j].array
        p2 = parent[1][j].array

        # creating middle of cromozom childs

        for i in range(cross[0], cross[1] + 1):
            child1[i] = p1[i]
            child2[i] = p2[i]

        # creating next to the childs cromozom

        # creating left-side
        for i in range(0, cross[0]):
            if not p2[i] in child1:
                child1[i] = p2[i]
            if not p1[i] in child2:
                child2[i] = p1[i]

        # creating right-side
        for i in range(cross[1] + 1, lens):
            if not p2[i] in child1:
                child1[i] = p2[i]
            if not p1[i] in child2:
                child2[i] = p1[i]

        # completing childs
        for i in range(0, lens):

            index1 = [j for j in range(len(child2)) if child1[j] == -1]
            index2 = [j for j in range(len(child2)) if child2[j] == -1]

            if not p2[i] in child1:
                if not (len(index1) == 0):
                    child1[index1[0]] = p2[i]
            if not p1[i] in child2:
                if not (len(index2) == 0):
                    child2[index2[0]] = p1[i]
        crom1 = Coromozom()
        crom2 = Coromozom()
        crom1.array = child1
        crom2.array = child2
        childs.append(crom1)
        childs.append(crom2)

    return childs


def addchildstopopulation(allpop, childs):
    for i in range(0, len(childs)):
        allpop.append(childs[i])
    return allpop


def showfitness(lists):
    plt.plot(lists)
    plt.title("ّFitness Function = " + str(lists[len(lists) - 1]))
    plt.ylabel("Value")
    plt.xlabel("Iteration")
    plt.show()
    return

def showWeight(lists , maxWeight):
    plt.plot(lists)
    plt.title("Weight = " + str(lists[len(lists) - 1]) + " Max Weight = " + str(maxWeight))
    plt.ylabel("Weight")
    plt.xlabel("Iteration")
    plt.show()
    return

def showWeightValue(lists):
    x=[]
    y=[]
    for i in range(0,len(lists)):
        x.append(lists[i].weight)
        y.append(lists[i].value)

    plt.plot(x,y)
    plt.title("Weight = " + str(lists[len(lists) - 1].weight) + " Value = " + str(lists[len(lists) - 1].value))
    plt.ylabel("Value")
    plt.xlabel("Weight")
    plt.show()
    return


##################### starting app from here  ######################


list_objects = []
bestcrom = []
bestfitness = []
bestweight = []
print("enter number of cities 'minimum 4' ")
while True:
    num = int(input())
    if num >= 4:
        break
    else:
        print("try again")

# intializing Coordinates of cities with random

start = time.time()

for j in range(num):
    weight = randint(0, 5)
    value = randint(0, 200)
    object1 = Object(weight, value)
    list_objects.append(object1)

print("input the population")
populationSize = int(input())

print("input maximum weight")
maxWeight = int(input())

print("input mutation rates")
mutationRate = int(input())

print("input crossover rates")
crossRate = int(input())

print("list of objects")
print(list_objects)

# ADT allgorithm

i = 0
j = 0
fit1 = 100
fit2 = 200
allPopulation = population(num , populationSize)
allPopulation = fitnessFunction(allPopulation, list_objects)
bestfitness.append(fetchBestCrom(allPopulation, maxWeight).value)
bestweight.append(fetchBestCrom(allPopulation, maxWeight).weight)
evaluate = abs(fit1 - fit2)
while j < 200:
    if evaluate < 1:
        j += 1
    else:
        j = 0
    print("Generation " + str(i) + "  Fitness: " + str(fit2) + "  Count fitness not change: " + str(j))
    parent = parentSelection(allPopulation, crossRate)
    childs = recombination(allPopulation, parent)
    childs = mutation(childs, mutationRate)
    childs = fitnessFunction(childs, list_objects)
    allPopulation = addchildstopopulation(allPopulation, childs)
    allPopulation = surviveSelection(allPopulation, populationSize)
    bestcrom.append(fetchBestCrom(allPopulation, maxWeight))
    bestfitness.append(bestcrom[len(bestcrom)-1].value)
    bestweight.append(bestcrom[len(bestcrom)-1].weight)
    fit2 = bestfitness[len(bestfitness) - 1]
    if len(bestfitness) > 1:
        fit1 = bestfitness[len(bestfitness) - 2]
    evaluate = abs(fit1 - fit2)
    i += 1
#bestcrom.sort(key=operator.attrgetter('value'), reverse=True)
showfitness(bestfitness)
showWeight(bestweight,maxWeight)
showWeightValue(bestcrom)
print("Fitness: " + str(fit2))
end = time.time()
print("Runtime of the program is " + str(end - start) + " seconds")
