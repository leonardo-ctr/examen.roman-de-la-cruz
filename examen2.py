print(" ")#define una linea en blanco
print("Roman De la Cruz Leonardo Antonio.3-w-1211")
print(" ")
# Definir el diccionario con los créditos de las asignaturas
califa_asignaturas = {'pensamiento matematico': 6, 'ecosistemas': 8, 'leoye': 8, 'humanidades': 9, 'ingles': 9, 'programacion': 10}

# Mostrar los créditos de cada asignatura
for asignatura, creditos in califa_asignaturas.items():
    print(" ")
    print(f"{asignatura} tiene {creditos} créditos")
    print(" ")

# Calcular el número total de créditos del curso
total_califa = sum(califa_asignaturas.values())
print(f"El número total de créditos del curso es: {total_califa}")
print(" ")
