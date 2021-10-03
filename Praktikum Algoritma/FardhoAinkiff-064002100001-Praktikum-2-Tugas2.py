@author: acer
Nama : Fardho Ainkiff Rasya
NIM  : 064002100001
"""
from math import sin, cos, sqrt, atan2, radians, acos
#perkiraan ruas bumi dalam KM
R = 6371

lat1 = radians(float(input("masukan lattitude 1 = ")))
lon1 = radians(float(input("masukan lattitude 2 = ")))
lat2 = radians(float(input("masukan longitude 1 = ")))
lon2 = radians(float(input("masukan longitude 2 = ")))

dlat = (lat2-lat1)
dlon = (lon2-lon1)

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

jarak = R * c


print("jarak antara dua titik adalah", jarak, "kilometer")
