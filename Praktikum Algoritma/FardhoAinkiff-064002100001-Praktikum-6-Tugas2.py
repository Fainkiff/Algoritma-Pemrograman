@author: acer
Nama : Fardho Ainkiff Rasya
NIM : 064002100001
"""

print("Program ini akan menentukan banyak hari pada bulan dan tahun yang diminta")
def tanggal_bulan(bulan):
    if bulan in [1,2,3,4,5,6,7,8,9,10,11,12]:
        if bulan == 2:
            tahun = int(input("Masukan Tahun : "))
            tanggal_tahun(tahun)
        else:
            if bulan in [1,3,5,7,8,10,12]:
                print("Ada 31 hari dalam 1 bulan")
            else:
                print('Ada 30 hari dalam 1 bulan')
    else:
        print(f"Angka bulan tidak valid : (month)")

def tanggal_tahun(tahun):
    if tahun%4==0:
        print("Ada 29 hari dalam 1 bulan")
        
    else:
        print("Ada 28 hari dalam 1 bulan")
        
ulang = True
while ulang == True:
    print('masukan angka -1 untuk berhenti')
    bulan = int(input("Masukan bulan (1-12) : "))
    if bulan == -1:
        ulang = False
        print("Program berhenti")
    else:
        tanggal_bulan(bulan)
