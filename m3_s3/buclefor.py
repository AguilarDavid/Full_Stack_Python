""" Tienes la siguiente lista de números: [45, 23, 67, 89, 12, 56, 78, 90] 
Encontrar el número más grande en la lista utilizando un bucle for."""

lista = [45, 23, 67, 136, 12, 56, 78, 90]
numero = 0
for elemento in lista:
    if elemento > numero:
        numero = elemento
print(numero)