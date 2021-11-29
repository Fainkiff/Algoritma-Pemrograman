@author: acer
Nama : Fardho AInkiff Rasya
NIM : 064002100001
"""

def write(string):
    file = open(f"{title}.txt","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{title}.txt", "r")
    teks = file.read()
    print(teks)
    
title = str(input("Judul File :"))
filename = (f"{title}.txt")
f = open(filename, "w")
f.close()

print(f"FILE {filename} Created")
print("Press x to end the program")


baris = True
while baris == True:
    isi = (input(""))
    if isi == "x" or isi == "X" :
        print("\nFile Saved")
        baris = False
    else:
        write(isi)
        read()
