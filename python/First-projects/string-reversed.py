oracion = input("Ingresa tu texto a invertir: ")

oracion_invertida = oracion[::-1]

no_spaces = oracion_invertida.replace(" ", "")

print(no_spaces)

