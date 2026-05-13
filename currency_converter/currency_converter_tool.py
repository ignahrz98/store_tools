"""
def set_tool(dolar_value, option):
	while True:
		try:
			amount = float(input("\nIngrese monto a convertir: "))
			break
		except:
			input("\nEl monto debe estar expresado en números.")

	if option == 1:
		print(f"\nMonto: ${amount:.2f} | Conversión: {amount * dolar_value :.2f}")
	elif option == 2:
		print(f"\nMonto: {amount:.2f} | Conversión: ${amount / dolar_value :.2f}")

	input("\nPresione para continuar.")
"""

import tkinter as tk
from tkinter import ttk
import json

entry_amount = None
combobox_select_operation = None
label_result = None

def tool_action(dolar_value_current):
	everything_is_ok = True
	amount_dolar = 0
	amount_other_currency = 0
	amount = 1.0
	print(f"$1 = {dolar_value_current}")

	try:
		amount = float(entry_amount.get())
		print(f"Amount: {amount}")
	except ValueError:
		print("Amount is not valid")
		everything_is_ok = False

	operation_selected = combobox_select_operation.current()
	
	if operation_selected == 0:
		print("Convert from dolar selected")
		amount_dolar = amount
		amount_other_currency = amount_dolar * dolar_value_current
	elif operation_selected == 1:
		print("Convert to dolar selected")
		amount_other_currency = amount
		amount_dolar = amount_other_currency / dolar_value_current
	else:
		everything_is_ok = False

	if everything_is_ok:
		label_result.config(text=f"${amount_dolar} = {amount_other_currency}")
	else:
		label_result.config(text="")

def toplevel_currency_converter(window_parent):
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

	print(f"Dolar current: {dolar_value_current}")

	label_title = tk.Label(tl_window, text="Currency converter", font=("TkDefaultFont",10, "bold"))
	label_title.pack(pady=(0,10))

	label_select_operation = tk.Label(tl_window, text="Select operation")
	label_select_operation.pack()

	global combobox_select_operation
	combobox_select_operation = ttk.Combobox(tl_window, state="readonly")
	combobox_select_operation.pack()
	elements_combobox_select_operation = ["Convert from dollar", "Convert to dollar"]
	combobox_select_operation["values"] = elements_combobox_select_operation

	label_amount = tk.Label(tl_window, text="Introduce amount")
	label_amount.pack()

	global entry_amount
	entry_amount = tk.Entry(tl_window, width=8)
	entry_amount.pack()

	btn_ok = tk.Button(tl_window, text="Ok")
	btn_ok.pack(pady=10)
	btn_ok.config(command=lambda: tool_action(dolar_value_current))

	global label_result
	label_result = tk.Label(tl_window, text="", font=(10))
	label_result.pack()