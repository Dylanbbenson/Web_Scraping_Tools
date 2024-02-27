# Web_Scraping_Tools
This is a repository with tools to scrape data from the web. I created this repo to help store the scripts I create for my data science projects. Hopefully you can find some use with them.

As of now, the following are in this repository:

**zillow_data_scrape.py**: This is a python script to scrape real estate data from the web. Simply download the script then run it from the command line using the python command (make sure you have the latest python kernel installed). The script will request a city and state to pull from, then will write out two csv files, one with homes for sale and another for apartments available to rent. These files will have many fields of data, including address, bedrooms and bathrooms, price, and an image source. The data is sorted on the best_deal field, which is price subtracted from the zillow estimate. 
- syntax: python3 zillow_data_scrape.py {city} {state}

**yelp_data_scrape.py**: This is a python script to scrape restaurant data from the web. Simply download the script then run it from the command line using the python command (make sure you have the latest python kernel installed). It uses the Yelp Fusion API to make 6 api calls and collect 300 rows of data (NOTE: you'll need to obtain your own api key from yelp.com/developers). The script will request from the user a city and state to pull from, then will populate a csv file for data analysis. This file contains many fields of data, including location, ratings, transactions, phone, and pricing.

**NFL_gamelog_scrape.py**: This is a python script to scrape game log data from pro-football-reference.com for a given team and season. The data is output to a csv file. A team and a season parameter will need to be provided. If not, then all teams and the current season are used by default.
- syntax: python3 NFL_gamelog_scrape.py {team} {season}

Stay tuned for more!
