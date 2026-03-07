# ejercicio 1.a.1

prod1 = float(input("ingrese el importe del primer producto: "))
prod2 = float(input("ingrese el importe del segundo producto: "))
prod3 = float(input("ingrese el importe del tercer producto: "))

t_bruto = prod1 + prod2 + prod3
print(f"importe bruto: {t_bruto}")

t_neto = t_bruto + (t_bruto * (21/100))
# t_neto = t_bruto + (t_bruto * 0.21)

# redondeo del importe total neto:
# hay dos formas de poder hacerlo:

# (1) directamente a la variable con la función 'round':
# t_neto = round(t_neto, 2)

# (2) desde 'print' con formateo de texto:
# print(f"importe neto: {t_neto:.2f}")

# print("importe neto: " + str(t_neto)) # sin formeteo de texto es necesario convertir el tipo de dato
print(f"importe neto: {t_neto} euros")  # con formateo de texto no es necesario convertir el tipo de dato