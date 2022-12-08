def fungsi_saya():                                     #Fungsi adalah blok kode terorganisir yang dapat dipanggil
    print('Latihan fungsi pertama')                    #berulang-ulang. Fungsi dapat digunakan untuk menyimpan data.
    print('Ini latihan fungsi saya :D')
def fungsi_anda():
    print('Latihan fungsi kedua')
    print('Ini latihan fungsi anda :$')
for i in range(1,4):
    fungsi_saya()
    fungsi_anda()

def salampagi(nama):
    print('Selamat pagi', nama)
salampagi('Zaky')
salampagi('Rafly')

def tambah(angka1,angka2):
    hasil = angka1 + angka2
    print(f'{angka1} + {angka2} = {hasil}')
tambah(2.3,4)

def LuasPersegiPanjang(panjang,lebar):
    luas = panjang*lebar
    print('Panjang :',panjang,'meter')
    print('Lebar :',lebar,'meter')
    print('Luas :',f'{panjang}*{lebar}={luas}','meter')
LuasPersegiPanjang(6,9)
LuasPersegiPanjang(19,8)
LuasPersegiPanjang(7.4,3.008)

def luas(panjang,lebar):
    luas2 = panjang*lebar
    return luas2                                        #Return gunanya adalah menampung sementara hasil dari
x = luas(10,2)                                          #operasi, baik dalam variabel ataupun dalam operasi
z = x*100                                               #itu sendiri.
print(z)

def tambah(angka1,angka2):
    return angka1+angka2
a = tambah(13,7)
b = tambah(5,3)
print(a)
print(b)

def operasi_mtk(angka1,angka2):
    kurang = angka1 - angka2
    kali = angka1 * angka2
    tambah = angka1 + angka2
    bagi =  angka1 / angka2
    return kurang,kali,tambah,bagi

a,b,c,d = operasi_mtk(7,8.2)                            #Contoh pertama
print(f'Hasil pengurangan = {a}')
print(f'Hasil perkalian = {b}')
print(f'Hasil penambahan = {c}')
print(f'Hasil pembagian = {d}')
e,f,g,h = operasi_mtk(3.22,7)                            #Contoh kedua
print(f'Hasil pengurangan = {e}')
print(f'Hasil perkalian = {f}')
print(f'Hasil penambahan = {g}')
print(f'Hasil pembagian = {h}')
