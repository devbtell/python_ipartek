# ejercicio 1_4.a.2

fin = False

while not fin:
    try:
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        oprd = input("Ingrese operador s/r/m/d : ").lower().strip()
        if oprd not in ["s", "r", "m", "d"]:
            raise Exception("Opción no valida")
        if oprd == "d" and num2 == 0:
            raise Exception("No se puede dividir por 0")
    except ValueError:
        print("Valor no numerico")
    except Exception as e:
        print(e)
    else:
        match oprd:
            case "s":
                print(num1 + num2)
            case "r":
                print(num1 - num2)
            case "m":
                print(num1 * num2)
            case "d":
                print(num1 / num2)
        fin = True