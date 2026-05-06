# Reto_semana_02_David_Emiliano
# Reto Semana 2: Clasificador de Temperaturas 

## Programación para Ciencia de Datos
**Instituto Politécnico Nacional | ESCOM** **Semestre:** Febrero-Julio 2026  
**Alumno:** David Emiliano Rodríguez Anduiza

## Componentes del Proyecto

Este repositorio contiene una solución integral para el procesamiento de datos climáticos:

### 1. `main.py` (El Motor)
Es el script principal desarrollado en Python. Su arquitectura sigue el flujo de:
* **Lectura:** Utiliza `sys.stdin` para procesar flujos de datos de forma eficiente.
* **Procesamiento:** Convierte unidades Fahrenheit a Celsius y aplica la lógica de clasificación.
* **Salida:** Genera un CSV estandarizado a través de `stdout` con precisión de un decimal.

### 2. `entrada.txt` (Datos de Prueba)
Archivo de texto con formato CSV que sirve para validar el programa. Contiene casos reales y "casos borde" (como temperaturas extremas o errores de formato) para asegurar que el código sea robusto y no truene con datos erróneos.

### 3. `.gitignore`
Archivo de configuración que instruye a Git para ignorar archivos temporales de Python (como `__pycache__`), manteniendo el repositorio limpio y profesional.

---

## Historial de Desarrollo (Commits)
El proyecto se desarrolló siguiendo una metodología de control de versiones con commits significativos:
* **feat:** Implementación de la lógica central y conversión de temperatura.
* **fix:** Refinamiento de datos (uso de `.title()` para ciudades y limpieza de espacios).
* **docs:** Documentación técnica y guía de usuario en el README.

---

## Cómo Ejecutar el Programa

Para procesar los datos de entrada y obtener el reporte de salida, ejecuta el siguiente comando en tu terminal:

```bash

# Uso de redirección de entrada
python main.py < entrada.txt

## Descripción del Proyecto
Este programa es una herramienta de procesamiento de datos diseñada para una agencia de viajes internacional. Su función principal es leer reportes de temperaturas globales en formatos mixtos (**Celsius** y **Fahrenheit**), estandarizarlos y generar un reporte clasificado según el clima de cada ciudad.

El sistema está optimizado para trabajar con flujos de datos a través de la entrada estándar (`stdin`) y salida estándar (`stdout`).

## Especificaciones Técnicas

### 1. Conversión de Unidades
Para las temperaturas recibidas en Fahrenheit, se aplica la fórmula de conversión estándar:
$$C = \frac{(F - 32) \times 5}{9}$$

### 2. Tabla de Clasificación
El programa categoriza cada ciudad basándose en los siguientes rangos de temperatura en Celsius:

| Temperatura (°C) | Clasificación | Ejemplo |
| :--- | :--- | :--- |
| < 0 | **Congelante** | Moscú en invierno |
| 0 a 15 | **Frio** | Londres en primavera |
| 16 a 25 | **Templado** | CDMX todo el año |
| 26 a 35 | **Calido** | Miami en verano |
| > 35 | **Extremo** | Dubai en agosto |

> **Nota:** Los límites son inclusivos (ej. 15.0°C es "Frio" y 16.0°C es "Templado").

## Guía de Uso

### Requisitos Previos
* Python 3.11 o superior instalado.
* Git configurado en el sistema.

### Ejecución en Terminal
Para procesar un archivo de datos (ej. `entrada.txt`), utiliza el operador de redirección en la terminal:

**Linux / macOS / Windows (CMD):**
```bash
python main.py < entrada.txt
