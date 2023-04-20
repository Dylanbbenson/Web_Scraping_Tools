# Web_Scraping_Tools
This is a repository with tools to scrape data from the web. I created this repo to help store the scripts I create for my data science projects. Hopefully you can find some use with them.

As of now, the following are in this repository:

1. zillow_web_scrape.py. This is a python script to scrape real estate data from the web. Simply download the script then run it from the command line using the python command (make sure you have the latest python kernel installed). The script will request a city and state to pull from, then will write out two csv files, one with homes for sale and another for apartments available to rent. These files will have many fields of data, including address, bedrooms and bathrooms, price, and an image source. The data is sorted on the best_deal field, which is price subtracted from the zillow estimate. 
- syntax: python3 zillow_web_scrape.py

Stay tuned for more!
