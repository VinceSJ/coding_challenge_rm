#!/usr/bin/env python3
# Should work fine with python2 as well, but testing and development was done in 3.

from time import sleep

# So, technically, the original question simply said: "Write a function to find the shortest sequence of numbers that
#  produces the the given output using the function in Q1."
# But it never said anything about the sequence being contiguous... Assuming the normal definition of sequence in math,
# any list of numbers is a sequence: repeats, order, none of that matters.

# Since Bryan said you're the kind of guy who has a sense of humor, here's the smart alec function:


# INPUT: a list of words containing only some mix of 'fizz', 'buzz', and 'fizzbuzz'.
# OUTPUT: a list of numbers that, when run through the function from Q1, will produce the original wordlist.
def smartalec(wordlist):
    numberlist = []  # Initialize an empty number list for filling as we progress.
    for word in wordlist:  # We progress through, swapping in known good values.
        if word == 'fizz':
            numberlist.append(3)
        if word == 'buzz':
            numberlist.append(5)
        if word == 'fizzbuzz':
            numberlist.append(15)
    return numberlist
    # Because each word creates only one swap in of a number, it must default to being shortest possible sequence.


test = ['fizz', 'buzz', 'fizzbuzz', 'fizzbuzz', 'fizz']
# Feel free to change as long as only 'fizz', 'buzz', 'fizzbuzz' is entered or you break the warranty.


print("Welcome to the smart alec version for answering Q2!")
print("We'll be converting the below wordlist into a numberlist.")
print(test)
print("\n\nAnnnnnd we get:")
print(smartalec(test))
sleep(2)
print("\nWhat? You said you wanted a sequence, right? That's as short as it's gonna get!")
sleep(1)
print("\nOh. A /contiguous/ sequence. Well, that's a different kettle of fish.")

# If this actually is the answer you were looking for and you didn't mean a contiguous sequence...
# Well.
#<sigh>
# I guess that's why you always double-check the specifications you're working to.
