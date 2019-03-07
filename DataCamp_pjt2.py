### Now, I am creating a function
### that can do the same thing as the former python statemente can do.

master_df = pd.read_csv('master.csv')

def count_entries(df, col_name):
    '''Return a dictionary with counts of
    occurrences as value for each key.'''
    langs_count = {}
    col = df[col_name]
    for entry in col:
        if entry in langs_count.keys():
            langs_count[entry] += 1
        else :
            langs_count[entry] = 1
    return langs_count

result = count_entries(master_df, 'country')

print(result)
