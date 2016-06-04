# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 09:22:15 2016

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
        if (x/y) > 1: 
            above_line = 1
        elif (x/y) == 1: 
            above_line = 0
        elif (x/y) < 1: 
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

#cycles through 20 randomly generated networks until it finds the most accurate one
def getOKNetwork(input_list, output_list):
    network = createNetwork(1, 2, 2) #three hidden layers, 2 inputs, 5 nodes/layer
    accuracy = getAccuracy(input_list, output_list, network)[0]
    print(accuracy)
    for i in range(50):
        new_network = createNetwork(1, 2, 2)
        new_accuracy = getAccuracy(input_list, output_list, new_network)[0]
        print(new_accuracy)
        if new_accuracy > accuracy:
            print("found better acc")
            network = new_network
            accuracy = new_accuracy
        print(accuracy)
    return network, accuracy

def accArray(input_list, output_list, network, step):
    accuracy_list = []
    initial_acc = getAccuracy(Input, Output, network)[0]
    print(initial_acc)
    networkAcc = network
    testAcc = network
    for i in range(2):
        for i in range(len(network)):
            for j in range(len(network[i])):
                for k in range(len(network[i][j])):
                    inner_acc = []
                    #initializes networkCopy to be the same as network
                    networkCopy = network
                    if initial_acc != getAccuracy(Input, Output, networkCopy)[0]: #I didn't change network at all though...
                        print ("ARG")
                        #break
                    else:
                        print("initial acc == newacc")
                    #networkAcc[i][j][k] = getAccuracy(Input, Output, network)[0]
        #print(networkAcc)
                        
                
""" the problem is in what is below
                    testAcc[i][j][k] = getAccuracy(Input, Output, networkCopy)[0]
                    networkCopy[i][j][k]=(network[i][j][k]+step)
                    inner_acc.append(getAccuracy(input_list, output_list, networkCopy)[0])
                    networkAcc[i][j][k]=getAccuracy(input_list, output_list, networkCopy)[0]
    for h in range(len(accuracy_list)):
        if accuracy_list[i][0] != accuracy_list[i][1]:
            print("I am broken")
            break
    return testAcc, networkAcc
"""

Input, Output = createData(100)
print(Input, Output)
print(len(Output))

network, acc = getOKNetwork(Input, Output)
print("final accuracy:", acc)
print("start array test")
print(accArray(Input, Output, network, 0.1))
print(accArray(Input, Output, network, 1))
#things to ask ms anderson about: initial accuracy is not the same as the accuracy created in the for loop. did not change network... 
#also accuracy test in for loop returns the same value every time