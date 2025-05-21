def convertir(temp, tipo):
    if tipo == "C":
        return (temp * 9/5) + 32, temp + 273.15
    elif tipo == "F":
        c = (temp - 32) * 5/9
        return c, c + 273.15
    elif tipo == "K":
        c = temp - 273.15
        return c, (c * 9/5) + 32
    else:
        return None, None

def main():
    print("Conversor de temperaturas")
    print("Ingresa la unidad origen: C, F o K")
    unidad = input("Unidad: ").upper()
    try:
        valor = float(input("Valor: "))
        res1, res2 = convertir(valor, unidad)
        if res1 is None:
            print("Unidad no válida.")
        else:
            print(f"Temperaturas equivalentes: {res1:.2f}, {res2:.2f}")
    except:
        print("Error al leer datos.")

main()

