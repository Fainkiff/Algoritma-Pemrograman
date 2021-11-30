@author: acer
Nama : Fardho Ainkiff Rasya
NIM : 064002100001
"""


def bubbsort(list):
    #-1 diberikan karena mulai dari index 0 dari len(list)
    #0 diberikan untuk angka yang dicapai di akhir, 
    #misal length 9 maka kita mulai dari 8 -> 0
    #-1 diberikan untuk mengurutkan data dari akhir -> awal
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            #untuk pertukaran jika angka kiri > angka kanan
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

        
pos = -1
def binarysearch(list, n):
    #untuk l mulai dari 0
    #untuk u mulai dari 8 (index)
    l = 0
    u = len(list)-1
    #lower bound tidak boleh melebihi upper
    while l <= u:
        mid = (l+u) // 2
        #jika nilai dari mid = n 
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        #jika nilai n < mid maka ubah upperbound saja
        #jika nilai n > mid maka ubah lowerbound saja
        else:
            if list[mid] < n:
                l = mid+1;
            else:
                u = mid-1;

    return False
                
list = [7, 2, 4, 5, 9, 13, 15, 18, 17]

print("Data sebelum di-sorting : ",list)
bubbsort(list)
print ("Sesudah di-sorting : ",list)

n=int(input("Masukan angka yang ingin dicari : "))
if binarysearch(list, n):
    print("Ditemukan pada index ke- ", pos)
else:
    print("Angka tidak ditemukan")
