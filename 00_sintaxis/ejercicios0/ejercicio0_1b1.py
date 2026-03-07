# ejercicio 1.b.1

import math

radio = float(input("digite el radio del circulo: "))

area = (radio ** 2) * math.pi
print(f"{'el area del circulo es':<30} : {area:>10.2f}")

perimetro = 2 * math.pi * radio
print(f"{'el perimetro del circulo es':<30} : {perimetro:>10.2f}")