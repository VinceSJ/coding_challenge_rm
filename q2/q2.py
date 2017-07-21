#!/usr/bin/env python3
# Should work fine with python2 as well, but testing and development was done in 3.

# Given a list of strings containing only values "fizz", "buzz" or "fizzbuzz", determine if there exists a sequence
# of numbers that will return the given string when run through the function from Q1. If such a sequence exists,
# determine the shortest such sequence. - If no such sequence exists, return an empty list: [] - If the sequence
# exists, return a list that is the shortest sequence: e.g., [9, 10] for an input of ["fizz", "buzz"]. - If multiple
# shortest sequences exist (consider that ["buzz", "fizz"] can be created at shortest length of 2 with both [5,
# 6] and [20, 21]), return the sequence with the lower starting number: e.g., in this case we would return [5,
# 6] for ["buzz", "fizz"]


# There's a lot of mathematical thought that went into this question.
# For the underlying reasons that we're doing the below stuff, check out the README.md file in this folder.
# The code below will be commented to explain what's happening moment-by-moment, but for a big picture understanding
# check out the reasoning in the markdown file (or just look at this folder on GitHub for pretty printing).


# This function determines whether or not a given wordlist can be created by a contiguous numberlist.
# INPUT: a list of words containing only some mix of 'fizz', 'buzz', and 'fizzbuzz'.
# There is basic error checking on this input. No promises, though.
# OUTPUT: True/False. If a wordlist can be constructed from a contiguous numberlist, True. If not, False.
def willitfizzbuzz(wordlist):
    # First, having 'fizz' and 'buzz' can be dangerous down the road for 'fizzbuzz', as they concatenate to a match.
    # Before we do anything, convert everything to unique identifiers:
    #  - 'fizz' becomes 'a'
    #  - 'buzz' becomes 'b'
    #  - 'fizzbuzz' becomes 'c'
    abc_wordlist = []  # Initialize an empty list to fill with unique identifiers as we work through wordlist.
    for word in wordlist:  # Since we work through in order, order for abc_wordlist matches new abc identifiers.
        if word == 'fizz':
            abc_wordlist.append('a')  # All 'fizz' strings become 'a' strings.
        if word == 'buzz':
            abc_wordlist.append('b')  # All 'buzz' strings become 'b' strings.
        if word == 'fizzbuzz':
            abc_wordlist.append('c')  # All 'fizzbuzz' strings become 'c' strings.
    # abc_wordlist is ready for use and is safer because of unique identifiers.
    # Ultimately, we'll need a string for a subpattern check, so convert it now:
    abc_wordstring = ''.join(abc_wordlist)  # This joins everything from abc_wordlist through concatenation.

    # Next, we need to construct an appropriate length masterpattern to test against.
    # First, we set our basic size from how long the wordlist is.
    length_of_wordlist = len(wordlist)

    # While we're here, let's throw in a basic error check.
    # This should catch most situations where our wordlist was not ONLY composed of 'fizz', 'buzz', 'fizzbuzz'.
    # Since abc_wordstring only came from those three key words, if the length does not match wordlist, it's bad news.
    if length_of_wordlist != len(abc_wordlist):  # Oh no, they didn't match!
        raise ValueError("It appears that not all inputs were exactly 'fizz', 'buzz', or 'fizzbuzz'.")
        # This might not be the best pick of errors to raise. I don't have that much experience with error codes.

    # Now that the error check is done, let's figure out our masterpattern's size.
    # Remember, our basic building block is ['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz'].
    # That has a length of 7, so our base size is length_of_wordlist divided by 7 and rounded up:
    baseblocknumber = (length_of_wordlist//7) + 1  # To avoid needing math library. Occasionally overlong, but that's okay.
    # From discussion in README, we need a "bit more" than above. Two more blocks of pattern should be plenty.
    bitmoreblocks = 2  # Could be changed if testing indicates an issue with current value.
    totalblocknumber = baseblocknumber + bitmoreblocks  # Number of building blocks to use in making masterpattern.

    # We have the totalblocknumber for how many building blocks to use in making the testing masterpattern.
    # Instead of converting the building block with code, since it never changes, we'll just do it by hand:
    buildingblock_string = 'abaabac'  # 'abaabac'  <--> ['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']
    # Concatenate a number of times equal to "bitmoreblocks" var above:
    masterpattern_abcstring = buildingblock_string * bitmoreblocks  # The string we're looking for a subpattern in.

    # Everything is ready, just need to see if the wordlist is a subpattern of masterpattern.
    return abc_wordstring in masterpattern_abcstring  # We return this True/False answer to user.


# This function serves as a simple lookup in the case where the wordlist does NOT contain 'fizzbuzz'.
# It is only intended for use inside of the final lookup function below.
# See README for full explanation and discussion of how these values were found.
# INPUT: a constructable wordlist that does NOT contain 'fizzbuzz', only 'fizz' and 'buzz'.
# There is no error checking on this input! It's only expected to be run by another function that passes trusted inputs.
# OUTPUT: a list of numbers. (Specifically, the shortest and earliest numberlist that will construct the wordlist.)
def lookup_no_fizzbuzz(wordlist):
    LOOKUP_DICT = {  # We'll do the lookup with a dictionary that has keys of strings representing the 9 options.
        'fizz' : range(3, 4),  # Remember, `range` is exclusive of ending number.
        'fizzbuzz' : range(9, 11),
        'fizzbuzzfizz' : range(3, 7),
        'fizzbuzzfizzfizz' : range(3, 10),
        'fizzbuzzfizzfizzbuzz' : range(3, 11),
        'fizzbuzzfizzfizzbuzzfizz' : range(3, 13),
        'buzzfizzfizzbuzzfizz' : range(5, 13),
        'fizzfizzbuzzfizz' : range(6, 13),
        'buzzfizz' : range(5, 7)
    }
    wordstring = ''.join(wordlist)  # We join the wordlist into a single string so we can look up in dictionary.
    # Sidenote: We don't have to worry about the abc stuff we did in last function, because there is no 'fizzbuzz'.
    desired_range = LOOKUP_DICT[wordstring]  # Note that this is a range. In Python3, that is not a list.
    return list(desired_range)  # Convert range into a numberlist just before returning.
    # For testing, I used following code, going through all possible iterations of 'test' variable.
    # test = ['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz']
    # print(lookup_no_fizzbuzz(test))


test = []

n = 0

for i in test:
    n = n+1

print(n)