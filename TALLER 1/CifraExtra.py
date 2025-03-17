n = int(input("Ingresa un numero: "))# ingresa un numero 
num= (str(n)) #convertimos el valor entero en una cadena.
cifras = ""#se asigna la variable vacia. 
for i in num: #leemos desde el primer numero del entero ingresado, ya convertido a cadena, hasta el último
    #se usa el residuo ya que el residuo de la suma de (9+1)%10 es 0 y de cualquier numero<10 es el mismo numero
    dig= ((int(i)+1)%10)#sumamos una unidad a la cifra que se toma de la lista
    cifras= cifras+str(dig)# vamos almacenando en cifras el nuevo numero ya sumado
print(cifras)#se imprime el nuevo numero..


