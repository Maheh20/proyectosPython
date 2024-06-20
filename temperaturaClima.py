
print('Identificar temperatura segun el cambio climatico\n')

clima = str(input("Digite el clima (Soleado/Lluvioso/Frio): "));

if clima == "Soleado" or clima == "soleado":
    print(f"El clima es {clima}, la temperatura está por encima de 24°C");
elif clima == "Lluvioso" or clima == "lluvioso":
    print(f"El clima es {clima}, temperaturas medias superiores a los 10°C");

elif clima == "Frio" or clima == "frio":
    print(f"El clima es {clima}, la temperatura está por debajo de 10°C");
else:
    print(f"El clima {clima} no es reconocido, no se puede determinar la temperatura");