import requests
import sys
import re
from bs4 import BeautifulSoup as bs

# CONFIG
jobTitleSelector = '/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/h1/text()'
companySelector = '/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div[1]/a/text()'

# Functions
def openUrls():
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        urls = f.read()
        f.close()
    
    urls = urls.split('\n')
    urls.remove('')

    return urls

if __name__ == "__main__":
    # ptn = re.compile('^(.*?)\..*')
    # fname = ptn.findall(sys.argv[1])[0]

    # open text file with URLs
    urls = openUrls()
    
    # loop through each URL and grab the following:
        # Job title
        # Company name
    # Create numbered list of jobs