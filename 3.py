"""Dada una lista de números, escribe un programa que calcule la suma de 
todos los elementos de la lista."""

numeros = [1, 2, 3, 4, 5]  
suma = 0
for i in numeros:
    suma += i
print(f'La suma de los números es: {suma}')