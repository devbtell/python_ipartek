# ejercicio 1_1.a.1

nombre = input("Hola, ¿cómo te llamas? : ")
print(f"Hola {nombre}, bienvenido!")
tiene_pareja = input("¿Tienes pareja? s/n : ").lower().strip()
if tiene_pareja == "s":
    nombre_pareja = input("¿Cómo se llama tu pareja? : ")
    print(f"Invitación para {nombre} y {nombre_pareja}.")
elif tiene_pareja == "n":
    print(f"Invitación para {nombre}.")
else:
    print("¿¡Sí o No?! ¡Adiós!")