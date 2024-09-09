"""Dada una lista de elementos, escribe un programa 
que imprima los elementos en orden inverso utilizando un bucle for. Utilizamos un range"""

elementos = [1, 2, 3, 4, 5] 
for i in range(len(elementos) - 1, -1, -1):
    print(elementos[i])

"""el primer -1 sirve para especificar el indice para iniciar la iteracion, el segundo el indice en el que va a terminar, osea justo antes de que i sea = a -1 (0), el tercer parametro es el step, es decir los pasos que va a realizar, en este caso es de -1 en -1. """