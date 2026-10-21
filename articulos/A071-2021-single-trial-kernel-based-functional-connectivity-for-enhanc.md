---
id: A071
titulo: "Single-Trial Kernel-Based Functional Connectivity for Enhanced Feature Extraction in Motor-Related Tasks"
tipo: articulo
temas: [T02, T01, T05]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [conectividad funcional, EEG de ensayo único, imaginación motora, ejecución motora, kernel gaussiano, selección esparsa]
fuente_resumen: abstract
anio: 2021
revista: "Sensors"
doi: 10.3390/s21082750
citas_openalex: 16
fuentes: [0000043222, 0001330950]
---

# Single-Trial Kernel-Based Functional Connectivity for Enhanced Feature Extraction in Motor-Related Tasks

**Autores:** Daniel Guillermo García-Murillo, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Sensors (2021)  
**DOI:** https://doi.org/10.3390/s21082750  
**Temas:** T02 Conectividad cerebral e imagen de fuentes neuronales; T01 Interfaces cerebro-computador y decodificación EEG; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Extracción de rasgos de conectividad funcional EEG ensayo a ensayo en tareas motoras (imaginación y ejecución).

## Problema de investigación
La variabilidad entre e intra sujetos dificulta cuantificar los cambios de conectividad asociados al aprendizaje motor.

## Propuesta o novedad
Se propone una medida de conectividad funcional basada en la distribución espectral cruzada con kernel gaussiano, con pesos espectrales optimizados mediante selección de rasgos esparsa con norma l2 alineada a las etiquetas motoras.

## Resultados
En tres bases de datos de imaginación y ejecución motora, la medida logra desempeños de clasificación muy competitivos.

## Conclusiones principales
La conectividad gaussiana por ensayo es útil para extracción de rasgos en tareas motoras.

## Métodos
- distribución espectral cruzada con kernel
- selección de rasgos esparsa
- conectividad funcional

## Idea para trabajo futuro
Evaluar la medida en BCI en línea con retroalimentación para seguir cambios de conectividad por aprendizaje.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Motor learning is associated with functional brain plasticity, involving specific functional connectivity changes in the neural networks. However, the degree of learning new motor skills varies among individuals, which is mainly due to the between-subject variability in brain structure and function captured by electroencephalographic (EEG) recordings. Here, we propose a kernel-based functional connectivity measure to deal with inter/intra-subject variability in motor-related tasks. To this end, from spatio-temporal-frequency patterns, we extract the functional connectivity between EEG channels through their Gaussian kernel cross-spectral distribution. Further, we optimize the spectral combination weights within a sparse-based ℓ2-norm feature selection framework matching the motor-related labels that perform the dimensionality reduction of the extracted connectivity features. From the validation results in three databases with motor imagery and motor execution tasks, we conclude that the single-trial Gaussian functional connectivity measure provides very competitive classifier performance values, being less affected by feature extraction parameters, like the sliding time window, and avoiding the use of prior linear spatial filtering. We also provide interpretability for the clustered functional connectivity patterns and hypothesize that the proposed kernel-based metric is promising for evaluating motor skills.

</details>
