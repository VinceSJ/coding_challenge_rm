# Coding challenge for RM
This repo contains answers to the interview questions sent by Andrew, done by me, Vincent.

Look inside each folder (q1, etc.) for a Python script that accomplishes the task set by each question. **Naming convention**: Q1 -> `q1.py`, etc. Folders may also contain additional material such as Readme, supporting files, and/or prep/experimentation.

**Unit tests**: For Q1 and Q2, you can find unit tests for the work done. They are in the appropriate folder and named as `test_q(#).py`.

For questions that rely on each other (Q2 on Q1, etc.), instead of referring to code in other scripts [the right way], I'm just going with the quick and dirty method of copy-pasting the pertinent parts. ~~Or wholesale copying the JSON file produced in Q3 into the directory for Q4.~~ I figured that would be okay for a quick test situation like this, but if you want otherwise, let me know and I'll abide.

**Addendum, after the fact:** The above didn't really happen in practice. Very little direct code re-use. I might still go on to do some more extensive tests for Q1 and Q2, and I could see Q2's tests requiring such, but that's about it. (Also, I was mistaken about Q3: misread it at first and thought I was supposed to *write* a JSON file, not serve it. So that part definitely did not happen.)

#### Python 3 Note:
All the development and testing was done in Python3. There are some print() statements that use Python3 only syntax in there, but if commented out, I think everything else will work with Python2. No promises though, haven't had the chance to test.


## Questions

### Question 1
##### Part A
Given a list of positive numbers, write a function that prints the following
"fizz" if number is divisible by 3
"buzz" if number is divisible by 5
"fizzbuzz" if number is divisible by 3 and 5

##### Part B
How do I implement this without looping?
(*I did it with **recursion**.)*

##### [Non-existent Part C]
*(This was not in the original, but I took another crack at it with **NumPy and vectorizing**, trying to figure out a different way to avoid for loops.)*


### Question 2 [original] -- **deprecated**
Given a list of strings containing values "fizz", "buzz" or "fizzbuzz"
Write a function to find the shortest sequence of numbers that produces the the given output using the function in Q1.

e.g.
    The sequences (3, 4, 5) and (9, 10) both produce ["fizz", "buzz"] when passed through the function from Q1
    Given ["fizz", "buzz"] as input, the function should produce (9, 10)
    and not (3, 4, 5)

#### Note for Question 2 -- **current version**
As discussed by email, the original task can cause issues because certain lists ["fizzbuzz", "fizzbuzz"] are impossible to accomplish with a contiguous sequence of integers. The question has now been modified to the following:

Given a list of strings containing only values "fizz", "buzz" or "fizzbuzz", determine if there exists a sequence of numbers that will return the given string when run through the function from Q1. If such a sequence exists, determine the shortest such sequence.
- If no such sequence exists, return an empty list: []
- If the sequence exists, return a list that is the shortest sequence: e.g., [9, 10] for an input of ["fizz", "buzz"].
- If multiple shortest sequences exist (consider that ["buzz", "fizz"] can be created at shortest length of 2 with both [5, 6] and [20, 21]), return the sequence with the lower starting number: e.g., in this case we would return [5,6] for ["buzz", "fizz"]


### Question 3
Build an API with the technology of your choice. Parse the contents of the provided CSV file props.csv and serve the results as a JSON object at the endpoint '/data'
The API results must contain only properties in California, and contain the following:
- PROP_NAME
- ADDRESS
- CITY
- STATE_ID
- ZIP
- MISSING_FIELD_COUNT (number of fields in a record that is missing data)
- MISSING_DATA_ENCODING - a number where each digit indicates consecutive columns with and without data
    e.g. [a,b,c,,,d,e] will be 322 (3 columns with data followed by 2 columns with missing data followed by 2 columns with data)

You are free to use data stores of your choice.


### Question 4
Using the frontend tools of your choice, build out an application to cansume the API you built in Q1 and display the results in a table.


### Bonus!
Unit tests for each of the questions above