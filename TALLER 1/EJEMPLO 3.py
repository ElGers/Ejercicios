n = int(input("Ingrese un número"))
m= str(n)
numero= len(m)
for i in m:
    if int(i)%2==0:
        print(f"El número {i} es par")
    else:
        print(f"El número {i} es impar")
print("La cantidad de cifras del numero ingresado es de:",numero)








 