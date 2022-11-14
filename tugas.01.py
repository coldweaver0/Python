# Zaky zaujan Jayaputra
# M. Rafly Syharul Fathan

def fungsi():
    print('Ini adalah fungsi')
fungsi()


def SuaraSapi():
    print('moooo!!!')
SuaraSapi()
def HargaSapi():
    print('Harga daging sapi per kg adalah Rp.100.000')
HargaSapi()


def HargaTotalSapi(kg):
    SuaraSapi()
    harga = 100000
    hargatotal = kg*harga
    print('Harga',kg,'kg daging sapi adalah',hargatotal)
HargaSapi()
HargaTotalSapi(4)
HargaTotalSapi(0.5)
HargaTotalSapi(1)
HargaTotalSapi(17)


def siswa(nama):
    print('Siswa ini bernama :',nama)
siswa('Rafly')


def guru(nama,pelajaran):
    print('Guru ini bernama :',nama)
    print('Mengajar :', pelajaran)
guru(nama='Wawan',pelajaran='Fisika')
guru(pelajaran='Penjas',nama='Endang')
guru('Olahraga','Rehan') #Contoh yang salah


def penjagasekolah(nama,shift='Siang',galak='Tidak'):
    print('Penjaga sekolah ini bernama :',nama)
    print('Shiftnya :',shift)
    print('Sifat :',galak)
penjagasekolah('Entis')
penjagasekolah('Maman',shift='Malam')
penjagasekolah('Asep',galak='Sangat galak')
penjagasekolah(shift='Malam',galak='Galak') #Hasilnya error karena tidak diberikan argumen 'nama'
