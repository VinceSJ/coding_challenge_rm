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
 
1
2
3  fizz
4
5  buzz
6  fizz
7 
8
9  fizz
10 buzz
11
12 fizz
13
14
15 fizzbuzz
---
16
17
18 fizz
19
20 buzz
21 fizz
22 
23
24 fizz
25 buzz
26
27 fizz
28
29
30 fizzbuzz
---
etc.

Notice that for every 15 numbers in a sequence, the pattern of words *must* repeat itself exactly. Because every numberlist must be a contiguous sequence of positive integers, a wordlist that can be constructed must follow this pattern.

More precisely, **every constructable wordlist must be a contiguous subsequence of this sequence:**
`['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz', ...repeat forever...]`

Furthermore, notice that the location of 'fizzbuzz' in the pattern never varies compared to the other elements. While 'fizz' and 'buzz' can be closer or further, 'fizzbuzz' is relatively fixed since the list repeats based on (mod 15) and 'fizzbuzz' appears at 0 (mod 15). We will use this fact to our advantage when dealing with wordlists containing 'fizzbuzz' when it comes time to construct a numberlist.


### Part 1 (Is a given wordlist possible?)

From our reasoning above, we can answer this by determining if a given wordlist is a contiguous subsequence of this sequence (hereafter, **subpattern**):
`['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz', ...repeat forever...]` (hereafter, we will call this the **masterpattern**)

If a given wordlist is a subpattern of the masterpattern, then the wordlist is constructable. If it is not a subpattern, then it is not constructable.

##### Implementation

Okay, that's all well and good, but how do we implement that in code? First, we can't have an infinite list (although it would be possible to do this with some sort of generator object). Second, how do we check if a given wordlist is a subpattern of the masterpattern?
 
###### Infinity Issue
 First, to get around the infinity issue, notice that we don't actually need our masterpattern to be infinitely long, it just needs to be *long enough* to show whether or not the wordlist is a subpattern. Because the masterpattern repeats every seventh element (the 'fizzbuzz' mark at 15), we just need to make our testing masterpattern **as long as the wordlist plus a bit more**. The extra "bit more" is so the wordlist can be allowed to "slide around" as we check to see if it's a subpattern or not. (To understand the necessity here, consider the list `['fizzbuzz', 'fizz']`. Definitely doable with `[15, 16, 17, 18]`, but if the masterpattern we tested against was only `['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']`, we would get a false negative.)
 
Consider the `['fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']` list as kind of building block. To get the base size, take the wordlist's length, divide by 7, and round up. Use that many building blocks to begin with. Then we need the "bit more": add an additional two (2) building blocks and I am quite confident that will be long enough to test against. (I actually think it's enough to just add one more building block as the "bit more", but since I haven't formally proven this, I'm going to go with being safe rather than sorry.)

###### Check for Subpattern
At first, we might be tempted to implement this by checking if a list has a "sublist" (subpattern). A little bit of Google seems to indicate that's not such a great option though. Instead, we can be a bit clever and convert both our wordlist and our testing masterpattern into strings via concatenation (see warning below). If the wordlist's string is contained within the masterpattern's string, then it is a subpattern, and conversely if it's not contained, it is not a subpattern.
  
  **Warning**: This works great, except that 'fizz' and 'buzz' when concatenated will make 'fizzbuzz'. This could cause issues. So instead, we need to create unique identifiers. Before converting the list into a concatenated string, we need to uniquely identify each "word". Use the following convention:
  - 'fizz'  --> a
  - 'buzz'  --> b
  - 'fizzbuzz' --> c
  Work through the wordlist and the testing masterpattern list, swap as above, then string-ify them. Finally, check if the wordlist string is in the masterpattern string.
  
  
### Part 2 (Finding the shortest numberlist)
Going to do a bit more thinking on this part, but you can use 'fizzbuzz' as an anchor if it's in the wordlist. Lock first 'fizzbuzz' occurrence to #15, work backwards and forwards from there. (We would already have checked if the wordlist is possible via part 1's function).
 
 In the case where 'fizzbuzz' is not contained in the wordlist, the wordlist has to be quite short. Because of this, I think there's like only ten or so options that can be constructed? Probably easiest to just build a bruteforce lookup table. Ain't terribly elegant, but almost certainly fastest.

