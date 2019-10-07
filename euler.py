from abc import ABC, abstractmethod
import logging
import argparse

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
            return list(inputValues)    
        
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

def main():       
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input',type=str, help='input file', default=r'c:\users\sjs2a\Downloads\triangle_input_reduce.txt')
    args = parser.parse_args()
    reader = InputFile(args.input)
    processor = EulerProcessor(reader)
    processor.process()
    logger.info("maximum value = {}".format(processor.getMax()))
     
if __name__ == "__main__":
    main()
