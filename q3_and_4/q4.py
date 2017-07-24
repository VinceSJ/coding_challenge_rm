#!/usr/bin/env python3

# ### Q4: Task Statement
# Using the frontend tools of your choice, build out an application to cansume the API you
# built in Q1 and display the results in a table.



import flask  # Framework for serving JSON and results page.
import requests  # For grabbing JSON via API call.



##################
# Running Flask
##################

app = flask.Flask(__name__)  # Fire up the Flask framework.

@app.route('/')  # Just in case they didn't read the README...
def home():
    return "You want to instead go to /table. Also, make sure the q3.py Flask framework is ALSO running."

@app.route('/table')  # Runs call to q3.py Flask serving JSON props data.
def call_and_make_table():
    api_call = requests.get('http://localhost:4747/data')  # Make sure matches port q3.py is serving on.
    top_level_dict = api_call.json()
    return flask.render_template('table_template.html', props_dict=top_level_dict)


app.run(port=8000, debug=True)  # Run it locally for testing.
