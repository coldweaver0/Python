# Tiap - tiap contoh di bawah harus dibuat dalam program terpisah agar dapat dijalankan.

nama = input('Siapa nama Anda ? ')                  #If & else dalam string.
if nama == 'Zaky':
  print('Kamu adalah Zaky.')            #TRUE
else:
  print('Kamu bukan Zaky.')             #FALSE
#
nilai = input(int('Masukkan nilai Anda ='))         #If & else dalam integer.
if(nilai>7):
  print('Selamat Anda lulus.')          #TRUE
else:
  print('Maaf Anda tidak lulus.')       #FALSE
#
hari_ini = input('Hari ini adalah hari ?')          #Contoh lain dalam penggunaan condition (if,else).
if hari_ini == 'Senin':
   print('Saya akan kuliah.')
elif hari_ini == 'Selasa':
   print('Saya akan pergi les.')
elif hari_ini == 'Rabu':
   print('Saya akan pergi latihan memanah.')
elif hari_ini == 'Kamis':
   print('Saya akan pergi memancing.')
elif hari_ini == 'Jumat':
   print('Saya akan pulang kampung.')
elif hari_ini == 'Sabtu':
   print('Saya akan bermain.')
elif hari_ini == 'Minggu':
   print('Saya libur kuliah.')
else:
   print('ERROR 404 NOT FOUND')
#
bilangan = input(int('Masukkan bilangan (0-20) ='))        #Contoh dari penggunaan if,else dalam menentukan bilangan ganjil/genap.
if (bilangan%2) == 0 and (0<bilangan<=20):
   print('Ini adalah bilangan genap.')
elif bilangan == 0:
   print('Nol bukanlah bilangan genap ataupun ganjil.')
elif bilangan<20:
   print('Tidak dapat mencari bilangan yang lebih dari 20.')
else:
   print('Ini adalah bilangan ganjil.')
