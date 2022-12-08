template = {
    'nama':'nama',
    'nim':'0000000000',
    'gender':'gender',
    'total_sks':'00'
}

data_mahasiswa = {}
i = 1

while True:
    print('DATA MAHASISWA')
    print('-'*20)

    mahasiswa = dict.fromkeys(template.keys())
    mahasiswa['nama'] = input('Nama Mahasiswa: ')
    mahasiswa['nim'] = input('NIM: ')
    mahasiswa['gender'] = input('Gender: ')
    mahasiswa['total_sks'] = input('Total SKS Mahasiswa: ')
    data_mahasiswa[i] = mahasiswa

    print(f"{'KEY':<6} | {'NAMA':<25} | {'NIM':<15} | {'GENDER':<15} | {'TOTAL SKS':<6}")
    print('-'*83)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        GENDER =data_mahasiswa[KEY]['gender']
        TOTAL_SKS = data_mahasiswa[KEY]['total_sks']

        print(f"{KEY:<6} | {NAMA:<25} | {NIM:<15} | {GENDER:<15} | {TOTAL_SKS:<6}")
    i = i+1

    ulang = input('Masukkan data lagi? (y/n) ')
    if ulang == 'y':
        continue
    if ulang == 'n':
        print('MENGHENTIKAN PROGRAM...')
        break
