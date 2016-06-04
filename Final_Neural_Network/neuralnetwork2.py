# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:51:35 2016

@author: Lily
"""

import math
import random
import numpy as np

#creates a dataset of x, y values, returns 1 if x > y, -1 if y < x
def createData(length):
    data_list = []
    output_list = []
    for i in range(length):
        x = random.random()
        y = random.random()
        if x/y > 1: 
            above_line = 1
        elif x/y == 1: 
            above_line = 0
        elif x/y < 1: 
            above_line = -1
            
        data_list.append([x, y])
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
    return np.array(layer)
    
#creates a network of arrays
def createNetwork(hid_layer_number, init_input_number, layer_size):
    layers = []
    layers.append(createLayer(layer_size, init_input_number))
    for i in range(hid_layer_number):
        layers.append(createLayer(layer_size, layer_size))
    layers.append(createLayer(1, layer_size))
    return np.array(layers)

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
    return round(output_list[0])
    
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

#makes an array of the change in accuracy given an initial step
def derivArray(input_list, output_list, network, initial_step):
    init_acc = getAccuracy(input_list, output_list, network)[0]
    print("Initial Accuracy:", init_acc)
    networkDeriv = network
    for i in range(len(networkDeriv)):
        for j in range(len(networkDeriv[i])):
            for k in range(len(networkDeriv[i][j])):
                networkCopy = network
                networkCopy[i][j][k]+=initial_step
                networkDeriv[i][j][k] = (init_acc - getAccuracy(input_list, output_list, networkCopy)[0])/initial_step
    return networkDeriv
    
def accuracyArray(input_list, output_list, network, initial_step):
    init_acc = getAccuracy(input_list, output_list, network)[0]
    print("Initial Accuracy:", init_acc)
    networkAcc = network
    saved_network = network
    for i in range(len(networkAcc)):
        for j in range(len(networkAcc[i])):
            for k in range(len(networkAcc[i][j])):
                networkCopy = network
                #checks to see if network and network copy are the same thing
                #they are
                if networkCopy[i][j][k] == networkCopy[i][j][k] == saved_network[i][j][k]:
                    #print("network copy is network is saved network")
                    ok = 0
                else:
                    print("I AM BROKEN")
                    break
                networkCopy[i][j][k] = (networkCopy[i][j][k] + initial_step)
                acc1 = getAccuracy(Input, Output, networkCopy)[0]
                acc2 = getAccuracy(Input, Output, networkCopy)[0]
                if (acc1 == acc2):
                    #print("accuracy is accuracy")
                    networkAcc[i][j][k] = acc1
                    #print("networkAcc", networkAcc[i][j][k])
                    #print("acc1", acc1)
                else: 
                    print("accuracy function is broken")
                    break
    return networkAcc
"""
                if (networkCopy[i][j][k]-initial_step) != network[i][j][k]:
                    print("something went wrong")
                    break
                else:
                    print("ok")
                networkDeriv[i][j][k] = init_acc - getAccuracy(input_list, output_list, networkCopy)[0]
    return networkDeriv
"""

#cycles through 20 randomly generated networks until it finds the most accurate one
def getOKNetwork(input_list, output_list):
    network = createNetwork(3, 2, 5) #three hidden layers, 2 inputs, 5 nodes/layer
    accuracy = getAccuracy(input_list, output_list, network)[0]
    print(accuracy)
    for i in range(50):
        new_network = createNetwork(3, 2, 5)
        new_accuracy = getAccuracy(input_list, output_list, new_network)[0]
        print(new_accuracy)
        if new_accuracy > accuracy:
            print("found better acc")
            network = new_network
            accuracy = new_accuracy
        print(accuracy)
    return network, accuracy

Input, Output = createData(100)
#network, acc = getOKNetwork(Input, Output)
network, acc = getOKNetwork(Input, Output)
print("final accuracy:", acc)
print("acc for loop")
for i in range(30):
    print(getAccuracy(Input, Output, network)[0])
print("start array test")
print(accuracyArray(Input, Output, network, 1))
print(accuracyArray(Input, Output, network, 1))
#accuracyArray(Input, Output, network, 1)
#network = createNetwork(1, 2, 5)
#print("accuracy:", getAccuracy(Input, Output, network)[0])
#print("accuracy:", getAccuracy(Input, Output, network)[0])
#print(accuracyArray(Input, Output, network, 1))
#print(accuracyArray(Input, Output, network, 1))
