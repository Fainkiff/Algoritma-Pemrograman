@author: acer
Nama : Fardho Ainkiff Rasya
NIM  : 064002100001
"""

print("Program ini akan menentukan banyak hari pada bulan dan tahun yang diminta")
ulang = True
while ulang == True:
    print("Masukan 0 untuk menghentikan program")
    bulan = int(input("Masukan Bulan: "))
    if bulan == 0:
        ulang = False
        print("")
    else:
        if bulan == 1 or bulan == 2 or bulan == 3 or bulan == 4 or bulan == 5 or bulan == 6 or bulan == 7 or bulan == 8 or bulan == 9 or bulan == 10 or bulan == 11 or bulan == 12:
            if bulan == 2:
                tahun = int(input("Masukan Tahun (cont. 2021): "))
                if (tahun%4==0) or (tahun%400==0):
                    print("Ada 29 Hari")
                else:
                    print("Ada 28 Hari")
            else:
                if(bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12):
                    print("Ada 31 Hari")
                else:
                    print("Ada 30 Hari")
        else:
            print("Angka yang dimasukan tidak valid", bulan)
