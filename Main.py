import sys

def fahrenheit_a_celsius(f):
    """Convierte Fahrenheit a Celsius."""
    return (f - 32) * 5 / 9

def clasificar(celsius):
    """Clasifica la temperatura según los rangos del IPN."""
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

def main():
    # 1. Imprimir encabezado de salida obligatorio
    print("ciudad,temperatura_celsius,clasificacion")
    
    # 2. Procesar línea por línea desde stdin
    primera_linea = True
    for linea in sys.stdin:
        linea = linea.strip()
        
        # Saltar encabezado de entrada y líneas vacías
        if primera_linea:
            primera_linea = False
            continue
        if not linea:
            continue
        
        # 3. Separar y validar columnas
        partes = linea.split(',')
        if len(partes) != 3:
            continue
            
        ciudad = partes[0].strip()
        temp_str = partes[1].strip()
        unidad = partes[2].strip().upper() # Maneja 'c' o 'C'
        
        # 4. Validar tipos de datos
        if unidad not in ['C', 'F']:
            continue
        try:
            valor_temp = float(temp_str)
        except ValueError:
            continue
            
        # 5. Lógica de conversión
        if unidad == 'F':
            celsius = fahrenheit_a_celsius(valor_temp)
        else:
            celsius = valor_temp
            
        # 6. Clasificar e imprimir con 1 decimal
        resultado_clase = clasificar(celsius)
        print(f"{ciudad},{celsius:.1f},{resultado_clase}")

if __name__ == "__main__":
    main()