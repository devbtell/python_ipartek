# Control de errores en Python::


# tipos de errores:
# a. errores sintácticos
# b. errores semánticos


# 01 - - - - -

# uso de 'try' y 'except':

try: # indica el código que podría lanzar uno o más errores
    valor = int(input("Ingrese un valor: "))
    # en el momento en que pongas un dato que no sea un entero, lanzara un error;
    # y no avanzara a la siguiente línea, sino que directamente al 'except'
    print(valor)
except: # se ejecuta si se produce algún error dentro del 'try'
    print("error")
print("end")

try:
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un numero: "))
    print(a / b)
except ValueError:
    print("Valor no numerico")
except ZeroDivisionError:
    print("Division por 0, no permitida")
# Los errores provienen de 'Exception', por lo cual:
# es capaz de capturar cualquier tipo de error;
# por lo cual es importante usar 'Exception' como la última exepción de un .
except Exception as e:
    # para saber exactamente cuál error se lanzó:
    print(e)
    print(type(e))
print("end")

# uso de 'else' y 'finally':

try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Valor no numerico")
else:
    # 'else' se ejecuta si no hubo ningún error en el 'try'
    print(f"El año que viene tendrás {edad + 1} años")
finally:
    # 'finally' se ejecuta siempre, independientemente si dio error o no
    print("end")

# uso de 'raise':

try:
    edad = int(input("Ingrese su edad: "))
    if not 18 <= edad <= 100:
        raise Exception("Edad fuera de rango") # con 'raise' podemos lanzar un error
except ValueError:
    print("Valor no numerico")
except Exception as e:
    print(e) # 'Edad fuera de rango'
else:
    print(f"Tu edad es {edad}")