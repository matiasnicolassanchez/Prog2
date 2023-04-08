respuestas = [1, 3, 2, 5, 4, 5, 2, 3, 1, 4]
legajos = [1001, 1002]
resultados = [[int() for ind0 in range(len(respuestas))] for ind1 in range(len(legajos))]
notas = []
opcion_elegida = int
respAlumno = int
correctas = int

# Recorro y lleno la matriz con las respuestas que cada alumno escogio
for i in range(len(legajos)):
    for j in range(len(respuestas)):
        opcion_elegida = int(input(f"Ingrese la respuesta del alumno: {legajos[i]} a la pregunta {j+1}: "))
        if opcion_elegida < 1 or opcion_elegida > 5:
            while opcion_elegida < 1 or opcion_elegida > 5:
                opcion_elegida = int(input(f"Ingrese la respuesta del alumno: {legajos[i]} a la pregunta {j+1}: "))
        else:
            if opcion_elegida < 6 and opcion_elegida > 0:
                resultados[i][j] = opcion_elegida

# Muestro la matriz donde se almacenaron las respuestas de cada alumno a cada respuesta
for i in range(len(legajos)):
    for j in range(len(respuestas)):
        resultados[i][j]
        print(" ", resultados[i][j], end="")
    print(" ")

# Recorro la matriz para obtener la cantidad de respuestas correctas y obtener la nota por alumno
for i in range(len(legajos)):
    correctas = 0
    for j in range(len(respuestas)):
        respAlumno = int(resultados[i][j])
        if respAlumno == respuestas[j]:
            correctas = correctas + 1
    notas.append(correctas)
    if correctas >= 6:
        print(f"El alumno {legajos[i]} APROBO con nota: {notas[i]}")

    else:
        print(f"El alumno {legajos[i]} DESAPROBO con nota: {notas[i]}")

# print(f"{notas}")


file = open("Notas de Alumnos.txt", "a")
for i in range(len(notas)):
    file.write(f"Legajo:{legajos[i]}|Nota:{notas[i]} \n")
file.close()

ruta = r"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Programacion II\Notas de Alumnos.txt"
with open(ruta, "a") as arch:
    for i in range(len(notas)):
        arch.write(f"Legajo:{legajos[i]}|Nota:{notas[i]} \n")
    file.close()