#!/usr/bin/env python3

import q1a  # The thing we're testing, should be in this folder.
    # Note, because q1a has some print statements, I believe they get spit out in the console prior to test. Ignore it.
import unittest  # We came to test!


############
# Note that we're only testing the fizzbuzz_translator function here.
# The other function in q1a is very boring: just a print() wrapper around fizzbuzz_translator.
############


class Test_fizzbuzz_translator(unittest.TestCase):

    def setUp(self):  # No general set up for tests.
        pass

    def tearDown(self):  # No general tear down for tests.
        pass

    def test_empty_list(self):
        list_of_numbers = []  # User input of an empty list.
        expected_result = []  # Result should be an output of an empty list.
        actual_result = q1a.fizzbuzz_translator(list_of_numbers)  # Actually running the function
        self.assertEqual(actual_result, expected_result)


    def test_basic_list(self):
        list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]  # User input a fairly basic list.
        expected_result = ['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']  # What it should be.
        actual_result = q1a.fizzbuzz_translator(list_of_numbers)  # Actually running the function
        self.assertEqual(actual_result, expected_result)


    def test_weird_list(self):
        list_of_numbers = [5, 10, 15, 16, 17, 19, 45, 60, 62, 7, 63]  # User input, more exotic.
        expected_result = ['buzz', 'buzz', 'fizzbuzz', 'fizzbuzz', 'fizzbuzz', 'fizz']  # What it should be.
        actual_result = q1a.fizzbuzz_translator(list_of_numbers)  # Actually running the function
        self.assertEqual(actual_result, expected_result)



if __name__ == '__main__':
    unittest.main()