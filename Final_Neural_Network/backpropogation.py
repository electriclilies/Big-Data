# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 09:45:24 2016

@author: Lily
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:14:30 2016

@author: Lily
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 09:22:15 2016

@author: Lily
"""


import math
import random
import numpy as np
import copy

#creates a dataset of x, y values, returns 1 if x > y, -1 if y < x
def createData(length):
    data_list = []
    output_list = []
    for i in range(length):
        x = random.random()
        y = random.random()
        data_list.append([x, y])
        if (x/y) > 1: 
            above_line = 1
        elif (x/y) == 1: 
            above_line = 0
        elif (x/y) < 1: 
            above_line = -1
        output_list.append(above_line)
    return data_list, output_list

#creates a layer of random node weights
def createLayer(node_number, input_number):
    #maximum the weight can be
    layer = []
    for i in range(node_number):
        node = []
        for j in range(input_number): 
            node.append((0.5-random.random())*2)
        layer.append(node)
    return layer
    
#creates a network of arrays
def createNetwork(hid_layer_number, init_input_number, layer_size):
    layers = []
    layers.append(createLayer(layer_size, init_input_number))
    for i in range(hid_layer_number):
        layers.append(createLayer(layer_size, layer_size))
    layers.append(createLayer(1, layer_size))
    return layers

#takes the dot product of the input list and weight list, then feeds it through the hyperbolic tangent function
def createOutput(input_list, weight_list):
    weighted_sum = 0
    for i in range(len(input_list)):
        weighted_sum+=(weight_list[i]*input_list[i])
    #takes the hyperbolic tangent of the weighted sum
    return math.tanh(weighted_sum)

#runs the neural network
def runNetwork(Input, network):
    #iterates through layers
    for i in range(len(network)): 
        #iterates through nodes in layers
        output_list = []
        for j in range(len(network[i])):
            output_list.append(createOutput(Input, network[i][j]))
        Input = output_list
    return output_list[0]
    
#gets the accuracy of the neural network for a test data set
def getAccuracy(input_list, output_list, network):
    accurate_total = 0
    predicted_output = []
    for i in range(len(input_list)):
        output = runNetwork(input_list[i], network)
        predicted_output.append(output)
        if output == output_list[i]:
            accurate_total+=1
    accuracy = accurate_total/len(output_list) * 100
    return accuracy, predicted_output
    
def squaredErrorArray(input_list, output_list, network):
    predicted_output = []
    for i in range(len(input_list)):
        output = runNetwork(input_list[i], network)
        predicted_output.append(output)
        if output == output_list[i]:
            accurate_total+=1
    accuracy = accurate_total/len(output_list) * 100
    return accuracy, predicted_output

def getSquaredError(input_list, output_list, network):
    Sum = 0
    for i in range(len(input_list)):
        Sum += (output_list[i]-runNetwork(input_list[i], network))**2
    error_avg = Sum/len(input_list)
    return error_avg

#cycles through 20 randomly generated networks until it finds the most accurate one
def getOKNetwork(input_list, output_list):
    network = createNetwork(1, 2, 5) #three hidden layers, 2 inputs, 5 nodes/layer
    error_avg = getSquaredError(input_list, output_list, network)
    print(error_avg)
    for i in range(20):
        new_network = createNetwork(3, 2, 5)
        new_error_avg = getSquaredError(input_list, output_list, new_network)
        if error_avg > new_error_avg:
            network = copy.deepcopy(new_network)
            error_avg = new_error_avg
            print(error_avg)
    print("Best error avg", error_avg)
    return network, error_avg

#returns an array of the change in accuracy
def errArray(input_list, output_list, network, step):
    initial_err = getSquaredError(Input, Output, network)
    errArray = copy.deepcopy(network)
    derivArray = copy.deepcopy(network)
    for i in range(len(network)):
        for j in range(len(network[i])):
            for k in range(len(network[i][j])):
                #initializes networkCopy to be the same as network
                networkCopy = copy.deepcopy(network)
                networkCopy[i][j][k] += step
                #if it's postitive, it's an improvement. if negative, not an improvement
                errArray[i][j][k] = initial_err - getSquaredError(input_list, output_list, networkCopy)
                derivArray[i][j][k]= (errArray[i][j][k]/step)
    return errArray, derivArray

def scaleWeight(input_list, output_list, network, step):    
    ErrArray, derivArray = errArray(input_list, output_list, network, step)
    #initializes old_error
    old_err = getSquaredError(input_list, output_list, network)
    #steps through network
    for i in range(len(network)):
        for j in range(len(network[i])):
            for k in range(len(network[i][j])):
                #adds a step proportional to the change in error and step size
                network[i][j][k] += ErrArray[i][j][k]*step
                #gets the new error
                err = getSquaredError(input_list, output_list, network)
                #repeats 5 times, or until error begins to increase
                while old_err > err:
                    for p in range(5):
                        network[i][j][k] += ErrArray[i][j][k]*step
                        err = getSquaredError(input_list, output_list, network)
                    break
                #reinitializes old_error
                old_err = err
                print(old_err)
    return network, err
    
Input, Output = createData(300)
network, err = getOKNetwork(Input, Output)
print(network, err)
print("Error Array")

for i in range(100): 
    new_network, err = scaleWeight(Input, Output, network, 0.1)
    network = new_network
    print(err)


Input2, Output2 = createData(100)
print("Average Squared Error of New Dataset:", getSquaredError(Input2, Output2, network))
for i in range(len(Input2)):
    predicted = runNetwork(Input2[i], network)
    print("Preidicted:", predicted, "Actual:", Output2[i])
    
