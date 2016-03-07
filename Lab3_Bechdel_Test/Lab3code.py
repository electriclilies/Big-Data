# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 13:56:54 2016

@author: Lily
"""

import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
import scipy.stats
import csv

with open('movies.csv', 'r') as f:
    reader = csv.reader(f)
    data_list = list(reader)

del(data_list[0])

year = [] #0
title = [] #2
test = [] #3 (includes whether there is disagreement)
clean_test = [] #4
binary = [] #5
budget_2013 = [] #10
domgross_2013 = [] #11
intgross_2013 = [] #12
tuple_list = []

dom_budget_ratio = [] #I am calculating this
int_budget_ratio = [] #I am calculating this

removed = 0
for jj in range(len(data_list)):
        #exclude datasets with N/A for domestic gross 2013 and international gross 2013
    if (data_list[jj][11] == "#N/A") or (data_list[jj][12] == "#N/A"):
        removed+=1
    else:
        year.append(int(data_list[jj][0]))
        title.append(data_list[jj][2])
        test.append(data_list[jj][3])
        clean_test.append(data_list[jj][4])
        binary.append(data_list[jj][5])
        budget_2013.append(int(data_list[jj][10]))
        domgross_2013.append(int(data_list[jj][11]))
        intgross_2013.append(int(data_list[jj][12]))
        #ratio = domestic gross 2013/budget
        dom_budget_ratio.append((int(data_list[jj][11])/int(data_list[jj][10])))
        #ratio = international gross 2013/budget
        int_budget_ratio.append(int(data_list[jj][12])/int(data_list[jj][10]))
        
for kk in range(len(year)):
    Tuple = (title[kk],#0
            year[kk],#1
            binary[kk],#2
            clean_test[kk],#3
            budget_2013[kk],#4 
            domgross_2013[kk],#5
            intgross_2013[kk], #6
            dom_budget_ratio[kk],#7
            int_budget_ratio[kk]) #8
    tuple_list.append(Tuple)
                

domgross_2013f = []
domgross_2013p = []
intgross_2013f = []
intgross_2013p = []
budget_2013f = []
budget_2013p = []
dom_budget_ratiof = []
dom_budget_ratiop = []
int_budget_ratiof = []
int_budget_ratiop = []

""" 
#WHY DID I WRITE THIS? WHO KNOWS
def organize(tuple_array, element):
    org_array = tuple_array
    for hh in len(org_array):
        try: 
            sorted(org_array, org_array[element])
        except:
            print("error")
    return org_array
