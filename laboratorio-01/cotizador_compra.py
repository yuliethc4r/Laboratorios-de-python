nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el nombre del producto: ")

precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto: "))

costo_envio = 1000

nombre_vendedor = input("Ingrese el nombre del vendedor: ")
codigo_cotizacion = input("Ingrese el código de cotización: ")

# Calculos de la compra
subtotal = precio_unitario * cantidad
valor_descuento = subtotal * (porcentaje_descuento / 100)
base_descuento = subtotal - valor_descuento
valor_impuesto = base_descuento * (porcentaje_impuesto / 100)
total = base_descuento + valor_impuesto + costo_envio

# Resumen de la cotizacion
print("\n===== COTIZACION DE COMPRA =====")
print("Nombre del cliente:", nombre)
print("Producto:", producto)
print("Precio unitario: $", round(precio_unitario, 2))
print("Cantidad:", cantidad)
print("Subtotal: $", round(subtotal, 2))
print("Descuento aplicado (%):", porcentaje_descuento)
print("Valor del descuento: $", round(valor_descuento, 2))
print("Base despues del descuento: $", round(base_descuento, 2))
print("Impuesto (%):", porcentaje_impuesto)
print("Valor del impuesto: $", round(valor_impuesto, 2))
print("Costo de envio: $", round(costo_envio, 2))
print("Nombre del vendedor:", nombre_vendedor)
print("Codigo de cotizacion:", codigo_cotizacion)
print("TOTAL FINAL: $", round(total, 2))
