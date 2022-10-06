# 0) Tuliskan PROGRAM STUDI SISTEM INFORMASI FAKULTAS SAINS DAN TEKNOLOGI
# 1) Panjang karakter.
# 2) Cek apakah ada huruf m di dalam kalimat di atas.
# 3) Cek apakah ada huruf T di dalam kalimat di atas.
# 4) Tampilkan index ke-8.
# 5) Tampilkan : SISTEM INFORMASI
# 6) Tampilkan : A I U E O

SI = 'PROGRAM STUDI SISTEM INFORMASI FAKULTAS SAINS DAN TEKNOLOGI'          #Jawaban dari no 0.

panjangSI = len(SI)
print('Panjang dari ' + SI + ' = ' + str(panjangSI))                        #Jawaban dari no 1.

m = 'm'
status1 = m in SI
print(m + ' ada di ' + SI + ' = ' + str(status1))                           #Jawaban dari no 2.

T = 'T'
status2 = T in SI
print(T + ' ada di ' + SI + ' = ' + str(status2))                           #Jawaban dari no 3.

print('Index ke-8 = ' + SI[8])                                              #Jawaban dari no 4.

print(SI[14:31])                                                            #Jawaban dari no 5.

print(SI[5] + ' ' + SI[12] + ' ' + SI[10] + ' ' + SI[18] + ' ' + SI[2])     #Jawaban dari no 6.
