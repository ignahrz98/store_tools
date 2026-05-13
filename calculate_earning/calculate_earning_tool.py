"""
def set_tool(dolar_value):
	print("\n* Calcular ganancia *")
	while True:
		try:
			start_amount = float(input("\nIngrese monto: "))
			break
		except:
			input("\nDebe ingresar un valor númerico.")

	while True:
		try:
			iva_percentage = float(input("\nIngrese porcentaje de IVA: "))
			break
		except:
			input("\nDebe ingresar un valor númerico.")

	while True:
		try:
			earning_percentage = float(input("\nIngrese porcentaje de ganancia: "))
			break
		except:
			input("\nDebe ingresar un valor númerico.")

	amount_more_iva = ((iva_percentage / 100) * start_amount) + start_amount
	#earning_amount = ((earning_percentage / 100) * amount_more_iva) + amount_more_iva
	earning_amount = amount_more_iva / (1 - (earning_percentage / 100))

	print("\n* Resultado de la suma de los porcentajes *")
	print(f"\n| Monto inicial: {start_amount:.2f} | Monto con IVA: {amount_more_iva:.2f} | Monto con ganancia: {earning_amount:.2f} |")
	print("\n* Resultado expresado en dolares *");
	print(f"\n| Monto inicial: ${start_amount / dolar_value :.2f} | Monto con IVA: ${amount_more_iva / dolar_value :.2f} | Monto con ganancia: ${earning_amount / dolar_value :.2f} |")
	input("\nPresione para continuar.")
"""

import tkinter as tk

entry_start_amount = None
entry_iva = None
entry_earning = None
label_result = None

def tool_action():
	everything_is_ok = True
	try:
		start_amount = float(entry_start_amount.get())
		print(f"Amount: {start_amount}")
	except ValueError:
		print("Amount is not valid")
		everything_is_ok = False

	try:
		iva = float(entry_iva.get())
		print(f"IVA: {iva}")
	except ValueError:
		print("IVA is not valid")
		everything_is_ok = False

	try:
		earning_percentage = float(entry_earning.get())
		print(f"Earning percentage: {earning_percentage}%")
	except ValueError:
		print("Earning percentage is not valid")
		everything_is_ok = False

	if everything_is_ok:
		amout_more_iva = ((iva / 100) * start_amount) + start_amount
		print(f"Amount (+IVA): {amout_more_iva}")
		price = amout_more_iva / (1 - (earning_percentage / 100))
		print(f"Price: {price}")

		label_result.config(text=f"Amount (+IVA): {amout_more_iva :.2f}\n\nPrice: {price :.2f}")
	else:
		label_result.config(text="")


def toplevel_calculate_earning_tool(window_parent):
	tl_window = tk.Toplevel(window_parent)
	tl_window.title("Tool")
	tl_window.geometry("400x300")
	tl_window.resizable(False, False)
	tl_window.grab_set()

	label_title = tk.Label(tl_window, text="Calculate earning", font=("TkDefaultFont",10, "bold"))
	label_title.pack(pady=(0,10))

	label_start_amount = tk.Label(tl_window, text="Introduce amount")
	label_start_amount.pack()

	global entry_start_amount
	entry_start_amount = tk.Entry(tl_window, width=8)
	entry_start_amount.pack()

	label_iva = tk.Label(tl_window, text="Introduce IVA (%)")
	label_iva.pack()

	global entry_iva
	entry_iva = tk.Entry(tl_window, width=8)
	entry_iva.pack()

	label_earning = tk.Label(tl_window, text="Introduce earning (%)")
	label_earning.pack()

	global entry_earning
	entry_earning = tk.Entry(tl_window, width=8)
	entry_earning.pack()

	btn_ok = tk.Button(tl_window, text="Ok")
	btn_ok.pack(pady=10)
	btn_ok.config(command=tool_action)

	global label_result
	label_result = tk.Label(tl_window, text="")
	label_result.pack()