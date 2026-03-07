# Variables en Python::

# This is a Commentary...
print()


# 00 - - - - -
# Convenciones de estilo:
# Python sugiere convenciones adicionales para mejorar la legibilidad del código...

# snake_case: Para nombres de variables, funciones y métodos; 'mi_variable', 'calcular_total()'.
# CamelCase: Para nombres de clases; 'MiClase', 'MiClaseEspecial'.
# mayus_snake_case: para el caso de constantes; 'CONSTANTE_DE_EJEMPLO'.


# 01 - - - - -
# Declaración de variables:
# nt: con 'type()' se puede ver el tipo de dato de una variable
# nt: 'print(f"")' cadena de texto con formato...

# Declaración de variables numericas:
edad = 20       # declaración de variable de un numero entero (type: int)
altura = 1.5    # declaración de variable de un numero decimal (type: float)
print(f"{edad} --> {type(edad)} | {altura} --> {type(altura)}")

# Declaración de variables logicas (booleanas):
operativo = True
funcional = False

# Declaración de variables de texto/cadena (string):
# nt: se puede usar comillas simples o dobles para encapsular texto...
nombre = 'Ford'         # con comillas simples
apellido = "Mustang"    # com comillas dobles

# Declaración de variables 'None' (null)
identificador = None


# 02 - - - - -
# Tipado dinámico y tipado fuerte de Python:

# 02.1 - - - -
# En Python las variables puden ser dinámicas:
print()
dinamico = 10
print(f"[{dinamico}] --> {type(dinamico)}")
dinamico = "Hi"
print(f"[{dinamico}] --> {type(dinamico)}")
print()

# 02.2 - - - -
# Python es fuertemente tipado: el tipo de dato de una variable no puede pretender ser otra...
# Conversión de tipos de datos:
a = 10
b = "20"
e = "1.50"
print(f"a({a}) --> {type(a)}")
print(f"b('{b}') --> {type(b)}")
print(f"e('{e}') --> {type(e)}")

# convertir cadena a entero
c = a + int(b)
print(f"a + b = c({c}) --> {type(c)}")

# convertir cadena a decimal
f = float(e) + a
print(f"e + a = f({f}) --> {type(f)}")

# convertir entero a cadena
d = b + str(a)
print(f"b + a = d('{d}') --> {type(d)})")

# conversión a booleanos
print()
print(bool(0))      # False
print(bool(1))      # True
print(bool(-1))     # True
print(bool(""))     # False
print(bool(" "))    # True


# 03 - - - - -
# Formas de asignar el valor a la variable:
print()

# asignación directa
var1 = 10
print(f"var1({var1})")
# asignación entre variables
var2 = var1
print(f"var2({var2})")
# asignación desde expresiones
var3 = var1 + var2
print(f"var3({var3})")
# asignación desde funciones
var4 = float(var3)
print(f"var4({var4})")