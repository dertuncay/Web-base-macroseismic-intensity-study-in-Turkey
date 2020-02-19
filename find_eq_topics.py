import mechanize, re, os, requests, warnings, urllib.request, shutil
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
warnings.filterwarnings('ignore')

# Open website
brwsr = mechanize.Browser()

response = brwsr.open('https://eksisozluk.com/basliklar/ara?SearchForm.Keywords=depremi&SearchForm.Author=&SearchForm.When.From=&SearchForm.When.To=&SearchForm.NiceOnly=false&SearchForm.FavoritedOnly=false&SearchForm.SortOrder=Count')
text = response.read()
soup = BeautifulSoup(text)
# Get the all results in terms of pages (eg. 1-20)
eqlinks = [];
for link in soup.findAll('a'):
    if 'href' in link.attrs:
        if 'depremi' in link['href']:
            eqlinks.append(link['href'])
# Get earthquakes in first page
first_page = eqlinks[2:-1]
first_page = ['https://eksisozluk.com' + s for s in first_page]
# Go to second page
next_page = 'https://eksisozluk.com' + eqlinks[-1]
# Part of the link to go to next pages
nextpage_link = eqlinks[-1][:-1]
response = brwsr.open(next_page)
text = response.read()
soup = BeautifulSoup(text)
eqlinks = [];
for link in soup.findAll('a'):
    if 'href' in link.attrs:
        if 'depremi' in link['href']:
            eqlinks.append(link['href'])
# Get earthquakes in second page
second_page = eqlinks[2:-1]
second_page = ['https://eksisozluk.com' + s for s in second_page]
mydivs = soup.findAll('div', {'class': 'pager'})
# Current page = 2
currentpage = int(mydivs[0]['data-currentpage'])
# Total number of pages
totalpages  = int(mydivs[0]['data-pagecount'])

# Go over pages
page_numbers = np.linspace(currentpage,totalpages,totalpages-currentpage+1,dtype=int)
# Gathering part
link_list = first_page + second_page
for page_n in page_numbers:
    next_page = 'https://eksisozluk.com' + nextpage_link + str(page_n)
    response = brwsr.open(next_page)
    text = response.read()
    soup = BeautifulSoup(text)
    eqlinks = []
    for link in soup.findAll('a'):
        if 'href' in link.attrs:
            if 'depremi' in link['href']:
                eqlinks.append(link['href'])
    eqlinks = ['https://eksisozluk.com' + s for s in eqlinks[2:-1]]
    link_list = link_list + eqlinks
links = pd.DataFrame(link_list,columns=['Links'])
links.to_csv('links.csv',index=False)