"""

def passing_percent(tuple_array):
    passing = 0
    for pp in range(len(tuple_array)):
        if (tuple_array[pp][2] == "PASS"):
            passing+=1
    return (passing/(len(tuple_array)))*100
    

for kk in range(len(domgross_2013)):
    if binary[kk] == "FAIL":
        domgross_2013f.append(domgross_2013[kk])
        intgross_2013f.append(intgross_2013[kk])
        budget_2013f.append(budget_2013[kk])
        dom_budget_ratiof.append(dom_budget_ratio[kk])
        int_budget_ratiof.append(int_budget_ratio[kk])
    else:
        domgross_2013p.append(domgross_2013[kk])
        intgross_2013p.append(intgross_2013[kk])
        budget_2013p.append(budget_2013[kk])
        dom_budget_ratiop.append(dom_budget_ratio[kk])
        int_budget_ratiop.append(int_budget_ratio[kk])
        
top_dom_gross = sorted(tuple_list, key=lambda s: -s[5])
top100_dom_gross = []
for ff in range(99):
    top100_dom_gross.append(top_dom_gross[ff])

#percent of movies that pass/fail the test
print("Percent passing:", (len(domgross_2013p)/len(domgross_2013))*100)
print("Percent failing:", (len(domgross_2013f)/len(domgross_2013))*100)
print("\n")


#means of domestic gross of all movies, passing movies and failing movies
print("Dom gross mean:", stat.mean(domgross_2013))
print("Dom ross mean f:", stat.mean(domgross_2013f))
print("Dom ross mean p:", stat.mean(domgross_2013p))
print("\n")

#difference between mean of domestic gross passing/failing and mean of all movies
print("Dom $above/below mean f", stat.mean(domgross_2013f)-stat.mean(domgross_2013))
print("Dom $above/below mean p", stat.mean(domgross_2013p)-stat.mean(domgross_2013))
print("\n")


#means of international gross of all movies, passing movies and failing movies
print("Int gross mean:", stat.mean(intgross_2013))
print("Int gross mean f:", stat.mean(intgross_2013f))
print("Int gross mean p:", stat.mean(intgross_2013p))
print("\n")


#difference between mean of international gross passing/failing and mean of all movies
print("Int $above/below mean f", stat.mean(intgross_2013f)-stat.mean(intgross_2013))
print("Int $above/below mean p", stat.mean(intgross_2013p)-stat.mean(intgross_2013))
print("\n")

#means of budget of all movies, passing movies and failing moves
print("Budget mean:", stat.mean(budget_2013))
print("Budget mean f:", stat.mean(budget_2013f))
print("Budget mean p:", stat.mean(budget_2013p))
print("\n")

#difference between mean of passing/failing and mean of all movies
print("$above/below mean f", stat.mean(budget_2013f)-stat.mean(budget_2013))
print("$above/below mean p", stat.mean(budget_2013p)-stat.mean(budget_2013))
print("\n")

#mean of the ratio of domestic gross to budget of all movies, passing movies and failing movies
print("dom_gross/budget ratio mean:", stat.mean(dom_budget_ratio))
print("dom_gross/budget ratio mean f:", stat.mean(dom_budget_ratiof))
print("dom_gross/budget ratio mean p:", stat.mean(dom_budget_ratiop))
print("\n")

#mean of the ratio of international gross to budget of all movies, passing movies and failing movies
print("int_gross/budget ratio mean:", stat.mean(int_budget_ratio))
print("int_gross/budget ratio mean f:", stat.mean(int_budget_ratiof))
print("int_gross/budget ratio mean p:", stat.mean(int_budget_ratiop))
print("\n")


#histograms of domestic gross, all movies
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.set_yscale("log")
plt.hist(domgross_2013, bins=(0, 0.2*10**9, 0.4*10**9, 0.6*10**9, 0.8*10**9, 1.0*10**9, 1.2*10**9, 1.4*10**9))
plt.axis([0, 1.4*10**9, 0, 1500])
plt.title("Gross Domestic Product of All Movies (Log Scale)")

#histograms of domestic gross, failing movies
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.set_yscale("log")
plt.hist(domgross_2013f, bins=(0, 0.2*10**9, 0.4*10**9, 0.6*10**9, 0.8*10**9, 1.0*10**9, 1.2*10**9, 1.4*10**9))
plt.axis([0, 1.4*10**9, 0, 1500])
plt.title("Gross Domestic Product of Failing Movies (Log Scale)")

#histograms of domestic gross, passing movies
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.set_yscale("log")
plt.hist(domgross_2013p, bins=(0, 0.2*10**9, 0.4*10**9, 0.6*10**9, 0.8*10**9, 1.0*10**9, 1.2*10**9, 1.4*10**9))
plt.axis([0, 1.4*10**9, 0, 1500])
plt.title("Gross Domestic Product of Passing Movies (Log Scale)")


#histogram of the ratio of domestic gross to budget
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.set_yscale("log")
plt.hist(dom_budget_ratio, bins=(100))
plt.axis([0, 200, 0, 1500])
plt.title("Ratio of Domestic Gross to Budget for All Movies (Log scale)")

#histogram of the ratio of domestic gross to budget for failing movies
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.set_yscale("log")
plt.hist(dom_budget_ratiof, bins=(100))
plt.axis([0, 200, 0, 1500])
plt.title("Ratio of Domestic Gross to Budget for Failing Movies (Log scale)")


#histogram of the ratio of domestic gross to budget for passing
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.set_yscale("log")
plt.hist(dom_budget_ratiop, bins=(100))
plt.axis([0, 200, 0, 1500])
plt.title("Ratio of Domestic Gross to Budget for Passing Movies (Log scale)")


#scatter plot of budget vs domestic gross of all movies
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.scatter(budget_2013, domgross_2013)
plt.title("All Movies")
plt.xlabel("Budget in 2013 Dollars")
plt.ylabel("Domestic Gross in 2013 Dollars")

#scatter plot of budget vs domestic gross of passing movies
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.scatter(budget_2013p, domgross_2013p)
plt.title("Passing Movies")
plt.xlabel("Budget in 2013 Dollars")
plt.ylabel("Domestic Gross in 2013 Dollars")

#scatter plot of budget vs domestic gross of failing movies
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.scatter(budget_2013f, domgross_2013f)
plt.title("Failing Movies")
plt.xlabel("Budget in 2013 Dollars")
plt.ylabel("Domestic Gross in 2013 Dollars")

#COLORED scatter plot of budget vs domestic gross of passing (green) and failing movies (red)
secondPlot = plt.figure()
ax2 = secondPlot.add_subplot(111)
ax2.scatter(budget_2013f, domgross_2013f, c=[1,0,0])
ax2.scatter(budget_2013p, domgross_2013p, c=[0,1,0])
plt.title("All Movies: Passing (green) and Failing (red)")
plt.xlabel("Budget in 2013 Dollars")
plt.ylabel("Domestic Gross in 2013 Dollars")

#top 100 grossing movies (domestically)
