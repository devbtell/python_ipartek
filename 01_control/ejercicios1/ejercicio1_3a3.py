# ejercicio 1_3.a.3

lista_notas = [4, 8, 3, 10, 5, 7, 2, 9]
c_aprobado = 0
c_excelente = 0

for nota in lista_notas:
    if nota < 5:
        print(f"{nota} --> Suspenso")
    elif nota < 9:
        print(f"{nota} --> Aprobado")
        c_aprobado += 1
    else:
        print(f"{nota} --> Excelente")
        c_excelente += 1

c_suspensos = len(lista_notas) - (c_aprobado + c_excelente)

print(f"N. de notas aprobadas: {c_aprobado}")
print(f"N. de notas excelentes: {c_excelente}")
print(f"N. de notas suspensos: {c_suspensos}")