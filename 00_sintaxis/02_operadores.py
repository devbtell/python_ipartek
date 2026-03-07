# Operadores en Python::


# 01 - - - - -
# operadores aritméticos:

num1 = 7
num2 = 3

suma = num1 + num2          # suma
resta = num1 - num2         # resta
multip = num1 * num2        # multiplicación
division = num1 / num2      # división decimal
division_e = num1 // num2   # división entera
resto = num1 % num2         # restante
exponente = num1 ** num2    # potenciación


# 02 - - - - -
# Operadores de asignación

asig = 10
asig = asig + 1

# operación de asignación de suma
asig += 1 # incrementa el valor de 'asig' a 1; es igual que 'asig = asig + 1'
# operación de asignación de resta
asig -= 1 # disminuye el valor de 'asig' a 1; es igual que asig = asig - 1'
# operación de asignación de multiplicación
asig *= 2 # multiplica el valor de 'asig' a 2; es igual que 'asig = asig * 2'
# operación de asignación de división decimal
asig /= 2 # divide el valor de 'asig' en 2; es igual que 'asig = asig / 2'
# operación de asignación de división entera
asig //= 2 # divide el valor de 'asig' en 2; es igual que 'asig = asig // 2'


# 03 - - - - -
# Operadores de comparación

com1 = 15
com2 = 10
com3 = 15

# comparación de igualdad
print(com1 == com2) # False
print(com1 == com3) # True

# comparación de desigualdad
print(com1 != com2) # True
print(com1 != com3) # False

# comparación de mayor, menor, mayor igual, menor igual
print(com1 > com2)  # True
print(com1 >= com2) # True
print(com1 < com2)  # False
print(com1 <= com2) # False


# 04 - - - - -
# Comparación de cadenas de texto
nom1 = "Jos"
nom2 = "JOS"
print(nom1 == nom2) # False
print(nom1 != nom2) # True

# 05 - - - - -
# Comparación lexicográfica
# 'A' es menor que la 'Z'
nom3 = "Anne"
nom4 = "Zara"
print(nom3 > nom4) # False
print(nom3 < nom4) # True

# 06 - - - - -
# Operadores lógicos
temperatura = 25
sensacion = 30
print(temperatura > 0)  # True
print(sensacion < 30)   # False

# operador lógico de conjunción ( and )
# retorna 'True' cuando todas las condiciones son verdaderas:
print(temperatura and sensacion == 25) #False
# 'print(temperatura > 0 and temperatura < 30)'...
# Para rangos numericos es preferible usar la sigiente sintaxis:
print(0 < temperatura < 30)     #True
print(0 <= temperatura <= 30)   #True

# operador lógico de disyunción ( or )
# retorna 'True' si alguna condición es verdadera (True):
# retorna 'False' si todas las condiciones son falsas (False):
hace_sol = True
marea_baja = False
print(hace_sol or marea_baja) # True

# operador lógico de negación ( not )
a = 10
b = 10
print(a == b)       #True
print(not a == b)   #False; --> 'print(a != b) '

print()

# operador condicional ternario (expresion condicional)
edad = int(input("Ingresa tu edad: "))
adulto = "Eres mayor de edad..." if edad > 18 else "Eres menor de edad..."
print(adulto)