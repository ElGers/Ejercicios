import random as rnd #Importamos librerias.

n = int(input("Por favor, ingrese la cantidad de números random: ")) #Ingresamos valor de números random
A = [] #Lista vacia.

for i in range(n):
    A.append(rnd.randint(0,100)) #Se ingresan valores random a la lista.
    
def media(z): #FUNCIÓN DE MEDIA
    media = sum(z) / len(z)
    return media

def varianza(z): #FUNCIÓN DE VARIANZA
    sum = 0
    for i in z:
        sum = sum + ((i - media(z))**2)
    varianza = sum / (len(z) - 1)
    return varianza

def desviacion(z): #FUNCIÓN DE DESVIACIÓN DE ESTANDAR. 
    desviacion = varianza(z)**(1/2)
    return desviacion

def rango(z): #FUNCIÓN DEL RANGO
    rango = max(z) - min(z)
    return rango

# Comprobar que se generaron elementos
if len(A) == 0:
    print("Por favor, ingrese un valor minimo a la lista.")
else:
    print("La lista generada aleatoriamente fue: ")
    print(A)
    print(f"La media de esa lista fue: {media(A)}")
    print(f"La varianza de esa lista fue: {varianza(A)}")
    print(f"La desviación estandar de esa lista fue: {desviacion(A)}")
    print(f"El rango de esa lista fue: {rango(A)}")