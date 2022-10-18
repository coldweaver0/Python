angka = 1                                 #Contoh penggunaan dari penambahan (variabel angka akan terus digantikan dengan yang terbaru.)
print(angka)
angka = angka+1
print(angka)
angka = angka+1
print(angka)
angka = angka+1
print(angka)
angka = angka+1
print(angka)
#
angka = 2                                 #Contoh penggunaan dari pengulangan (variabel angka akan terus ditambah selama variabel angka memenuhi kondisi, yakni <=10.)
while angka<=10:                          #Outputnya akan berbentuk seperti 2,\n4,\n6,\n8,\n10 (\n disini berarti ditulis di line baru. Tiap angka berada di line berbeda.)
  print(angka)                            #Dalam penggunaan "\n (line baru)" ditulis dalam bentuk string.
  angka = angka+2                         #[PENTING] Variabel angka yang dimodifikasi seperti di samping tidak boleh ditulis sebelum while. Hal ini juga sama seperti "if,for,dsb".
#
angka = (1,2,3,4,5)                       #Kurung yang digunakan boleh apa saja, seperti "" ( , [ , { "".
for i in angka:
    print(i)                              #Angka menghasilkan output dari content variabel angka secara berurutan, seperti contoh di atas.)
#
buah = ('apel','nanas','jeruk')           #Menghasilkan output dengan string yg ditulis + dengan masing-masing content dari variabel buah.
for anj in buah:                          #Contoh dari output : Zaky apel,\nZaky nanas,\nZaky jeruk
  print('Zaky',anj)
#
i = 2                                     #Contoh program untuk mengoutput bilangan-bilangan prima.
while(i<100):
    j = 2
    while(j<=(i/j)):
        if not (i%j): break
        j = j+1
    if (j>i/j):
        print(i)
    i = i + 1
#
for i in range(5):                        #Range(x) artinya bilangan-bilangan dari 0 sampai sebelum x.
    for j in range(6):
        print('[',i,j,']',end=' ')        #Penggunaan end di sini berguna untuk mengganti spasi yang menjadi bawaan dengan spasi.
    print()                               #Digunakan untuk memberi spasi setiap range(6).

#Di bawah ini adalah berbagai pengimplementasian dari pengulangan (loop) dalam membentuk bagun datar.
sk = int(input('Masukkan jumlah bintang : '))     #Segitiga siku-siku
for i in range(1,sk):
    print(i*'*')
#
p = int(input('Masukkan jumlah bintang : '))      #Persegi
for i in range(0,p):
    print(p*'*')
#
ss = int(input('Masukkan jumlah bintang : '))     #Segitiga sama kaki
for i in range(1,ss+1):
    print((ss-i)*' '+(i)*'*'+(i-1)*'*')
    
#[PENTING] Perbedaan antara While dan For, yakni While akan terus mengulang selama kondisi bernilai true (1) dan akan berhenti saat bernilai false (0). Sedangkan For
#Digunakan untuk mengulangi item/content dari urutan apapun. ex:(1,2,3,4,5) atau ('aku','suka','daging') ataupun campuran dari bebrbagai tipe data.
