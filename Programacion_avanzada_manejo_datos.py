# Fundamenos de Programacion: Programacion avanzada y manejo de datos
# ANÁLISIS DE VENTAS CON PANDAS Y NUMPY
# Estudiante: Lorena Rubio Navolotskaya
# ============================================

# Importamos las librerias de python necesarias, en este caso pandas y numpy
# Segun la documentación, es recomendable iniciar un entorno virtual de Python para poder instalar las librerias con el comando Pip Install
# Python -m venv ventas > source ventas/bin/activate > pip install <libreria>


import pandas as pd
import numpy as np


# ========================================
# PASO 1: CARGA DE DATOS
# ========================================
# Cargamos los datos necesarios para el programa, como menciona el enunciado, utilizaremos un csv como nuestra data para trabajar
# Nos aseguraremos de que el csv este en el mismo directorio de ejecucion que nuestro programa ( nuestro fichero .py )
# Mediante def_cargar_datos() definimos nuestra primera funcion, con pandas se encarga de leer el archivo ventas_mes.csv, carga el dataframe y lo devuelve

def cargar_datos():
    """
    Lee el archivo ventas_mes.csv usando pandas.
    Devuelve un DataFrame con todos los datos.
    """
    dataframe = pd.read_csv('ventas_mes.csv')
    return dataframe

# ========================================
# PASO 2: PREPARACIÓN Y LIMPIEZA DE DATOS
# ========================================
# Definimos nuestra segunda función, preparar_datos, esta función se encargará de limpiar los datos, convirtiendolos en numericos, y eliminando los valores faltantes

def preparar_datos(dataframe):
    """
    Limpia y prepara los datos:
    - Convierte tipos numéricos
    - Crea la columna 'importe' (unidades * precio)
    - Elimina valores faltantes
    """
    
    # Convertir columnas a tipo numérico
    # Convertimos la columna unidades a numerico, si hay algo que no se puede convertir se queda como NaN (vacio), usando errors='coerce'
    dataframe['unidades'] = pd.to_numeric(dataframe['unidades'], errors='coerce')
    
    # Convertimos la columna precio_unitario a numerico, lo mismo que antes pero para esta columna
    dataframe['precio_unitario'] = pd.to_numeric(dataframe['precio_unitario'], errors='coerce')
    
    # Creamos la columna 'importe' multiplicando las dos columnas anteriores
    dataframe['importe'] = dataframe['unidades'] * dataframe['precio_unitario']
    
    # Eliminamos las filas inconsistentes, aquellas vacías que tienen valor NaN (vacio), con el objetivo de limpiar los datos
    dataframe = dataframe.dropna(subset=['importe'])
    
    # Devolvemos el dataframe para usarlo en el resto del programa
    return dataframe

# ========================================
# PASO 3: RESUMEN GENERAL
# ========================================
# Definimos la tercera funcion, obtener_resumen_general, esta funcion utiliza un diccionario que se guarda como resulen general

def obtener_resumen_general(dataframe):
    """
    Calcula métricas generales de las ventas.
    Devuelve un diccionario con los resultados.
    """
    
    resumen_general = {
        # Calculamos cuantas filas hay en el dataframe
        'total_ventas': len(dataframe),
        # Sumamos todos los numeros de la columna unidades
        'total_unidades': dataframe['unidades'].sum(),
        # Sumamos todos los importes de la columna importe
        'total_importe': dataframe['importe'].sum(),
        # Calculamos la venta promedio de los importes
        'importe_medio': dataframe['importe'].mean(),
        # Calculamos el valor más bajo de la columna importe
        'importe_minimo': dataframe['importe'].min(),
        # Calculamos el valor más alto de la columna importe
        'importe_maximo': dataframe['importe'].max()
    }
    
    # Devolvemos el diccionario para que se use en el programa
    return resumen_general


# ========================================
# PASO 4: RESUMEN POR CATEGORÍA
# ========================================
# Se define la cuarta función, obtener_resumen_por_categoria

def obtener_resumen_por_categoria(dataframe):
    """
    Agrupa las ventas por categoría y suma el importe.
    Devuelve una serie ordenada de mayor a menor.
    """
    
    # Agrupar por categoría y sumar importe
    # Utilizamos groupby para agrupar por categoria, y de cada grupo tomamos solo la columna importe, sumando el importe para cada grupo (categoria)
    resumen_por_categoria = dataframe.groupby('categoria')['importe'].sum()
    
    # Ordenamos los valores de mayor a menor utilizando .sort_values(ascending=False)
    resumen_por_categoria = resumen_por_categoria.sort_values(ascending=False)
    
    return resumen_por_categoria


