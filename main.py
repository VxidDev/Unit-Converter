import customtkinter as ctk
from random import choice

window = ctk.CTk()
window.geometry("300x150")
window.resizable(width=False , height=False)
window.title('Unit Converter')

previous_input_len = 0

lenght_units = ["cm" , "m" , "km"]
lenght_value = {
            "cm": 0.01,
            "m": 1,
            "km": 1000
        }
weight_value = {
            "g": 0.001,
            "kg": 1,
            "t": 1000
        }
weight_units = ["kg" , "g" , "t"]

all_units = lenght_units + weight_units

starting_unit = ctk.StringVar()
convert_unit = ctk.StringVar()

starting_amount = ctk.StringVar()
converted_amount = ctk.StringVar()

starting_amount_label = ctk.CTkLabel(window , text="Amount" , font=("arial" , 20 , "bold"))
starting_amount_display = ctk.CTkEntry(window , textvariable=starting_amount , width=100 , height=50 , font=("arial" , 25 , "bold"))
starting_amount_display.place(x=85 , y=15)
starting_amount_label.place(x=5 , y=25)

converted_amount_display = ctk.CTkEntry(window , state="disabled" , textvariable=converted_amount, width=100 , height=50 , font=("arial" , 25 , "bold"))
converted_amount_display.place(x=190 , y=85)
converted_amount_label = ctk.CTkLabel(window , text="Converted Amount" , font=("Arial" , 20 , "bold"))
converted_amount_label.place(x=5 , y=95)

starting_unit_selector = ctk.CTkOptionMenu(window , font=("arial" , 20 , "bold"),width=75 , dynamic_resizing=False , variable=starting_unit , values=all_units)
starting_unit_selector.place(x=195 , y=15)

convert_unit_selector = ctk.CTkOptionMenu(window , font=("arial" , 20 , "bold"),width=75 , dynamic_resizing=False , variable=convert_unit)
convert_unit_selector.place(x=195 , y=45)

def convert():
    try:
        if convert_unit_selector.cget("values") == lenght_units:
            base_value = float(starting_amount.get()) * float(lenght_value[starting_unit.get()])
            converted_amount.set(base_value / lenght_value[convert_unit.get()])
        else:
            base_value = float(starting_amount.get()) * float(weight_value[starting_unit.get()])
            converted_amount.set(f"{base_value / weight_value[convert_unit.get()]} {convert_unit.get()}")
    except KeyError:
        pass
    except ValueError:
        pass

def update_unit_options():
     if starting_unit.get() in lenght_units:
        if convert_unit_selector.cget("values") == lenght_units:
            pass
        else:
            convert_unit_selector.configure(values=lenght_units)
            if convert_unit.get() != "":
                convert_unit.set(choice(lenght_units))
     else:
        if convert_unit_selector.cget("values") == weight_units:
            pass
        else:
            convert_unit_selector.configure(values=weight_units)
            if convert_unit.get() != "":
                convert_unit.set(choice(weight_units))

def update_conversion():
    global previous_input_len
    if len(starting_amount.get()) != previous_input_len:
        previous_input_len = len(starting_amount.get())
        convert()

def update():
    update_unit_options()
    update_conversion()

    window.after(150 , update) 

update()

window.mainloop()
