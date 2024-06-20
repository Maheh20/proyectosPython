
print("Verificando si es elegible o no para solicitar tarjeta\n")
nombre = str(input("Nombre del solicitante: "))
edad = int(input("Edad del solicitante: "))
trabaja = str(input("Esta trabajando (si/no)? "))
tiempoLaborar = str(input("Cuanto tiempo lleva trabajando?  "))
sueldoActual = int(input("Cual es su sueldo actual? "))


if edad >= 18:
    if trabaja == "Si" or trabaja == "si":
        if sueldoActual >= 35000:
            print(
            f'''
            Nombre del solicitante: {nombre}
            Edad del solicitante: {edad}
            Esta trabajando: {trabaja}
            Tiempo de trabajo: {tiempoLaborar}
            Sueldo actual: {sueldoActual}

            Felicidades eres elegible para solicitar una tarjeta con beneficios
            ''')
        elif sueldoActual >= 20000 and sueldoActual < 35000:
            print(
            f'''
            Nombre del solicitante: {nombre}
            Edad del solicitante: {edad}
            Esta trabajando: {trabaja}
            Tiempo de trabajo: {tiempoLaborar}
            Sueldo actual: {sueldoActual}

            El solicitante es elegible para solicitar una tarjeta regular
            ''')
        else:
            print(
            f'''
            Nombre del solicitante: {nombre}
            Edad del solicitante: {edad}
            Esta trabajando: {trabaja}
            Tiempo de trabajo: {tiempoLaborar}
            Sueldo actual: {sueldoActual}

            El solicitante no es elegible para solicitar una tarjeta, su sueldo no es suficiente.
            ''')
    else:
        print(
        f'''
        Nombre del solicitante: {nombre}
        Edad del solicitante: {edad}
        Esta trabajando: {trabaja}
        Tiempo de trabajo: {tiempoLaborar}
        Sueldo actual: {sueldoActual}

        El solicitante es mayor de edad, pero no cuenta con un empleo, no es elegible para solicitar una tarjeta.
        ''')
else:
    print(
    f'''
    Nombre del solicitante: {nombre}
    Edad del solicitante: {edad}
    Esta trabajando: {trabaja}
    Tiempo de trabajo: {tiempoLaborar}
    Sueldo actual: {sueldoActual}

    El solicitante es menor de edad, no es elegible para solicitar una tarjeta.
    ''')