#!/usr/bin/env python3
# Should work fine with python2 as well, but testing and development was done in 3.

# Q1c
# This one is a self-imposed bonus challenge.
# Tried to figure out another way to to do q1 without using for loops.
# Did this one using NumPy and vectorization.

# Given a list of positive numbers, write a function that prints the following
# "fizz" if number is divisible by 3
# "buzz" if number is divisible by 5
# "fizzbuzz" if number is divisible by 3 and 5


import numpy as np # This forms the core of what's doing the work.
    # Also, let's be frank, there are probably some for loops happening in the numpy methods I'm using.
    # But at least they're hidden in the shadows and this miiiiiiiight go faster on gigantic numberlists.


# This is the function that does the actual work.
# Different from answer in Q1a and Q1b in that this is doing it via NumPy arrays.
# INPUT: a list of integer numbers.
# Input list can contain any quantity of entries, from en empty list to arbitrarily large.
# There is no error checking on the input. If strings or floats are passed, bad things might happen.
# Similarly, non-positive integers will be weird, albeit not necessarily function-breaking.
# OUTPUT: returns a list of "fizz", "buzz", and "fizzbuzz" depending on input list of numbers.
def numpy_fizzbuzz_translator(list_of_numbers):
    # We need to create a numpy array from the original list. Because these are just standard numbers, it's easy.
    array_data = np.array(list_of_numbers)  # Create an array of the input to figure out where we 3 and 5 divisibility.
    mod3_array = np.mod(array_data, 3)  # Returns a (mod 3) array of array_data (e.g. [1 2 3 4 5] --> [1 2 0 1 2])
    mod5_array = np.mod(array_data, 5)  # Returns a (mod 5) array of array_data (e.g. [1 2 3 4 5] --> [1 2 3 4 0])
    # Note that we do not need a (mod 15) version.
        # Because we have both the mod3 and mod5 arrays, we know that 15 divisibility occurs where they "overlap".

    # More setup.
    # We need arrays of strings to build off of. One for doing nothing (''), one for fizz, and one for buzz.
    # For each of the below, we are making an array that is as long as our original list_of_numbers, then filling it.
    # The 'dtype' statement is very important: it declares that we're working with strings of given lengths.
    # Since these are all simple ASCII, fizz and buzz are both at length 4, while the empties just take 1.
    # Note that these strings are all bytestrings, so we will eventually want to undo that down the road.
    empties_array = np.full(len(list_of_numbers), fill_value='', dtype='S1')  # Match list_of_numbers length, all empty strings.
        # Be careful to not use np.empty -- it does not set the values in memory, just allocates.
        # This will break things, so we have to make sure the values get set to the empty string ourselves.
    array_of_all_fizz = np.full(len(list_of_numbers), fill_value='fizz', dtype='S4')  # All 'fizz' strings.
    array_of_all_buzz = np.full(len(list_of_numbers), fill_value='buzz', dtype='S4')  # All 'buzz' strings.

    # We can now use these arrays to do some conditionals based on divisibility.
    # For both of the below, we use np.where(condition, TrueThings, FalseThings) for slotting in based on divisibility.
    # The mod#_array goes in the first argument to determine which array we pull from to slot that location.
    # Because 0's (implying divisibility) are False, we put the word ('fizz'/'buzz') to slot in the third argument.
    # Anything other than 0 (implying non-divisibility) are True, we put the empty strings in the second argument.
    slot_in_fizz = np.where(mod3_array, empties_array, array_of_all_fizz)  # Puts a 'fizz' at 3 divisible, '' otherwise.
    slot_in_buzz = np.where(mod5_array, empties_array, array_of_all_buzz)  # Puts a 'buzz' at 5 divisible, '' otherwise.

    # Because 15 is divisible by 3 and 5, we can avoid having to slot in 'fizzbuzz' because of concatenation.
    # Note that 'fizzbuzz' is just 'fizz' + 'buzz', so if we just concatenate all of our strings from both arrays,
    # we'll have a fully slotted array with 'fizz', 'buzz', 'fizzbuzz', and empty strings '' in correct spots.
    # To use concatenation, we need to change the type of these arrays to np.char.array (not standard for np.array).
    fully_slotted_array = np.char.array(slot_in_fizz) + np.char.array(slot_in_buzz)  # np.char.array enables concat +
    # Additionally, because we declare them as np.char.arrays above, we no longer have the length restriction of 'S4'.
    # That's important because otherwise it would truncate our 'fizzbuzz'.

    # Also, because we're now in the world of np.char.array, we can do standard Python string methods like .decode()
    fully_slotted_array = fully_slotted_array.decode('utf-8')  # Back to the ordinary world of text. Byte strings yucky.

    # Finally, we need to get rid of all those empty strings from our array so we can spit it out as a list and finish.
    # We'll do this by finding the locations of all empty strings, then creating a new array with them deleted.

    # Below conditional is just an edge case dodge: NumPy gets grumpy if we do comparisons on an empty array.
    if len(fully_slotted_array) > 0:
        empty_locations = np.argwhere(fully_slotted_array == '')  # Array of all locations where we have empty strings.
        finished_array = np.delete(fully_slotted_array, empty_locations)  # Arrays non-mutable, so declare new var.
    else:  # If the full_slotted_array was empty, we just need to pass it along.
        finished_array = fully_slotted_array  # This could also be a return of []. But let's not break the flow.

    # Finally, we need to convert back from NumPy array into standard Python list land. We do this as we return.
    return finished_array.tolist()  # Hand back the finished product as a list.


test = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

print("Running NumPy (no loop) version on this input:", test)

print("Our output:", numpy_fizzbuzz_translator(test))
