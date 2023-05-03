# Tuplas () 

tupla = (4,"Hola",6.78,[1,2,3],4)
tupla.append(5)
print(tupla) # pedimos agregar el valor 5 pero te responderá que en dupla no puedes agregar

tupla[0] = 8 # pedimos cambiar el indice 0 por el valor 8 pero nos dirá que no podemos modificar
tupla.pop() # pedimos borrar el elemento del final de la lista pero nos dirá que en dupla no se puede borrar

# En dupla no se puede agregar, modificar ni quitar indices, solo se puede buscar

print(tupla[1]) # mostrará el indice 1 de la tupla
print(tupla[-1]) # mostrará el ultimo indice de la lista
print(4 in tupla) # preguntamos si está el valor 4 en la lista y responde verdadero ej: True
print(tupla.index("Hola")) # pedimos el indice del valor "Hola" y responde ej: 1
print(tupla.index(4)) # pedimos el indice del valor 4 y responde ej: 0 ya que es el primero que encuentra
print(tupla.count(4)) # pedimos que cuente cuanta veces está el valor 4 en la tupla y responde ej: 2
print(len(tupla)) # preguntamos cuantos elementos tiene la dupla, responde ej: 5

lista = list(tupla) 
print(lista) # se convierte la tupla en lista en otra variable lista pero la tupla no se modifica 
# quedaaria así [4,"Hola",6.78,[1,2,3],4]

lista = [4,"Hola",6.78,[1,2,3],4] # si tenemos una lista 
tupla = tuple(lista) # y la queremos convertir a tupla
print(tupla) # imprimimos la tupla y quedaría así ej: (4,"Hola",6.78,[1,2,3],4)