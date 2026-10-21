---
id: A109
titulo: "Time Series Prediction for Kernel-based Adaptive Filters Using Variable Bandwidth, Adaptive Learning-rate, and Dimensionality Reduction"
tipo: articulo
temas: [T05]
cluster: "C10 Visión por computador y representación kernel"
palabras_clave: [filtros adaptativos kernel, correntropía, ancho de banda, tasa de aprendizaje, esparsificación, predicción de series]
fuente_resumen: abstract
anio: 2019
revista: "IEEE International Conference on Acoustics Speech and Signal Processing"
doi: 10.1109/ICASSP.2019.8683117.
citas_openalex: 0
fuentes: [0000043222]
---

# Time Series Prediction for Kernel-based Adaptive Filters Using Variable Bandwidth, Adaptive Learning-rate, and Dimensionality Reduction

**Autores:** Sergio García-Vega, Eder Arley Leon-Gomez, German Castellanos-Dominguez  
**Revista:** IEEE International Conference on Acoustics Speech and Signal Processing (2019)  
**DOI:** https://doi.org/10.1109/ICASSP.2019.8683117.  
**Temas:** T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C10 Visión por computador y representación kernel

## Aplicación
Predicción de series de tiempo con filtros adaptativos basados en kernel.

## Problema de investigación
Los filtros adaptativos en espacios de Hilbert con kernel reproductor son sensibles a la selección del ancho de banda y la tasa de aprendizaje, y su costo crece con el número de muestras.

## Propuesta o novedad
Se propone un marco que optimiza secuencialmente el ancho de banda del kernel y la tasa de aprendizaje mediante gradiente estocástico que maximiza la correntropía, e incorpora una esparsificación basada en reducción de dimensión para eliminar muestras redundantes.

## Resultados
La validación con datos sintéticos y reales indica que la propuesta converge a valores relativamente bajos de error cuadrático medio y ofrece soluciones estables en aplicaciones reales.

## Conclusiones principales
El ajuste automático de parámetros y la esparsificación hacen más práctico el filtrado adaptativo con kernel.

## Métodos
- filtros adaptativos kernel
- correntropía
- gradiente estocástico
- reducción de dimensión

## Idea para trabajo futuro
Extender el marco a entornos con deriva de concepto y evaluarlo frente a criterios de esparsificación de diccionario en tiempo real.

## Relacionados (similitud semántica)
- extendido por: [[A084-2020-a-time-series-prediction-framework-using-sequential-learning]] — A time-series prediction framework using sequential learning algorithms and dimensionality reduction within a sparsification approach

<details><summary>Abstract</summary>

Kernel-based adaptive filters are sequential learning algorithms, operating on reproducing kernel Hilbert spaces. Their learning performance is susceptible to the selection of appropriate values for kernel bandwidth and learning-rate parameters. Additionally, as these algorithms train the model using a sequence of input vectors, their computation scales with the number of samples. We propose a framework that addresses the previous open challenges of kernel-based adaptive filters. In contrast to similar methods, our proposal sequentially optimizes the bandwidth and learning-rate parameters using stochastic gradient algorithms that maximize the correntropy function. To remove redundant samples, a sparsification approach based on dimensionality reduction is introduced. The framework is validated on both synthetic and real-world data sets. Results show that our proposal converges to relatively low values of mean-square-error while provides stable solutions in real-world applications.

</details>
