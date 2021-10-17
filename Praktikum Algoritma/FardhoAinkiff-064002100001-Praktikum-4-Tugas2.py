@author: acer
Nama : Fardho Ainkiff Rasya
NIM  : 064002100001
"""

print("Program ini akan menentukan banyak hari pada bulan dan tahun yang diminta")
print("Ketik n untuk berhenti")


ulang = "Y"
while ulang == "Y" or ulang == "y" :
    bulan = int(input("Masukan Bulan : "))
    tahun = int(input("Masukan Tahun : "))
    if(bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12):
        print("Ada 31 hari")
    elif((bulan == 2) and ((tahun%400==0) or (tahun%4==0 and tahun%100!=0))):
        print("Ada 29 hari")
    elif(bulan == 2):
        print("Ada 28 hari")
    else:
        print("Ada 30 hari")
    ulang = input("coba lagi? ")
