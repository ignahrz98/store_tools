"""
def set_tool():
	print("\n* Peso digital *")

	while True:
		try:
			price_kg = float(input("\nIngrese el precio (Kg): "))
			break
		except:
			input("\nIngrese un valor numérico.")

	price_g = price_kg / 1000;

	while True:
		print("\n* Información del producto *")
		print(f"\n| Precio (Kg): {price_kg:.2f} | Precio (g): {price_g:.2f} |")

		while True:
			try:
				product_grames = int(input("\nIngrese peso en gramos (g): "))
				break
			except:
				input("\nIngrese peso en números.")

		final_price = product_grames * price_g

		print(f"\n| Peso (g): {product_grames}g | Precio: {final_price:.2f}")

		flag_not_exit = True

		while flag_not_exit:
			option_weight = input("\nPesar otra vez. (Y / n): ")

			if option_weight == "y":
				print("\nVolver a pesar.")
				break
			elif option_weight == "n":
				print("\nNo volver a pesar.")
				flag_not_exit = False	
			else:
				print("\nIngrese una respuesta válida.")

		if flag_not_exit == False:
			break
"""

import tkinter as tk

entry_price_kg = None
entry_weight = None
label_result = None

def tool_action():
	everything_is_ok = True
	try:
		price_kg = float(entry_price_kg.get())
		print(f"Price (Kg): {price_kg}")
	except ValueError:
		print("Price kg is not valid")
		everything_is_ok = False

	try:
		weight = int(entry_weight.get())
		print(f"Weight (g): {weight}")
	except ValueError:
		print("Weight is not valid")
		everything_is_ok = False

	if everything_is_ok:
		price_g = price_kg / 1000
		price_weight = weight * price_g
		print(f"Price weight: {price_weight}")

		label_result.config(text=f"The price is: {price_weight}")

def toplevel_digital_weight_tool(window_parent):
	tl_window = tk.Toplevel(window_parent)
	tl_window.title("Tool")
	tl_window.geometry("400x300")
	tl_window.resizable(False, False)
	tl_window.grab_set()

	label_title = tk.Label(tl_window, text="Digital weight", font=("TkDefaultFont",10, "bold"))
	label_title.pack(pady=(0,10))

	label_price_kg = tk.Label(tl_window, text="Price (Kg)")
	label_price_kg.pack()

	global entry_price_kg
	entry_price_kg = tk.Entry(tl_window, width=8)
	entry_price_kg.pack()

	label_weight = tk.Label(tl_window, text="Introduce weight (g)")
	label_weight.pack(pady=(10,0))

	global entry_weight
	entry_weight = tk.Entry(tl_window, width=8)
	entry_weight.pack()

	btn_ok = tk.Button(tl_window, text="Ok")
	btn_ok.pack(pady=10)
	btn_ok.config(command=tool_action)

	global label_result
	label_result = tk.Label(tl_window, text="", font=(12))
	label_result.pack()