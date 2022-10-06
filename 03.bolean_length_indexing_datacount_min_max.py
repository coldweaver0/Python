nama1 = 'Zaky'
nama2 = 'Zaujan'
nama3 = 'Jayaputra
nama_lengkap = nama1 + ' ' + nama2 + ' ' + nama3
panjang = len(nama_lengkap)                                       #Menghitung banyak karakter (spasi termasuk dalam karakter).
print('Panjang dari ' + nama_lengkap + ' = ' + str(panjang))
#
n = 'n'
status1 = n in nama_lengkap
print('n ada di ' + nama_lengkap + ' = ' + str(status1))          #Mengecek apakah benar atau tidak (True or False).
N = 'N'
status2 = N in nama_lengkap
print('N ada di ' + nama_lengkap + ' = ' + str(status2))
status3 = N not in nama_lengkap
print('N tidak ada di ' + nama_lengkap + ' = ' + str(status3))
#
print('Index ke-0 = ' + nama_lengkap[0])                          #Meng-output karakter dari ke-x.
print('Index ke-(-7) = ' + nama_lengkap[-7])
print('Index ke-4 sampai ke-8 = ' + nama_lengkap[4:9])
print('Index ke-1,3,5,7,9,11 = ' + nama_lengkap[1:12:2])
#
print('Paling kecil = ' + min(nama_lengkap))                      #Meng-output karakter terkecil & terbesar (Karakter terkecil dimulai dari spasi<tanda baca<huruf kapital
print('Paling besar = ' + max(nama_lengkap))                      #<huruf kecil).
#
data = 'Zaky Zaujan Jayaputra'                                    #Menghitung jumlah banyak karakter.
jumlah = data.count('a')
print('Jumlah dari a pada ' + nama_lengkap + ' = ' + str(jumlah))
