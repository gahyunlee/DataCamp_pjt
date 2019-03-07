### trying to make a dictionary from a dataframe using iteration (for loop)
### the dictrionary has each word inside a column of a dataframe as a key 
### and the number of its occurrence as its value.

import os
import pandas as pd 
cwd = os.getcwd()
print(cwd) # to check where I am
os.chdir("/Users/Sophie/Downloads/suicide-rates-overview-1985-to-2016")
print(cwd) # to check I successfuly changed my working directory 
df = pd.read_csv('master.csv') # read my csv dataset as a dataframe
langs_count = {}
col = df['country']
for entry in col:
    if entry in langs_count.keys():
        langs_count[entry] += 1
    else :
        langs_count[entry] = 1

print(langs_count)
