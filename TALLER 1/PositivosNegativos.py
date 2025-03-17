n = int(input("ingrese un número: "))#Se ingresa solo el primer numero de prueba
#Se crea la condición.
if n == 0:
    print("El número es cero.")
elif n>0:
    print("El número es positivo.")
else:
    print("El numero es negativo.")
#Se asignan varaibles vacias que van a almacenar la cantidad de positivos, de negativos y sus promedios
i = 1
neg = 0
pos = 0
num_pos = 0
num_neg = 0
print(" ") 
print("Ingrese la cantidad de numeros positivos o negativos que desee, si no desea ingresar más por favor ingrese 0.") #Opción.
while i!=0: #Mientras i sea distinto a 0 se seguira reptiendo el bucle.
    m = int(input()) #Número.
    i = m #Se reemplaza el valor de i al número ingresado.
    if m<0: #Condición que determina si es negativo.
        neg= neg + 1 #Contador.
        num_neg = num_neg + m #Suma de negativos para sacar promedio de ellos.
    elif m>0:
        pos= pos + 1 #Contador.
        num_pos= num_pos + m #Suma de positivos para sacar promedio de ellos.
    else:#cuando se ingrese el 0, se acaba el conteo y nos da el promedio de positivos y de negativos.
        print(" ")
        print("La cantidad de numeros positivos fue de: "); print(pos)
        print("y su promedio de:");print(num_pos/pos)
        print(" ")
        print("La cantidad de numeros negativos fue de: ");print(neg)
        print("y su promedio de: ");print(num_neg/neg)
        