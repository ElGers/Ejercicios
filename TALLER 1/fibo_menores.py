n = int(input("Ingrese un número:")) #Ingresa el número.
print("los números de la serie de fibonacci menores que "+ str(n)+ " son:")
a = 0 #Variable
b = 1 #Variable
i = a #Variable
while i < n: #se inicia un bucle en donde se hacen las operaciones
    suma = a + b
    a = b
    b = suma
    if b < n: #se coloca la condición para garantizar que sean menores que n
        print(b)# se va imprimiendo cada numero menor.
    else:
        i = n #Garantiza el bucle.
