@author: acer
Nama : Fardho Ainkiff Rasya
NIM  : 064002100001
"""

def fibonacci(n):
    if n < 0:
        print("Masukan angka yang benar")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)
    
loop = True
while loop == True:
    n = int(input("Masukan sebuah bilangan : "))
    if n == -1:
        loop = False
        print("Terima kasih sudah menggunakan program")
        break
    else:
        print("Bilangan fibonacci ke-",n,"adalah",fibonacci(n))
