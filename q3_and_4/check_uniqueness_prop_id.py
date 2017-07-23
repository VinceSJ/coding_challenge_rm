#!/usr/bin/env python3

# Need to quickly verify that the MSA_ID field is always a unique value (or at least on this CSV I was given).

import csv

# Use context manager, cuz why not?
with open('props.csv', 'rt')  as csv_in:  # Read in the properties CSV (in this folder, I sure hope) as text.
    infodump = csv.DictReader(csv_in)  # Slurp up the file into an infodump object.
    datarows = [row for row in infodump]  # Create list of dicts, where each dict is a row and has keys of column heads.

# Did a quick test, comparing dictionary results for some random rows to equivalent CSV opened in spreadsheet reader.
# Reading works fine.
# Crud. MSA_ID 12420 shows up a bunch. There goes that. Just stumbled on to it by random chance, too.


# Well, let's try the PROP_ID field instead.

# Make a list of all of them:
list_of_Prop_IDs = []  # initialize
for row in datarows:
    list_of_Prop_IDs.append(row['PROP_ID'])

# Check everything worked with a quick test:
# print(list_of_Prop_IDs)
# Stuff matches nicely at top and very last, reasonable to assume it's all good.

# Let's see if there are any empty fields in those PROP_IDs:
# print('' in list_of_Prop_IDs)  # Yay, returns false.

# Now let's see if there's any overlap.
# Going to be so clever, instead of a for loop, just check size of list_of_Prop_IDs, then compare to a set of same.
# If set is smaller in size, then there is overlap. If same size, we're safe.

size_of_list = len(list_of_Prop_IDs)
print("LIST: Size of PROP_ID list, allows for repeats: ", size_of_list)

set_of_Prop_IDs = set(list_of_Prop_IDs)
size_of_set = len(list_of_Prop_IDs)
print("SET: Size of PROP_ID set, does not allow repeats: ", size_of_set)

if size_of_set == size_of_list:
    print("Yaaayyyy. They're the same size, we can use PROP_ID as a unique marker.")
else:
    print("Booooooo. They're different sizes, we gotta chuck PROP_ID")