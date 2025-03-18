print("Escoge una de las siguiente operaciones:")
print("Operación 1: Comprobar si el número es par o impar")
print("Operación 2: comprobar si el número es primo o no")
m= int(input())
if m==1:
    n = int(input("Ingresa un número: "))
    if n%2==0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")
elif m==2:
    n = int(input("Ingresa un número: "))
    div = 3
    x=n
    while div > 2:
        div = 0 
        for i in range(1,x+1):
            if x % i == 0:
                div= div +1
        if div>2:
            print("El numero ingresado no es primo")
        else:
            print("El número ingresado es primo")
else:
    print("La operación indicada no es valida")

