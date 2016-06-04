# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:45:23 2016

@author: Lily
"""
import math
import random
import numpy as np

#good function to learn: xor 
#single layer neural network cannot learn xor. proved by marvin minsky

#creates a list of random data points in the x, y plane, and whether they are above or below the y=x line
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

#takes the input for each node and multiplies it by the node's weights. returns 1 if > threshold, else 0
#possibly remove threshold?
def createOutput(input_list, weight_list):
    weighted_sum = 0
    for i in range(len(input_list)):
        weighted_sum+=weight_list[i]*input_list[i]
    #takes the hyperbolic tangent of the weighted sum
    return math.tanh(weighted_sum)

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

#creates an array of layers. cannot vary the number of nodes in each hidden layer
def createLayers(hid_layer_number, init_input_number, layer_size):
    layers = []
    layers.append(createLayer(layer_size, init_input_number))
    for i in range(hid_layer_number):
        layers.append(createLayer(layer_size, layer_size))
    layers.append(createLayer(1, layer_size))
    return np.array(layers)

def runNetwork(Input, network):
    #iterates through layers
    for i in range(len(network)): 
        #iterates through nodes in layers
        output_list = []
        for j in range(len(network[i])):
            output_list.append(createOutput(Input, network[i][j]))
        Input = output_list
    return round(output_list[0])

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

#randomly adjusts the weights until it finds a better one  
def trainNetwork(input_list, output_list, network):
    oldAccuracy = getAccuracy(input_list, output_list, network)[0]
    print("Initial Accuracy:", oldAccuracy, "%")
    for i in range(len(network)):
        for j in range(len(network[i])):
            for k in range(len(network[i][j])):
                old_weight = network[i][j][k]
                network[i][j][k] = random.random() #assigns a new random value to the edge
                newAccuracy = getAccuracy(input_list, output_list, network)[0] 
                tries=0
                while newAccuracy <= oldAccuracy:
                    tries+=1
                    network[i][j][k] = random.random()
                    newAccuracy = getAccuracy(input_list, output_list, network)[0]
                    if tries>250:
                        tries=0
                        network[i][j][k] = old_weight
                        print("no better weight found")
                        break
                tries=0
                oldAccuracy = newAccuracy
                print(oldAccuracy)
    return network, oldAccuracy

#moves weights up and down until it finds a good one
def trainNetwork2(input_list, output_list, network, step_size):
    oldAccuracy = getAccuracy(input_list, output_list, network)[0]
    print("Initial Accuracy:", oldAccuracy, "%")
    for i in range(len(network)):
        for j in range(len(network[i])):
            for k in range(len(network[i][j])):
                network[i][j][k]+=step_size #assigns a new random value to the edge
                newAccuracy = getAccuracy(input_list, output_list, network)[0] 
                if newAccuracy > oldAccuracy: 
                    while newAccuracy > oldAccuracy:
                        network[i][j][k]+=step_size
                        newAccuracy = getAccuracy(input_list, output_list, network)[0]
                        oldAccuracy = newAccuracy
                        network[i][j][k] += step_size
                        newAccuracy = getAccuracy(input_list, output_list, network)[0]
                        print(newAccuracy)
                else: 
                    network[i][j][k]+=(step_size*-2) #assigns a new random value to the edge
                    newAccuracy = getAccuracy(input_list, output_list, network)[0] 
                    while newAccuracy > oldAccuracy:
                        network[i][j][k]+=(step_size*-1)
                        newAccuracy = getAccuracy(input_list, output_list, network)[0]
                        oldAccuracy = newAccuracy
                        network[i][j][k]+=(step_size*-1)
                        newAccuracy = getAccuracy(input_list, output_list, network)[0]
                        print(newAccuracy)
               
#randomly adjusts the weights until it finds a better one  
def trainNetwork3(input_list, output_list, network, scale):
    oldAccuracy = getAccuracy(input_list, output_list, network)[0]
    print("Initial Accuracy:", oldAccuracy, "%")
    for i in range(len(network)):
        for j in range(len(network[i])):
            for k in range(len(network[i][j])):
                old_weight = network[i][j][k]
                network[i][j][k] = random.random() #assigns a new random value to the edge
                newAccuracy = getAccuracy(input_list, output_list, network)[0]
                tries=0
                while newAccuracy <= oldAccuracy:
                    tries+=1
                    network[i][j][k] *= scale * (0.5-random.random())*2.0
                    newAccuracy = getAccuracy(input_list, output_list, network)[0]
                    if tries>250:
                        tries=0
                        network[i][j][k] = old_weight
                        print("no better weight found")
                        break
                tries=0
                oldAccuracy = newAccuracy
                print(oldAccuracy)
    return network, oldAccuracy
               
#randomly adjusts the weights until it finds a better one  
def trainNetwork4(input_list, output_list, network, scale_init):
    scale = 1
    for x in range(1):
        scale *= scale_init
        for y in range(2):
            oldAccuracy = getAccuracy(input_list, output_list, network)[0]
            print("Initial Accuracy:", oldAccuracy, "%")
            for i in range(len(network)):
                for j in range(len(network[i])):
                    for k in range(len(network[i][j])):
                        old_weight = network[i][j][k]
                        network[i][j][k] += scale * (0.5-random.random())*2.0
                        #network[i][j][k] += random.random() * (0.5-random.random())*2.0 #assigns a new random value to the edge
                        newAccuracy = getAccuracy(input_list, output_list, network)[0]
                        tries=0
                        while newAccuracy <= oldAccuracy:
                            tries+=1
                            network[i][j][k] = old_weight
                            network[i][j][k] += scale * (0.5-random.random())*2.0
                            newAccuracy = getAccuracy(input_list, output_list, network)[0]
                            #if newAccuracy > 50: #SPECIFICALLY FOR WHEN I DO BACK PROPOGATION AFTER
                            #    break
                            if tries>250:
                                tries=0
                                network[i][j][k] = old_weight
                                print("no better weight found")
                                break
                        #print(network)
                        #print("\n")
                        tries=0
                        if newAccuracy > oldAccuracy: 
                            oldAccuracy = getAccuracy(input_list, output_list, network)[0]
                        print(oldAccuracy)
                        #if oldAccuracy >= 50:
                            #return network, oldAccuracy
    return network, oldAccuracy
               
#creates an array of the change in accuracy
def trainNetwork5(input_list, output_list, network, initial_step):
    init_acc = getAccuracy(input_list, output_list, network)[0]
    print("Initial Accuracy:", init_acc)
    networkAccuracy = network
    for i in range(len(networkAccuracy)):
        for j in range(len(networkAccuracy[i])):
            for k in range(len(networkAccuracy[i][j])):
                networkCopy = network
                networkCopy[i][j][k]+=initial_step
                networkAccuracy[i][j][k] = init_acc - getAccuracy(input_list, output_list, networkCopy)[0]
    
    print(init_acc, "\n", networkAccuracy)
    
def trainNetwork6(input_list, output_list, initial_step):
    network = createLayers(3, 2, 5)
    accuracy = getAccuracy(input_list, output_list, network)[0]
    print(accuracy)
    for i in range(20):
        new_network = createLayers(3, 2, 5)
        new_accuracy = getAccuracy(input_list, output_list, new_network)[0]
        print(new_accuracy)
        if new_accuracy > accuracy:
            network = new_network
            accuracy = new_accuracy
            print(accuracy)
    return network, new_accuracy
    """
    init_acc = getAccuracy(input_list, output_list, network)[0]
    print("Initial Accuracy:", init_acc)
    networkAccuracy = network
    for i in range(len(networkAccuracy)):
        for j in range(len(networkAccuracy[i])):
            for k in range(len(networkAccuracy[i][j])):
                networkCopy = network
                networkCopy[i][j][k]+=initial_step
                networkAccuracy[i][j][k] = init_acc - getAccuracy(input_list, output_list, networkCopy)[0]
    
    print(init_acc, "\n", networkAccuracy)
    """
"""
NOTES:
-some networks train up really fast, others get stuck in local mins
-usually you can get them up to 50%, however, they get stuck after that
-then I check and see how much changing each weight effects the accuracy

because data set is 100, accuracy should always be an integer.. like 30.0 not 32.222... this isn't always true which is concerning

THE PROGRAM ISNT SUPPOSED TO LET ACCURACY GO DOWN BUT IT DOES SOMETIMES. 

maybe try doing a bunch, finding a line of best fit? 
"""  
        
Input, Output = createData(100)
network = createLayers(3, 2, 5) #1 hidden layers, 2 initial inputs, 3 nodes/layer
print(getAccuracy(Input, Output, network))
trainNetwork5(Input, Output, network, 1)
trainNetwork5(Input, Output, network, 1)


