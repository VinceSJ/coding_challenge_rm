# Math Thinking for Question 2

### Problem Statement:
Given a list of strings containing only values "fizz", "buzz" or "fizzbuzz", determine if there exists a sequence of numbers that will return the given string when run through the function from Q1. If such a sequence exists, determine the shortest such sequence.
- If no such sequence exists, return an empty list: []
- If the sequence exists, return a list that is the shortest sequence: e.g., [9, 10] for an input of ["fizz", "buzz"].
- If multiple shortest sequences exist (consider that ["buzz", "fizz"] can be created at shortest length of 2 with both [5, 6] and [20, 21]), return the sequence with the lower starting number: e.g., in this case we would return [5,6] for ["buzz", "fizz"]


## Approach
We'll approach this problem as two major parts, and we will build two functions that deal with each of these:

First, we'll determine if it is possible for the **wordlist** (*e.g. `['fizz', 'buzz', 'fizz']`*) to be represented by a contiguous sequence of positive integers, **numberlist** (*e.g. `[3, 4, 5, 6]`*). The function will either return `True` if possible or `False` if impossible (*e.g. `['fizzbuzz', 'fizzbuzz']`*).

Second, assuming that it is possible for a given **wordlist** to be represented by a **numberlist** (`True` from above), we need to find the shortest possible sequence (tie-breaker goes to numberlists that start at a smaller number). This function will return that shortest numberlist or, if impossible, will return an empty list.
 
 
### Major Realization
 
 Basically, all the logic here comes down to the realization that the fizz/buzz translation process is identical over **(mod 15)**. To understand this better, consider what happens if we apply the fizz/buzz translation to the numbers 1 -> 30.
 
1.
2.
3.  fizz
4.
5.  buzz
6.  fizz
7. 
8.
9.  fizz
10. buzz
11.
12. fizz
13.
14.
15. fizzbuzz
---
16.
17.
18. fizz
19.
20. buzz
21. fizz
22. 
23.
24. fizz
25. buzz
26.
27. fizz
28.
29.
30. fizzbuzz
---
etc.

Notice that for every 15 numbers in a sequence, the pattern of words *must* repeat itself exactly. Because every numberlist must be a contiguous sequence of positive integers, a wordlist that can be constructed must follow this pattern.

More precisely, **every constructable wordlist must be a contiguous subsequence of this sequence:**

`['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz', ...repeat forever...]`

Furthermore, notice that the location of 'fizzbuzz' in the pattern never varies compared to the other elements. While 'fizz' and 'buzz' can be closer or further, 'fizzbuzz' is relatively fixed since the list repeats based on (mod 15) and 'fizzbuzz' appears at 0 (mod 15). We will use this fact to our advantage when dealing with wordlists containing 'fizzbuzz' when it comes time to construct a numberlist.


### Part 1 (Is a given wordlist possible?)

From our reasoning above, we just need to determine if a given wordlist is a contiguous subsequence (hereafter, **subpattern**) of this sequence:

`['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz', ...repeat forever...]` (hereafter, we will call this the **masterpattern**)

If a given wordlist is a subpattern of the masterpattern, then the wordlist is constructable. If it is not a subpattern, then it is not constructable.

#### Implementation

Okay, that's all well and good, but how do we implement that in code? First, we can't have an infinite list (although it would be possible to do this with some sort of generator object). Second, how do we check if a given wordlist is a subpattern of the masterpattern?
 
##### Infinity Issue
 First, to get around the infinity issue, notice that we don't actually need our masterpattern to be infinitely long, it just needs to be *long enough* to show whether or not the wordlist is a subpattern. Because the masterpattern repeats every seventh element (the 'fizzbuzz' mark at 15), we just need to make our testing masterpattern **as long as the wordlist plus a bit more**. The extra "bit more" is so the wordlist can be allowed to "slide around" as we check to see if it's a subpattern or not. (To understand the necessity here, consider the list `['fizzbuzz', 'fizz']`. Definitely doable with `[15, 16, 17, 18]`, but if the masterpattern we tested against was only `['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']`, we would get a false negative.)
 
Consider the `['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']` list as kind of building block. To get the base size, take the wordlist's length, divide by 7, and round up. Use that many building blocks to begin with. Then we need the "bit more": add an additional two (2) building blocks and I am quite confident that will be long enough to test against. (I actually think it's enough to just add one more building block as the "bit more", but since I haven't formally proven this, I'm going to go with being safe rather than sorry.)

