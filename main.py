# IMPORTS
import requests
import sys
import webbrowser
from lxml import etree
from datetime import datetime

# CONFIG
jobTitleSelector = '/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/h1/text()'
companySelector = '/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div[1]/a/text()'
liFormat = '<li><a href="{url}">{jobTitle} @ {company}</a></li>'
body = 'Jobs {today}<ol>{lis}</ol>'

# FUNCTIONS
def open_urls():
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        urls = f.read()
        f.close()
    
    urls = urls.split('\n')
    if urls[-1] == '': urls = urls[:-1]

    return list(set(urls)) # remove duplicates

def select_and_format(url):
    r = requests.get(url)
    dom = etree.HTML(r.content)
    
    jobTitle = dom.xpath(jobTitleSelector)
    company = dom.xpath(companySelector)
    
    li = liFormat.format(url=url, jobTitle=jobTitle, company=company)
    return li

def create_html(lis):
    today = datetime.today().strftime('%m-%d-%Y')
    html = body.format(today=today, lis=lis)

    fname = today + '.html'
    with open(fname, 'w') as f:
        f.write(html)
        f.close()

    webbrowser.open(fname)
    
# MAIN
if __name__ == "__main__":
    # open text file with URLs
    urls = open_urls()
    
    # loop through each URL and grab job title and company name into <li> for <ol>
    lis = ''.join([select_and_format(url) for url in urls])
    
    # export results to html and open in browser
    create_html(lis)


