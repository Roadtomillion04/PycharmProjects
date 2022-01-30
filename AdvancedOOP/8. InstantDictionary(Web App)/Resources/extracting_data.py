import pandas as pd

df = pd.read_csv('data.csv')
all_words = df.word # gets word col

# .loc is primarily label based, but may also be used with a boolean array.
r1 = df.loc[df['word']=='bee'] # gets specific df
print(r1)

r2 = r1.definition # gets df with only definition col
print(r2)

result = tuple(r2) # some words has more definition, So appending all to a tuple
print(result)
