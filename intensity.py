#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, warnings, glob
import pandas as pd
import numpy as np
from termcolor import colored
warnings.filterwarnings('ignore')

# Load topics
csvs = glob.glob('analyzed_topics/*')

# Read Topics
for csv in csvs:
    topic = csv.split('/')[-1]
    # Analyze only non analyzed topics
    print(colored(topic,'red'))
    entries = pd.read_csv(csv)
    feel_len = len(entries.dropna(subset=['e_feel']))
    intensity_len = len(entries.dropna(subset=['e_intensity']))
    if feel_len != intensity_len:
      len_col = entries.shape[0]
      for i, entry in enumerate(entries['Entry']):
        if entries['e_feel'][i] == 1 and pd.isna(entries['e_intensity'][i])  == True:
          print(str(i) + ' out of ' + str(len_col))
          print(entry)
          indx = entries[entries['Entry']==entry].index.values.astype(int)[0]
          try:
            uresp = input('Intensity ')
          except SyntaxError:
            uresp = None
          if uresp is not None:
            entries.loc[i, 'e_intensity'] = uresp
      entries.to_csv('analyzed_topics/' + topic,index=False)
