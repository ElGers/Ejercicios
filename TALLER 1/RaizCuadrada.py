n = int(input("Por favor, ingrese un número:"))#Se ingresa un número.
if n**(1/2) - int(n**(1/2)) == 0: #Se saca raiz cuadrada de un número y a esta se le resta la raiz cuadrada entera.
    print("El número ingresado tiene por raiz entera: ", (n**(1/2)))# Si la resta da 0, es el cuadrado de un número.
else:
    print("El número ingresado no tiene raiz cuadrada entera.")# si no da 0 no es el cuadrado de otro..