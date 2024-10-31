print(" ")#define una linea en blanco
print("Roman De la Cruz Leonardo Antonio.3-w-1211")
print(" ")

#materias
materias = ["pensamiento matematico", "prgramacion", "leoye", "ecosistemas", "ingles", "humanidades"]

#hace un diccionario
califa = {}

#solicita valores
for materias in materias:
    total = input(f'Ingresa lo que sacaste con tus esfuerzos en {materias}: ')
    califa[materias] = total

#imprime las calificaciones
for materias, total in califa.items():
    print(f'En {materias} has sacado {total}')
