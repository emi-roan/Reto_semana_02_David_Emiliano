import sys

def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

def clasificar_temperatura(celsius):
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"

def procesar_linea(linea):
    partes = [p.strip() for p in linea.strip().split(",")]

    if len(partes) != 3:
        return None

    ciudad, temp_str, unidad = partes
    unidad = unidad.upper()

    if not ciudad:
        return None

    if unidad not in ("C", "F"):
        return None

    try:
        temperatura = float(temp_str)
    except ValueError:
        return None

    if unidad == "F":
        celsius = fahrenheit_a_celsius(temperatura)
    else:
        celsius = temperatura

    clasificacion = clasificar_temperatura(celsius)

    return ciudad, celsius, clasificacion

def main():
    print("ciudad,temperatura_celsius,clasificacion")

    primera_linea = True

    for linea in sys.stdin:
        if not linea.strip():
            continue

        if primera_linea:
            primera_linea = False

            if "ciudad" in linea.lower():
                continue

        resultado = procesar_linea(linea)

        if resultado is not None:
            ciudad, celsius, clasificacion = resultado
            print(f"{ciudad},{celsius:.1f},{clasificacion}")

if __name__ == "__main__":
    main()
