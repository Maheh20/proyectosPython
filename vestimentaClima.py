
print('Recomendacion de vestimenta segun el cambio climatico\n')

clima = str(input("Digite el clima (Soleado/Lluvioso/Frio): "));

if clima == "Soleado" or clima == "soleado":
    print(f"El clima es {clima}, utiliza ropa ligera y fresca");

elif clima == "Lluvioso" or clima == "lluvioso":
    print(f"El clima es {clima}, utiliza ropa impermeable y no olvide llevar su sombrilla");

elif clima == "Frio" or clima == "frio":
    print(f"El clima es {clima}, utiliza ropa abrigada y no olvides tu abrigo en casa");
else:
    print(f"El clima {clima} no es reconocido");