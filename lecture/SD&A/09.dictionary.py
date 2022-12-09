#Dictionary Key
data = {                                                          # Terdiri dari KEY('nama) & VALUE('Budi).
    'nama':'Budi',
    'alamat':'Padang'
}
print(data['nama'])                                               # Yang akan ter-print adalah KEY.
print(data['alamat'])

#Menghitung Data Dictionary
panjang = len(data)
print('\nBanyak data dictionary:',panjang)

#Mengakses Nilai Dictionary
print(data['nama'])
print(data.get('nim','Key nim tidak ada dalam dictionary'))

#Mengupdate Data Dictionary
data['nama'] = 'Ari'                                              # Meng-update VALUE dari suatu KEY.
print(data['nama'])

data['nim'] = '14022'                                             # KEY yang sebelumnya tidak ada akan tetap muncul,
print(data['nim'])                                                # mengakibatkan terbentuknya KEY baru dalam DICTIONARY.

data.update({'nim':'2217020199'})
print(data)

#Menghapus Dictionary
del data['nim']
print(data)
del data['alamat']
print(data)

#Looping
buah_buahan = {
    'buah1':'Apel',
    'buah2':'Jeruk',
    'buah3':'Mangga'
}
for buah in buah_buahan:                                          # Yang dipanggil adalah KEY.
    print(buah)

value = buah_buahan.values()                                      # Mengisi variabel dengan VALUE dari suatu DICTIONARY.
print(value)
for value in buah_buahan.values():                                # Yang dipanggil adalah VALUE.
    print(value)

for key,value in buah_buahan.items():                             # Ketika dipanggil akan berbentuk dictionary.
    print('key:',key,'value:',value)