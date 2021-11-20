@author: acer
Nama : Fardho Ainkiff Rasya
NIM  : 064002100001
"""
def perpangkatan(bil, pangkat):
    if pangkat == 0:
        return 1
    elif pangkat < 0:
        return 1 / perpangkatan(bil, -pangkat)
    else:
        return bil * perpangkatan(bil, pangkat-1)
    
while True:
    bil = int(input("Masukan angka : "))
    pangkat = int(input("Masukan pangkat : "))
    print(perpangkatan(bil, pangkat),"\n")
