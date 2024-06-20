num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

Mayor = num1 > num2 
Igual = num1 == num2
Menor = num1 < num2
Distinto = num1 != num2 

Verdadera = True
Falso = False

resultado_And = Verdadera and Falso
resultado_Or = Verdadera or Falso
resultado_NOT = not Verdadera


print(f'{num1} es mayor que {num2}, {Mayor}')
print(f'{num1} es igual  {num2}, {Igual}')
print(f'{num1} es menor que {num2}, {Menor}')
print(f'{num1} es distinto que {num2}, {Distinto}')


print("True AND False", resultado_And)
print("True OR False", resultado_Or)
print("NOT True ", resultado_NOT)
