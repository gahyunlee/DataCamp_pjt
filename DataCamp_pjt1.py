import os
import pandas as pd
cwd = os.getcwd()
print(cwd)
os.chdir("/Users/Sophie/Downloads/suicide-rates-overview-1985-to-2016")
print(cwd)
df = pd.read_csv('master.csv')
langs_count = {}
col = df['country']
for entry in col:
    if entry in langs_count.keys():
        langs_count[entry] += 1
    else :
        langs_count[entry] = 1

print(langs_count)
