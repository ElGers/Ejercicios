n = int(input("ingrese un numero: ")) #Ingresa un numero cualquiera
print("escoja una de las siguientes bases:")
print("2, 4, 8 o 16:") #Escoge la base.
b = int (input()) #Escoge la base.
factor = 1 #Inicia la variable Factor.
m=0 #Inicia la variable para bases 2 4 8 
hexadecimal="" #Incia la variable para base 16
if b==2 or b==4 or b==8: #Condición para base 2, 4, 8
    while n>0: #Bucle mientras n sea mayor a 0
        r = n % b #residuo
        n = n // b #división entera que determina el While.
        m = m + factor * r #Numero en base
        factor = factor * 10 #valor posicional del numero
    print(m)  
elif b == 16: #Condición para base 16
        while n>0: #Bucle mientras n sea mayor a 0
            r = n % b #residuo
            if r<10: #se agregan las letras hexadecimales 
                hexadecimal = str(r) + hexadecimal
            elif r == 10:
                hexadecimal = "A" + hexadecimal  
            elif r == 11:
                hexadecimal = "B" + hexadecimal  
            elif r == 12:
                hexadecimal = "C" + hexadecimal  
            elif r == 13:
                hexadecimal = "D" + hexadecimal  
            elif r == 14:
                hexadecimal = "E" + hexadecimal  
            elif r == 15:
                hexadecimal = "F" + hexadecimal  
            n = n // b   #división entera que determina el While.
        print(hexadecimal) # se imprime la variable que contiene los numeros o letras
else:
    print ("Ingrese una base valida.") #Base incorrecta..

    


  
    


