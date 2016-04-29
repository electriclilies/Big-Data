# -*- coding: utf-8 -*-
"""
K-nearest neighbors algorithm
Jason Brownlee, http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
Implemented by Emma Anderson
Written for the Iris dataset
"""
import csv
import random
import math
import operator

def euclideanDistance(item1, item2, attributes):
    distance = 0
    for x in range(attributes):
        distance+=(item1[x] - item2[x])**2
    return math.sqrt(distance)

def getNeighbors(trainingSet, test, k):
    distances = []
    length = len(test) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(test, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    #sort on the distance, not the data point
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct+=1
    return (correct/float(len(testSet)))*100.0

def loadDataset(filename, split, trainingSet, testSet):    
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            #this needs changing for other datasets
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

def main():
    trainingSet = []
    testSet = []
    split = 0.10
    loadDataset('irises.txt', split, trainingSet, testSet)
    print(testSet)
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('predicted:' + result + ', actual:'+testSet[x][-1])
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + str(accuracy) + '%')

main()

#testSet = [[1, 1, 1, 'a'], [2, 2, 2, 'b'], [3, 3, 3, 'a']]
#predictions= ['a', 'a', 'a']
#print(getAccuracy(testSet, predictions))

#trainingSet = []
#testSet = []
#loadDataset('iris.txt', 0.9, trainingSet, testSet)
#print(len(trainingSet))
#print(len(testSet))

#data1 = [2, 2, 2, 'a']
#data2 =[4, 4, 4, 'b']
#distance = euclideanDistance(data1, data2, 3)
#print(distance)

#trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
#test = [5, 5, 5]
#k=1
#print(getNeighbors(trainSet, test, k))

#neighbors = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
#response = getResponse(neighbors)
#print(response)
