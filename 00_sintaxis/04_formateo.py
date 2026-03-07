# Formateo en Python::


pi = 3.1415927
precio = 12525620
porcentaje = 0.75
codigo = 34

print()
print(f'pi = {pi:.2f}')                         # 3.14
print(f'precio = {precio:,}')                   # 12,525,620
print(f'porcentaje = {porcentaje:.1%}')         # 75.0%
print(f'codigo = {codigo:05d}')                 # 00034

entero = 5
print()
print(f'|{entero:<10d}|')                       # |5         |
print(f'|{entero:>10d}|')                       # |         5|
print(f'|{entero:>010d}|')                      # |0000000005|
print(f'|{entero:<010d}|')                      # |5000000000|

decimal = 10.219
print()
print(f'{decimal:.2f}')                         # 10.22
print(f'{decimal:.1f}')                         # 10.2
print(f'|{decimal:^10.2f}|')                    # |10.22     |
print(f'|{decimal:<10.2f}|')                    # |10.22     |
print(f'|{decimal:>10.2f}|')                    # |     10.22|
print(f'|{decimal:<010.2f}|')                   # |10.2200000|
print(f'|{decimal:>010.2f}|')                   # |0000010.22|

titulo = "TITULAR"
print()
print(f'|{titulo:<30}|')                        # |TITULAR                       | sangrado a la izquierda
print(f'|{titulo:^30}|')                        # |           TITULAR            | centrado
print(f'|{titulo:>30}|')                        # |                       TITULAR| sangrado a la derecha

valor = 3.1415927
print()
print(f'|{valor:<30.2f}|')                      # |3.14                          | sangrado a la izquierda
print(f'|{valor:^30.2f}|')                      # |              3.14            | centrado
print(f'|{valor:>30.2f}|')                      # |                          3.14| sangrado a la derecha