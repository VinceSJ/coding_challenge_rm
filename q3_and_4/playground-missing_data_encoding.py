#!/usr/bin/env python3

import itertools

# This is a playground just for figuring out a clever way to format the info_exists_encoded_list variable.
# info_exists_encoded_list comes as a list of 1's and 0's:
    # 1's represent data in that field, 0's represent blank field.
# Desired output is alternating numbers of fields that exist vs. blank fields. Delimited by spaces: ' '.
    # e.g. [1,1,1,0,0,1,1] will be '3 2 2' (3 columns with data, then 2 columns empty, followed by 2 columns with data)

# Later in the code, once we have the info_exists_encoded_list (e.g. [1,1,1,0,0,1,1]), we need to parse that and
# write a string delimited with spaces that represents how many at a time were missing.
# INPUT: a list of 1's and 0's, where 1's represent data in that field, 0's represent blank field.
# OUTPUT: a string representing count of filled fields, alternating with count of blank fields. Space delimited.
    # e.g. [1,1,1,0,0,1,1] will be '3 2 2' (3 columns with data, then 2 columns empty, followed by 2 columns with data)
# It is assumed that the first output of string always represents filled fields.
    # i.e., if list was [0,0,1,1,1,1,1], we would have '0 2 5', with the 0 representing the lack of fill at start.
    # Dealing with this is an edge case (although currently does not exist in CSV file).
    # Requires a little bit of extra code, but would allow for handling those weird cases if/when they come up.
def info_exists_encoded_list_parser(info_exists_encoded_list):
    starts_filled = True  # Initialize to what usually happens: first column filled.
    if info_exists_encoded_list[0] == 0:  # Check if first column was actually not filled.
        starts_filled = False  # If first column was not filled, instead set to False.
    grouped_by_existence = []  # Initialize empty list. We'll fill it with more lists, grouped by existence status.
    for k, g in itertools.groupby(info_exists_encoded_list):  # itertools has easy method to break up by matched status.
        #     In above, k is key part, unneeded for our purposes, stays unused. g is group iterator.
        grouped_by_existence.append(list(g))  # Convert group iterator to a list, put list in grouped_by_existence.
    # Did a quick test, printed the grouped_by_existence list results on a few test inputs, works fine.

    # At this point, the grouped_by_existence var has a list of lists, broken down by matched status.
        # e.g., original input of  [1,1,1,0,0,1,1]  -->  grouped_by_existence = [ [1, 1, 1],  [0, 0],  [1, 1] ]
    # Let's make a list of each of their counts, going in order.
    match_status_count_list = []  # Initialize.
    # Only possible wrinkle is if first column was empty, because we assume first value is count of filled cols.
    # Deal with that issue now by checking if it was filled, then possibly adding a 0 to start match_status_count_list.
    if not starts_filled:  # If first column was empty, we need to indicate that count of nothing now.
        match_status_count_list.append(0)  # There was a lack of fill in first column.
    for status_list in grouped_by_existence:  # Go through our grouped list from above.
        match_status_count_list.append( len(status_list) )  # Count number of elements in each group, append count.
    # Did a quick test, printed the match_status_count_list results on a few test inputs, works fine.

    # Now we have what we need to encode our finished string and return it to user
    # Because alternation is already implied, we don't need any clever logic, just join above with spaces.
    # .join method only works on strings, but our list has int types, so we construct a list of strings in join call.
    return ' '.join( [str(i) for i in match_status_count_list] )
    # Above explanation: comprehension creates list of strings from the integer status count values.
    # ' '.join(list) joins everything together with spaces between, then we immediately return that and we're done!




test = [0, 0, 0, 0, 1,1,1,0,0,1,1,1,1,0,0,1,0,1]

output = info_exists_encoded_list_parser(test)

print(output)
print(type(output))
print(output + "Hello world!")