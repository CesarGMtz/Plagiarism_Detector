import string
import random

def construir_contraseña(tamaño):
    elementos = list(string.ascii_letters + string.digits + string.punctuation)
    contraseña = ""
    for _ in range(tamaño):
        contraseña += random.choice(elementos)
    return contraseña

def comprobar_unicidad(lista, nueva):
    return nueva not in lista

def generar_contraseñas_unicas(cantidad, tamaño):
    resultado = []
    while len(resultado) < cantidad:
        temp = construir_contraseña(tamaño)
        if comprobar_unicidad(resultado, temp):
            resultado.append(temp)
    return resultado

def main():
    n = int(input("¿Número de contraseñas únicas? "))
    contraseñas = generar_contraseñas_unicas(n, 12)
    for i in range(len(contraseñas)):
        print(f"{i+1}) {contraseñas[i]}")

main()

