# euler
## Description
Utilizes abiility to reduce paths and store in a single row table for dynamic programming.<br>
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.<br>
3<br>
7 4<br>
2 4 6<br>
8 5 9 3<br>
That is, 3 + 7 + 4 + 9 = 23.<br>
Find the maximum total from top to bottom .<br>

## Test Cases
* empty file : result is 0
* 1 row
* 10 rows
* not valid numbers
* negative numbers
    
## TODO: 
1. add unittests using python unit tests 
2. add classes in separate file
3. add timeit decorator to test performance 
4. apply validation to input
5. identify use cases on how the processor would be used
6. add an input processor that puts input into queue, and processor reading from queue
7. add to a git repo *** 
8. CICD
9. automate checkout and deploy on aws for testing

