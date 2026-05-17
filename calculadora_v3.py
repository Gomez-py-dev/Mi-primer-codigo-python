#PRIMER CALCULADORA

# PARTE 1, piezas de los clientes
piezas_mes = int(input("¿Cuántas piezas vendes al mes? "))
meses = 12
precio_venta = float(input("¿A cuánto vendes cada pieza? $"))
precio_costo = float(input("¿Cuánto te cuesta cada pieza? $"))
clientes = int(input("¿Cuántos clientes tienes? "))

#PARTE 2 matematicas
piezas_año = piezas_mes * meses
ventas_año = piezas_año * precio_venta
costo_año = piezas_año * precio_costo
ganancia = ventas_año - costo_año

# PARTE 3 clientes venta anual
print("Número de piezas al año:", piezas_año)
print("Ventas de un año: $", ventas_año)
print("Ganancia: $", ganancia)
ganancia_por_cliente = ganancia / clientes
impuesto = ganancia * 0.16  # IVA 16%
ganancia_neta = ganancia - impuesto

print("Ganancia por cliente: $", ganancia_por_cliente)
print("IVA a pagar: $", impuesto)  
print("Ganancia neta: $", ganancia_neta)