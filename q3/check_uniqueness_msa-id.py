#!/usr/bin/env python3

# Need to quickly verify that the MSA_ID field is always a unique value (or at least on this CSV I was given).

import csv

# Use context manager, cuz why not?
with open('props.csv', 'rt')  as csv_in:  # Read in the properties CSV (in this folder, I sure hope) as text.
    infodump = csv.DictReader(csv_in)  # Slurp up the file into an infodump object.
    datarows = [row for row in infodump]  # Create list of dicts, where each dict is a row and has keys of column heads.

print(datarows[47])


# Crud. MSA_ID 12420 shows up a bunch. There goes that. Just stumbled on to it by random chance, too.
