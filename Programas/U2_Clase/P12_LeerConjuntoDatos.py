nombre_instancia = "../Archivos/Datos_Calificaciones.csv"

archivo = open(nombre_instancia)

contenido = archivo.readlines()

print(contenido)

instancia = [linea.split(",") for linea in contenido]
del instancia[0]
instancia = [[registro[0], int(registro[1])] for registro in instancia]

instancia.sort(key=lambda x:x[1],reverse=True)
print(instancia)

mayor = instancia[0][1]
altos = []

for i in instancia:
    if i[1] >= mayor:
        altos.append(i)

print("Alumnos con calificacion mas alta = ", altos)