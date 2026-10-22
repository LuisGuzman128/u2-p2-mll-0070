import numpy as np
# Axel Guzman NC 0070
# ejemplos de numpy Numerical python
print("-- espaciado linallmente en array -- 0070")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("-- matriz identidad en array -- 0070")
matrix=np.eye(3)
print(matrix)
print("-- genera numeros al azar(aleatorios)en 2D array -- 0070")
numale=np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)
print("generar 9 numeros aleatorios entre cero y uno")
numale=np.random.random((3,3)) # genera 12 numeros aleatorios
print(numale)
# como generar numeros 9 aleatorios comprendidos entre  1 y 20
#  con numpy en un arreglo de 3 por 3
print("generar 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=(3, 3)) # 
print(arre)
print("Axel Guzman 0070")