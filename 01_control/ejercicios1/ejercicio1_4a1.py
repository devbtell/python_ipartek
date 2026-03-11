# ejercicio 1_4.a.1

fin = False

while not fin:
    try:
        num = int(input("Introduce un numero: "))
        if not 1 <= num <= 10:
            raise Exception("Numero fuera de rango")
    except ValueError:
        print("Valor no numerico")
    except Exception as e:
        print(e)
    else:
        for i in range(1, 11):
            print(f"{num} x {i} = {i * num}")
        fin = True