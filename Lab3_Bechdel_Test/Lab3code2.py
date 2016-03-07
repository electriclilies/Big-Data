# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:06:07 2016

@author: Lily
"""

import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
import scipy.stats
import csv
import math

with open('movies.csv', 'r') as f:
    reader = csv.reader(f)
    data_list = list(reader)

del(data_list[0])
tuple_list = []
removed = 0

for kk in range(len(data_list)):
        #exclude datasets with N/A for domestic gross 2013 and international gross 2013
    if (data_list[kk][11] == "#N/A") or (data_list[kk][12] == "#N/A"):
        removed+=1
    else:
                #0 title
        Tuple = (data_list[kk][2], 
                #1 year
                 int(data_list[kk][0]), 
                #2 binary
                data_list[kk][5], 
                #3 clean test (how did movie fail)
                data_list[kk][4],
                #4 test (includes whether there was disagreement)
                data_list[kk][3],
                #5 budget (2013 dollars)
                int(data_list[kk][10]),
                #6 domestic gross (2013 dollars)
                int(data_list[kk][11]),
                #7 international gross (2013 dollars)
                int(data_list[kk][12]),
                #8 domestic gross/budget ratio
                (int(data_list[kk][11])/int(data_list[kk][10])),
                #9 international gross/budget ratio (2013 dollars)
                (int(data_list[kk][12])/int(data_list[kk][10])))
            
    tuple_list.append(Tuple)
    
#function creates a new tuple list conaining tuples from the original
def includeIfValue(some_tuple_list, element, value):
    new_list = []
    for ii in range(len(some_tuple_list)):
        if some_tuple_list[ii][element] == value:
            new_list.append(some_tuple_list[ii])
    return new_list
    
#prints an element of a tuple list
def printElementOf(some_tuple_list, element):
    for ii in range(len(some_tuple_list)):
        print(some_tuple_list[ii][element])
        
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
    if averageType == "mean":
        return stat.mean(new_list)
    if averageType == "median":
        return stat.median(new_list)
    if averageType == "mode":
        return stat.mode(new_list)

#finds the correlation coefficient bewteen two elements in a tuple array
def pearsonRTuple(some_tuple_list, element1, element2):
    new_list1 = []
    new_list2 = []
    for ii in range(len(some_tuple_list)):
        new_list1.append(some_tuple_list[ii][element1])
        new_list2.append(some_tuple_list[ii][element2])
    return scipy.stats.pearsonr(new_list1, new_list2)
    
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
    
def newPlot(title, xlabel, ylabel):
    secondPlot = plt.figure()
    ax2 = secondPlot.add_subplot(111)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def newLogPlot(title, xlabel, ylabel):
    secondPlot = plt.figure()
    ax2 = secondPlot.add_subplot(111)
    ax2.set_yscale("log")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

newPlot("Budget", "Budget in 2013 Dollars", "Number of Occurences")
createHist(tuple_list, 5, 0)
newPlot("Budget vs Domestic Gross", "Budget in 2013 Dollars", "Domestic Gross in 2013 Dollars")
createScatter(tuple_list, 5, 6)

        
"""
passing_list = includeIfValue(tuple_list, 2, "PASS")
failing_list = includeIfValue(tuple_list, 2, "FAIL")
printElementOf(passing_list, 0)
print(averageTuple(passing_list, 5, "mean"))
print(averageTuple(failing_list, 5, "mean"))
print(percent(tuple_list,  2, "PASS"))
print(percent(tuple_list,  2, "FAIL"))
"""

#EXTRA PLOTS FROM LAB 3 IN JUPYTER NOTEBOOK: NOT TESTED IN THIS FILE!
"""
newPlot("Figure 6: \n means of all movies gross and budget", "bla", "bla")
createScatterColor(mean_gross_year, 1, 0, "green")
createScatterColor(mean_budget_year, 1, 0, "red")

newPlot("Figure 7: \n passing", "bla", "bla")
createScatterColor(mean_gross_yearp, 1, 0, "green")
createScatterColor(mean_budget_yearp, 1, 0, "red")

newPlot("Figure 8: \n failing", "bla", "bla")
createScatterColor(mean_gross_yearf, 1, 0, "green")
createScatterColor(mean_budget_yearf, 1, 0, "red")

newPlot("Figure 9: \n passing (green) and failing (orange) budget", "bla", "bla")
plt.axis([1970, 2020, 10**0, 0.5*10**9])
createScatterColor(mean_budget_yearp, 1, 0, "green")
createScatterColor(mean_budget_yearf, 1, 0, "red")

newPlot("Figure 10: \n passing (green) and failing (orange) domestic gross", "bla", "bla")
plt.axis([1970, 2020, 10**0, 0.8*10**9])
createScatterColor(mean_gross_yearp, 1, 0, "green")
createScatterColor(mean_gross_yearf, 1, 0, "red")




newLogPlot("bla", "year", "return on investment")
createScatter(tuple_list, 1, 8)
newLogPlot("bla", "year", "return on investment(p)")
createScatter(passing_movies, 1, 8)
newLogPlot("bla", "year", "return on investment(f)")
createScatter(failing_movies, 1, 8)

newLogPlot("bla", "year", "domestic gross")
createScatterColor(tuple_list, 1, 6, "orange")
newLogPlot("bla", "year", "domestic gross(p)")
createScatterColor(passing_movies, 1, 6, "orange")
newLogPlot("bla", "year", "domestic gross(f)")
createScatterColor(failing_movies, 1, 6, "orange")

newLogPlot("bla", "year", "budget")
createScatterColor(tuple_list, 1, 5, "pink")
newLogPlot("bla", "year", "budget(p)")
createScatterColor(passing_movies, 1, 5, "pink")
newLogPlot("bla", "year", "budget(f)")
createScatterColor(failing_movies, 1, 5, "pink")

"""