##### Check for Subpattern
At first, we might be tempted to implement this by checking if a list has a "sublist" (subpattern). A little bit of Google seems to indicate that's not such a great option though. Instead, we can be a bit clever and convert both our wordlist and our testing masterpattern into strings via concatenation (see warning below). If the wordlist's string is contained within the masterpattern's string, then it is a subpattern, and conversely if it's not contained, it is not a subpattern.
  
  **Warning**: This works great, except that 'fizz' and 'buzz' when concatenated will make 'fizzbuzz'. This could cause issues. So instead, we need to create unique identifiers. Before converting the list into a concatenated string, we need to uniquely identify each "word". Use the following convention:
  - 'fizz'  --> a
  - 'buzz'  --> b
  - 'fizzbuzz' --> c
  
  Work through the wordlist and the testing masterpattern list, swap as above, then string-ify them. Finally, check if the wordlist string is in the masterpattern string.
  
  
### Part 2 (Finding the shortest numberlist)
Assuming that the wordlist can actually be constructed into a numberlist, there are one of two possibilities: either the wordlist contains 'fizzbuzz' or it does not.

##### Does NOT contain 'fizzbuzz' (inherently short)
Remember, `['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']` forms the building block of all constructable wordlists. Thus, if a given wordlist is constructable and does not contain 'fizzbuzz', it must be no more than six elements long. Furthermore, because it has to be a subpattern of that building block, there are actually ~~just nine patterns in total that are possible.~~ Whoops! Turns out there are 13 possible patterns! Went through naively the first time. Double-checked carefully, should be only 13, no more surprises.

This means, with just ~~nine~~ thirteen patterns possible, we can make a lookup table. Not my most elegant work, but it's easy. Listed below are all the possible wordlists that do not contain 'fizzbuzz'. To the right of each is a `range` that will spit out the appropriate numberlist (remember, `range(3,6) = [3,4,5]`, we don't actually hit end number of range). These were figured by hand, but it's pretty fast and easy to do. Compare them to the fizz/buzz translation in "Major Realization" above to check work and see they are best picks.

1. fizz `range(3, 4)`
1. buzz `range(5, 6)`
2. fizz, buzz `range(9, 11)`
2. buzz, fizz `range(5, 7)`
3. fizz, buzz, fizz `range(3, 7)`
3. buzz, fizz, fizz `range(5, 10)`
3. fizz, fizz, buzz `range(6, 11)` 
4. fizz, buzz, fizz, fizz `range(3, 10)`
4. buzz, fizz, fizz, buzz `range(5, 11)` 
4. fizz, fizz, buzz, fizz `range(6, 13)`
5. fizz, buzz, fizz, fizz, buzz `range(3, 11)`
5. buzz, fizz, fizz, buzz, fizz `range(5, 13)`
6. fizz, buzz, fizz, fizz, buzz, fizz `range(3, 13)`




This can be implemented pretty easily with a dictionary. Just remember that lists can't be used for lookup keys, so we have to use ~~tuples or~~ strings *(Ed: went with strings)*. Also, we must convert the wordlist we're checking into a matching type so we can then just use it as a key.
 
 
##### DOES contain 'fizzbuzz' (potentially very long)
Because the wordlist contains 'fizzbuzz', the first instance of 'fizzbuzz' in the wordlist must occur at a number divisible by 15. Furthermore, since the pattern is identical by (mod 15), having that first 'fizzbuzz' occur at 15 will ultimately result in a numberlist that is the same length as if we chose a different number for the first 'fizzbuzz' (say, 30 or 45). Thus, since length ties go to the numberlists that start earlier, we should **always place the first 'fizzbuzz' at 15.

This makes our first 'fizzbuzz' an anchor. It's at the number 15, we just need to work backwards to the start of the wordlist from there. We could do this with an algorithm, but it's so short (seven options only due to masterpattern), we'll just create a lookup table. (You can see the prep work done to figure this out in the file `experimentation_lookups.py`.)

From there, we can count the total number of occurrences of 'fizzbuzz' in the word list. Each one of these will occur at a multiple of 15: first 'fizzbuzz' at 15, second at 30, third at 45, etc. Thus, if we know how many fizzbuzzes occur, the last will happen at that multiplied by 15. This gives us an ending anchor as well.

Finally, we just need to know how many elements happen after the final 'fizzbuzz', and we can figure out how much farther it is the final number in the numberlist with another lookup (once again, seven options only due to masterpattern, prep work in same file as above).

We know our first number and our last number, we just need to generate a numberlist and we're done!