# ========================================
# PASO 5: RESUMEN POR CANAL
# ========================================
# Se define la quinta funcion obtener_resumen_por_canal

def obtener_resumen_por_canal(dataframe):
    """
    Agrupa las ventas por canal y suma el importe.
    Devuelve una serie y un diccionario de descripciones.
    """
    
    # Declaramos un diccionario que asocia: canal-descripcion (web  > 'Tienda online (web)') 
    descripcion_canales = {
        #clave1 : valor1 (clave=web, valor=tienda online(web)
        'web': 'Tienda online (web)',
        'app': 'Aplicacion movil',
        'tienda_fisica': 'Tienda fisica'
    }
    
    # Agrupar por canal y sumar, igual que en el paso 4, agrupamos por canal y sumamos la columna importe
    resumen_por_canal = dataframe.groupby('canal')['importe'].sum()
    
    # Ordenamos el resultado de mayor a menor
    resumen_por_canal = resumen_por_canal.sort_values(ascending=False)
    
    # Devolvemos dos objetos, la agrupacion por canal y la descripcion por canales
    return resumen_por_canal, descripcion_canales


# ========================================
# PASO 6: FILTRADO POR UMBRAL
# ========================================
# Definimos nuestra ultima funcion, filtrar_por_umbral, filtrará datos y devolvera 3 valores e imprimira un reporte estructurado

def filtrar_por_umbral(dataframe):
    """
    Pide un umbral de importe mínimo y filtra las ventas.
    Devuelve el umbral, cantidad de ventas y DataFrame filtrado.
    """
    
    # Pedimos un umbral al usuario, transformando su input en un float
    umbral_minimo = float(input("\n Cual es el importe minimo para filtrar? (en euros): "))
    
    # Utilizamos un condicional para validar que el umbral es positivo
    while umbral_minimo < 0:
        print("Error: El umbral debe ser positivo")
        umbral_minimo = float(input("Intentar de nuevo: "))
    
    # Filtrar: mostramos solo filas donde importe >= umbral
    ventas_filtradas = dataframe[dataframe['importe'] >= umbral_minimo]
    
    # Contamos cuantas ventas cumplen el umbral
    cantidad_ventas_filtradas = len(ventas_filtradas)
    
    # Devolvemos 3 objetos, el umbral que el usuario ha introducido, la cantidad de ventas que lo cumplen y el dataframe filtrado
    return umbral_minimo, cantidad_ventas_filtradas, ventas_filtradas


# ========================================
# PASO 7: MOSTRAR INFORME FINAL
# ========================================
# Utilizamos nuestras funciones declaradas anteriormente para realizar el calculo del informe final

def mostrar_informe(dataframe, resumen_general, resumen_por_categoria, resumen_por_canal, descripcion_canales, umbral_minimo, cantidad_ventas_filtradas):
    """
    Muestra un informe completo con todos los resultados.
    Mantiene nombres descriptivos y sin abreviaturas para mayor claridad.
    """
    
    # Igual que en la Actividad 2, utilizaremos esto para estructurar mejor visualmente nuestro codigo
    print("\n" + "=" * 50)
    print("INFORME COMPLETO DE ANALISIS DE VENTAS")
    print("=" * 50)
    
    # Generamos un resumen general, formateamos los resultados por los decimales que nos interesen, y aquellos numeros que requiramos los dejaremos como float (f)
    # Para mejor visualizacion alineamos elementos utilizando :>10.., lo cual creara 10 espacios a la derecha al valor a mostrar

    print("\nRESUMEN GENERAL")
    print("-" * 70)
    print(f"  Total de transacciones:    {resumen_general['total_ventas']:>10} ventas")
    print(f"  Total de unidades:         {resumen_general['total_unidades']:>10.0f} unidades")
    print(f"  Total en euros:            {resumen_general['total_importe']:>10.2f} EUR")
    print(f"  Importe medio por venta:   {resumen_general['importe_medio']:>10.2f} EUR")
    print(f"  Importe minimo:            {resumen_general['importe_minimo']:>10.2f} EUR")
    print(f"  Importe maximo:            {resumen_general['importe_maximo']:>10.2f} EUR")
    
    # Generamos el resumen por categoria
    print("\n RESUMEN POR CATEGORIA (de mayor a menor venta)")
    print("-" * 50)
    # Declaramos un bucle for que iterara sobre resumen_por_categoria
    for categoria, importe in resumen_por_categoria.items():
        barra = "#" * int(importe / 500)  # Barra visual, recomendada segun documentacion para mejor orden visual
        # Imprimimos la categoria y el importe con 2 decimales
        print(f"  {categoria:20} -> {importe:10.2f} EUR  {barra}")
    
    # Generamos el resumen por canal de venta
    print("\nRESUMEN POR CANAL DE VENTA")
    print("-" * 50)
    # Declaramos un bucle for para iterar sobre las series de canales, canal.items() devolverá canal_nombre y su importe
    for nombre_canal, importe in resumen_por_canal.items():
        # Por cada serie, busca su descripcion en el diccionario(web, app, tienda_fisica), lo usamos en esta sección 

        descripcion = descripcion_canales[nombre_canal]
        # Imprimimos descripcion del diccionario más el importe
        print(f"  {descripcion:30} -> {importe:10.2f} EUR")
    
    # Filtramos por umbral, por minimo establecido y ventas que cumplen el objetivo
    print("\nFILTRADO POR UMBRAL")
    print("-" * 50)
    print(f"  Umbral minimo establecido: {umbral_minimo:>10.2f} EUR")
    print(f"  Ventas que cumplen:        {cantidad_ventas_filtradas:>6} transacciones")
    
    print("\n" + "=" * 50)
    print("Fin del informe")
    print("=" * 50 + "\n")


