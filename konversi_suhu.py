import tkinter as tk

def convert_temperature():
    temperature = float(entry.get())
    from_unit = from_var.get()
    to_unit = to_var.get()

    if from_unit == "Celcius":
        if to_unit == "Fahrenheit":
            result = (temperature * 9/5) + 32  # Celcius ke Fahrenheit
        elif to_unit == "Reamur":
            result = temperature * 4/5  # Celcius ke Reamur
        elif to_unit == "Kelvin":
            result = temperature + 273.15  # Celcius ke Kelvin
    elif from_unit == "Fahrenheit":
        if to_unit == "Celcius":
            result = (temperature - 32) * 5/9  # Fahrenheit ke Celcius
        elif to_unit == "Reamur":
            result = (temperature - 32) * 4/9  # Fahrenheit ke Reamur
        elif to_unit == "Kelvin":
            result = (temperature - 32) * 5/9 + 273.15  # Fahrenheit ke Kelvin
    elif from_unit == "Reamur":
        if to_unit == "Celcius":
            result = temperature * 5/4  # Reamur ke Celcius
        elif to_unit == "Fahrenheit":
            result = (temperature * 9/4) + 32  # Reamur ke Fahrenheit
        elif to_unit == "Kelvin":
            result = (temperature * 5/4) + 273.15  # Reamur ke Kelvin
    elif from_unit == "Kelvin":
        if to_unit == "Celcius":
            result = temperature - 273.15  # Kelvin ke Celcius
        elif to_unit == "Fahrenheit":
            result = (temperature - 273.15) * 9/5 + 32  # Kelvin ke Fahrenheit
        elif to_unit == "Reamur":
            result = (temperature - 273.15) * 4/5  # Kelvin ke Reamur

    result_label.config(text=f"Hasil: {result} {to_unit}")

root = tk.Tk()
root.title("Konversi Suhu")


# Label
label = tk.Label(root, text="Masukkan suhu:")
label.pack()

# Entry
entry = tk.Entry(root)
entry.pack()

# From Unit OptionMenu
from_var = tk.StringVar(root)
from_var.set("Celcius")  # Set default value

from_label = tk.Label(root, text="Dari:")
from_label.pack()

from_optionmenu = tk.OptionMenu(root, from_var, "Celcius", "Fahrenheit", "Reamur", "Kelvin")
from_optionmenu.pack()

# To Unit OptionMenu
to_var = tk.StringVar(root)
to_var.set("Fahrenheit")  # Set default value

to_label = tk.Label(root, text="Ke:")
to_label.pack()

to_optionmenu = tk.OptionMenu(root, to_var, "Celcius", "Fahrenheit", "Reamur", "Kelvin")
to_optionmenu.pack()

# Button
convert_button = tk.Button(root, text="Konversi", command=convert_temperature)
convert_button.pack()

# Result Label
result_label = tk.Label(root)
result_label.pack()

root.geometry("300x200")  # Mengatur lebar dan tinggi jendela
root.mainloop()
