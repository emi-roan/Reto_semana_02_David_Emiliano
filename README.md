# Reto Semana 2: Clasificador de Temperaturas 

## Programación para Ciencia de Datos
**Instituto Politécnico Nacional | ESCOM** **Semestre:** Febrero-Julio 2026  
**Alumno:** David Emiliano Rodríguez Anduiza

## Descripción del Proyecto
Este proyecto implementa un **pipeline de datos (ETL)** robusto diseñado para procesar información climática de diversas ciudades. El programa lee datos desde la entrada estándar (`stdin`), normaliza las temperaturas a grados Celsius y clasifica el clima según rangos térmicos predefinidos.

## Especificaciones de Transformación
Para asegurar la integridad de la salida, el programa aplica las siguientes reglas de negocio:

1.  **Conversión de Unidades**: Si la entrada está en Fahrenheit, se aplica la fórmula $$C = (F - 32) \cdot \frac{5}{9}$$
2.  **Categorización**:
    * **Congelante**: < 0°C
    * **Frio**: 0°C a 15°C
    * **Templado**: 16°C a 25°C
    * **Calido**: 26°C a 35°C
    * **Extremo**: > 35°C
3.  **Robustez**: El programa omite automáticamente líneas con formatos incorrectos, unidades no reconocidas o valores no numéricos.
4.  **Formato de Salida**: CSV con precisión de un decimal en la temperatura procesada.

## Estructura del Repositorio
* `main.py`: Lógica principal de procesamiento y transformación.
* `README.md`: Documentación del reto.
* `entrada.csv`: (Opcional) Archivo de prueba con datos térmicos.

## Instrucciones de Uso

### Ejecución en Consola
El programa está diseñado para trabajar con redirección de entrada en sistemas Unix (Linux/Mac) y Windows:

```bash
# Ejecución estándar
python main.py < datos_clima.csv

# Guardar resultados en un archivo nuevo
python main.py < datos_clima.csv > resultados_clasificados.csv


Entrada:

Fragmento de código
ciudad,temperatura,unidad
CDMX,22,C
New York,45,F
Toronto,-5,C

Salida:

Fragmento de código
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
New York,7.2,Frio
Toronto,-5.0,Congelante
