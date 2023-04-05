def terkecil():
  a = int(input('\nBanyak angka yang ingin diurutkan : '))
  angka = [None]*a

  for i in range(a):
   str_i = str(i+1)
   b = int(input('Masukkan angka ke-'+str_i+' : '))
   angka[i] = b
  print(' ')

  sort = list.copy(angka)
  n = len(angka)
  cek = 0
  fase = 0
  if n<=10:
    urutan = input('Tampilkan proses pengurutan? (y/n) ')
    print(' ')
    if urutan == "y" and "Y":
      print('Berikut proses pengurutannya: ')
      for j in range (n-1,0,-1):
          for k in range(j):
            cek = cek + 1
            str_cek = str(cek)
            if sort[k] > sort[k+1]:
              temp = sort[k]
              sort[k] = sort[k+1]
              sort[k+1] = temp
              fase = fase + 1
              str_fase = str(fase)
            print('Pengecekan ke-'+str_cek+' (Fase '+str_fase+') : ',sort)
      print(' ')
    else:
      for j in range (n-1,0,-1):
          for k in range(j):
            if sort[k] > sort[k+1]:
              temp = sort[k]
              sort[k] = sort[k+1]
              sort[k+1] = temp
  else:
    for j in range (n-1,0,-1):
        for k in range(j):
          if sort[k] > sort[k+1]:
            temp = sort[k]
            sort[k] = sort[k+1]
            sort[k+1] = temp

  print('Sebelum diurutkan :',angka)
  print('Setelah diurutkan :',sort)
  print(' ')


print('\nPROGRAM BUBBLE SORT')
print('-------------------')
print('Pilih salah satu :')
print('1. Terbesar ke Terkecil (Ascending)')
print('2. Terkecil ke Terbesar (Descending)')
pilih = input('')
if pilih == '2':
  terkecil() 
