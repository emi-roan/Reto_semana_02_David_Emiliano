# Reto_semana_02_David_Emiliano
# Reto Semana 2: Clasificador de Temperaturas 🌍

## Programación para Ciencia de Datos
**Instituto Politécnico Nacional | ESCOM** **Semestre:** Febrero-Julio 2026  
**Alumno:** David Emiliano Rodríguez Anduiza

---

## 📝 Descripción del Proyecto
Este programa es una herramienta de procesamiento de datos diseñada para una agencia de viajes internacional. Su función principal es leer reportes de temperaturas globales en formatos mixtos (**Celsius** y **Fahrenheit**), estandarizarlos y generar un reporte clasificado según el clima de cada ciudad.

El sistema está optimizado para trabajar con flujos de datos a través de la entrada estándar (`stdin`) y salida estándar (`stdout`).

## 🛠️ Especificaciones Técnicas

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

## 🚀 Guía de Uso

### Requisitos Previos
* Python 3.11 o superior instalado.
* Git configurado en el sistema.

### Ejecución en Terminal
Para procesar un archivo de datos (ej. `entrada.txt`), utiliza el operador de redirección en la terminal:

**Linux / macOS / Windows (CMD):**
```bash
python main.py < entrada.txt