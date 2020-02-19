import mechanize, re, os, requests, warnings, urllib.request, shutil
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
warnings.filterwarnings('ignore')

# Load Database
df = pd.read_csv('earthquake_w_pages.csv')
num_eqs = len(df['Links'][:20])
flags = [];
for i, link in enumerate(df['Links'][:20]):
    print(i,num_eqs,link)#
    eq_name = link.split('/')[-1]
    # Open website
    brwsr = mechanize.Browser()
    # Get only first earthquake. Later Do the for loop!
    response = brwsr.open(link)
    text = response.read()
    soup = BeautifulSoup(text)
    # Get page information
    mydivs = soup.findAll('div', {'class': 'pager'})
    if mydivs == []:
        currentpage = 1
        totalpages  = 1
    else:
        currentpage = int(mydivs[0]['data-currentpage'])
        # Total number of pages
        totalpages  = int(mydivs[0]['data-pagecount'])
    # Go over pages
    page_numbers = np.linspace(currentpage,totalpages,totalpages-currentpage+1,dtype=int)
    brwsr.close()
    # Lists that are fed by the data
    suser_list = []; entry_date_list = []; entry_link_list = []; entry_list = [];
    for page in page_numbers:
        # Open website
        brwsr = mechanize.Browser()
        # Get only first earthquake. Later Do the for loop!
        response = brwsr.open(link + '?p=' + str(page))
        text = response.read()
        soup = BeautifulSoup(text)
        entries = soup.findAll('div', {'class': 'content'})
        entry_dates = soup.findAll('a', {'class': 'entry-date permalink'})
        susers = soup.findAll('a', {'class': 'entry-author'})
        # Get information of the page
        for entry,date,suser in zip(entries,entry_dates,susers):
            entry_list.append(entry.get_text(' ', strip=True))
            suser_list.append(suser.string)
            entry_date_list.append(date.string)
            entry_link_list.append('https://eksisozluk.com' + date['href'])
    topic = pd.DataFrame({'Entry': entry_list,'User': suser_list,'EntryDates': entry_date_list,'EntryLinks': entry_link_list})
    topic.to_csv('topics/' + eq_name + '.csv',index=False)
