
print(
'''Supongamos que queremos recomendar diferentes actividades
dependiendo de si es mañana, tarde o noche'''
)

hora = int(input("Digite la hora: "))

if hora >= 5 and hora < 12:
    print("Buenos dias! Es hora de hacer ejercicio al aire libre")
elif hora >= 12 and hora < 18:
    print("Buenas tardes! Es un buen momento para trabajar o almorzar")
elif hora >= 18 and hora < 22:
    print("Buenas noches! Es un buen momento para salir a cenar")
else:
    print("Hora de dormir, Es tarde, asegurate de descansar lo suficiente")