import numpy as np
import pandas as pd

prc_ser = pd.Series(data=prices, index=dates)
bday_ser = pd.Series(data=bday, index=dates)

df = pd.DataFrame({'Close': prc_ser, 'Bday': bday_ser})

print(df)

df_new = df_nan.convert_dtypes()
print(df_new.info())

print(df_new.loc['3000-01-01'])

import pandas as pd

data = {
    'col_a': [1, 2, 3],
    'col_b': [10.0, None, 13.0]
}


df0 = pd.DataFrame(data)
print('\nprint(df0) -->')
print(df0)
print('\ndf0.info() --> ')
df0.info()


idx = ['2020-01-01', '2020-01-02', '2020-01-03']
df1 = pd.DataFrame(data, index=idx)
print('\nprint(df1) -->')
print(df1)
print('\ndf1.info() --> ')
df1.info()


idx_dt = pd.to_datetime(idx)
df2 = pd.DataFrame(data, index=idx_dt)
print('\nprint(df2) -->')
print(df2)
print('\ndf2.info() --> ')
df2.info()


def find_most_common_word(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    most_common_word = None
    max_count = 0

    for word, count in word_count.items():
        if count > max_count:
            most_common_word = word
            max_count = count

    return most_common_word, max_count


file_path = 'iso.txt'
common_word, frequency = find_most_common_word(file_path)
print(f"The most common word is '{common_word}' with a frequency of {frequency}.")


def freqword(filepath):
    with open(filepath) as file:

        counts = dict()
        for line in file:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word,0) + 1

        maxcount = None
        maxword = None
        for word,count in counts.items():
            if maxcount is None or count > maxcount:
                maxword = word
                maxcount = count

    return(f"The most frequent word is: {maxword}, and the number of times appeared is: {maxcount}")

