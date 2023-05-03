"""
Calcular la resistencia total dado el ingreso por consola
"""

#Lleer valores de entrada por consola
r1 = float(input("Resistencia 1: "))
r2 = float(input("Resistencia 2: "))
r3 = float(input("Resistencai 3: "))

#Se calcula la resistencia total
rt = 1/((1/r1) + (1/r2) + (1/r3))

#Imprimir la resistencia total en consola
print("La resistencia total es de", rt)

"""
Validar el ingreso de la resistencia,que sea mayor que 0, controlar error y utilizar funciones
"""
#Funcion para validar el ingreso de la resistencia en float
def validate_input_float(texto):
#Ingreso de valores
    while True:
        try:
            r = float(input(texto)) #float(), str(), int(), casteo o transformacion, conversion del tipo de dato
            if r > 0:
                abs(r)
                return r
            else:
                print("El valor es menor a 0")
        except Exception as error:
            print("El valor es menor a 0")
except Exception as error:
    print("Ha ocurrido un erro en el ingreso de la resistencia" ,error)
    print("Ha ocurridoun error, ingrese de nuevo el valor de la resistencia")


#INCOMPLETO