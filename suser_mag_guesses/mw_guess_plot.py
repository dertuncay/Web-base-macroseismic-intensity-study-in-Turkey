#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, warnings, glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

def average(lst): 
    return sum(lst) / len(lst)

fig = plt.figure()    
ax = fig.add_subplot(1,1,1)
topics = pd.read_csv('mw_guess_results2.csv')
plt.hlines(0,0,len(topics['topicID']),colors = 'r', linestyles = '--')
guess = []
for i,(topicid,mw,mw_g,no_g) in enumerate(zip(topics['topicID'],topics['Mw'],topics['Av Mw Guess'],topics['No of Guess'])):
  if no_g != 0:
    # mag = plt.scatter(i,mw,color='k',label='Magnitude')
    # u_guess = plt.plot([i-.5, i+.5],[mw_g,mw_g],'r--',label='Average')
    
    plt.scatter(i,mw-mw_g,color='k')
    guess.append(abs(mw_g-mw))
print(average(guess))

plt.ylabel('Residual')
plt.xlabel('topicID')
plt.xticks(np.arange(len(topics['topicID'])), topics['topicID'].values.tolist(), rotation=90)
#plt.legend([mag],['Magnitude'])
#plt.legend(handles=u_guess)
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')
plt.xlim([-0.5,26.5])
plt.tight_layout()
#plt.show()
plt.savefig('mag_uguess.png')


# figlegend = plt.figure(figsize=(3,2))
# ax = fig.add_subplot(111)
# #plt.scatter(range(10),range(10), c='black')#'Magnitude', 
# lines = ax.plot(range(10),range(10),'r--',range(10),range(10),'ko')
# #lines = ax.scatter(range(10),range(10),color='k')
# figlegend.legend(lines, ('Average','Magnitude'), 'center')
# figlegend.show()
# figlegend.savefig('legend.png')
