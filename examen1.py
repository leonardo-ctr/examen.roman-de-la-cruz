print(" ")#define una linea en blanco
print("Roman De la Cruz Leonardo Antonio.3-w-1211")
print(" ")

# Crear una lista con las asignaturas del curso
materias = ["pensamiento matematico", "leoye", "ecosistemas", "ingles", "humanidades","programacion"]

#almacena las notas
califa = {}

#solicita valores
for asignatura in materias:
    calif = float(input("Ingresa la nota de " + asignatura + ": "))
    print(" ")
    califa[asignatura] = calif

#quita las aprobadas
for asignatura, calif in califa.items():
    if calif >= 5.0 and asignatura in materias:
        materias.remove(asignatura)

#imprime lo que hay que repetir
print("Las asignaturas que debes repetir son:")
print(" ")
for asignatura in materias:
    print(" ")
    print(asignatura)
    print(" ")
