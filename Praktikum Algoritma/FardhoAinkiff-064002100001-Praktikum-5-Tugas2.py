@author: acer
Nama : Fardho Ainkiff Rasya
NIM : 064002100001
"""
print('Selamat datang di anco(u)r')
input('Taman Bermain Keluarga')

while True:
    umur = int(input('Masukan Umur Pengunjung : '))
    bayar = True
    if umur <= 2:
        price = 0
        print("Tiket gratis")
        bayar = False
    elif umur >= 3 and umur <= 12:
        price = 14
        print('Harga tiket $',price)
    elif umur >=65:
        price = 18
        print('Harga tiket $',price)
    else:
        price = 23
        print('Harga tiket $',price)
        
    if bayar == True:
        juang = int(input('Masukan jumlah uang :'))
        if juang == price:
            print('Uang anda pas :D')
        elif juang < price:
            print('uang yang dimasukan kurang')
        elif juang > price:
            juang -= price
            print('Jumlah kembalian : $', juang)
