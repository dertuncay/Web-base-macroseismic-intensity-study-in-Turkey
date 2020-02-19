import pandas as pd
import numpy  as np
import os, warnings, glob
from termcolor import colored
warnings.filterwarnings('ignore')

# Load EQ list
eqs = pd.read_csv('../earthquake_info.csv')
# Read EQ files
csvs = glob.glob('../analyzed_topics/*')
topics = [];
for csv in csvs:
  topics.append(csv.split('/')[-1])

for name,mw in zip(eqs['Name'],eqs['Mw']):
  fname = name + '.csv'
  #print(colored(fname,'red'))
  if name in ['17-haziran-2017-izmir-depremi--5392358','10-ekim-2019-yalova-depremi--6208576-2','10-ekim-2019-yalova-depremi--6208576-3','10-ekim-2019-yalova-depremi--6208576-4','10-aralik-2019-balikesir-depremi--6277350-2','10-aralik-2019-balikesir-depremi--6277350-3']:
    continue
  elif name == '17-haziran-2017-izmir-depremi--5392358-2':
    topic_pd = pd.read_csv('../analyzed_topics/' + name[:-2] + '.csv')
    topic_pd = topic_pd.iloc[20:]
  elif name == '10-ekim-2019-yalova-depremi--6208576':
    topic_pd = pd.read_csv('../analyzed_topics/' + name + '.csv')
    topic_pd = topic_pd.iloc[0:199]
  elif name == '6-subat-2017-canakkale-depremi--5296414':
    topic_pd = pd.read_csv('../analyzed_topics/' + fname)
    topic_pd = topic_pd.iloc[0:86]
  elif name == '6-subat-2017-canakkale-depremi--5296414-2':
    topic_pd = pd.read_csv('../analyzed_topics/' + name[:-2] + '.csv')
    topic_pd = topic_pd.iloc[86:]
  else:
    topic_pd = pd.read_csv('../analyzed_topics/' + fname)
  #print('Magnitude of earthquake: ' + str(mw))
  for i,g in enumerate(topic_pd['e_guess']):
    if g == ' ':
      topic_pd['e_guess'][i] = float('NaN')
  topic_pd['e_guess']= pd.to_numeric(topic_pd.e_guess)
  #print('Average of suser guesses: ' + str(round(topic_pd['e_guess'].mean(),1)) + ' out of ' + str(topic_pd.count()['e_guess']) + ' guess')
  print(name + ',' + str(mw) + ',' + str(round(topic_pd['e_guess'].mean(),1)) + ',' + str(topic_pd.count()['e_guess']))
