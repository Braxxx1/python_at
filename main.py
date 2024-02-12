import pandas as pd


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())
one_hot_data = pd.DataFrame(columns=['robot', 'human'])

for index, row in data.iterrows():
    if row['whoAmI'] == 'robot':
        one_hot_data.loc[index] = [1, 0]
    else:
        one_hot_data.loc[index] = [0, 1]

print(one_hot_data.head())