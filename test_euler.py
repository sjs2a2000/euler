# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 07:09:24 2019

@author: sjs2a
"""

import unittest

#TODO: test negative input
#TODO: test 0 input
#TODO: test extra line empty
#TODO: test with streaming input

import logging
from functools import reduce
from InputProcessor import InputFile 
from OutputProcessor import EulerProcessor
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestInput(unittest.TestCase):

    def test_noinputfile(self):
        input_f = r"c:\users\sjs2a\Downloads\triangle_no_input.txt"
        self.assertFalse(InputFile(input_f).inputValid())
    
    def test_smallinputfile(self):
        input_f = r"c:\users\sjs2a\Downloads\triangle_input_reduce.txt"
        reader = InputFile(input_f).readInput()        
        self.assertTrue(reduce((lambda x, y: x + 1), reader, 0), 10)
    
    def test_largeinputfile(self):
        input_f = r"c:\users\sjs2a\Downloads\triangle_input.txt"
        reader = InputFile(input_f).readInput()  
        self.assertTrue(reduce((lambda x, y: x + 1), reader, 0), 100)

    def test_throwNoInput(self):
        input_f = r"c:\users\sjs2a\Downloads\triangle_no_input.txt"
        with self.assertRaises(Exception): InputFile(input_f).readInput()
     
    def test_emptyFile(self):
        input_f = r"c:\users\sjs2a\Downloads\triangle_empty_input.txt"
        with self.assertRaises(Exception): InputFile(input_f).readInput()
        pass
    
    def test_emptylineInfile(self):
        pass
        
    def test_streamInput(self):
        pass

class TestProcessor(unittest.TestCase):
    def test_eulerNoInput(self):
        inputf = "no_file"
        reader = InputFile(inputf)
        with self.assertRaises(Exception): EulerProcessor(reader)
    
    def test_eulerOneLine(self):
        inputf = r'c:\users\sjs2a\Downloads\triangle_input_1line.txt'
        reader = InputFile(inputf)
        processor = EulerProcessor(reader)
        processor.process()
        self.assertEqual(processor.getMax(), 1)
    
    def test_eulerTenLines(self):
        inputf = r'c:\users\sjs2a\Downloads\triangle_input_10line.txt'
        reader = InputFile(inputf)
        processor = EulerProcessor(reader)
        processor.process()
        self.assertEqual(processor.getMax(), 401)
    
    def test_eulerHundredLines(self):
        inputf = r'c:\users\sjs2a\Downloads\triangle_input.txt'
        reader = InputFile(inputf)
        processor = EulerProcessor(reader)
        processor.process()
        self.assertEqual(processor.getMax(), 7272)
    
    def test_eulerBaseInput(self):
        inputf = r'c:\users\sjs2a\Downloads\triangle_base_input.txt'
        reader = InputFile(inputf)
        processor = EulerProcessor(reader)
        processor.process()
        self.assertEqual(processor.getMax(), 23)
        
    def test_eulerNegInput(self):
        inputf = r'c:\users\sjs2a\Downloads\triangle_input_neg.txt'
        reader = InputFile(inputf)
        processor = EulerProcessor(reader)
        processor.process()
        self.assertEqual(processor.getMax(), -1)
    
class TestInputAndProcessor(unittest.TestCase):
    def test_all(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
