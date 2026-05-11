import json
from menu_app import main_menu_app
from menu_app import currency_converter_menu
from currency_converter import currency_converter_tool
from calculate_earning import calculate_earning_tool
from digital_weight import digital_weight_tool
from dolar_value import dolar_value_tool

import tkinter as tk

window = tk.Tk()
window.title("Store tools")
window.geometry("400x300")
window.resizable(False, False)

top_menu = tk.Menu(window)
window.config(menu=top_menu)

tools_menu = tk.Menu(top_menu, tearoff=0)
top_menu.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Calculate earning")
tools_menu.add_command(label="Currency converter")
tools_menu.add_command(label="Digital weight")

config_menu = tk.Menu(top_menu, tearoff=0)
top_menu.add_cascade(label="Config", menu=config_menu)
config_menu.add_command(label="Update dolar value")

# Get the dolar_value from the file.
try:
	with open("data/dolar_value.json", "r") as file_dolar_value:
		data = json.load(file_dolar_value)
		dolar_value = data["dolar_value"]

		print("Valor del dólar cargado desde el archivo.")
except:
	data = {
		"dolar_value": 0.0
	}

	# Create file for dolar_value
	with open("data/dolar_value.json", "w") as file_dolar_value:
		json.dump(data, file_dolar_value, indent=4)
		print("El archivo para valor del dólar ha sido creado")

	dolar_value = data["dolar_value"]

label_dolar_value = tk.Label(text=f"Dolar ($1): {dolar_value}")
label_dolar_value.pack()

# Show the main menu.
while True:
	option = main_menu_app.get_menu(dolar_value)

	if option == 1:
		option_currency_converter_menu = currency_converter_menu.get_menu()

		if option_currency_converter_menu == 1:
			currency_converter_tool.set_tool(dolar_value,1)
		elif option_currency_converter_menu == 2:
			currency_converter_tool.set_tool(dolar_value,2)
	elif option == 2:
		calculate_earning_tool.set_tool(dolar_value)
	elif option == 3:
		digital_weight_tool.set_tool()
	elif option == 4:
		dolar_value = dolar_value_tool.set_tool(dolar_value)
	elif option == 5:
		break

window.mainloop()