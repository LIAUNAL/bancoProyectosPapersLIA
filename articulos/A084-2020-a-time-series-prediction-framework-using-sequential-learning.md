---
id: A084
titulo: "A time-series prediction framework using sequential learning algorithms and dimensionality reduction within a sparsification approach"
tipo: articulo
temas: [T05, T13]
cluster: "C10 Visión por computador y representación kernel"
palabras_clave: [series de tiempo, filtros adaptativos de kernel, correntropía, esparsificación, tasa de aprendizaje]
fuente_resumen: abstract
anio: 2020
revista: "Pattern Recognition Letters"
doi: 10.1016/j.patrec.2019.11.031
citas_openalex: 1
fuentes: [0000043222]
---

# A time-series prediction framework using sequential learning algorithms and dimensionality reduction within a sparsification approach

**Autores:** Sergio García-Vega, Eder Arley Leon-Gomez, German Castellanos-Dominguez  
**Revista:** Pattern Recognition Letters (2020)  
**DOI:** https://doi.org/10.1016/j.patrec.2019.11.031  
**Temas:** T05 Métodos kernel y aprendizaje basado en teoría de la información; T13 Representación de datos, reducción de dimensión y agrupamiento  
**Clúster:** C10 Visión por computador y representación kernel

## Aplicación
Predicción de series de tiempo con filtros adaptativos de kernel.

## Problema de investigación
El desempeño depende del ancho de banda y la tasa de aprendizaje, y el costo crece con el número de muestras.

## Propuesta o novedad
Se propone maximizar la función de correntropía para optimizar ancho de banda y tasa de aprendizaje, junto con esparsificación por reducción de dimensión para remover muestras redundantes.

## Resultados
En datos sintéticos y reales se observa convergencia a bajos valores de error cuadrático medio.

## Conclusiones principales
El marco automatiza hiperparámetros y reduce el costo computacional.

## Métodos
- correntropía
- filtros adaptativos de kernel
- reducción de dimensión

## Idea para trabajo futuro
Aplicar el marco a pronóstico de series no estacionarias en energía con deriva de concepto.

## Relacionados (similitud semántica)
- extiende: [[A109-2019-time-series-prediction-for-kernel-based-adaptive-filters-usi]] — Time Series Prediction for Kernel-based Adaptive Filters Using Variable Bandwidth, Adaptive Learning-rate, and Dimensionality Reduction

<details><summary>Abstract</summary>

Abstract The adaptive kernel filters are sequential learning algorithms that operate in a particular functional space called a reproducing kernel Hilbert space. However, their performance depends on the selection of two hyper-parameters, i.e., kernel bandwidth and learning-rate. Besides, as these algorithms train the model using a sequence of input vectors, their computation scales with the number of samples. In this work, we propose to address the previous challenges of these sequential learning algorithms. The proposed framework, unlike similar methods, maximizes the correntropy function to optimize the bandwidth and learning-rate parameters. Further, we introduce a sparsification strategy based on dimensionality reduction to remove redundant samples. The framework is tested on both synthetic and real-world data sets, showing convergence to relatively low values of mean-square-error.

</details>
