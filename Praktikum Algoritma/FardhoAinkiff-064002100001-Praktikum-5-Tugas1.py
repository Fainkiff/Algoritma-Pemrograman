nilai = 0    
datasiswa = list() 

ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    x = str(input('"00" untuk mengakhiri!\nNilai siswa: ')) 
    if x == '00': 
        ulang = 1
    else: 
        if x == 'A': 
            nilai = float(4.00)
        elif x == 'A-':
            nilai = float(3.75)
        elif x == 'B+':
            nilai = float(3.50)
        elif x == 'B':
            nilai = float(3.00)
        elif x == 'B-':
            nilai = float(2.75)
        elif x == 'C+':
            nilai = float(2.50)
        elif x == 'C':
            nilai = float(2.00)
        elif x == 'C-':
            nilai = float(1.75)
        elif x == 'D':
            nilai = float(1.50)
        elif x == 'E':
            nilai = float(1.25)
        else:
            print('Nilai tidak valid')
            skor = 0
        print(('\nNilai {0} = {1}').format(nomor,nilai))
        datasiswa.append(nilai)
    
rata2 = sum(datasiswa) / len(datasiswa) 
print('Rata ratanya :', rata2)
