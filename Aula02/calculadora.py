salario = int(input("Digite o seu salario:"))

imposto = 27.
while imposto > 0:
	imposto = input("imposto em % (ex: 27.5)?")
	if not imposto:
		imposto = 27.5
	elif imposto == "s":
		break
	else:
		imposto =  float(imposto)
	print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))
