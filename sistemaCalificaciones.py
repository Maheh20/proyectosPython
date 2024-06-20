

print('Sistema de calificacion escolar\n')

nota = int(input("Digita la nota del estudiante: "));

if nota >= 90 and nota <= 100:
    print("A");
elif nota >= 80 and nota < 90:
    print("B");

elif nota >= 70 and nota < 80:
    print("C");

elif nota >= 60 and nota < 70:
    print("D");

elif nota >= 0 and nota < 60:
    print("F");
else:
    print("Nota no valida");