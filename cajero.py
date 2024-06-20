
'''
Realizar un menu con diferentes operacion que te permita consultar, depositar,
transferir y salir, tambien que te permita iniciar el valor con un saldo.
'''
nombre = str(input("Ingrese el nombre del cliente: "));
numeroTransaccion = 3354760009
saldo = 1000;

print(f'''
    ********************************
        Seleccione su banco:
    ********************************
            1. Popular
            2. Banreservas
            3. BHD
            4. Otro
    ''')

banco = int(input("Seleccione su banco: "));
if banco == 1:
    banco = "Popular"
elif banco == 2:
    banco = "Banreservas"
elif banco == 3:
    banco = "BHD"
elif banco == 4:
    banco = str(input("Nombre del banco: "));
else:
    print(f"\nOpcion no valida, banco no seleccionado");
    banco = "No valido"
    
while True:
    
    print(f'''
    ******************************************************
        Bienvenido {nombre} a su cuenta de banco {banco}.
                Cuenta bancaria: {numeroTransaccion}
    ******************************************************
        Seleccione una de las siguientes opciones:
            1. Consultar saldo
            2. Depositar
            3. Transferir
            4. Salir
    ''')

    opcion = int(input("Seleccione una opcion: "));

    if opcion == 1:
        print(f"\nSu saldo disponible es: {saldo:.2f}");
    
    elif opcion == 2:
        deposito = float(input("Digite el monto a depositar: "));
        if deposito > 0:
            saldo += deposito;
            print(f'''\nDepositaste ${deposito:.2f} a tu cuenta.\nSu saldo disponible es: {saldo:.2f}''');
        else:
            print(f"\nEl monto a depositar debe ser mayor a 0");
    
    elif opcion == 3:
        transferencia = float(input("Digite el monto a transferir: "));
        if transferencia > 0 and transferencia <= saldo:
            saldo -= transferencia;
            print(f"\nSu saldo disponible es: {saldo:.2f}");
        elif transferencia > saldo:
            print(f"\nEl monto a transferir debe ser mayor a 0 y menor o igual a su saldo");
    
    elif opcion == 4:
        print(f"\nGracias por usar nuestros servicios");
        break;

    else:
        print(f"\nIngrese una opcion valida");


