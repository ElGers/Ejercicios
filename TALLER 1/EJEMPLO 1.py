n= int(input("Ingresa un número :"))
m=""
if n<0:
    n=n*-1 
cadena= str(n)
numeros= len(cadena)
for i in range(numeros-1,-1,-1):
        m= m+ cadena[i]
if int(m)==n:
    print("el numero ingresado es capicúa")
else:
    print("El número ingresado no es capicúa")

        




n= int(input("Ingresa un número:"))
if n<0:
    n=n*-1 
cadena= str(n)
m=""
for i in cadena:
    m= i+m
if int(m)==n:
    print("el numero ingresado es capicúa")
else:
    print("El número ingresado no es capicúa")