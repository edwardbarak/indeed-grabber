# IMPORTS
import requests
import sys
from lxml import etree

# CONFIG
jobTitleSelector = '/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/h1/text()'
companySelector = '/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div[1]/a/text()'
liFormat = '<li><a href="{url}">{jobTitle} @ {company}</a></li>'

# FUNCTIONS
def open_urls():
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        urls = f.read()
        f.close()
    
    urls = urls.split('\n')
    urls.remove('')

    return urls

def select_and_format(url):
    r = requests.get(url)
    dom = etree.HTML(r.content)
    jobTitle = dom.xpath(jobTitleSelector)
    company = dom.xpath(companySelector)
    li = liFormat.format(url=url, jobTitle=jobTitle, company=company)
    return li
    
# MAIN
if __name__ == "__main__":
    # open text file with URLs
    urls = open_urls()
    
    # loop through each URL and grab job title and company name into <li> for <ol>
    ol = [select_and_format(url) for url in urls]
    
    # export results to  html

