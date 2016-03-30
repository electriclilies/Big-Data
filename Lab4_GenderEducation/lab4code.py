# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:34:48 2016

@author: Lily
"""
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
import scipy.stats
import csv
import math

#read in contraception data
with open('contraceptiveUN.csv', 'r') as f:
    reader = csv.reader(f)
    data_list = list(reader)

removed = 0
# ".." is no value

#contraception arrays

code = [] #column 0
country = [] #column 1
year = [] #column 2
any_method = [] #column 3
modern_method = [] #column 4
condom = [] #column 5
    
for kk in range(len(data_list)-1):
    
    code.append(data_list[kk][0])
    country.append(data_list[kk][1])
    year.append(float(data_list[kk][2]))
    any_method.append(data_list[kk][3])
    modern_method.append(data_list[kk][4])
    condom.append(data_list[kk][3])
    
#create list of contraception data
contraception_list = []
for ii in range(len(country)):
    if (any_method[ii] != '..') and (modern_method[ii] != '..') and (condom[ii] != '..'):
        Tuple = (code[ii], 
                 country[ii], 
                 year[ii], 
                 float(any_method[ii]), 
                 float(modern_method[ii]), 
                 float(condom[ii]),
                 float(any_method[ii])-float(modern_method[ii]),
                 float(any_method[ii])-float(condom[ii]),
                 float(modern_method[ii])-float(condom[ii]))
        contraception_list.append(Tuple)

#read in ppp GDP per capita data
with open('pppGDPperCapita.csv', 'r') as f:
    reader = csv.reader(f)
    data_list2 = list(reader)

#GDP arrays
removed2 = 0
# ".." is no value
GDP_list = []

del(data_list2[0])

#creates a tuple list of the countries and thier GDPs by year
for ii in range(len(data_list2)):
    #1990
    if(data_list2[ii][4] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                 1990, #year
                 float(data_list2[ii][4])) #ppp GDP per capita
        GDP_list.append(Tuple)
    #2000
    if(data_list2[ii][5] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                2000, #year
                float(data_list2[ii][5])) #ppp GDP per capita
        GDP_list.append(Tuple)
    #2006
    if(data_list2[ii][6] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                 2006, #year
                 float(data_list2[ii][6])) #ppp GDP per capita
        GDP_list.append(Tuple)
    #2007
    if(data_list2[ii][7] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                2007, #year
                float(data_list2[ii][7])) #ppp GDP per capita
        GDP_list.append(Tuple)
    #2008
    if(data_list2[ii][8] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                 2008, #year
                 float(data_list2[ii][8])) #ppp GDP per capita
        GDP_list.append(Tuple)
    #2009
    if(data_list2[ii][9] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                2009, #year
                float(data_list2[ii][9])) #ppp GDP per capita
        GDP_list.append(Tuple)
    #2010
    if(data_list2[ii][10] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                2010, #year
                float(data_list2[ii][10])) #ppp GDP per capita
        GDP_list.append(Tuple)
    #2011
    if(data_list2[ii][11] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                 2011, #year
                 float(data_list2[ii][11])) #ppp GDP per capita
        GDP_list.append(Tuple)
    #2012
    if(data_list2[ii][12] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                 2012, #year
                 float(data_list2[ii][12])) #ppp GDP per capita
        GDP_list.append(Tuple)
    #2013
    if(data_list2[ii][13] != '..'):
        Tuple = (data_list2[ii][3], #country code (STR)
                data_list2[ii][2], #country name 
                 2007, #year
                 float(data_list2[ii][13])) #ppp GDP per capita
        GDP_list.append(Tuple)    

#country code file: creating a dictionary
with open('countrycodes.csv', 'r') as f:
    reader = csv.reader(f)
    data_list3 = list(reader)
    
del(data_list3[0])

country_code = {}
#creating dictionary: number code, string code
for jj in range(len(data_list3)): 
    country_code[data_list3[jj][0]] = data_list3[jj][2]

#literacy rates CSV
with open('literacyrates.csv', 'r') as f:
    reader = csv.reader(f)
    data_list4 = list(reader)
    
#LIST INDEX OUT OF RANGE
literacyRate = []
for ii in range(1, len(data_list4)):
    for kk in range(2, 25, 2): #from 2 to 25, skip by 2s
        if (data_list4[ii][kk] != '..') and (data_list4[ii][kk+1] !='..'):
            Tuple = (data_list4[ii][1], #country code (str)
                     float(data_list4[0][kk][0:4]), #year
                     float(data_list4[ii][kk]), #adult literacy rate 15+ female
                     float(data_list4[ii][kk+1])) #adult literacy rate 15+ male
            literacyRate.append(Tuple)
    
#GDP and Contraception Data: Overlapping Years
GDP_Contraception = []
for ii in range(len(contraception_list)):
    for kk in range(len(GDP_list)):
        if (country_code[contraception_list[ii][0]]==GDP_list[kk][0]) and (contraception_list[ii][2]==GDP_list[kk][2]):
            Tuple = (contraception_list[ii][0], #column 0: country code (number)
                    contraception_list[ii][1], #column 1: country name
                    contraception_list[ii][2], #column 2: year
                    contraception_list[ii][3], #column 3: any method
                    contraception_list[ii][4], #column 4: modern method
                    contraception_list[ii][5], #column 5: condom
                    GDP_list[kk][3], #column 6: GDP ppp
                    contraception_list[ii][6], #column 7: difference between anymethod and modern method) 
                    contraception_list[ii][7], #column 8: difference between anymethod and condom
                    contraception_list[ii][8]) #column 9: difference between modern method and condom
            GDP_Contraception.append(Tuple)
print("GDP_Contraception done")
#GDP, Contraception and Literacy Rates: Overlapping years
GDP_Contra_Lit = []
for ii in range(len(contraception_list)):
    for kk in range(len(GDP_list)):
        for jj in range(len(literacyRate)):
            if (country_code[contraception_list[ii][0]]==GDP_list[kk][0]==literacyRate[jj][0]) and (contraception_list[ii][2]==GDP_list[kk][2]==literacyRate[jj][1]):
                Tuple = (contraception_list[ii][0], #column 0: country code (number)
                        contraception_list[ii][1], #column 1: country name
                        contraception_list[ii][2], #column 2: year
                        contraception_list[ii][3], #column 3: any method
                        contraception_list[ii][4], #column 4: modern method
                        contraception_list[ii][5], #column 5: condom
                        GDP_list[kk][3], #column 6: GDP ppp
                        contraception_list[ii][6], #column 7: difference between anymethod and modern method) 
                        contraception_list[ii][7], #column 8: difference between anymethod and condom
                        contraception_list[ii][8], #column 9: difference between modern method and condom
                        literacyRate[jj][2], #column 10: adult literacy rate, FEMALE, 15+
                        literacyRate[jj][3]) #column 11: adult literacy rate, MALE, 15+ 
                GDP_Contra_Lit.append(Tuple)
                
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

def newLogPlot(title, xlabel, ylabel):
    secondPlot = plt.figure()
    ax2 = secondPlot.add_subplot(111)
    ax2.set_yscale("log")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


print("any method, modern method", pearsonRTuple(GDP_Contraception, 3, 4))
print("any method, condom", pearsonRTuple(GDP_Contraception, 3, 5))
print("modern method, condom", pearsonRTuple(GDP_Contraception, 4, 5))
print("GDP, any method", pearsonRTuple(GDP_Contraception, 3, 6))
print("GDP, modern method", pearsonRTuple(GDP_Contraception, 4, 6))
print("GDP, condom", pearsonRTuple(GDP_Contraception, 5, 6))

print("GDP, difference between any and modern method", pearsonRTuple(GDP_Contraception, 6, 7))
#print("GDP, difference between any method and condom", pearsonRTuple(GDP_Contraception, 6, 8))
print("GDP, difference between modern method and condom", pearsonRTuple(GDP_Contraception, 6, 9))
createScatter(GDP_Contraception, 3, 6)
newPlot("","","")
createScatter(GDP_Contraception, 4, 6)
newPlot("","","")
createScatter(GDP_Contraception, 5, 6)
newPlot("","","")
createScatter(GDP_Contraception, 2, 3)
print("mean contraception use", averageTuple(GDP_Contraception, 3, "mean"))
print("mean modern contraception use", averageTuple(GDP_Contraception, 4, "mean"))
print("mean condom use", averageTuple(GDP_Contraception, 5, "mean"))

print("median contraception use", averageTuple(GDP_Contraception, 3, "median"))
print("median modern contraception use", averageTuple(GDP_Contraception, 4, "median"))
print("median condom use", averageTuple(GDP_Contraception, 5, "median"))

print("mode contraception use", averageTuple(GDP_Contraception, 3, "mode"))
print("mode modern contraception use", averageTuple(GDP_Contraception, 4, "mode"))
print("mode condom use", averageTuple(GDP_Contraception, 5, "mode"))


print("mean literacy rate women", averageTuple(literacyRate, 2, "mean"))
print("mean literacy rate men", averageTuple(literacyRate, 3, "mean"))
print(len(GDP_Contra_Lit))
print("GDP, literacy rate F", pearsonRTuple(GDP_Contra_Lit, 6, 2))
print("literacy rate F, contraception (any)", pearsonRTuple(GDP_Contra_Lit, 3, 2))
print("GDP, any method", pearsonRTuple(GDP_Contra_Lit, 3, 6))
print("GDP, modern method", pearsonRTuple(GDP_Contra_Lit, 4, 6))
print("GDP, condom", pearsonRTuple(GDP_Contra_Lit, 5, 6))
print(len(GDP_Contra_Lit))