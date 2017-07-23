#!/usr/bin/env python3

# This is a playground for creating the data that will eventually get output as JSON.
# Desired structure is a dictionary of dictionaries:
# First level is PROP_ID as keys, with values being dictionaries:
    # Second level is dictionaries that have key-value pairs for - PROP_NAME
        # - ADDRESS
        # - CITY
        # - STATE_ID
        # - ZIP
        # - MISSING_FIELD_COUNT
        # - MISSING_DATA_ENCODING  (delimiter of space: ' ')

import csv  # For reading CSV.
import itertools  # For one specific function, groupby, that allows us to easily break up a list based on changes.

# Context manager for CSV file.
with open('props.csv', 'rt')  as csv_in:  # Read in the properties CSV (in this folder, I sure hope) as text.
    infodump = csv.DictReader(csv_in)  # Slurp up the file into infodump, a CSV object.
    datarows = [row for row in infodump]  # Create list of dicts, where each dict is a row and has keys of column heads.
# The thing we have our info in is 'datarows'.
# 'datarows' has the added benefit of being a list of OrderedDicts, so we can also call based on location.
    # This fact will be quite helpful when it comes time to get MISSING_DATA_ENCODING.


top_level_dict = {}  # Initialize an empty dictionary.
for row in datarows:
    if row['STATE_ID'] == 'ca':  # Only do the work on California properties.
        building_dict = {}  # The second level dictionary where all info about this property goes.
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


        prop_id = row['PROP_ID']  # Snag the PROP_ID for that row (a unique identifier, see check_uniqueness file)
        top_level_dict[row['PROP_ID']] = building_dict  # Insert key of PROP_ID with value of dict of associated info.


