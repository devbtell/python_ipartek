# ejercicio 1_1.a.3

altura = float(input("Digite su altura en m: "))
peso = float(input("Digite su peso en kg: "))
imc = round(peso / (altura ** 2), 1)

if imc < 18.5:
    estado = "Anorexia"
elif 18.5 <= imc <= 24.9:
    estado = "Peso normal"
elif 25 <= imc <= 29.9:
    estado = "Sobrepeso"
elif 30 <= imc <= 34.9:
    estado = "Obesidad I"
elif 35 <= imc <= 39.9:
    estado = "Obesidad II"
else:
    estado = "Obesidad III"

print(f"Su índice de masa corporal es {imc}.")
print(f"Su estado de salud es {estado}.")