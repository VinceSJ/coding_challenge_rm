# Stuff about Question 3 & 4

Since so much of what happens in Q3 directly connects to Q4, figured it was better to just hit them together or at least keep the work in a single folder.

------

### Q3: Task Statement
Build an API with the technology of your choice. Parse the contents of the provided CSV file props.csv and serve the results as a JSON object at the endpoint '/data'
The API results must contain only properties in California, and contain the following:
- PROP_NAME
- ADDRESS
- CITY
- STATE_ID
- ZIP
- MISSING_FIELD_COUNT (number of fields in a record that is missing data)
- MISSING_DATA_ENCODING - **[modified, per email]** a string where each number, delimited by spaces (`' '`), indicates consecutive columns with and without data, e.g. [a,b,c,,,d,e] will be `3 2 2` (3 columns with data followed by 2 columns with missing data followed by 2 columns with data).  
**[another spec addition]** While working, I realized issues could pop up in encoding if first column was blank (since likely a decoder would assume first value is always existing info). This does not occur in CSV, but just in case I wrote in that if first column is blank, it begins with a `0` to show lack of info at start, e.g. [ , b, c, d, , , g, h] would encode as `0 1 3 2 2`

You are free to use data stores of your choice.

### Q4: Task Statement
Using the frontend tools of your choice, build out an application to cansume the API you built in Q1 and display the results in a table.


-----

## Working Log / Thoughts

**Note to reader:** Feel free to poke around in here, but it's somewhat stream of consciousness. Mostly exists for me to think through planning and what I'm doing.

### Q3
I see this task as basically breaking into four major components:
1. Read in and parse the CSV file.
2. Take that information and manipulate it.
3. Write information we want into a data format that can be JSON-ified (likely a dictionary)
4. Have a framework that spits out that JSON object when requested.

There is likely to be a lot of overlap between task 2 & 3, along with some overlap between 3 & 4.

At the moment, the CSV file we're reading is small enough (under 50KB) that we can probably do all this without any need for a fancy data store. When the API is called, we slurp up the the whole CSV file, process it, write all the results into a dictionary as we process, then spit it out via some JSON-ification.

We'll want some way to manage each of our property objects, so let's just manage it ~~by associating each proprty with its MSA_ID.~~ (~~Pretty sure those are unique...~~ *self, make sure to check MSA_ID is unique!*  **Yay self!** Checked, and... **they're not unique**.) Probably a good idea to have them associated with that ID anyway.

Wheulp. Looks like we'll need something else to associate them with. I guess it could also just be an array of objects, but that seems so *untidy*... Could just iterate through. Property 1, then 2, etc. Oooh, how about we append a sequential number to the MSA_ID? Then again, maybe the MSA_ID doesn't matter at all? Eh, I guess an array would be fine...?

Ah, wait, poking around the file, I now realize that PROP_ID might be the unique one. Let's go check...  Yay! **PROP_ID** is unique! You can run the `check_uniqueness` script on any future CSV file if you think that uniqueness was just a fluke or you're worried it has become no longer unique.

Good news, STATE_ID field in CSV is all lower caps, so we can just match to string 'ca', no worries about alternative versions for California.

Realized a possible issue with format of MISSING_DATA_ENCODING. A decoding process would very likely assume first value indicates a run of filled columns, but it is possible that the first value could be empty (does not appear in CSV, so an edge case, but conceivable). As such, should have a 0 placed as first value in string if first column is empty to indicate empty at start and that next number is run of missing fields. Spec added to Q3 task statement at top.



#### Learning JSON
Uhhh... So, I'll be frank, I have very little experience with JSON. So you'll find a file in here called `gitgud_learning_json.py`, possibly also some output files written as `gitgud_OtherStuff` -- these form the playground where you can see some of my experimentation with the library, etc.