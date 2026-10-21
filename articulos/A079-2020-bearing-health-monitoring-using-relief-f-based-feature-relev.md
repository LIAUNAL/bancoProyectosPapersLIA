---
id: A079
titulo: "Bearing Health Monitoring Using Relief-F-Based Feature Relevance Analysis and HMM"
tipo: articulo
temas: [T09]
cluster: "C06 Diagnóstico de fallas y sistemas de energía"
palabras_clave: [diagnóstico de rodamientos, ReliefF, modelo oculto de Markov, vibraciones, mantenimiento de motores]
fuente_resumen: abstract
anio: 2020
revista: "Applied Sciences"
doi: 10.3390/app10155170
citas_openalex: 16
fuentes: [0001330950]
---

# Bearing Health Monitoring Using Relief-F-Based Feature Relevance Analysis and HMM

**Autores:** José Alberto Hernández-Muriel, Jhon Bryan Bermeo-Ulloa, Mauricio Holguín Londoño, Andrés Marino Álvarez-Meza, Alvaro Angel Orozco  
**Revista:** Applied Sciences (2020)  
**DOI:** https://doi.org/10.3390/app10155170  
**Temas:** T09 Monitoreo industrial y sistemas de energía  
**Clúster:** C06 Diagnóstico de fallas y sistemas de energía

## Aplicación
Monitoreo de salud de rodamientos de motores eléctricos industriales a partir de vibraciones.

## Problema de investigación
La señal de vibración es dinámica y no estacionaria, y el diagnóstico de fallas y severidad es complejo.

## Propuesta o novedad
Se introduce la selección estocástica de rasgos (SFS), que combina ranking ReliefF y un modelo oculto de Markov entrenados con esquema de ventanas sobre rasgos de tiempo, frecuencia y tiempo-frecuencia.

## Resultados
Sobre una base pública, la propuesta resulta competitiva y permite interpretar los atributos relevantes.

## Conclusiones principales
SFS es una herramienta de apoyo al diagnóstico de condición de rodamientos.

## Métodos
- ReliefF
- HMM
- selección de rasgos

## Idea para trabajo futuro
Probar la SFS en datos de planta con ruido operativo y fallas combinadas.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Nowadays, bearings installed in industrial electric motors are constituted as the primary mode of a failure affecting the global energy consumption. Since industries’ energy demand has a growing tendency, interest for efficient maintenance in electric motors is decisive. Vibration signals from bearings are employed commonly as a non-invasive approach to support fault diagnosis and severity evaluation of rotating machinery. However, vibration-based diagnosis poses a challenge concerning the signal properties, e.g., highly dynamic and non-stationary. Here, we introduce a knowledge-based tool to analyze multiple health conditions in bearings. Our approach includes a stochastic feature selection method, termed Stochastic Feature Selection (SFS), highlighting and interpreting relevant multi-domain attributes (time, frequency, and time–frequency) related to the bearing faults discriminability. In particular, a relief-F-based ranking and a Hidden Markov Model are trained under a windowing scheme to achieve our SFS. Obtained results in a public database demonstrate that our proposal is competitive compared to state-of-the-art algorithms concerning both the number of features selected and the classification accuracy.

</details>
