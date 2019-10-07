import logging
import argparse
from InputProcessor import InputFile 
from Processors import EulerProcessor
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
 
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
