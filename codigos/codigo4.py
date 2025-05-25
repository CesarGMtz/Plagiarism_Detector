import statistics

entrada = input("Introduce números separados por coma: ")

numeros = []
for valor in entrada.split(","):
    try:
        numeros.append(float(valor.strip()))
    except:
        print(f"'{valor}' no es válido y se omitirá.")

if numeros:
    media = sum(numeros) / len(numeros)
    mediana = statistics.median(numeros)
    try:
        moda = statistics.mode(numeros)
    except:
        moda = "No definida (varios valores con misma frecuencia)"
    desviacion = statistics.stdev(numeros) if len(numeros) > 1 else 0.0

    print("=== Estadísticas ===")
    print("Números:", numeros)
    print("Promedio:", media)
    print("Mediana:", mediana)
    print("Moda:", moda)
    print("Desviación estándar:", desviacion)
else:
    print("No se ingresaron números válidos.")

