"""Escribe un programa que cuente cuántas 
vocales hay en una cadena de texto."""

texto = "Cadena de texto"  
vocales = "AEIOUaeiou"
contador_vocales = 0

for char in texto:
    if char in vocales:
        contador_vocales += 1

print(f'Número de vocales en la cadena: {contador_vocales}')