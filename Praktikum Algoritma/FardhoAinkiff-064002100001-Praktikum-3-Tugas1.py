@author: acer
Nama : Fardho Ainkiff Rasya
NIM  : 064002100001
"""

a = int(input("masukan sisi 1 : "))
b = int(input("masukan sisi 2 : "))
c = int(input("masukan sisi 3 : "))

if (a == b == c) :
    print("segitia tersebut sama sisi")
elif (a + b <= c) or (a + c <= b) or (b + c <=a) :
    print("ini bukan segitiga")
elif (a == b or a == c or b == c) :
    print("segitiga tersebut sama kaki")
elif  (a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a) :
    print("segitiga tersebut siku siku")
else :
    print("segitiga tersebut segitiga sembarang")
