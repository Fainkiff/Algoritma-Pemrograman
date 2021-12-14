# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 23:16:17 2021

@author: acer
"""

file = open('Negara.csv','r')

class dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

data = dictionary()
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []

x = 0
for delimiter in file:
    x += 1
    delimiter = delimiter.split(',')
    if x == 1:
        pass
    else:
        p1 = delimiter[0]
        c1.append(p1)
        p2 = delimiter[1]
        c2.append(p2)
        p3 = delimiter[2]
        c3.append(p3)
        p4 = int(delimiter[3])
        c4.append(p4)
        p5 = int(delimiter[4])
        c5.append(p5)

data.add('Negara',c1)
data.add("Ibu Kota",c2)
data.add('Benua',c3)
data.add('Luas',c4)
data.add('Populasi',c5)


import pandas as pd


hasil = pd.DataFrame(data)
print('\n Data dan Luas Negara di Dunia \n\n',hasil)

mean= hasil.groupby(['Benua']).mean()
std= hasil.groupby(['Benua']).std()

print('\nRata rata :\n',mean)
print('\nStandar Deviasi :\n',std)
