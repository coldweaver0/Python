list_mahasiswa = []

def biodata():
    print('Masukkan data biodata')
    print('='*21)
    nama = input('Nama: ')
    umur = input('Umur: ')
    alamat = input('Alamat: ')

    biodata = [nama,umur,alamat]
    list_mahasiswa.append(biodata)

    print('-'*57)
    print('|No|\tNama\t|\tUmur\t|\tAlamat\t\t|')
    print('-'*57)

    for num,data in enumerate(list_mahasiswa):
        print(f'|{num+1} |\t{data[0]}\t|\t{data[1]}\t|\t{data[2]}\t|')
    
while True:
    biodata()
    input_lagi = input('Apakah input lagi? (y/n)')
    if input_lagi == 'y':
        continue
    elif input_lagi == 'n':
        break
