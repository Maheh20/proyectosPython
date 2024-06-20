
# Declarar variables
nombre = str(input("Nombre Cliente: ")); # Cantidad de precios productos
agregar = 'si' #str(input("Listo para pagar? (si/no): ")); # Cantidad de precios productos
tasaImpuesto = 0.18; # La variable del impuesto
descuento = 0.20; # Variables de descuento
i = 0; # Variable contador
subtotal = 0;


# Ciclo para calcular el total de la compra
while agregar == 'si' or agregar == 'Si':
    i += 1;
    precioProductos = float(input(f'Precio Producto {i}: ')); # Agregar precios productos
    cantidad = int(input(f'Cantidad: ')); # Agregar cantiddad de producto x
    totalCantidad = precioProductos * cantidad; # Calcular el total de el precio del producto por la cantidad
    subtotal += totalCantidad; # Calcular el subtotal de la compra
    
    agregar = str(input(f'Desea agregar otro producto? (si/no): ')); # Confirmar si el usuario quiere agregar algo mas.

# Calcular la compra
totalDescuento = subtotal * descuento; # Descuento sin aplicar
totalConDescuento = subtotal - totalDescuento; # Aplicar descuento a mi compra
impuesto = totalConDescuento * tasaImpuesto; 
total = totalConDescuento + impuesto; # Total final a pagar

# Imprimiendo valores en pantalla utilizando la impresion multilineas
print(
f'''
********************** FACTURACION **********************

Nombre Cliente: Sr(a): {nombre}

Subtotal: {round(subtotal, 3)}
Total Descuento: {round(totalDescuento, 3)}
Total Descuento Aplicado: {round(totalConDescuento, 3)}
Impuesto: {round(impuesto, 3)}
Total Final: {total}

***************** GRACIAS POR SU COMPRA ***************** 
'''
)




