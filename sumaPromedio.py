
# Suma promedio
valor = int(input("Digite cantidad de # a calcular: "));

i = 0; # Declaramos un contador
suma = 0;

while (i < valor):
    i += 1;
    num = int(input(f'Digite valor {i}: '));
    suma += num;

promedio = suma / i;

print(f'\nLa suma es:  {suma}');
print(f'El promedio es:  {promedio}');
