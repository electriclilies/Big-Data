# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:05:28 2016

@author: Lily
"""

#%matplotlib inline #impt for graphing in jupyter notebook, but messes up spyder
import csv
import random
import math
import operator
import statistics as stat
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

##idk if you need all of these but some are definately required

def includeIfValue(some_tuple_list, element, operator, value):
    new_list = []
    if (operator == "=="):
        for ii in range(len(some_tuple_list)):
            if some_tuple_list[ii][element] == value:
                new_list.append(some_tuple_list[ii])
    elif  (operator == "<"):
        for ii in range(len(some_tuple_list)):
            if some_tuple_list[ii][element] < value:
                new_list.append(some_tuple_list[ii])
    elif (operator == ">"):
        for ii in range(len(some_tuple_list)):
            if some_tuple_list[ii][element] > value:
                new_list.append(some_tuple_list[ii])
    return new_list
    
#reads in a tuple list, a function that returns a boolean (input is a tuple), and a value
#returns a list of tuples
def newTupleList(some_tuple_list, f, Value):
    new_list = []
    for ii in range(len(some_tuple_list)):
        if (f(some_tuple_list[ii], Value)):
            new_list.append(some_tuple_list[ii])
    return new_list

#prints an element of a tuple list
def printElementOf(some_tuple_list, element):
    for ii in range(len(some_tuple_list)):
        print(some_tuple_list[ii][element])

#turns an element of a tuple list into an array
def tupleList(some_tuple_list, element):
    new_list = []
    for ii in range(len(some_tuple_list)):
        new_list.append(some_tuple_list[ii][element])
    return new_list

#finds the percent of an element in a list that is a value
def percent(some_tuple_list, element, value):
    elementPresent = 0
    for ii in range(len(some_tuple_list)):
        if some_tuple_list[ii][element] == value:
            elementPresent+=1
    return (elementPresent/len(some_tuple_list))*100

#averages a column in a tuple list (averageType = mean, median or mode)
def averageTuple(some_tuple_list, element, averageType):
    new_list = []
    for ii in range(len(some_tuple_list)):
        new_list.append(some_tuple_list[ii][element])
    try:
        if averageType == "mean":
            return stat.mean(new_list)
        if averageType == "median":
            return stat.median(new_list)
        if averageType == "mode":
            return stat.mode(new_list)
    except:
        print("No data points found")
        return 0
        
#finds the correlation coefficient bewteen two elements in a tuple array
def pearsonRTuple(some_tuple_list, element1, element2):
    new_list1 = []
    new_list2 = []
    for ii in range(len(some_tuple_list)):
        new_list1.append(some_tuple_list[ii][element1])
        new_list2.append(some_tuple_list[ii][element2])
    return scipy.stats.pearsonr(new_list1, new_list2)[0]
    
#creates a histogram of an element in a tuple array, with a specified bin size
#if bin_size = 0, auto sets binsize
def createHist(some_tuple_list, element, bin_size):
    new_list = []
    for ii in range(len(some_tuple_list)):
        new_list.append(some_tuple_list[ii][element])
    maximum = int(math.ceil(max(new_list)))
    if bin_size != 0: 
        bins_list = []
        for hh in range(int(math.ceil(maximum/bin_size))):
            bins_list.append(bin_size*hh)
        plt.hist(new_list, bins_list)
    else: 
        plt.hist(new_list)

def createScatter(some_tuple_list, elementx, elementy):
    new_listx = []
    new_listy = []
    for ii in range(len(some_tuple_list)):
        new_listx.append(some_tuple_list[ii][elementx])
        new_listy.append(some_tuple_list[ii][elementy])
    plt.scatter(new_listx, new_listy)
    
def createScatterColor(some_tuple_list, elementx, elementy, color):
    new_listx = []
    new_listy = []
    for ii in range(len(some_tuple_list)):
        new_listx.append(some_tuple_list[ii][elementx])
        new_listy.append(some_tuple_list[ii][elementy])
    plt.scatter(new_listx, new_listy, c=color)
    
def newPlot(title, xlabel, ylabel):
    secondPlot = plt.figure()
    ax2 = secondPlot.add_subplot(111)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def newLogPlotY(title, xlabel, ylabel):
    secondPlot = plt.figure()
    ax2 = secondPlot.add_subplot(111)
    ax2.set_yscale("log")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
def newLogPlotX(title, xlabel, ylabel):
    secondPlot = plt.figure()
    ax2 = secondPlot.add_subplot(111)
    ax2.set_xscale("log")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)