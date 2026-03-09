# Condicionales en Python::


# 01 - - - - -
# Condicional de 1 rama:

nombre = input("Digite su nombre: ")
if nombre == "Anna":
    print(f"Hola {nombre}, encantado de conocerte.")


# 02 - - - - -
# Condicional de 2 ramas:

nombre = input("Digite su nombre: ")
if nombre == "Anna":
    print(f"Hola {nombre}, encantado de conocerte.")
else:
    print(f"Adiós {nombre}...")


# 03 - - - - -
# Anidamiento de condiciones:

tiene_licencia = True
es_novato = False

if tiene_licencia:
    if es_novato:
        print("Tienes que llevar la L")
    else:
        print("Puedes conducir sin la L")
else:
    print("No puedes conducir")

if tiene_licencia and es_novato:
    print("Tienes que llevar la L")
else:
    if tiene_licencia and not es_novato:
        print("Puedes conducir sin la L")
    else:
        print("No puedes conducir")


# 04 - - - - -
# Condicionales excluyentes

temperatura = 50
if temperatura <= 0:
    print("Hielo")
elif temperatura <= 100:
    print("Agua")
else:
    print("Vapor")


# 05 - - - - -
# Condicionales de multiple rama

opcion = 1
match opcion:
    case 1:
        print("Sumar")  # si 'opcion' es igual a 1
    case 2:
        print("Restar") # si 'opcion' es igual a 2
    case _:
        print("¿?")     # si 'opcion' no coincide con ningún 'case'