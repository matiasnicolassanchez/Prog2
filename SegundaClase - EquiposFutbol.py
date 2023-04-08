goles_convertidos = [[int() for ind0 in range(5)] for ind1 in range(5)]
goles = int
partidos_ganados = int
partidos_perdidos = int
partidos_empatados = int
triunfos = []
derrotas = []
empates = []
goles_conseguidos = []
goles_recibidos = []
goles_favor = int
goles_contra = int

# Se cargan los goles convertidos en la matriz
for i in range(5):
    for j in range(5):
        if i == j:
            goles_convertidos[i][j] = 0
        else:
            goles = int(input(f"Ingrese los goles convertidos del equipo {i+1} al equipo {j+1}: "))
            goles_convertidos[i][j] = goles

# Se imprimi la matriz de los goles cargados
for i in range(5):
    for j in range(5):
        goles_convertidos[i][j]
        print(" ", goles_convertidos[i][j], end="")
    print(" ")

# Se recorre la matriz completa comparando los goles convertidos con los recibidos para saber cuantos partidos gano, empato y perdio cada equipo
# Los partidos ganados, empatados y perdidos por cada equipo se almacenan en sus respectivos vectores.
for i in range(5):
    partidos_ganados = 0
    partidos_perdidos = 0
    partidos_empatados = 0
    for j in range(5):
        if i != j:
            if goles_convertidos[i][j] > goles_convertidos[j][i]:
                partidos_ganados += 1
            elif goles_convertidos[i][j] < goles_convertidos[j][i]:
                partidos_perdidos += 1
            elif goles_convertidos[i][j] == goles_convertidos[j][i]:
                partidos_empatados +=1
    triunfos.append(partidos_ganados)
    derrotas.append(partidos_perdidos)
    empates.append(partidos_empatados)

# Se recorren los vectores de partidos ganados, empatados y perdidos para imprimir los registros por cada equipo
for i in range(5):
    print(f"El equipo {i+1} registra: \n {triunfos[i]} partidos ganados \n {derrotas[i]} partidos perdidos \n {empates[i]} partidos empatados")

# Se recorre la matriz completa para obtener la cantidad de goles que convirtio cada equipo durante el campeonato
# Los goles convertidos en el campeonato por cada equipo se almacenan en su respectivo vector
for i in range(5):
    goles_favor = 0
    for j in range(5):
        if i != j:
            goles_favor += goles_convertidos[i][j]
    goles_conseguidos.append(goles_favor)

# Se recorre la matriz completa para obtener la cantidad de goles que recibio cada equipo durante el campeonato
# Los goles recibidos en el campeonato por cada equipo se almacenan en su respectivo vector
for j in range(5):
    goles_contra = 0
    for i in range(5):
        if i != j:
            goles_contra += goles_convertidos[i][j]
    goles_recibidos.append(goles_contra)

# Se recorren los vectores de goles convertidos y recibidos por equipo para imprimir el registro en el campeonato
for i in range(5):
    print(f"El equipo {i+1} registra: \n {goles_conseguidos[i]} goles convertidos en el campeonato y \n {goles_recibidos[i]} goles recibidos en el campeonato")

# Aqui se crea un archivo .txt localmente en pycharm
file = open("Registo de Campeonato.txt", "a")
for i in range(5):
    file.write(f"Equipo{i+1}|Ganados:{triunfos[i]}|Perdidos:{derrotas[i]}|Empatados:{empates[i]}|GF:{goles_conseguidos[i]}|GC:{goles_recibidos[i]} \n")
file.close()

# Aqui se indica la ruta del archivo .txt donde quiero escribir los registros y los escribo
ruta = r"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Programacion II\Registro de Campeonato.txt"
with open(ruta, "a") as archivo:
    for i in range(5):
        archivo.write(
            f"Equipo{i + 1}|Ganados:{triunfos[i]}|Perdidos:{derrotas[i]}|Empatados:{empates[i]}|GF:{goles_conseguidos[i]}|GC:{goles_recibidos[i]} \n")
    file.close()

