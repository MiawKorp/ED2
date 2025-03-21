"""
Programa para contar vocales en un texto ingresado por el usuario
"""

def contar_vocales(texto):
    """Devuelve el número de vocales en un texto"""
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vocales:
            contador += 1

    return contador

# Solicitar un texto
texto_usuario = input("Ingresa un texto:  ")

# Contar vocales y mostrar la cantidad de vocales
cantidad_vocales = contar_vocales(texto_usuario)
print(f"El texto tiene {cantidad_vocales} vocales")
