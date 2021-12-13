nama : fardho ainkiff
nim : 064002100001
  
class mahasiswa:

    jumlah = 0

    def __init__(self,nama,nim,tahun):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.tahun = str(tahun)
        mahasiswa.jumlah += 1


    def URUTAN(self):
        return f"{self.nama} ; {self.nim} ; {self.tahun}"



    def JMLHDATA(self):
        print()
        print('Nama:',self.nama)
        print('NIM:',self.nim)
        print('Tahun:',self.tahun)
        print()
        input(f'Jumlah mahasiswa sekarang : {mahasiswa.jumlah} orang\nPRESS ENTER')

class settermethod:  
    jumlah = 0
    jumlah = 0
    
    def __init__(self,nama,nim,tahun):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.tahun = str(tahun)
        mahasiswa.jumlah += 1


    def URUTAN(self):
        return f"{self.nama} ; {self.nim} ; {self.tahun}"



    def JMLHDATA(self):
        print()
        print('Nama:',self.nama)
        print('NIM:',self.nim)
        print('Tahun:',self.tahun)
        print()
        input(f'Jumlah mahasiswa sekarang : {mahasiswa.jumlah} orang\nPRESS ENTER')
    
    def nama(self, a):
        self.nama = a

    def nim(self, b):
        self.nim = b   

    def tahun(self,c):
        self.tahun = c

class gettermethod:
    jumlah = 0
   
    def __init__(self,nama,nim,tahun):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.tahun = str(tahun)
        mahasiswa.jumlah += 1


    def URUTAN(self):
        return f"{self.nama} ; {self.nim} ; {self.tahun}"

    def JMLHDATA(self):
        print()
        print('Nama:',self.nama)
        print('NIM:',self.nim)
        print('Tahun:',self.tahun)
        print()
        input(f'Jumlah mahasiswa sekarang : {mahasiswa.jumlah} orang\nPRESS ENTER')
    def nama(self):
        return self.nama
    def nim(self):
        return self.nim
    def tahun(self):
        return self.tahun




while True:
    print("ketik 1 untuk method setter")
    print("ketik 2 untuk method getter")
    print(f'DATA KE {(mahasiswa.jumlah)+1}\nKetik selain 1 dan 2 untuk mengakhiri!')
    method = int(input('\nMasukan pilihan (1-2): '))

    if method == 1:
        print(f'\nDATA KE {(mahasiswa.jumlah)+1}')
        print("program menggunaakan method setter")
        a = str(input('Masukan Nama: '))
        b = str(input('Masukan NIM: '))
        c = str(input('Masukan TAHUN ANGKATAN: '))
        n = settermethod(a,b,c)
        n.JMLHDATA()
       

    elif method == 2:
        print(f'\nDATA KE {(mahasiswa.jumlah)+1}')
        print("program menggunaakan method getter")
        a = str(input('Masukan Nama: '))
        b = str(input('Masukan NIM: '))
        c = str(input('Masukan TAHUN ANGKATAN: '))
        n = gettermethod(a,b,c)
        n.JMLHDATA()
        

    else :
        break
