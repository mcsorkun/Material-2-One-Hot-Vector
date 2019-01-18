#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:53:57 2019

@author: Murat Cihan Sorkun
"""

import pandas as pd
import matplotlib.pyplot as pyplot
import re

def main():
    data = pd.read_csv('2d-materials-list.csv', header=0)
    formulas= data['Formula'].values
    
    allElementsList = CreateElementList(formulas)
    elementsCount = CountElements(formulas,allElementsList)
    pyplot.figure(figsize=(14,5))
    pyplot.bar(allElementsList,elementsCount, width = 1/2)
    
    oneHotVector = CreateOneHotVector(formulas,allElementsList)
    oneHotVector.to_csv("OneHotVector.csv", sep=',', encoding='utf-8')
    
    print("Resulst are written in file:OneHotVector.csv")



#Create list for all elements dataset includes
def CreateElementList(formulas):

    allElementsList=[]
    for formula in formulas:
        elementList=re.findall('[A-Z][^A-Z]*', formula)
        for elem in elementList:
            element, number = splitNumber(elem)
            if not element in allElementsList:
                allElementsList.append(element)
    
    return allElementsList


#parses elements and number of occurences from element-number couple
def splitNumber(text):

    element = text.rstrip('0123456789')
    number = text[len(element):]
    if number=="":
        number=1
    return element, int(number)


#counts number of occurences from the formula list     
def CountElements(formulas,allElementsList):

    elementCounts=[0]*len(allElementsList)
    for formula in formulas:
        elementList=re.findall('[A-Z][^A-Z]*', formula)
        for elem in elementList:
            element, number = splitNumber(elem)
            elementIndex=allElementsList.index(element)
            elementCounts[elementIndex]=elementCounts[elementIndex]+1
    
    return elementCounts

#parses elements and number of occurences from the formula list and create one hot vector    
def CreateOneHotVector(formulas,allElementsList):

    vectors = []   
    for formula in formulas:
        elementVector=[0]*len(allElementsList)
        elementList=re.findall('[A-Z][^A-Z]*', formula)
        for elem in elementList:
            element, number = splitNumber(elem)
            elementIndex=allElementsList.index(element)
            elementVector[elementIndex]=number
        vectors.append(elementVector)    
    oneHotVectorDF=pd.DataFrame(index = formulas, data=vectors, columns=allElementsList)
    
    return oneHotVectorDF

if __name__== "__main__":
    main()


