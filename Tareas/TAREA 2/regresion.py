import matplotlib.pyplot as plt
import random as rnd 

n = int(input("Por favor ingrese el número de elementos aleatorios para la regresión lineal: ")) #Cantidad de números para la regresión lineal.
X = [] #Se inicia lista vacia
Y = [] #Se inicia lista vacia

for i in range(n):
    X.append(rnd.random()) #Se ingresan valores random a las cadenas.
    Y.append(rnd.random()) #Se ingresan valores random a las cadenas.


sum_XpY = 0 #Se inician las variables en '0
sum_X2 = 0 #Se inician las variables en '0
sum_X = 0 #Se inician las variables en '0
sum_Y = 0 #Se inician las variables en '0
for i in range(n):
    sum_XpY = sum_XpY + (X[i] * Y[i]) #Se dan valores a las variables mediante las operaciones que nse necesitan en la formula más adelante.
    sum_X2 = sum_X2 + X[i]**2  #Se dan valores a las variables mediante las operaciones que nse necesitan en la formula más adelante.
    sum_X = sum_X + X[i] #Se dan valores a las variables mediante las operaciones que nse necesitan en la formula más adelante.
    sum_Y = sum_Y + Y[i] #Se dan valores a las variables mediante las operaciones que nse necesitan en la formula más adelante.
    
m = ((n * sum_XpY) - (sum_X * sum_Y)) / ((n * sum_X2) - (sum_X**2)) #FORMULA PENDIENTE.
    

b = ((sum_Y * sum_X2) - (sum_X * sum_XpY)) / ((n * sum_X2) - (sum_X**2)) #FORMULA CORTE Y.

Y2 = [] #LISTA VACIA
for i in X:
    Y2.append(i*m + b) #Se ingresa valores a la lista en base a la formula de la recta.

plt.plot(X, Y, "r*", X, Y2, "g-") #SE MUESTRA LA GRÁFICA.
plt.show() #SE MUESTRA LA GRÁFICA.