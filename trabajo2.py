import math


def primos():
    
    losprimos=[] # se genera los numros primos en la lista

    print("seva encontrar la lista desde los numeros 1000000000,1000000101 en la cual seva mirar cuantos son y cuales son  ")

    for x in range(1000000000,1000000101): #se pone el inicio y el final de la lista que se quiere ver
        val = True
        m = math.isqrt(x)
        for i in range(2,m):

            if x%i == 0:
                val = False
                break
        if val:
             losprimos.append(x) 
    return losprimos     
        
print(primos())
print("la cantidad de numeros primos que se encuentra son: ",len(primos())) # como es una lista se utiliza len para que cuente todos los numeros que se encuentre hay