# ========================================
# FUNCIÓN PRINCIPAL
# ========================================
# Definimos la ejecución del programa, donde llamaremos todas las funciones declaradas anteriormente para ser ejecutadas.

def main():
    """
    Función principal que ejecuta el análisis completo.
    Ejecuta todos los pasos en orden: carga, preparacion, análisis y presentación de resultados.
    """
    
    # PASO 1: Llamar a la funcion Cargar datos, lo cual nos devolvera el csv que necesitamos para usar el programa
    print("=" * 70)
    print("SISTEMA DE ANALISIS DE VENTAS - PANDAS Y NUMPY")
    print("=" * 70)
    print("\nCargando datos...")
    
    dataframe = cargar_datos()
    
    # PASO 2: Iniciamos la funcion preparar_datos, se encargara de convertir los numeros, crear la columna importe y eliminar las filas inconsistentes
    print("Preparando datos...")
    dataframe = preparar_datos(dataframe)
    
    # Obtenemos las dimensiones del dataframe y las mostramos al usuario
    filas, columnas = dataframe.shape
    print(f"Archivo cargado: {filas} filas, {columnas} columnas")
    print("\nPrimeras 3 filas del archivo:")
    print(dataframe.head(3))
    
    # PASO 3: Llamamos esta funcion para calcular totales, promedios, min y max, y devolvemos el diccionario
    print("\nCalculando resumen general...")
    resumen_general = obtener_resumen_general(dataframe)
    
    # PASO 4: Agrupamos por categoria, sumamos el importe por grupo, y ordenamos de mayor a menor
    print("Calculando resumen por categoria...")
    resumen_por_categoria = obtener_resumen_por_categoria(dataframe)
    
    # PASO 5: Ejecutamos esta funcion para obtener una agrupacion por canal, sumar el importe por canal
    print("Calculando resumen por canal...")
    resumen_por_canal, descripcion_canales = obtener_resumen_por_canal(dataframe)
    
    # PASO 6: Filtramos los datos por umbral definido
    print("Filtrando por umbral...")
    umbral_minimo, cantidad_ventas_filtradas, dataframe_filtrado = filtrar_por_umbral(dataframe)
    
    # PASO 7: Mostramos el informe final estructurado para el usuario
    mostrar_informe(dataframe, resumen_general, resumen_por_categoria, resumen_por_canal, 
                    descripcion_canales, umbral_minimo, cantidad_ventas_filtradas)
    
    # Información adicional: mostrar detalles de las ventas filtradas
    print("\nDETALLES DE LAS VENTAS FILTRADAS (primeras 10):")
    print("-" * 70)
    columnas_mostrar = ['fecha', 'producto', 'categoria', 'canal', 'unidades', 'precio_unitario', 'importe']
    print(dataframe_filtrado[columnas_mostrar].head(10).to_string())
    
    print("\nAnalisis completado correctamente.")


# ========================================
# Ejecución del programa
# ========================================

if __name__ == "__main__":
    main()
