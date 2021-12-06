class mahasiswa:
    jumlah = 0
    
    def __init__(self, nama, nim, tahun):
        self.nama = nama
        self.nim = nim
        self.tahun =  tahun
        mahasiswa.jumlah += 1
    
    def displaymahasiswa(self):
        print("\nNama : ", self.nama)
        print("NIM : ", self.nim)
        print("Tahun Angkatan : ", self.tahun)

loop = True
while loop == True:
    print(f"\nMahasiswa {(mahasiswa.jumlah)+1}\nEnter untuk mengakhiri")
    nama = input("Masukan Nama : ")
    if nama == '':
        break
    nim = input("Masukan Nim : ")
    tahun = input("Masukan Tahun Angkatan : ")
    out = mahasiswa(nama,nim,tahun)
    
    out.displaymahasiswa()
