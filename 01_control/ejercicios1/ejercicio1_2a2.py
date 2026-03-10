# ejercicio 1_2.a.2

import random

tec = ""
bye = "salir"

aleatorio = random.randint(1, 100)
# print(f"El numero aleatorio es {aleatorio}")

# .isdigit() para verificar si una cadena solo contiene solo numeros

while tec != aleatorio:
    tec = input("Adivina un numero entre 1 y 100: ")
    if tec == bye.lower().strip():
        break

    tec = int(tec)
    if not 1 <= tec <= 100:
        print("El valor esta fuera del rango")
    elif tec < aleatorio:
        print("El varlor es demasiado bajo")
    elif tec > aleatorio:
        print("El valor es demasido alto")
    else:
        print("¡Has adivinado el numero!")

print("Programa finalizado...")