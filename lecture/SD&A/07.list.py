data = ['flashdisk',100,'harddisk']
data_0 = data[0]
data_terakhir = data[-1]                                        # Bisa juga 2.
data_100 = data[2]                                              # Bisa juga 1.
print('Data list pertama (index 0) =',data_0)
print('Data list terakhir (index -1) =',data_terakhir)
print('Data list kedua (index -2) =',data_100)
#
data = ['flashdisk',100,'harddisk']
print(data)
index_flashdisk = data.index('flashdisk')                       # Mencari index suatu data pada list.
index_harddisk = data.index('harddisk')
print('Posisi index untuk flashdisk :',index_flashdisk)
print('Posisi index untuk harddisk :',index_harddisk)
#
data = ['flashdisk',100,'harddisk']
panjang = len(data)                                             # Menghitung berapa banyak data pada list.
print('Panjang data dalam list :',panjang)
data.insert(0,'Zaky')                                           # Menambahkan suatu data dalam list dengan format "(index,data)".
data.insert(2,'Memory')
data.insert(5,55)
print('Data setelah ditambah :',data)
banyak = len(data)
print('Banyak data dalam list sekarang :', banyak)
data.append(700)                                                # Menambahkan suatu data pada list di paling akhir.
print('Data setelah ditambah APPEND',data)
#
data = ['flashdisk',100,'harddisk']
data_baru = [55,'VGA','RAM']
data.extend(data_baru)                                          # Menggabungkan dua list.
print('List gabungan :',data)
data_saya = ['Python',77,'Javascript']                          # Contoh kedua dari penggabungan list.
data.extend(data.saya)
print('List gabungan baru :',data)
data[1] = 200                                                   # Mengupdate suatu list, data yang sebelumnya berada pada index tersebut akan di-replace.
print('List update :',data)
#
angka = [4,7,8,4,4,9,1,3,2,3,1]
angka4 = angka.count(4)                                         # Menghitung banyak dari suatu data pada list.
angka1 = angka.count(1)
print('Banyaknya angka 4 :',angka4)
print('Banyaknya angka 1 :',angka1)
angka.sort()                                                    # Mengurutkan data pada list (kecil - besar).
print('Angka yang sudah disort :',angka)
angka.reverse()                                                 # Mengurutkan data pada list (besar - kecil).
print('Angka yang sudah direverse :',angka)
#
data = ['flashdisk',100,'harddisk']
data1 = data                                                    # Isi dari "data1" akan selalu sama dengan "data".
print('List variabel data :',data)
print('List variabel data1',data1)

data1[0] = 'VGA'                                                # Karena data = data1, index pada "data" juga ikut berubah.
print(data)
print(data1)

data2 = data.copy()                                             # Mengcopy/menyalin suatu list.
data2[0] = 'memory'                                             # Mengcopy list dapat digunakan bila ingin mengganti data hanya pada satu list dengan data yang sama.
print('List variabel data :',data)
print('List variabel data1 :',data1)
print('List variabel data2 :',data2)
data1 = data.copy()                                             # Contoh kedua dalam penyalinan list.
data1[1] = 200
print('List variabel data :',data) 
print('List variabel data1 :',data1)
