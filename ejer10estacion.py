hemisferio = input("Ingrese el hemisferio (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))

if 3 <= mes <= 5:
    estacion_norte, estacion_sur = "Primavera", "Otoño"
elif 6 <= mes <= 8:
    estacion_norte, estacion_sur = "Verano", "Invierno"
elif 9 <= mes <= 11:
    estacion_norte, estacion_sur = "Otoño", "Primavera"
else:
    estacion_norte, estacion_sur = "Invierno", "Verano"

estacion = estacion_norte if hemisferio == "N" else estacion_sur
print(f"La estación actual es: {estacion}")
