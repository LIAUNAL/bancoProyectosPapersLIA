---
id: A075
titulo: "CNN-based framework using spatial dropping for enhanced interpretation of neural activity in motor imagery classification"
tipo: articulo
temas: [T01, T07]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, EEG, redes convolucionales, descarte espacial, wavelet continua, interpretabilidad]
fuente_resumen: abstract
anio: 2020
revista: "Brain Informatics"
doi: 10.1186/s40708-020-00110-4
citas_openalex: 27
fuentes: [0000043222, 0001330950]
---

# CNN-based framework using spatial dropping for enhanced interpretation of neural activity in motor imagery classification

**Autores:** Diego Fabián Collazos-Huertas, Andrés Marino Álvarez-Meza, Carlos Daniel Acosta-Medina, G. A. Castaño-Duque, German Castellanos-Dominguez  
**Revista:** Brain Informatics (2020)  
**DOI:** https://doi.org/10.1186/s40708-020-00110-4  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Clasificación de imaginación motora en EEG con interpretación de patrones neuronales espaciales.

## Problema de investigación
La variabilidad intra e inter sujeto dificulta la identificación de acciones imaginadas y su interpretación.

## Propuesta o novedad
Se desarrolla una CNN con proyección topográfica de EEG y un algoritmo de descarte espacial (spatial dropping) que elimina pesos asociados a zonas no involucradas; se contrastan PSD y CWT como rasgos 2D.

## Resultados
En escenarios bi-clase y tres-clase, la combinación de umbralización con CWT mejora la exactitud y la interpretabilidad.

## Conclusiones principales
El descarte espacial mejora la lectura de las áreas cerebrales relevantes.

## Métodos
- CNN
- CWT
- PSD
- spatial dropping

## Idea para trabajo futuro
Extender el descarte espacial a arquitecturas con atención para interpretar dinámica temporal además de espacial.

## Relacionados (similitud semántica)
- extendido por: [[A068-2021-spatial-interpretability-of-time-frequency-relevance-optimiz]] — Spatial interpretability of time-frequency relevance optimized in motor imagery discrimination using Deep&Wide networks

<details><summary>Abstract</summary>

Interpretation of brain activity responses using motor imagery (MI) paradigms is vital for medical diagnosis and monitoring. Assessed by machine learning techniques, identification of imagined actions is hindered by substantial intra- and inter-subject variability. Here, we develop an architecture of Convolutional Neural Networks (CNN) with an enhanced interpretation of the spatial brain neural patterns that mainly contribute to the classification of MI tasks. Two methods of 2D-feature extraction from EEG data are contrasted: Power Spectral Density and Continuous Wavelet Transform. For preserving the spatial interpretation of extracting EEG patterns, we project the multi-channel data using a topographic interpolation. Besides, we include a spatial dropping algorithm to remove the learned weights that reflect the localities not engaged with the elicited brain response. We evaluate two labeled scenarios of MI tasks: bi-class and three-class. Obtained results in an MI database show that the thresholding strategy combined with Continuous Wavelet Transform improves the accuracy and enhances the interpretability of CNN architecture, showing that the highest contribution clusters over the sensorimotor cortex with a differentiated behavior of rhythms [Formula: see text] and [Formula: see text].

</details>
