import requests
import sys
import re
from bs4 import BeautifulSoup as bs

# CONFIG
jobTitleSelector = ''
companySelector = ''

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

    # print(openUrls())


# open text file with URLs
# loop through each URL and grab the following:
    # Job title
    # Company name
# Create numbered list of jobs