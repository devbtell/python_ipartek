# Funciones en Python::


# 01 - - - - -
# Funciones de entrada y salida:


# 01.1 'print':

print()
print("Hello World !")

pal0 = "Hello World !"
print(pal0)

print()
pal1 = "Hello"
pal2 = "World"
print(pal1, pal2)
print(pal1, pal2, sep="_") #default: sep=" "
print(pal1, pal2, end=" ") #default: end="\n"
print("!")

print()
nombre = "Nicolás"
apellido = "Maduro"
edad = 64

# 'print' sin formateo de texto
print("Hola, te llamas " + nombre + " " + apellido + " y tienes " + str(edad) + " años.")
# 'print' con formateo de texto
print(f"Hola, te llamas {nombre} {apellido} y tienes {edad} años.")


# 01.2 'input':

print()
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: ")) # importante convertir de cadena a numerico, si despues harás operaciones...
print(f"Hola {nombre}, el próximo año tendras: {edad + 1}")