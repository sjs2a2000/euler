-*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:10:03 2019

@author: sjs2a
"""

from abc import ABC, abstractmethod
import logging
import os.path 
import os

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
 
"""
provide base reader class for all input
"""
   
class Input(ABC):
    def __init__(self):
        self.error = ""
        
    @abstractmethod
    def inputValid(self):
        pass
    
    @abstractmethod
    def reader(self):
        pass
    
    def readInput(self):
        if self.inputValid():
            return self.reader()
        else:
            raise Exception("invalid input: " + self.error)
"""
File input class
"""
    
class InputFile(Input):
    def __init__(self, filename_):
        self.fname=filename_
    
    def inputValid(self):
        if os.path.exists(self.fname) and os.path.isfile(self.fname) and os.stat(self.fname).st_size > 0:
            return True
        self.error = "invalid file input, file does not exist or is not a file or is empty: " + self.fname
        return False
    
    #will throw an error if yopu don't check the reader valid
    def reader(self):
        with open(self.fname) as f:
            line = f.readline()
            while line:          
                yield line.split()
                line = f.readline()
