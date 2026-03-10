# ejercicio 1_2.a.1

import random

num = 0
aleatorio = random.randint(1, 100)
# print(f"El numero aleatorio es {aleatorio}")

while num != aleatorio:
    num = int(input("Adivina un numero entre 1 y 100: "))
    if not 1 <= num <= 100:
        print("El valor esta fuera del rango")
    elif num < aleatorio:
        print("El varlor es demasiado bajo")
    elif num > aleatorio:
        print("El valor es demasido alto")
    else:
        print("¡Has adivinado el numero!")