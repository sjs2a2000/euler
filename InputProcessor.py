# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:10:03 2019

@author: sjs2a
"""

from abc import ABC, abstractmethod
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
 
"""
provide base reader class for all input
"""
   
class Input(ABC):
    @abstractmethod
    def reader(self):
        pass

"""
File input class
"""
    
class InputFile(Input):
    def __init__(self, filename_):
        self.fname=filename_
    
    #TODO: put input into queue
    def reader(self):
        with open(self.fname) as f:
            line = f.readline()
            while line:          
                yield line.split()
                line = f.readline()
