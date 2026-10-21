---
id: P012
titulo: "Procesamiento de señales de EEG en BCI orientado a la detección de IM utilizando modelos de aprendizaje profundo y medidas de conectividad"
tipo: proyecto
temas: [T01, T07, T02]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [BCI, imaginación motora, EEG, conectividad, redes convolucionales, Monte Carlo dropout]
fuente_resumen: resumen
inicio: 2021
fin: 2021
codigo_hermes: 53223
quipu: 206010033325
estado_hermes: Finalizado
origen: CvLAC
tipo_proyecto: Investigación y desarrollo
---

# Procesamiento de señales de EEG en BCI orientado a la detección de IM utilizando modelos de aprendizaje profundo y medidas de conectividad

**Periodo:** 2021–2021  
**Código Hermes:** 53223 · QUIPU 206010033325  
**Convocatoria (Hermes):** CONVOCATORIA PARA EL APOYO A ESTUDIANTES DE POSGRADO DE LA FACULTAD DE INGENIERÍA Y ARQUITECTURA DE LA UNIVERSIDAD NACIONAL DE COLOMBIA SEDE MANIZALES MEDIANTE EL OTORGAMIENTO DE BECA - PASANTÍA 2021  
**Estado en Hermes:** Finalizado  
**Financiador:** No reportado en CvLAC  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T07 Aprendizaje profundo y explicabilidad; T02 Conectividad cerebral e imagen de fuentes neuronales  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Detección de imaginación motora en sistemas BCI basados en EEG.

## Problema de investigación
La interacción de señales EEG en BCI enfrenta sobreajuste por pocas muestras y bajo desempeño en sujetos con baja precisión.

## Propuesta o novedad
Representar el EEG en topogramas de tiempo, frecuencia y espacio basados en medidas de conectividad (coherencia, transferencia de entropía, entre otras), usarlos como entrada de una red convolucional profunda y regularizar con Monte Carlo dropout.

## Resultados
Se busca mejorar la precisión en todos los sujetos, en especial los de bajo rendimiento, usando bases de datos públicas. No se reportan cifras.

## Conclusiones principales
La combinación de conectividad y regularización se plantea como estrategia frente a la escasez de muestras.

## Productos tecnológicos principales
- Esquema de representación de topogramas de conectividad
- Modelo de red convolucional profunda con Monte Carlo dropout

## Estrategia de apropiación social
No reportada en CvLAC

## Aliados
- No reportados en CvLAC (verificar en Hermes)

## Idea para trabajo futuro
Evaluar la generalización entre sujetos y sesiones con datos propios y en tiempo real.

## Relacionados (similitud semántica)
- produjo: [[A069-2021-deep-neural-regression-prediction-of-motor-imagery-skills-us]] — Deep Neural Regression Prediction of Motor Imagery Skills Using EEG Functional Connectivity Indicators
- produjo: [[A066-2021-regularized-chained-deep-neural-network-classifier-for-multi]] — Regularized chained deep neural network classifier for multiple annotators
- produjo: [[A058-2022-subject-dependent-artifact-removal-for-enhancing-motor-image]] — Subject-dependent artifact removal for enhancing motor imagery classifier performance under poor skills
- produjo: [[A049-2023-posthoc-interpretability-of-neural-responses-by-grouping-sub]] — Posthoc Interpretability of Neural Responses by Grouping Subject Motor Imagery Skills Using CNN-Based Connectivity

<details><summary>Resumen original (CvLAC)</summary>

La propuesta para afrontar los desafíos de la interacción de señales de EEG en sistemas BCI es realizar un esquema de trabajo para el procesamiento de señales orientadas a la detección de IM, basadas en conectividades (coherencia (COH), leucomalacia periventricular (LPV)[8], Redes de funciones de base radial (RNA), y Transferencia de entropia(TE)) para realizar un esquema de representación de topogramas de tiempo, frecuencia y espacio [1], esta representación sería la entrada de una red convolucional profunda, para prevenir el sobre ajuste de la red generado por la poca cantidad de muestras [1] usando como referente bases de datos públicas,mejorando la precisión de todos los sujetos y añadiendo la regularización con estrategias de Monte carlo y capas de deserción (MCD) para mejorar la precisión concentrándose principalmente en los sujetos con bajo rendimiento [1].

</details>
