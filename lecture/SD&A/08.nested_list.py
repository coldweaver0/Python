data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]
print('List biasa:',data_list_biasa)

list_2D = [data_0,data_1]                                       # Contoh dari Nested List.
print('Nested list:',list_2D)                                  # Nested List = list di dalam list.

peserta_0 = ['Zain',19,'Laki-Laki']
peserta_1 = ['Rafly',18,'Laki-Laki']
peserta_2 = ['Zaky',18,'Laki-Laki']

list_peserta = [peserta_0,peserta_1,peserta_2]
print(list_peserta)

#Looping list
kumpulan_angka = [3,5,6,2,1]
print('\nLooping list')
print('-'*12)
for angka in kumpulan_angka:
    print('Angka:',angka)

panjang = len(kumpulan_angka)
print('\nLooping list len')
print('-'*17)
for angka in range(panjang):
    print('Angka:',kumpulan_angka[angka])

#Comprehension
kumpulan_angka = [3,5,6,2,1,1000]
print('\nComprehension')
print('-'*13)
[print('Data:',angka) for angka in kumpulan_angka]

#Enumerate
kumpulan_angka = [3,5,6,2,1,2000]
print('\nEnumerate')
print('-'*9)
for index,data in enumerate(kumpulan_angka):
    print('Index:',(index),'Data:',data)

#Membuat biodata tanpa input dengan nested list
peserta_0 = ['Zain',19,'Laki-Laki','Bandung']
peserta_1 = ['Rafly',18,'Laki-Laki','Bengkulu']
peserta_2 = ['Zikra',19,'Laki-Laki','Painan']
peserta_3 = ['Zaky',18,'Laki-Laki','Pekanbaru']
list_peserta = [peserta_0,peserta_1,peserta_2,peserta_3]

print('\nBiodata peserta')
print('-'*15)
for peserta in list_peserta:
    print('\nNama   :',peserta[0])
    print('Umur   :',peserta[1])
    print('Gender   :',peserta[2])
    print('Alamat   :',peserta[3])

#Membuat biodata memakai input dengan nested list
print('*'*15)
print('Biodata')
print('*'*15)
nama = input('Nama: ')
umur = input('Umur: ')
gender = input('Gender: ')
alamat = input('Alamat: ')
peserta_x = [nama,umur,gender,alamat]
print(peserta_x)

#Program biodata yang menyimpan data sebelumnya memakai nested list, terdapat di "python/biodata_list.py"

#List berdasarkan index
data = ['ani','budi','sari']
print(data[2])
data[1] = 'ari'
print(data[1])
print(data)