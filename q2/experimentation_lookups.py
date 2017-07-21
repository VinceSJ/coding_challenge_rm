#!/usr/bin/env python3

# Intended to help figure out start values and end values for numberlist via lookups.
# We look at first 'fizzbuzz' and last 'fizzbuzz' as anchors, then see number of elements before/after.
# Because everything must follow masterpattern building block:
# ['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz'],
# knowing how many elements before or after final fizzbuzz allows lookup table. (see README for more info)


##############
# First, we do the start of things.

blocknumbers = [3, 5, 6, 9, 10, 12, 15]  # Numbers matching to master pattern starting block
startblock = ['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']  # Master pattern start block

start_tied_numbers_words = list(zip(blocknumbers, startblock))
# zip into tuples for playing around. list because we don't want zip object headaches.


reverseorder_start_tied = list(reversed(start_tied_numbers_words))  # More headaches, this time reverse() being object.
# This is very useful because the index of the first fizzbuzz in a list matches to the associated number for that
# same index in the above var.

for i in range(0,7):  #All seven possible options.
    print("When first 'fizzbuzz' at index", i, "use numberstart of ", reverseorder_start_tied[i][0])
# Manually verify above worked. Yup, it did! Totally matches with what I see working on paper.

# Easy copy-paste to make lookup in primary script:
start_list = [] # Empty to initialize.
for i in range(0,7):
    start_number = reverseorder_start_tied[i][0]  # Value of startnumber for first fizzbuzz index at i.
    start_list.append(start_number)  # Catch them all in a list.

print("\nBelow is list of startnumbers based on index of first 'fizzbuzz'")
print(start_list)

# Heh heh. I did all that work. And it just wound up being a reversal. Heh.

print('\n\n')  # Some whitespace for reading, since we will be copy-pasting from terminal output.


##############
# Second, the end of things.

# For ease, treat final fizzbuzz as being at 15.

endnumbers = [15, 18, 20, 21, 24, 25, 27]  # Numbers matching to effective ending block
# Don't sweat the numbers too much, we're only looking for delta (difference).
startblock = ['fizzbuzz', 'fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz']  # Ending block word pattern


end_deltas_list=[] #empty to initialize
for num_of_elements_after_fizzbuzz in range(0, 7):  # After final fizzbuzz, could be 0<-->6 elements.
    delta = endnumbers[num_of_elements_after_fizzbuzz] - 15  # Distance from final 'fizzbuzz' number to endnumber.
    end_deltas_list.append(delta)

print("Below is list of deltas between last 'fizzbuzz' and endnumber for number list.")
print("(Example: last fizzbuzz happens at 30 and has a fizz and a buzz after, that's two elements,")
print("so it would need a delta of /5/ to get to the endnumber of 35.)")
print(end_deltas_list)

# Heh heh. I did all that work. Again. And it's so obvious when I look at. Heh.
