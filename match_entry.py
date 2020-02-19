#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, warnings, glob
import pandas as pd
import numpy as np
from termcolor import colored
warnings.filterwarnings('ignore')

def tr2en(df):
    # Replace Turkish characters to English
    df = df.str.replace('İ','i')
    df = df.str.replace('Ü','u')
    df = df.str.replace('Ö','o')
    df = df.str.replace('Ş','s')
    df = df.str.replace('Ç','c')
    df = df.str.replace('ı','i')
    df = df.str.replace('ü','u')
    df = df.str.replace('ö','o')
    df = df.str.replace('ş','s')
    df = df.str.replace('ç','c')
    df = df.str.replace('ğ','g')
    df = df.str.replace('(','<')
    df = df.str.replace(')','>')
    return df
# Load topics
csvs = glob.glob('topics/*')
# Load Analyzed Topics
a_csvs = glob.glob('analyzed_topics/*')
a_csvs = [i.split('/')[-1] for i in a_csvs]
# Load settlements
settlements = pd.read_csv('settlements/settlements.csv')
city = settlements.drop_duplicates(subset='city', keep="last")
city = city['city'].tolist()
town = settlements.drop_duplicates(subset='town', keep="last")
town = town['town'].tolist()
district = settlements.drop_duplicates(subset='district', keep="last")
district = district['district'].tolist()
neighborhood = settlements.drop_duplicates(subset='neighborhood', keep="last")
neighborhood = neighborhood['neighborhood'].tolist()
settlements = city + town + district + neighborhood
# Read Topics
for csv in csvs:
    topic = csv.split('/')[-1]
    # Analyze only non analyzed topics
    if topic not in a_csvs:
        print(colored(topic,'red'))
        entries = pd.read_csv(csv)
        entries['e_feel'] = ''
        entries['e_city'] = np.nan
        entries['e_town'] = np.nan
        entries['e_neighborhood'] = np.nan
        entries['e_intensity'] = np.nan
        entries['e_guess'] = np.nan
        len_col = entries.shape[0]
        # TR2EN
        entries['Entry'] = tr2en(entries['Entry'])
        # Read Entries
        e_city = []; e_town = []; e_district = []; e_neighborhood = []; e_feel = []; e_intensity = []; e_guess = [];
        for i, entry in enumerate(entries['Entry']):
            if any(settlement in entry for settlement in settlements):
                print(str(i) + ' out of ' + str(len_col))
                print(entry)
                indx = entries[entries['Entry']==entry].index.values.astype(int)[0]
                uresp = input('Il, ilce, mahalle (space ile ayir) ')
                if len(uresp) != 0:
                    entries.loc[i, 'e_feel'] = 1
                    if len(uresp.split()) == 1:
                        entries.loc[i, 'e_city'] = uresp
                    else:
                        ans = uresp.split(' ')
                        entries.loc[i, 'e_city'] = ans[0]
                        entries.loc[i, 'e_town'] = ans[1]
                        if len(ans) == 3:
                            entries.loc[i, 'e_neighborhood'] = ans[2]
                buyukluk = input('Suser Tahmini: ')
                if len(buyukluk) != 0:
                    entries.loc[i, 'e_guess'] = buyukluk
        entries.to_csv('analyzed_topics/' + topic,index=False)
