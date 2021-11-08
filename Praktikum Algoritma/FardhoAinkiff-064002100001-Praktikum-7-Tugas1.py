@author: acer
Nama : Fardho Ainkiff Rasya
NIM : 064002100001
"""

def cetakbilprima(num):
    if num > 1:
       angkaditentukan(num) 
    else:
        print(num, 'adalah bilangan prima')
        
def angkaditentukan(num):
    for i in range(2, num):
            if(num % i == 0):
                print(num, 'adalah bukan bilangan prima')
                print(i,'kali',num//i, '=',num)
                break
    else:
        print(num, "adalah bilangan prima")

loop = 1
while loop == 1:
     num = int(input("masukan bilangan yang ingin dicek : "))
     cetakbilprima(num)
