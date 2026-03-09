# ejercicio 1_1.a.2

precio = 0

horario = input("¿Horario diurno o nocturno? d/n : ").lower().strip()
if horario == "d":
    precio += 20
elif horario == "n":
    precio += 25
else:
    print("No te entiendo ...")
    exit()

zona = input("¿Zona común o reservada? c/r : ").lower().strip()
if zona == "c":
    precio += 1
elif zona == "r":
    precio += 3
else:
    print("No te entiendo ...")
    exit()

equipaje = input("¿Llevarás equipaje? s/n :").lower().strip()
if equipaje == "s":
    precio += 5
elif equipaje == "n":
    precio += 0
else:
    print("No te entiendo ...")
    exit()

print(f"El precio final del billete es: {precio}$")
