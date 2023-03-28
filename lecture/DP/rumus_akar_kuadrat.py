a = int(input('Masukkan angka a (selain nol): '))
if a==0:
    print('Mohon masukkan angka selain nol')
    exit()
b = int(input('Masukkan angka b: '))
c = int(input('Masukkan angka c: '))

x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
print('Nilai dari x1:',x1)
print('Nilai dari x2:',x2)

if b**2 - 4*a*c < 0:
    print('b2-4ac < 0, maka akarnya imajiner')
elif b**2 - 4*a*c > 0:
    print('b2-4ac > 0, maka akarnya rill dan x1 tidak sama dengan x2')
else:
    print('b2-4ac = 0, maka akarnya rll dan x1 sama dengan x2')
