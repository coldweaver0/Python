import time

#Soal 1 (Kalkulator Sederhana)
print(20*'=')
print('Kalkulator Sederhana')
print(20*'=')
bil1 = float(input('Masukkan bilangan ke-1 : '))
opr = str(input('Masukkan operasi (+,-,*,/) : '))
bil2 = float(input('Masukkan bilangan ke-2 : '))
if opr=='+':
    print('Hasil dari',bil1,opr,bil2,'=',bil1+bil2)
elif opr=='-':
    print('Hasil dari',bil1,opr,bil2,'=',bil1-bil2)
elif opr=='*':
    print('Hasil dari',bil1,opr,bil2,'=',bil1*bil2)
elif opr=='/':
    print('Hasil dari',bil1,opr,bil2,'=',bil1/bil2)
else:
    time.sleep(0.7)
    print('Dimohon agar memasukkan operasi yang benar.')
    counter = ['3','2','1']
    time.sleep(1.5)
    for reboot in counter:
        print(reboot)
        time.sleep(1.5)
    print('Menutup program...')
    time.sleep(1.5)
    print('Harap memulai ulang program.')
    exit()

#Soal 2 (Belah Ketupat)
bin = int(input('Masukkan jumlah bintang (bilangan ganjil) : '))
if (bin%2)==0:
    print('Ini bukan ganjil.')
    time.sleep(1.5)
    print('Menutup program...')
    time.sleep(2)
    print('Harap memulai ulang program.')
    exit()
for t in range(1,bin+1):
    if t<(bin/2):
        print((bin-t)*' '+t*'*'+(t-1)*'*')
    else :
        print((t-1)*' '+(bin-t)*'*'+((bin-t)+1)*'*')
