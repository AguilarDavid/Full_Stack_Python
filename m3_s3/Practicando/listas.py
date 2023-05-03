# Listas []

lista = ["Lunes", "Maretes", "Miercoles", "Jueves", "Viernes"]
print(lista[3]) # Imprime el jueves porque le estamos indicando la posición o indice 3, recuerda que comienza desde el cero
print(lista[7]) # Si seleccionamos un indice fuera de la lista dará IndexError o Excepción
print(lista[0:4]) # imprimiremos las posiciones del 0 al 4 = ['Lunes', 'Martes', 'Miercoles', 'Jueves'] tips: recuerda que se imprime hasta una posición antes
print(lista[-1]) # imprime el ultimo indice de la lista
print(lista[1:4]) # imprime desde la opción seleccionada hasta la otra opción selecionada Ej: ['Martes', 'Miercoles', 'Jueves']
print(lista[1:]) # imprime desde la posición seleccionada hasta el final de la lista


lista = ["Lunes", "Maretes", "Miercoles", "Jueves", "Viernes", 40, 5.17, True[1, 2, 3]]

print(len(lista)) # imprime cuantos elementos hay en la lista ej: 9, tips: valores dentro de la segumnda lista cuentan como 1

lista = [1,2,3,4,5]

lista.appened(6) # agreag el valor 6 al final de la lista [1, 2, 3, 4, 5, 6]
lista. appened("David") # agreag el valor 6 al final de la lista [1, 2, 3, 4, 5, 6, David]

lista = [1,2,4,5]
lista.insert (2,3) # inserta en la posición 2 de la lista el valor 3 ej: [1,2,3,4,5]  

lista = [1,2,3,4,5]
lista.extend([6,7,8]) # extiende la lista con los nuevos valores proporcionados ej: [1, 2, 3, 4, 5, 6, 7, 8]

lista1 = [1,2,3,4,5]
lista2 = [6,7,8]
lista3 = lista1 + lista2 
print(lista3) # imprime la suma de las dos listas ej: [1, 2, 3, 4, 5, 6, 7, 8]

lista = [1, 2, 3, 4, 5,"David"]
print(3 in lista) # preguntamos si 3 está en la lista y nos indica verdadero ej: True
print(10 in lista) # preguntamos si 10 está en la lista y nos indica falso ej: False
print(lista.index(5)) # pedimos que nos indique en que indice se encuentra el valor 5 y nos indica que está en el indice 4 ej: 4
print(lista.index(10)) # pedimos el indice del valor 10 nos dice que el diez no está en la lista ej: ValueError: 10 is not in list

lista = [1, 2, 3, 4, 5, "David", 1, 2, 3, 1, "David", 1]
print(lista.count(1)) # imprime cuantas veces está el valor 1 en la lista ej: 4
print(lista.count("David")) # imprime cuantas veces está el valor David en la lista ej: 2
print(lista.count(10)) # imprime cuantas veces está el valor 10 en la lista ej: 0

lista = [1, 2, 3, 4, 5,"David"]
lista.pop(2)
print(lista) # pedimos que borre el 2 indice de la lista ej: [1, 2, 4, 5,"David"]

lista.pop() # borra el ultimo indice que encuentre en la lista ej: [1, 2, 3, 4, 5]
lista.remove(5) # borra el valor indicado en la lista ej: [1, 2, 3, 4, "David"]
lista.clear() # borra tods los indices de la lista ej: []
lista.reverse() # voltea todos los valores de la lista ej:["David", 5, 4, 3, 2, 1]
lista = [1, 2, 3, 4, 5,"David"]*2 # se multiplica la lista ej: [1, 2, 3, 4, 5,"David", 1, 2, 3, 4, 5,"David"]

lista = [5,4,-7,9,0,1,3]
lista.sort() # ordena la lista ascendentemente [-7, 0, 1, 3, 4, 5, 9]
lista.sort(reverse=True) # ordena la lista descendentemente [9, 5, 4, 3, 1, 0, -7]