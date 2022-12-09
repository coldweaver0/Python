#Membuat biodata tanpa input dengan nested dictionary
mahasiswa1 = {
    'nama':'DONI',
    'gender':'Laki-Laki',
    'alamat':'Lubuk Buaya',
    'prodi':'Sistem Informasi'
}
mahasiswa2 = {
    'nama':'RISKA',
    'gender':'Perempuan',
    'alamat':'Lubuk Lintah',
    'prodi':'Matematika'
}
mahasiswa3 = {
    'nama':'DEBI',
    'gender':'Perempuan',
    'alamat':'Lubuk Alung',
    'prodi':'Aktuaria'
}
data_mahasiswa = {
    'MHS1':mahasiswa1,
    'MHS2':mahasiswa2,
    'MHS3':mahasiswa3
}

print(f"{'KEY':<6} | {'NAMA' :<10} | {'GENDER' :<10} | {'ALAMAT':<15} | {'PRODI':<25}")  # Gunakan tanda kutip yang berbeda
print('-'*70)                                                                            # antara setelah 'f' dengan tiap KEY.

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    GENDER = data_mahasiswa[KEY]['gender']
    ALAMAT = data_mahasiswa[KEY]['alamat']
    PRODI = data_mahasiswa[KEY]['prodi']

    print(f"{KEY:<6} | {NAMA:<10} | {GENDER:<10} | {ALAMAT:<15} | {PRODI:<25}")

#Program biodata yang menyimpan data sebelumnya memakai nested list, terdapat di "python/biodata_dictionary.py"