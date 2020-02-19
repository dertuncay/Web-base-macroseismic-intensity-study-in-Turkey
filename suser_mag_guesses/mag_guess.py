#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, warnings, glob
import pandas as pd
import numpy as np
warnings.filterwarnings('ignore')
# Load EQ list
eqs = pd.read_csv('../maps.csv')
# Load topics
csvs = glob.glob('../analyzed_topics/*')


# Read Topics

for csv in csvs:
    topic = csv.split('/')[-1]
    # Multiple earthquakes
    if topic == '6-subat-2017-canakkale-depremi--5296414.csv':
      topic_pd1 = pd.read_csv(csv, nrows=87)
      print(topic[:-4].split('--')[-1] + ',' + str(eqs.loc[eqs['Name'] == '6-subat-2017-canakkale-depremi--5296414', 'Mw'].iloc[0]) + ',' + str(round(topic_pd1['e_guess'].mean(),1)) + ',' + str(topic_pd1.count()['e_guess']))
      topic_pd2 = pd.read_csv(csv, skiprows=range(1, 88))
      print(topic[:-4].split('--')[-1] + '-2' + ',' + str(eqs.loc[eqs['Name'] == '6-subat-2017-canakkale-depremi--5296414-2', 'Mw'].iloc[0]) + ',' + str(round(topic_pd2['e_guess'].mean(),1)) + ',' + str(topic_pd2.count()['e_guess']))
    elif topic == '17-haziran-2017-izmir-depremi--5392358.csv':
      topic_pd1 = pd.read_csv(csv, nrows=13)
      print(topic[:-4].split('--')[-1] + ',' + str(eqs.loc[eqs['Name'] == '17-haziran-2017-izmir-depremi--5392358', 'Mw'].iloc[0]) + ',' + str(round(topic_pd1['e_guess'].mean(),1)) + ',' + str(topic_pd1.count()['e_guess']))      
      topic_pd2 = pd.read_csv(csv, skiprows=range(1, 14))
      print(topic[:-4].split('--')[-1] + '-2' + ',' + str(eqs.loc[eqs['Name'] == '17-haziran-2017-izmir-depremi--5392358-2', 'Mw'].iloc[0]) + ',' + str(round(topic_pd2['e_guess'].mean(),1)) + ',' + str(topic_pd2.count()['e_guess']))      
    elif topic == '10-ekim-2019-yalova-depremi--6208576.csv':
      topic_pd1 = pd.read_csv(csv, nrows=200)
      print(topic[:-4].split('--')[-1] + ',' + str(eqs.loc[eqs['Name'] == '10-ekim-2019-yalova-depremi--6208576', 'Mw'].iloc[0]) + ',' + str(round(topic_pd1['e_guess'].mean(),1)) + ',' + str(topic_pd1.count()['e_guess']))      
      topic_pd2 = pd.read_csv(csv, skiprows=range(1, 201),nrows=51)
      print(topic[:-4].split('--')[-1] + '-2' + ',' + str(eqs.loc[eqs['Name'] == '10-ekim-2019-yalova-depremi--6208576-2', 'Mw'].iloc[0]) + ',' + str(round(topic_pd2['e_guess'].mean(),1)) + ',' + str(topic_pd2.count()['e_guess']))       
      topic_pd3 = pd.read_csv(csv, skiprows=range(1, 252),nrows=226)
      print(topic[:-4].split('--')[-1] + '-3' + ',' + str(eqs.loc[eqs['Name'] == '10-ekim-2019-yalova-depremi--6208576-3', 'Mw'].iloc[0]) + ',' + str(round(topic_pd3['e_guess'].mean(),1)) + ',' + str(topic_pd3.count()['e_guess']))         
      topic_pd4 = pd.read_csv(csv, skiprows=range(1, 478),nrows=210)
      print(topic[:-4].split('--')[-1] + '-4' + ',' + str(eqs.loc[eqs['Name'] == '10-ekim-2019-yalova-depremi--6208576-4', 'Mw'].iloc[0]) + ',' + str(round(topic_pd4['e_guess'].mean(),1)) + ',' + str(topic_pd4.count()['e_guess']))         
    elif topic == '10-aralik-2019-balikesir-depremi--6277350.csv':
      topic_pd1 = pd.read_csv(csv, nrows=257)
      print(topic[:-4].split('--')[-1] + ',' + str(eqs.loc[eqs['Name'] == '10-aralik-2019-balikesir-depremi--6277350', 'Mw'].iloc[0]) + ',' + str(round(topic_pd1['e_guess'].mean(),1)) + ',' + str(topic_pd1.count()['e_guess']))        
      topic_pd2 = pd.read_csv(csv, skiprows=range(1, 258),nrows=115)
      print(topic[:-4].split('--')[-1] + '-2' + ',' + str(eqs.loc[eqs['Name'] == '10-aralik-2019-balikesir-depremi--6277350-2', 'Mw'].iloc[0]) + ',' + str(round(topic_pd2['e_guess'].mean(),1)) + ',' + str(topic_pd2.count()['e_guess']))         
      topic_pd3 = pd.read_csv(csv, skiprows=range(1, 373),nrows=142)
      print(topic[:-4].split('--')[-1] + '-3' + ',' + str(eqs.loc[eqs['Name'] == '10-aralik-2019-balikesir-depremi--6277350-3', 'Mw'].iloc[0]) + ',' + str(round(topic_pd3['e_guess'].mean(),1)) + ',' + str(topic_pd3.count()['e_guess']))           
    else:
      topic_pd = pd.read_csv(csv)
      print(topic[:-4].split('--')[-1] + ',' + str(eqs.loc[eqs['Name'] == csv[19:-4], 'Mw'].iloc[0]) + ',' + str(round(topic_pd['e_guess'].mean(),1)) + ',' + str(topic_pd.count()['e_guess'])) 
