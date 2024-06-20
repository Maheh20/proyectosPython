
# Declarar variables
cantidaPrecioProductos = int(input("Cantidad Precio Productos: ")); # Cantidad de precios productos
tasaImpuesto = 0.18; # La variable del impuesto
descuento = 0.20; # Variables de descuento
i = 0; # Variable contador
subtotal = 0;

# Ciclo para calcular el total de la compra
while i < cantidaPrecioProductos:
    i += 1;
    precioProductos = float(input(f'Precio Producto {i}: ')); # Agregar precios productos

    subtotal += precioProductos; # Calcular el subtotal de la compra
    totalDescuento = subtotal * descuento; # Descuento sin aplicar
    totalConDescuento = subtotal - totalDescuento; # Aplicar descuento a mi compra
    impuesto = totalConDescuento * tasaImpuesto; # Calculando el impuesto

total = totalConDescuento + impuesto; # Total final a pagar

# Imprimiendo valores en pantalla
print(f'\nSubtotal: {round(subtotal, 3)}  \nTotal Descuento: {round(totalDescuento, 3)} \nTotal Descuento Aplicado: {round(totalConDescuento, 3)}'); 
print(f'Impuesto: {round(impuesto, 3)} \nTotal Final: {total}'); 

