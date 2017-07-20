#!/usr/bin/env python3
# Should work fine with python2 as well, but testing and development was done in 3.

# Q1a
# Given a list of positive numbers, write a function that prints the following
# "fizz" if number is divisible by 3
# "buzz" if number is divisible by 5
# "fizzbuzz" if number is divisible by 3 and 5



# This is the function that does the actual work.
# INPUT: a list of integer numbers.
# Input list can contain any quantity of entries, from en empty list to arbitrarily large.
# There is no error checking on the input. If strings or floats are passed, bad things might happen.
# Similarly, non-positive integers will be weird, albeit not necessarily function-breaking.
# OUTPUT: returns a list of "fizz", "buzz", and "fizzbuzz" depending on input list of numbers.
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


# Being technical, the question told us to create a function that PRINTED finished list of "fizz" and co.
# Make another function that just does the printing for us.
# Note that this function has no return. Don't go setting var = fizzbuzz_printer(input) unless you want var = None.
def fizzbuzz_printer(listofnumbers):
    print(fizzbuzz_translator(listofnumbers))  # Just passes it to the fizzbuzz_translator above, then prints result.
    # This has no return, so it will return None, because it's just intended to print.



#  The actual work is done at this point, now we're just showing off.

numberlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]  # This can be any list of integers, feel free to modify.

# Let the user in on what is about to happen.
print("About to swap in 'fizz', 'buzz', and 'fizzbuzz' accordingly for this list of numbers:")
print(numberlist)  # Show them there's nothing up your sleeves.
print('\n\n')  # Who doesn't love a bit of whitespace?

fizzbuzz_printer(numberlist)  # What we all came to see.
