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
  if fname in topics:
    #print(colored(fname,'red'))
    topic_pd = pd.read_csv('../analyzed_topics/' + fname)
    #print('Magnitude of earthquake: ' + str(mw))
    for i,g in enumerate(topic_pd['e_guess']):
      if g == ' ':
        topic_pd['e_guess'][i] = float('NaN')
    topic_pd['e_guess']= pd.to_numeric(topic_pd.e_guess)
    #print('Average of suser guesses: ' + str(round(topic_pd['e_guess'].mean(),1)) + ' out of ' + str(topic_pd.count()['e_guess']) + ' guess')
    print(fname + ',' + str(mw) + ',' + str(round(topic_pd['e_guess'].mean(),1)) + ',' + str(topic_pd.count()['e_guess']))
