def ordinalNumber(num):
   ordinal = lambda n: str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(10<=n%100<=20 and n or n % 10, 'th')
   print(ordinal(num))

print("Ordinal Number")
print("-1 untuk menghentikan program")

loop = True
while loop == True:
    num = int(input("Masukan Angka : "))
    if num == -1:
        loop = False
        print("Terima kasih sudah menggunakan program")
        break
    else:
        ordinalNumber(num)
