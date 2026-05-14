import json

"""
def set_tool(dolar_value):
	print("\n* Cambiar valor del dólar *")
	print(f"\n| Valor actual | $1.00 | {dolar_value:.2f} |")

	while True:
		try:
			new_dolar_value = float(input("\nIngrese nuevo valor para dólar: "))
			break
		except:
			input("\nIngrese un valor númerico.")

	print(f"\nEl valor del dólar será actualizado de {dolar_value:.2f} al nuevo valor {new_dolar_value:.2f}")
	input("\nPresione para continuar.")

	# Save dolar_value to the file.
	data = {
		"dolar_value": new_dolar_value
	}

	with open("data/dolar_value.json", "w") as file_dolar_value:
		json.dump(data, file_dolar_value, indent=4)
		print("\nEl nuevo valor del dólar fue actualizado en el archivo.")

	return new_dolar_value
"""

import tkinter as tk

entry_dolar = None
label_message  = None

def tool_action(text_variable_dolar_value):
	try:
		dolar_value_update = float(entry_dolar.get())
		print(f"New dolar value: {dolar_value_update}")

		data = {
			"dolar_value": dolar_value_update
		}

		with open("data/dolar_value.json", "w") as file_dolar_value:
			json.dump(data, file_dolar_value, indent=4)
			print("Dolar value updated")
			label_message.config(text="Dollar has been updated", fg="#135821")

			text_variable_dolar_value.set(f"Dollar ($1): {dolar_value_update}")
	except ValueError:
		print("Value for dolar is not valid")
		label_message.config(text="Dollar value is not valid", fg="#4B0404")

def toplevel_dolar_value(window_parent, text_variable_dolar_value):
	tl_window = tk.Toplevel(window_parent)
	tl_window.title("Tool")
	tl_window.geometry("400x300")
	tl_window.resizable(False, False)
	tl_window.grab_set()

	# Load dolar value from file
	try:
		with open("data/dolar_value.json", "r") as file_dolar_value:
			data = json.load(file_dolar_value)
			dolar_value_current = data["dolar_value"]

			print("Dolar value loaded from file")
	except:
		print("Data for dolar value can't be loaded")
		dolar_value_current = 0.0

	print(f"Dollar value: {dolar_value_current}")
	#text_variable_dolar_value.set("working")

	label_title = tk.Label(tl_window, text="Dollar value", font=("TkDefaultFont",10, "bold"))
	label_title.pack(pady=(0,10))

	label_dolar = tk.Label(tl_window, text="Introduce dollar value ($1)")
	label_dolar.pack()

	global entry_dolar
	entry_dolar = tk.Entry(tl_window, width=8)
	entry_dolar.insert(0, dolar_value_current)
	entry_dolar.pack()

	btn_ok =tk.Button(tl_window, text="Ok")
	btn_ok.pack(pady=10)
	btn_ok.config(command=lambda: tool_action(text_variable_dolar_value))

	global label_message
	label_message = tk.Label(tl_window, text="", font=("TkDefaultFont",10, "bold"))
	label_message.pack()