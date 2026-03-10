# Bucles en Python::


# 01 - - - - -
# Bucles indeterminados

clave = "key"
acertado = False
# (1 - n) ...
while not acertado:
    respuesta = input("Ingresa la clave: ")
    acertado = respuesta == clave

clave = "key"
respuesta = input("Ingresa la clave: ")
# (0 - n) la condición se evalua antes de ejecutar el codigo
while respuesta != clave:
    print("Clave incorrecta")
    respuesta = input("Vuelve a ingresar la clave: ")

# bucles infinitos (peligro!):

a = 0
b = 0
# al menos 1 de las variables de la condición del bucle,
# tiene que ser modificada dentro del mismo para que tenga un fin
while a >= 0:
    b += 1
    print(b)

# break:
while True:
    respuesta = input("Digite 'n' para terminar: ")
    if respuesta == "n":
        break # con 'break' podemos romper el bucle y salir;

# en la mayoria de las ocasiones,
# es preferible no usar 'break', por ejemplo:
while respuesta != "n":
    respuesta = input("Digite 'n' para terminar: ")
    if respuesta != "n":
        print("Iteración")

# continue:
while a < 10:
    a += 1
    if a % 2 == 0:
        continue # salta el resto del codigo hasta la siguiente iteración
    print(a)

# bucle con clausula 'else':

sumatorio = 0
contador = 0

while contador < 5:
    valor = int(input("Ingrese un numero: "))
    if valor > 0:
        sumatorio += valor
        contador += 1
        print(f"El valor {valor} ha sido sumado")
    else:
        print("El numero no es valido")
        break
else:
    # solo se ejecuta cuando el bucle termina por su condicion (contador)
    # y si no es interrompido por el 'break'
    print(f"El sumatorio es {sumatorio}")


# 02 - - - - -
# Bucles determinados:

# con 'range' establecemos una secuencia de valores,
# que determinan el número de iteraciones del bucle

for i in range(5):
    print(i) # 0,1,2,3,4

for i in range(5,10):
    print(i) # 5,6,7,8,9

for i in range(0,10,2):
    print(i) # 0,2,4,6,8

# el 'for' es una buena herramienta para recorrer valores

# cadena --> colección de caracteres
cadena = "planeta"
for caracter in cadena:
    print(caracter)

# lista --> colección de valores
numeros = [0,5,10,15,20]
for num in numeros:
    print(num)