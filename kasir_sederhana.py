import tkinter as tk
from tkinter import messagebox as msgbox

window = tk.Tk()
window.title('Kasir Sederhana')
window.configure(bg='light blue')

menu_makanan = {}
total_harga_makanan = sum(menu_makanan.values())
total_pesanan = 0

def entry_menu():
    global total_pesanan
    makanan = input1.get()
    harga = input2.get()

    if makanan != "" and harga != "":
        menu_makanan[makanan] = int(harga)
        input1.delete(0, "end")
        input2.delete(0, "end")
        total_pesanan = total_pesanan + 1
        label5.config(text=f"Total Pesanan : {total_pesanan}")
        global total_harga_makanan
        total_harga_makanan = sum(menu_makanan.values())
        label6['text']=f"Total Harga = Rp.{total_harga_makanan}"
    else:
        msgbox.showerror(title='ERROR', message='Tiap kolom wajib diisi')

def window_menu():
    menu = tk.Tk()
    menu.title('List')
    judul_list_menu = tk.Label(menu, text="Menu yang Dipesan :")
    judul_list_menu.pack()
    list_menu = tk.Listbox(menu, width=32, height=10)
    list_menu.pack()

    for makanan, harga in menu_makanan.items():
        list_makanan = f"{makanan} = Rp.{harga}"
        list_menu.insert("end", list_makanan)

def reset_list():
    global menu_makanan
    menu_makanan = {}
    global total_pesanan
    total_pesanan = 0
    label5.config(text=f"Total Pesanan : {total_pesanan}")
    global total_harga_makanan
    total_harga_makanan = sum(menu_makanan.values())
    label6['text'] = f"Total Harga : Rp.{total_harga_makanan}"

label1 = tk.Label(window, text="Nama Makanan atau Minuman : ", bg='light blue')
label2 = tk.Label(window, text="Harga : ", bg='light blue')
label3 = tk.Label(window, text="      ", bg='light blue')
label4 = tk.Label(window, text="      ", bg='light blue')
label5 = tk.Label(window, text = f"Total Pesanan : {total_pesanan}", bg='light blue')
label6 = tk.Label(window, text="Total Harga : Rp.0", bg='#95c4c2')
label7 = tk.Label(window, text="catatan :", justify="left", bg='light blue')
label8 = tk.Label(window, text="- Kolom nama & harga tidak boleh kosong.", justify="left", bg='light blue')
label9 = tk.Label(window, text="- Harap masukkan harga yang sesuai (angka).", justify="left", bg='light blue')
label10 = tk.Label(window, text="      ", bg='light blue')

input1 = tk.Entry(window, text="input 1")
input1.config(width=34)
input2 = tk.Entry(window, text="input 2")
input2.config(width=34)

button1 = tk.Button(window, text= "Masukkan ke Menu", command=entry_menu)
button2 = tk.Button(window, text= "List Pesanan", command=window_menu)
button3 = tk.Button(window, text= 'Reset List', command=reset_list)

label1.grid(row=0, column=0)
label2.grid(row=2, column=0)
label3.grid(row=4, column=0)
label4.grid(row=0, column=1)
label5.grid(row=0, column=2)
label6.grid(row=6, column=0)
label7.grid(row=7, column=0, sticky="w")
label8.grid(row=8, column=0, sticky="w")
label9.grid(row=9, column=0, sticky="w")
label10.grid(row=2, column=2)

input1.grid(row=1, column=0)
input2.grid(row=3, column=0)

button1.grid(row=5, column=0)
button2.grid(row=1, column=2)
button3.grid(row=3, column=2)

if __name__ == "__main__":
    window.mainloop()