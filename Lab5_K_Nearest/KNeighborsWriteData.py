# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:02:56 2016

@author: Lily
"""


import csv
import random
import math
import operator

def loadDataset(filename, split, trainingSet, testSet, Range):    
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        del(dataset[0])
        Array = []
        for x in range(len(dataset)-1):
            #this needs changing for other datasets
            for y in Range:
                Array.append(float(dataset[x][y]))
            if random.random() < split:
                trainingSet.append(Array)
            else:
                testSet.append(Array)
            Array = []
            
def euclideanDistance(item1, item2, attributes):
    distance = 0
    for x in range(attributes-1):
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

def main(split, k, Range):
    trainingSet = []
    testSet = []
    #split = 0.30
    loadDataset("datatraining.txt", split, trainingSet, testSet, Range)
    predictions = []
    #k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        #print('predicted:' + str(result) + ', actual:'+str(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    return accuracy
    #print('Accuracy: ' + str(accuracy) + '%')



iterations = 10 #cant make this bigger than 10 with 0.001 split bc you get 0 data points
#also: possibly make test dataset to do stats stuff
kMax = 10
splitMax = 0.05

text_file = open("splitdata.txt", "a")
text_file.write("K,split,accuracy")

for x in range(1, int(splitMax*100)+1):
    for k in range(1, kMax+1): 
        for j in range(1, iterations+1): 
            text_file.write(str(k))
            text_file.write(",")
            text_file.write(str(x/100))
            text_file.write(",")
            text_file.write(str(main(x/100,k,range(2,8))))
            text_file.write("\n")
text_file.close()

print("done")
