# Bucle while: Bucle con indeterminada cantidad de veces 

import math
numero = int(input("Digite un numero: "))

while numero<0:       #mientras el numero sea menor a cero, le pediremos otra vez el número
    print("Error -> Debería ser un número positivo") #Si el numero es negativo le pedirá nuevamente un digito"
    numero = int(input("Digite un número: "))
    
print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}") #Si el número es positivo entonces cumple la condición y continua enviando la raiz cuadrada
