cant_suc = int(input("Ingrese la cantidad de sucursales de su compañia: "))
reg_ventas_total = [[int() for ind0 in range(12)] for ind1 in range(cant_suc)]
ventas_anuales_suc = []
ventas_totales_comp = 0
ventas_totales_suc = int
mayor_venta = 0
suc_mayor_venta = int
reg_ventas = 0
menor_venta = 0
mes_menor_venta = int
suc_menor_venta = int

# Se cargan los datos a la matriz de ventas
for i in range(cant_suc):
    for j in range(12):
        reg_ventas_total[i][j] = int(input(f"Ingrese la venta mensual de la sucursal {i + 1} en el mes {j + 1}: "))

# Se recorre toda la matriz para sumar todas las ventas y obtener las ventas anual de la compañia
for i in range(cant_suc):
    for j in range(12):
        ventas_totales_comp = ventas_totales_comp + (int(reg_ventas_total[i][j]))
print(f"Las ventas totales de la compañia en los 12 meses son de: {ventas_totales_comp} ventas")

# Se recorre la matriz por filas para encontrar las ventas anual de cada sucursal y se almacenan en un vector
for i in range(cant_suc):
    ventas_totales_suc = 0
    for j in range(12):
        ventas_totales_suc = ventas_totales_suc + (int(reg_ventas_total[i][j]))
    ventas_anuales_suc.append(ventas_totales_suc)

# Se recorre el vector de ventas anual por sucursal para imprimir las ventas anuales por sucursal
for i in range(cant_suc):
    print(f"La sucursal N° {i + 1} registro un total de ventas anual de {ventas_anuales_suc[i]} ventas")

# Se recorre el vector de ventas anual por sucursal y se comparan las cant de ventas para obtener la sucursal que
# mayor ventas tuvo
for i in range(cant_suc):
    if ventas_anuales_suc[i] > mayor_venta:
        mayor_venta = ventas_anuales_suc[i]
        suc_mayor_venta = i + 1
print(
    f"La sucursal con mayor numero de ventas en este año es la sucursal N°{suc_mayor_venta} con un registro de {mayor_venta} ventas en este año")

# Se recorre la matriz por columnas para obtener las ventas mensuales de la compañia e ir comparandolos entre ellos y
# obtener el mes que menos ventas tuvo la compañia
for j in range(12):
    reg_ventas = 0
    for i in range(cant_suc):
        reg_ventas = reg_ventas + reg_ventas_total[i][j]
    if menor_venta == 0:
        menor_venta = reg_ventas
        mes_menor_venta = j + 1
    elif reg_ventas < menor_venta:
        menor_venta = reg_ventas
        mes_menor_venta = j + 1
print(f"El mes que menos ventas registro la compañia es en el mes {mes_menor_venta} con {menor_venta} ventas")

file = open("Registro de Ventas.txt", "a")
file.write(
        f"VentaTotalComp:{ventas_totales_comp}|SucMayVentas:{suc_mayor_venta}|MesMenosVentasComp:{mes_menor_venta}\n"
        "VENTAS ANUALES POR SUCURSALES:\n")
for i in range(cant_suc):
    file.write(f"Suc{i + 1}:{ventas_anuales_suc[i]}|")
file.write("\n-----------------------------------------------------------------------------------------------------")
file.close()


ruta = r"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Programacion II\Registro de Ventas.txt"
with open(ruta, "a") as arch:
    arch.write(
        f"VentaTotalComp:{ventas_totales_comp}|SucMayVentas:{suc_mayor_venta}|MesMenosVentasComp:{mes_menor_venta}\n"
        "VENTAS ANUALES POR SUCURSALES:\n")
    for i in range(cant_suc):
        arch.write(f"Suc{i + 1}:{ventas_anuales_suc[i]}|")
    arch.write("\n "
               "-----------------------------------------------------------------------------------------------------")
    arch.close()