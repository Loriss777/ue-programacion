# ============================================
# Fundamenos de Programacion: Programación esencial en Python
# ANÁLISIS SEMANAL DE VENTAS - TIENDA ONLINE
# Estudiante: Lorena Rubio Navolotskaya
# ============================================

# PASO 1: Pedimos al usuario el objetivo semanal
# Para hacer el codigo mas visual, utilizaremos varias veces este metodo que imprimita "=" por 50 veces con el objetivo de dividir los inputs y outputs en la consola,
# También haremos uso de /n para realizar un salto de linea en el codigo y generar un programa más organizado visualmente para el usuario
print("=" * 50)
print("SISTEMA DE ANÁLISIS DE VENTAS")
print("=" * 50)

#Pedimos al usuario el objetivo de la semana y lo transformamos a float, ya que el input del usuario será un string
objetivo = float(input("\n¿Cuál es tu objetivo de ventas para esta semana (en euros)? "))

#Utilizamos un condicional para validar que el valor es positivo, en el caso de no cumplir la condición dara un error y volvera a preguntar el valor, hasta que se cumpla la condicion
while objetivo <= 0:
    print(" Error: El objetivo debe ser un número positivo.")
    objetivo = float(input("Intenta de nuevo. ¿Cuál es tu objetivo de ventas? "))

print(f" Objetivo establecido: {objetivo} euros")

# PASO 2: Registrar ventas diarias
#Declaramos la variable dias_semana con la cual usamos una lista para definir los días y una lista vacia ventas_diarias donde guardaremos las ventas de cada día 
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas_diarias = []

print("\n" + "=" * 50)
print("REGISTRO DE VENTAS DIARIAS")
print("=" * 50)

#Declaramos un bucle for para que recorra todos los dias declarados en nuestra lista, y para guardarlos en la lista vacia declarada anteriormente
for dia in dias_semana:
    venta = float(input(f"Ventas del {dia} (en euros): "))
    
    # Validar que sea positivo
    while venta < 0:
        print(" Error: Las ventas no pueden ser negativas.")
        venta = float(input(f"Intenta de nuevo. Ventas del {dia} (en euros): "))
    
    ventas_diarias.append(venta)

print(f"\n Ventas registradas correctamente")

# PASO 3: Calcular métricas básicas
# Utilizamos operadores aritmeticos para definir las variables total_ventas y media_diaria, las cuales se alimentan de los datos declarados anteriormente
total_ventas = sum(ventas_diarias)
media_diaria = total_ventas / 7

# Contar cuántos días las ventas fueron mayores o iguales al umbral, se define el umbral como se sugiere en el ejercicio = 100€ 
# Definimos la variable dias_por_encima_umbral = 0 la cual ira sumando los dias que si han cumplido con este condicional, venta mayor o igual que umbral
umbral = 100
dias_por_encima_umbral = 0

for venta in ventas_diarias:
    if venta >= umbral:
        dias_por_encima_umbral += 1

# PASO 4: Evaluar el objetivo
# Durante la evaluacion y print de los valores, formateamos los numeros para mejor comprension y reduccion de decimales, utilizando ":" aplicamos el formato,
# ".2" le decimos al programa que solo imprima 2 decimales y con "f" declaramos que el valor es float, un numero decimal
print("\n" + "=" * 50)
print("ANÁLISIS DE RESULTADOS")
print("=" * 50)

print(f"\n MÉTRICAS CALCULADAS:")
print(f"  - Total de ventas:              {total_ventas:.2f} euros")
print(f"  - Media diaria:                 {media_diaria:.2f} euros")
print(f"  - Días con ventas >= {umbral}€:        {dias_por_encima_umbral}/7 días")

# PASO 5: Comparación con objetivo
print(f"\n EVALUACIÓN DEL OBJETIVO:")
print(f"  - Objetivo establecido:         {objetivo:.2f} euros")
print(f"  - Total logrado:                {total_ventas:.2f} euros")

# Utilizamos el condicional if con operadores logicos," si el total de ventas es mayor o igual que el objetivo" cumple el condicional y resta el total - objetivo
#Si no se cumple el condicional, avisa al usuario que vendio menos que el objetivo declarado, mostrandole el numero que le falta para cumplir su objetivo
if total_ventas >= objetivo:
    diferencia = total_ventas - objetivo
    print(f"  - Resultado:                     OBJETIVO ALCANZADO")
    print(f"  - Superaste en:                 {diferencia:.2f} euros")
else:
    falta = objetivo - total_ventas
    print(f"  - Resultado:                     OBJETIVO NO ALCANZADO")
    print(f"  - Te falta:                     {falta:.2f} euros")

# PASO 6: Resumen final
print("\n" + "=" * 50)
print("RESUMEN FINAL SEMANAL")
print("=" * 50)

print(f"\nDetalles por día:")
for i, dia in enumerate(dias_semana):
    print(f"  {dia:12} → {ventas_diarias[i]:8.2f} euros", end="")
    if ventas_diarias[i] >= umbral:
        print(" Ventas en el umbral declarado")
    else:
        print()

print(f"\nTOTAL SEMANA:     {total_ventas:8.2f} euros")
print(f"PROMEDIO DIARIO:  {media_diaria:8.2f} euros")
print(f"OBJETIVO:         {objetivo:8.2f} euros")

print("\n" + "=" * 50)
if total_ventas >= objetivo:
    print(" ¡Objetivo cumplido")
else:
    print(" El objetivo no se ha cumplido")
print("=" * 50 + "\n")
