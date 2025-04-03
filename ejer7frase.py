texto = input("Ingrese una frase o palabra: ")
print(texto + "!" if texto[-1].lower() in "aeiou" else texto)
