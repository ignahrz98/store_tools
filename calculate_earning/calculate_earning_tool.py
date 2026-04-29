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