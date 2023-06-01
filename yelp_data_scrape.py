from yelpapi import YelpAPI
import requests
import pandas as pd
import json
import sys
import re
import warnings
from datetime import date

# take in command line arguments
city = sys.argv[1]
state = sys.argv[2]
current_date = date.today().strftime('%Y-%m-%d')

# input checking and modification
if city == '': 
    city = input("Enter the city name: ")

if state == '':
    state = input("Enter the state in abbreviation format (eg: Minnesota = MN) : ")

while len(state) != 2:
    print("Invalid state entry. Try again.")
    state = input("Please try again: ")

city = city.replace(" ", "-")
city = city.capitalize()
city_state = city + ", " + state

# authenticate your requests with your Yelp API key
with open('credentials.json') as f:
    credentials = json.load(f)

api_key = credentials['yelp'] 

yelp_api = YelpAPI(api_key)

# make API call to search for businesses
offsets = [0, 50, 100, 150, 200, 250]
dfs = []
for offset in offsets:
    raw_data = yelp_api.search_query(term='restaurants', location=city_state, offset=offset, limit=50)
    df = pd.DataFrame(raw_data['businesses'])
    dfs.append(df)

# Concatenate them vertically
combined_df = pd.concat(dfs)

# Reset the index, since it will have duplicate values
combined_df = combined_df.reset_index(drop=True)

######################################################
# data cleaning and conversion



######################################################

combined_df.to_csv("./data/" + city + "_Restaurants_"+current_date+".csv")