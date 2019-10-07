# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:18:01 2019

@author: sjs2a
"""

from abc import ABC, abstractmethod

"""
add processor base class
"""

class Processor(ABC):
    def __init__(self, input_):
        self._input = input_.reader()
        self._results = []
        
    @abstractmethod
    def processInput(self, input_):
        pass
        
    @abstractmethod
    def validateInput(self, input_):
        pass
    
    #TODO: should be able to read from queue
    def process(self):
        for inputValues in self._input:
            self._results = self.processInput(inputValues)

"""
add a type of processor which takes in the input class reference
"""       
class EulerProcessor(Processor):
    def __init__(self, input_):
        super().__init__(input_)
        self._max = 0
    
    def add(self, x, y, orig_value):
        value = max(x+y, orig_value)      
        self._max = max(value, self._max)
        return value
        
    def getParents(self, i):
        if i == 0:
            return (i,)
        elif i == len(self._results):
            return (i-1,)
        return (i-1, i)
    
    def processInput(self, inputValues):
        if not len(self._results): 
            inputValues = list(map(lambda x : int(x), inputValues))
            self._max = max(inputValues)
            return inputValues  
        
        for i, val in enumerate(inputValues):
            x = int(val)
            indices = self.getParents(i)
            for index in indices:  
                inputValues[i] = self.add(self._results[index], x, int(inputValues[i]))
        return inputValues
    
    def getMax(self):
        return self._max
    
    def validateInput(self, input_):
        return True
