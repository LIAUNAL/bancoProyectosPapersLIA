---
id: A118
titulo: "Enhanced Data Covariance Estimation Using Weighted Combination of multiple Gaussian Kernels for Improved M/EEG Source Localization."
tipo: articulo
temas: [T02, T05]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [covarianza, kernels gaussianos múltiples, divergencia de Kullback-Leibler, M/EEG, localización de fuentes, datos no gaussianos]
fuente_resumen: abstract
anio: 2019
revista: "International Journal of Neural Systems"
doi: 10.1142/S0129065719500011
citas_openalex: 11
fuentes: [0000043222]
---

# Enhanced Data Covariance Estimation Using Weighted Combination of multiple Gaussian Kernels for Improved M/EEG Source Localization.

**Autores:** Juan David Martinez-Vargas, Leonardo Duque‐Muñoz, J. F. Vargas‐Bonilla, José David López, German Castellanos-Dominguez  
**Revista:** International Journal of Neural Systems (2019)  
**DOI:** https://doi.org/10.1142/S0129065719500011  
**Temas:** T02 Conectividad cerebral e imagen de fuentes neuronales; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Localización de fuentes en M/EEG con datos no gaussianos y no estacionarios.

## Problema de investigación
La estructura no gaussiana y no estacionaria de los datos M/EEG complica la estimación de covarianza para localizar fuentes.

## Propuesta o novedad
Se introduce WM-MK, una estimación de covarianza que combina ponderadamente múltiples kernels gaussianos, donde el peso de cada kernel se asocia a su relevancia mediante la divergencia de Kullback-Leibler.

## Resultados
En datos simulados y reales no estacionarios y no gaussianos, WM-MK incrementa la precisión de la estimación de fuentes al explotar estructuras no lineales.

## Conclusiones principales
La covarianza multikernel ponderada mejora la localización de fuentes.

## Métodos
- múltiples kernels gaussianos
- divergencia KL
- beamformer

## Idea para trabajo futuro
Estudiar la selección automática del conjunto de kernels y su efecto en la resolución temporal.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

In the recent past, estimating brain activity with magneto/electroencephalography (M/EEG) has been increasingly employed as a noninvasive technique for understanding the brain functions and neural dynamics. However, one of the main open problems when dealing with M/EEG data is its non-Gaussian and nonstationary structure. In this paper, we introduce a methodology for enhancing the data covariance estimation using a weighted combination of multiple Gaussian kernels, termed WM-MK, that relies on the Kullback-Leibler divergence for associating each kernel weight to its relevance. From the obtained results of validation on nonstationary and non-Gaussian brain activity (simulated and real-world EEG data), WM-MK proves that the accuracy of the source estimation raises by more effectively exploiting the measured nonlinear structures with high time and space complexity.

</details>
