# Comenzando con el lenguaje de Python

"""
Bloque de comentario
Se puede escribir comentarios en linea y en bloque con 3 simples comillasdobles o simples al comienzo y final
"""

'''
Comillas sencillas para un bloque de comentario
Inicio con estructura basica de Python
'''
# metodo para impresion de consolas
print("Full Stack Python")
print(2)
print(2+1)

# Declaración de variables
# Las variables el nombre es su identificador
cadena = "Cadena de caracteres o un String"

#Indentacion en Python, se realiza con tabulaciones o 1, 2, ...,
if True:
    print("probando condicional")
    print("otra impresion")
    if True:
        print("indentacion en python")

#separación de bloques de codigo con 2 lineas hacia abajo
print("separacion de bloques de codigo con 2 lineas hacia abajo")

#tipos de datos
print(type(5)) #int <clas 'int'>
print(type(cadena)) #str <class 'str'>
print(type(True)) #bool <class 'bool'>
print(type(False)) #bool <class 'bool'>
print (type([])) #list <class 'list'>
print(type(2 + 1j)) #complex <class 'complex'>
print(type("2")) #str <class 'str'>
print(type(None)) #None <class 'NoneType'>
print(type(1.5)) #float <class 'float'>
