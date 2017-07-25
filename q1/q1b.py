#!/usr/bin/env python3
# Should work fine with python2 as well, but testing and development was done in 3.

# Q1b
# Given a list of positive numbers, write a function that prints the following
# "fizz" if number is divisible by 3
# "buzz" if number is divisible by 5
# "fizzbuzz" if number is divisible by 3 and 5
#
# Do it without a loop!


# Taking hint from email: "recursion is one option"

################
# NOTES:
# 1) This is a /destructive/ function. When you run it on an input, that input goes bye-bye.
# 2) Pass it /two/ arguments, where the second is an empty list.
    # This is due to the default argument being mutable, and so on later calls, it messes things up.
    # The lazy solution (what we're doing here and now) is to just pass it an empty list to avoid that issue.
    # A better solution would involve a default of a tuple or something to keep it from mutating.
        # Okay, I mocked up a somewhat better solution that does it with a default string.
        # It's under 'testy' below, no careful commenting because it's time to go to bed.
        # Still don't fully understand why the empty list issue is happening, but oh well. Maybe I will tomorrow.
################


# This is the function that does the actual work.
# Different from answer in Q1a in that this is doing it via recursion.
# INPUT: a list of integer numbers.
# Input list can contain any quantity of entries, from en empty list to arbitrarily large.
# There is no error checking on the input. If strings or floats are passed, bad things might happen.
# Similarly, non-positive integers will be weird, albeit not necessarily function-breaking.
# OUTPUT: returns a list of "fizz", "buzz", and "fizzbuzz" depending on input list of numbers.
def recursive_fizzbuzz_translator(list_of_numbers, list_to_fill=[]):
    # Note the list_to_fill is the second argument, and it defaults to an empty list.
    # This is effectively a way to get around initializing it inside of the function, as that would break recursion.
    # If something other than an empty list is passed at very start, it don't work so good.
    if len(list_of_numbers) > 0:  # Process things if the list has not been emptied out yet.
        # We now investigate the divisibilty of the front number and choose what to do.
        if list_of_numbers[0] % 15 == 0:  # First, check if divisible by 15. [MUST go first, because 15|3 and 15|5.]
            list_to_fill.append("fizzbuzz")  # It was divisible by 15, so place a "fizzbuzz" in list.
        elif list_of_numbers[0] % 5 == 0:  # Next, check if divisible by 5.
            list_to_fill.append("buzz")  # Divisible by 5, so place a "buzz" in list.
        elif list_of_numbers[0] % 3 == 0:  # Finally, check if divisible by 3.
            list_to_fill.append("fizz")  # Divisible by 3, so place a "fizz" in list.
            # Note that if none of the above conditions kicked off, the number is ignored.
            # Which is exactly what we want to do: ignore numbers that are not divisible 15 or 5 or 3.
        # Since we've now dealt with the fizz(and/or)buzz translation part, we cut off that number and throw it out.
        del list_of_numbers[0]  # Delete the first element of the numberlist. We're done with that element.
        return recursive_fizzbuzz_translator(list_of_numbers, list_to_fill)  # Now DO IT AGAIN.
        # This part here is the magic recursion part. Because it returns the function, it happens again.
        # We pass on the remainder of the list_of_numbers, allowing us to deal with the next element in line.
        # Additionally, we also pass on the list we're filling so that we can continue appending to it as we go.

    else:  # If we get to this point, it means the list_of_numbers has been emptied out.
        return list_to_fill  # We now return the list we've been filling.



def testy(list_of_numbers, list_to_fill = ""):
    # Note the list_to_fill is the second argument, and it defaults to an empty list.
    # This is effectively a way to get around initializing it inside of the function, as that would break recursion.
    # If something other than an empty list is passed at very start, it don't work so good.
    if len(list_of_numbers) > 0:  # Process things if the list has not been emptied out yet.
        # We now investigate the divisibilty of the front number and choose what to do.
        if list_of_numbers[0] % 15 == 0:  # First, check if divisible by 15. [MUST go first, because 15|3 and 15|5.]
            list_to_fill = list_to_fill + " fizzbuzz"  # It was divisible by 15, so place a "fizzbuzz" in list.
        elif list_of_numbers[0] % 5 == 0:  # Next, check if divisible by 5.
            list_to_fill = list_to_fill + " buzz"  # Divisible by 5, so place a "buzz" in list.
        elif list_of_numbers[0] % 3 == 0:  # Finally, check if divisible by 3.
            list_to_fill = list_to_fill + " fizz"  # Divisible by 3, so place a "fizz" in list.
            # Note that if none of the above conditions kicked off, the number is ignored.
            # Which is exactly what we want to do: ignore numbers that are not divisible 15 or 5 or 3.
        # Since we've now dealt with the fizz(and/or)buzz translation part, we cut off that number and throw it out.
        del list_of_numbers[0]  # Delete the first element of the numberlist. We're done with that element.
        return testy(list_of_numbers, list_to_fill)  # Now DO IT AGAIN.
        # This part here is the magic recursion part. Because it returns the function, it happens again.
        # We pass on the remainder of the list_of_numbers, allowing us to deal with the next element in line.
        # Additionally, we also pass on the list we're filling so that we can continue appending to it as we go.

    else:  # If we get to this point, it means the list_of_numbers has been emptied out.
        return list_to_fill.split()  # We now return the list we've been filling.


test = [1,2,3,4,5]

print("Running recursive version on this input:", test)

print("Our output:", recursive_fizzbuzz_translator(test, []))

print("\nAGAIN\n")

test = [1,2,3,4,5]

print("Running alternate version based on string on this input:", test)

print("Our output:", testy(test))