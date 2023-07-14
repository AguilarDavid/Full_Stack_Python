"""
Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones
1. Si el primer número de la sublista es cero, omitir la impresión de toda la sublista
2. Si existe un cero en cualquier otra posición, omitir solo la impresión del cero
3. Adicionalmente, crear un diccionario donce asignaremmos la primera sublista a la clave A, la segunda clave B, la tercera clave C y la cuarta clave D
Finalmente, imprimir en pantalla el diccionario resultante
"""

lista_de_listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

diccionario = dict() 
otro_diccionario = dict()
claves = ["A", "B", "C", "D"]

contador = 0 #conocer posición de la lista para las claves y agregar elementos al diccionario

for lista in lista_de_listas:
    #insertar nombre _dicionario[clave] = valor
    diccionario[claves[contador]] = lista #diccionario[lista[indice]] = elemento_que_se_recorre
    otro_diccionario[claves[lista_de_listas.index(lista)]] = lista
    contador += 1 
    if lista[0] == 0: 
        continue 
    for num in lista: 
        if num == 0: 
            continue 
        print(num)
    
print(diccionario)
print(otro_diccionario)