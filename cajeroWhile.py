
nombre = str(input("Ingrese el nombre del cliente: "));
banco = str(input("Ingrese el nombre del banco: "));
pin = 1234;
maxi = 3;
contador = 0;
guardarPin = ""



while contador <= maxi:
    guardarPin = int(input("Ingrese su pin: "));

    if guardarPin == pin:
        print(f"\nPin correcto. \nBienvenido {nombre} a su cuenta");
        break;
    else:
        contador += 1;
        print(f"\nPin incorrecto, tiene {maxi - contador} intentos disponibles");

        if contador == max:
            print(f"Ha excedido el numero de intentos permitidos y su cuenta a sido bloqueada. \n Por favor comunicarse al banco {banco} para desbloquear su cuenta");
            break;

print("Grancias por usar nuestros servicios")