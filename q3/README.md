# Stuff about Question 3

### Task Statement
Build an API with the technology of your choice. Parse the contents of the provided CSV file props.csv and serve the results as a JSON object at the endpoint '/data'
The API results must contain only properties in California, and contain the following:
- PROP_NAME
- ADDRESS
- CITY
- STATE_ID
- ZIP
- MISSING_FIELD_COUNT (number of fields in a record that is missing data)
- MISSING_DATA_ENCODING - **[modified, per email]** a string where each number, delimited by spaces (`' '`), indicates consecutive columns with and without data, e.g. [a,b,c,,,d,e] will be `3 2 2` (3 columns with data followed by 2 columns with missing data followed by 2 columns with data)

You are free to use data stores of your choice.


### Working Log / Thoughts
I see this task as basically breaking into four major components:
1. Read in and parse the CSV file.
2. Take that information and manipulate it.
3. Write information we want into a data format that can be JSON-ified (likely a dictionary)
4. Have a framework that spits out that JSON object when requested.

There is likely to be a lot of overlap between task 2 & 3, along with some overlap between 3 & 4.

At the moment, the CSV file we're reading is small enough (under 50KB) that we can probably do all this without any need for a fancy data store. When the API is called, we slurp up the the whole CSV file, process it, write all the results into a dictionary as we process, then spit it out via some JSON-ification.



#### Learning JSON
Uhhh... So, I'll be frank, have very little experience with JSON. So you'll find a file in here called `gitgud_learning_json.py`, possibly also some output files written as `gitgud_OtherStuff` -- these form the playground where you can see some of my experimentation with the library, etc.