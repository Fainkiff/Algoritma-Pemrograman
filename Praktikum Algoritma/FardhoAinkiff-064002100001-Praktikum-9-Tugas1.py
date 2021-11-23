print ("Selamat datang di Program Biodata")
print ("=================================")

def write(string):    
    file = open("biodata01.txt", "w")
    file.write(str(string))
    file.close()
    

def read():   
    file = open("biodata01.txt", "r")
    biodata = file.read()
    print(biodata)

# Ambil input dari user
Nama = str(input("Masukan Nama mu: "))
Umur = str(input("Masukan Umur mu: "))
Alamat = str(input("Masukan Alamatmu: "))
Email = str(input("Masukan Emailmu: "))
Dosen = str(input("Masukan Dosen Walimu: "))
biodata = ("Nama: {}\nUmur: {}\nAlamat: {}\nEmail: {}\nDosen Wali : {}").format(Nama,Umur,Alamat,Email,Dosen)


write(biodata)  
read()
