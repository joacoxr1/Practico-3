nombre = input("Ingrese su nombre: ")
print("Hola " + nombre + "!")

print("Elija una opción:")
print("1 = MAYUSCULAS")
print("2 = minusculas")
print("3 = Primera letra en mayuscula")
numero = int(input("Ingrese un numero: "))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Opción no válida")