#!/usr/bin/env python3

# This is a playground for creating the data that will eventually get output as JSON.
# Desired structure is a dictionary of dictionaries:
# First level is PROP_ID as keys, with values being dictionaries:
    # Second level is dictionaries that have key-value pairs for
        # - PROP_NAME
        # - ADDRESS
        # - CITY
        # - STATE_ID
        # - ZIP
        # - MISSING_FIELD_COUNT
        # - MISSING_DATA_ENCODING  (delimiter of space: ' ')

import csv  # For reading CSV.
import itertools  # Helps in defining function info_exists_encoded_list_parser below.
    # Imported for "groupby", which allows us to easily break up a list based on changes.


# Function that does most of the work for parsing missing field data into string MISSING_DATA_ENCODING.
# Later in the code, once we have the info_exists_encoded_list (e.g. [1,1,1,0,0,1,1]), we need to parse that and
# write a string delimited with spaces that represents how many at a time are missing.
# INPUT: a list of 1's and 0's, where 1's represent data in that field, 0's represent blank field.
# OUTPUT: a string representing count of filled fields, alternating with count of blank fields. Space delimited.
    # e.g. [1,1,1,0,0,1,1] will be '3 2 2' (3 columns with data, then 2 columns empty, followed by 2 columns with data)
# It is assumed that the first output of string always represents filled fields.
    # i.e., if list was [0,0,1,1,1,1,1], we would have '0 2 5', with the 0 representing the lack of fill at start.
    # Dealing with this is an edge case (currently does not exist in CSV file), but could be bad later otherwise.
    # Requires a little bit of extra code, but would allow for handling those weird cases if/when they come up.
def info_exists_encoded_list_parser(info_exists_encoded_listing):
    starts_filled = True  # Initialize to what usually happens: first column filled.
    if info_exists_encoded_listing[0] == 0:  # Check if first column was actually not filled.
        starts_filled = False  # If first column was not filled, instead set to False.
    grouped_by_existence = []  # Initialize empty list. We'll fill it with more lists, grouped by existence status.
    for k, g in itertools.groupby(info_exists_encoded_listing):  # itertools has easy way to break up by matched status.
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
        match_status_count_list.append(0)  # There was a lack of fill in first column, mark it in our list.
    for status_list in grouped_by_existence:  # Go through our grouped list from above.
        match_status_count_list.append(len(status_list))  # Count number of elements in each group, append count.
    # Did a quick test, printed the match_status_count_list results on a few test inputs, works fine.

    # Now we have what we need to encode our finished string and return it to user
    # Because alternation is already implied, we don't need any clever logic, just join above with spaces.
    # .join method only works on strings, but our list has int types, so we construct a list of strings in join call.
    return ' '.join( [str(i) for i in match_status_count_list] )
    # Above explanation: list comprehension creates list of strings from the integer status count values.
    # ' '.join() joins everything together with spaces between, then we immediately return that and we're done!


# Context manager for CSV file.
with open('props.csv', 'rt') as csv_in:  # Read in the properties CSV (in this folder, I sure hope) as text.
    infodump = csv.DictReader(csv_in)  # Slurp up the file into infodump, a CSV object.
    datarows = [row for row in infodump]  # Create list of dicts, where each dict is a row and has keys of column heads.
# The thing we have our info in is 'datarows'.
# 'datarows' has the added benefit of being a list of OrderedDicts, so we can also call based on location.
    # This fact will be quite helpful when it comes time to set up for MISSING_DATA_ENCODING.


top_level_dict = {}  # Initialize an empty dictionary.
for row in datarows:
    if row['STATE_ID'] == 'ca':  # Only do the work on California properties.
        building_dict = {}  # The second level dictionary where all info about this property goes.
        building_dict['PROP_NAME'] = row['PROP_NAME']  # Insert property name.
        building_dict['ADDRESS'] = row['ADDRESS']  # Insert address value.
        building_dict['CITY'] = row['CITY']  # Insert city value.
        building_dict['STATE_ID'] = row['STATE_ID']  # Insert state value, which is 'ca', but whatever, extensible.
        building_dict['ZIP'] = row['ZIP']  # Insert address value.
        # Did a quick test, printed the dictionary, checked a few randomly selected values, looks good.

        # Next, we'll pull info to help build the MISSING_Stuff values.
        # There are more direct ways to do the _FIELD_COUNT, but this will make the _DATA_ENCODING easier.
        # We're going to create a list that encodes whether or not there is info.
        # If 1 in a spot, that column has info, if 0, there's no info (a blank string '') in column.
        info_exists_encoded_list = []  # Initialize.
        for i in row:  # i is each key for row, comes in order of columns in CSV.
            # This is where we are taking advantage of CSV DictReader object being OrderedDict.
            # Because ordered, these match to appropriate locations and not standard no-order dict.
            if row[i] == '':  # If the value for the column is an empty string, we encode 0 in our list.
                info_exists_encoded_list.append(0)
            else:  # If anything other than empty string, there is info, so encode a 1.
                info_exists_encoded_list.append(1)
        # Quick and dirty test: Use below command, compare to CSV manually by just picking a few and checking.
        # print(row['PROP_ID'], info_exists_encoded_list)

        # Great, now that we have the info_exists_encoded_list, it's easier to make stuff.
        missing_field_count = info_exists_encoded_list.count(0)  # Count 0's in list, that's your missing field count.
        # Now that we know the value, add it to our dictionary of info.
        building_dict['MISSING_FIELD_COUNT'] = missing_field_count  # Insert missing field count.
        # NOTE: This is internally an int type. Should cause no issues, but heads up.

        # Let's get our last required field, MISSING_DATA_ENCODING.
        missing_data_encoded_string = info_exists_encoded_list_parser(info_exists_encoded_list)
        # Above just runs the parsing function (defined above), gives us the string we want.
        building_dict['MISSING_DATA_ENCODING'] = missing_data_encoded_string  # Insert encoded string.


        prop_id = row['PROP_ID']  # Snag the PROP_ID for that row (a unique identifier, see check_uniqueness file)
        top_level_dict[row['PROP_ID']] = building_dict  # Insert key of PROP_ID with value of dict of associated info.





# Alright, all the work is done at this point, just do a few quick and dirty tests by hand.

# TESTING!
for thing in top_level_dict:
    if top_level_dict[thing]["MISSING_FIELD_COUNT"] > 0:
        print(thing, top_level_dict[thing])

# Read a few of these off to yourself. These are only the ones where there are missing fields, because they're the
# cases more likely to go wrong.

# Checked a few, everything worked fine.
# Most vicious property was PROP_ID 66820 with 8 missing fields all over the place, still worked fine.
