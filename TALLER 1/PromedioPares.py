#CANTIDAD DE NUMEROS QUE QUIERE INGRESAR
n = int(input("¿Cuántos números desea ingresar? ")) 
i = 0
suma = 0
pares = 0

for i in range(1, n + 1):
    elementos = int(input("Ingrese números:"))#Ingresa la cantidad de numeros establecida
    if elementos % 2 == 0: #Comprueba si es par
        suma = suma + elementos
        pares = pares + 1
print("El promedio de los numeros pares es: ",(suma/pares))#Se saca el promedio de solo los pares.