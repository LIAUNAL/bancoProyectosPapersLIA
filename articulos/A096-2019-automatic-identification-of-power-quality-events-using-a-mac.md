---
id: A096
titulo: "Automatic identification of power quality events using a machine learning approach"
tipo: articulo
temas: [T09]
cluster: "C06 Diagnóstico de fallas y sistemas de energía"
palabras_clave: [calidad de potencia, clasificación de perturbaciones, rasgos tiempo-frecuencia, ReliefF, IEEE 1159, robustez al ruido]
fuente_resumen: abstract
anio: 2019
revista: "Scientia et technica"
doi: 10.22517/23447214.20661
citas_openalex: 4
fuentes: [0001330950]
---

# Automatic identification of power quality events using a machine learning approach

**Autores:** Andrés Felipe Valencia-Duque, Andrés Marino Álvarez-Meza, Alvaro Angel Orozco  
**Revista:** Scientia et technica (2019)  
**DOI:** https://doi.org/10.22517/23447214.20661  
**Temas:** T09 Monitoreo industrial y sistemas de energía  
**Clúster:** C06 Diagnóstico de fallas y sistemas de energía

## Aplicación
Identificación de eventos de calidad de potencia (PQ) en sistemas eléctricos industriales.

## Problema de investigación
Es necesario clasificar rápido y con precisión las perturbaciones para reducir costos y pérdidas.

## Propuesta o novedad
Se propone aprendizaje de máquina con rasgos de tiempo y frecuencia, relevancia supervisada con ReliefF y evaluación de clasificadores bajo ruido con validación cruzada de 10 particiones sobre una base sintética según IEEE 1159.

## Resultados
Se evalúa la clasificación de eventos con distintos clasificadores y niveles de ruido sobre datos sintéticos.

## Conclusiones principales
El esquema con ReliefF es robusto para identificar eventos PQ.

## Métodos
- ReliefF
- validación cruzada
- clasificadores supervisados

## Idea para trabajo futuro
Validar con registros reales de redes eléctricas y eventos compuestos.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Actualmente, los eventos de calidad de potencia (PQ) se han estudiado dado su importancia para las industrias, en cuanto a la eficiencia y la vida útil de los elementos conectados a los sistemas eléctricos. Si las perturbaciones relacionadas con los eventos de PQ se clasifican (identifican) rápidamente y con una precisión confiable, los costos y las pérdidas generadas se reducirían. En este trabajo presentamos un enfoque basado en aprendizaje de máquina para la identificación automática de eventos PQ. Nuestra propuesta comprende las siguientes etapas: empleamos un espacio de representación de características basado en parámetros de tiempo y frecuencia. Además, utilizamos una técnica de análisis de relevancia supervisada, llamada Relieff, para resaltar la capacidad discriminante de las características consideradas. Luego, evaluamos el éxito de la clasificación de eventos PQ con diferentes clasificadores agregando diferentes niveles de ruido bajo un esquema de validación cruzada de 10 particiones. En este sentido, se genera una base de datos sintética basada en el estándar IEEE 1159, considerando 3000 señales y diez clases (300 muestras por clase). Los resultados obtenidos muestran un rendimiento de clasificación adecuado con clasificadores simples, cuadrático y k-NN, en comparación con las metodologías más avanzadas del estado del arte.

</details>
