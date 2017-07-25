#!/usr/bin/env python3

import q2  # The thing we're testing, should be in this folder.
    # Note, because q2 has some print statements, I believe they get spit out in the console prior to test. Ignore it.
import unittest  # We came to test!
import random  # For the most aggressive test, we call in some random values.


# Below is the central code from Q1a. Quick and dirty copy-paste. In a perfect world, it would refer to where q1 lives.
# It gets used in the most aggressive test.
def fizzbuzz_translator(listofnumbers):
    finishedlist = []  # Initialize empty list for appending as we work.
    # Because we check one step at a time and append as we go, order from listofnumbers is preserved.
    for i in listofnumbers:
        # All of the below uses mod operator '%' to check for divisibility. Remember, 8 (mod 2) = 0, etc.
        # Also, note that for a number to be divisible by 3 and 5, it is divisible by 15.
        if i % 15 == 0:  # First, check if divisible by 15. [MUST go first, due to 15 being divisible by 5 & 3.]
            finishedlist.append("fizzbuzz")  # It was divisible by 15, so place a "fizzbuzz" in list.
        elif i % 5 == 0:  # Next, check if divisible by 5.
            finishedlist.append("buzz")  # Divisible by 5, so place a "buzz" in list.
        elif i % 3 == 0:  # Finally, check if divisible by 3.
            finishedlist.append("fizz")  # Divisible by 3, so place a "fizz" in list.
            # Note that if none of the above conditions kicked off, the number just gets chucked.
            # Which is exactly what we want to do: chuck numbers that are not divisible 15 or 5 or 3.
    return finishedlist


##############
# Testing two things here:
# 1) The willitfizzbuzz function.
# 2) The findnumberlist function.
# We ignore testing the lookup_no_fizzbuzz function, as it's just a simple lookup table and gets called as part of #2.
##############


class Test_q2(unittest.TestCase):

    def setUp(self):  # No general set up for tests.
        pass

    def tearDown(self):  # No general tear down for tests.
        pass

    ############
    # Testing willitfizzbuzz

    def test_willitfizzbuzz_false1(self):  # Example of something that should fail.
        list_of_words = ['fizzbuzz', 'fizzbuzz']
        expected_result = False
        actual_result = q2.willitfizzbuzz(list_of_words)
        self.assertEqual(actual_result, expected_result)

    def test_willitfizzbuzz_false2(self):  # Another example of something that should fail.
        list_of_words = ['fizz', 'buzz', 'fizz', 'buzz']
        expected_result = False
        actual_result = q2.willitfizzbuzz(list_of_words)
        self.assertEqual(actual_result, expected_result)

    def test_willitfizzbuzz_true1(self):  # An example of something that should pass.
        list_of_words = ['fizz', 'buzz', 'fizz']
        expected_result = True
        actual_result = q2.willitfizzbuzz(list_of_words)
        self.assertEqual(actual_result, expected_result)

    def test_willitfizzbuzz_true2(self):  # An example of something that should pass.
        list_of_words = ['fizz', 'buzz', 'fizz', 'fizzbuzz']  # Effectively a start from 9 --> 15
        masterpattern = ['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']  # For tacking on.
        list_of_words.extend(masterpattern*10)  # Add to additional masterpatterns. Will not affect it working.
        endportion = ['fizz', 'buzz']  # Just a little more to make the test even more aggressive.
        list_of_words.extend(endportion)  # A bit beyond the end.
        expected_result = True
        actual_result = q2.willitfizzbuzz(list_of_words)
        self.assertEqual(actual_result, expected_result)

    #############
    # Testing findnumberlist

    def test_findnumberlist_empty(self):  # Test on an impossible wordlist, should return an empty list.
        list_of_words = ['fizzbuzz', 'fizzbuzz']
        expected_result = []
        actual_result = q2.findnumberlist(list_of_words)
        self.assertEqual(actual_result, expected_result)

    def test_findnumberlist_short1(self):  # Test on a short wordlist.
        list_of_words = ['fizz', 'buzz']
        expected_result = [9, 10]  # Manually checked to be correct.
        actual_result = q2.findnumberlist(list_of_words)
        self.assertEqual(actual_result, expected_result)

    def test_findnumberlist_short2(self):  # Another test on a short wordlist.
        list_of_words = ['fizz']
        expected_result = [3]  # Manually checked to be correct.
        actual_result = q2.findnumberlist(list_of_words)
        self.assertEqual(actual_result, expected_result)

    def test_findnumberlist_short3(self):  # Yet another test on a short wordlist.
        list_of_words = ['fizz', 'fizzbuzz', 'fizz']
        expected_result = [12, 13, 14, 15, 16, 17, 18]  # Manually checked to be correct.
        actual_result = q2.findnumberlist(list_of_words)
        self.assertEqual(actual_result, expected_result)

    def test_findnumberlist_long(self):  # Test on a long wordlist.  (Well "long" for certain rather short lengths.)
        list_of_words = ['fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz', 'fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']
        expected_result = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]  # Manually checked.
        actual_result = q2.findnumberlist(list_of_words)
        self.assertEqual(actual_result, expected_result)


    # This is by far the most aggressive test.
    # Randomly generates a range of numbers that is some sequential subset of numbers in 1 --> 9,999.
    # It then uses the function from q1 (just copied in wholesale at top of this file) to convert that to a wordlist.
        # NOTE: This assumes that the code for q1 works in all scenarios. Should be true, but a potential flaw.
    # We then run the actual findnumberlist function on that wordlist to create a new numberlist.
    # Next, we run the q1 function on the new numberlist and compare the two wordlists, which should be identical.
    # Finally, we do one more tests ( I know not best practice, but unsure how to share random vars between tests)
    # The second test verifies that the length of the secondary numberlist is no larger than the initial.
    def test_findnumberlist_aggressive(self):
        i, j = random.randint(1, 10000), random.randint(1, 10000)  # Generate two numbers from 1 --> 10,000.
        if j < i:  # In a few moments, we will assume that i < j. If otherwise, we need to change order.
            i, j = j, i  # In case they were ordered "wrong" (50/50 chance), flip the ordering.
        randomized_numberlist = list(range(i,j))  # Create range() object, then list() it because list is input spec.
            # The list() method should actually be unnecessary above, but it is technically the expected input.
        trusted_wordlist = fizzbuzz_translator(randomized_numberlist)  # Use q1 function.
            # This gives us a trusted wordlist of what should come out.
        result_numberlist = q2.findnumberlist(trusted_wordlist)  # What comes out of the q2 function we're testing.
        compare_wordlist = fizzbuzz_translator(result_numberlist)  # Use q1 again so we can do a comparison.
        self.assertEqual(compare_wordlist, trusted_wordlist)  # Compare the trusted version with q2 function result.
        ##############
        #  Second portion: additionally, it should be that the result_numberlist was no longer than the randomized one.
        self.assertLessEqual(len(result_numberlist), len(randomized_numberlist))



if __name__ == '__main__':
    unittest.main()