@author: acer
Nama : Fardho Ainkiff Rasya
NIM : 064002100001
"""
import cmath as cm

a = int(input("Masukan Nilai A : "))
b = int(input("Masukan Nilai B : "))
c = int(input("Masukan Nilai C : "))



if a == 0 :
    print("Nilai a != 0 ")
    
else :
    D = (b*b) - (4*a*c) #cari nilai D
    
    if D>0 :
        x1 = (-b+cm.sqrt(D))/(2*a)
        x2 = (-b-cm.sqrt(D))/(2*a)
        print("Memiliki akar berbeda")
    elif D == 0 :
        x1 = -b/2*a
        x2 = -b/2*a
        print("Memiliki akar sama")
    else :
        x1 = (-b+cm.sqrt(D))/(2*a)
        x2 = (-b-cm.sqrt(D))/(2*a)
        print("Merupakan akar imajiner")
print('Persamaan kuadrat : ({0}x^2 +{1}x + {2})'.format(a, b, c))
print("Diskriminannya = ", D)
print("Akar x1 = ", x1)
print("Akar x2 =", x2)
