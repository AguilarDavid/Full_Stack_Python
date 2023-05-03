""" Tienes la siguiente lista de números:
[45, 23, 67, 89, 12, 56, 78, 90]
Encontrar el número más grande en la lista utilizando un bucle for. """

lista = [45, 23, 67, 89, 12, 56, 78, 90]
mayor = lista[0]
menor = lista[0]
repetido = []
for elemento in lista: #para el elemento en la lista
    if elemento > mayor: #si el elemento es mayor encontrado en la lista
        mayor = elemento
    if elemento < menor:
        menor = elemento
    if lista.count(elemento) > 1 and elemento not in repetido: #si la cuenta de la lista es mayor a 1 y el elemento no esta en "repetido"
            
            
print(f"El mayor {mayor}")
print(f"El menor {menor}")
print(f"El repetido {repetido}")