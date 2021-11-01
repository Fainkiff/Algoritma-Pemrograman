@author: acer
Nama : Fardho Ainkiff Rasya
NIM : 064002100001
"""

def fungsi_ratarata(): 
    nilai = 0 
    ulang = 1
    nomor = 0
    while ulang == 1:
        nomor += 1
        x = str(input('"00" untuk mengakhiri!\nNilai siswa: ')) 
        if x == '00':
             nomor -= 1
             ulang = 0
        else:
            if x == 'A': 
                nilai += float(4.00)
                a = '4'
            elif x == 'A-':
                nilai += float(3.75)
                a = '3.75'
            elif x == 'B+':
                nilai += float(3.50)
                a = '3.5'
            elif x == 'B':
                nilai += float(3.00)
                a = '3'
            elif x == 'B-':
                nilai += float(2.75)
                a = '2.75'
            elif x == 'C+':
                nilai += float(2.50)
                a = '2.5'
            elif x == 'C':
                nilai += float(2.00)
                a = '2'
            elif x == 'C-':
                nilai += float(1.75)
                a = '1.75'
            elif x == 'D':
                nilai += float(1.50)
                a = '1.5'
            elif x == 'E':
                nilai += float(1.25)
                a = '1.25'
            else:
                print('Nilai tidak valid')
                nomor -= 1
                a = "0"          
            print(f'nilai ke-{nomor} = {a}')
    
    ratarata = nilai / nomor
    return ratarata
                  
print("reratanya adalah : ", fungsi_ratarata())
