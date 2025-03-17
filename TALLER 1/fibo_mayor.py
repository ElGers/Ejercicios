n = int(input("Ingrese un número:"))# se ingresa un número.
a = 0
b = 1
i = ("inicio")#se crea una variable para iniciar el bucle.
while i == ("inicio"):
    suma = a + b
    if n-suma<=0: # el numero de la serie mayor a n, será el que al restarselo a n va a dar un numero negativo 
        i = ("fin")# se finaliza el bucle.
    else:
        a = b
        b = suma
print("El siguiente número de la serie de fibonacci de " + str(n)+" es: " + str(suma))
        