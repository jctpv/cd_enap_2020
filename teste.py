import pandas as pd
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

names1880 = pd.read_csv('datasets/babynames/yob1880.txt', names=['name', 'sex', 'births'])

print(names1880.head())

years = range(1880, 2019)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'datasets/babynames/yob{0}.txt'.format(year)
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)
print(names)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
print(total_births)

plt.plot(total_births, title='Total births by sex and year')

