a = int(input('Masukkan bilangan positif: '))
if a<0:
    print('Mohon masukkan bilangan positif')
    exit()
n = int(input('Masukkan nilai n (n>=0): '))
if n<0:
    print('Mohon masukkan nilai n, dengan n>=0')
    exit()

b = a

if n==0:
    b = 1

for i in range(n-1):
    b *= a

print('hasil dari',a,'pangkat',n,'=',b)
