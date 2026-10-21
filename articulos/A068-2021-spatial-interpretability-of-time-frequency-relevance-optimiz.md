---
id: A068
titulo: "Spatial interpretability of time-frequency relevance optimized in motor imagery discrimination using Deep&Wide networks"
tipo: articulo
temas: [T01, T07]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, tiempo-frecuencia, wavelet continua, patrones espaciales comunes, interpretabilidad, relevancia de rasgos]
fuente_resumen: abstract
anio: 2021
revista: "Biomedical Signal Processing and Control"
doi: 10.1016/j.bspc.2021.102626
citas_openalex: 5
fuentes: [0000043222, 0001330950]
---

# Spatial interpretability of time-frequency relevance optimized in motor imagery discrimination using Deep&Wide networks

**Autores:** Diego Fabián Collazos-Huertas, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Biomedical Signal Processing and Control (2021)  
**DOI:** https://doi.org/10.1016/j.bspc.2021.102626  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Interpretación espacial y tiempo-frecuencia de clasificadores de imaginación motora para diagnóstico y monitoreo.

## Problema de investigación
Las CNN mejoran la clasificación MI pero son poco interpretables, y la variabilidad entre sujetos complica el análisis.

## Propuesta o novedad
Se extrae una representación 2D combinando transformada wavelet continua y patrones espaciales comunes, que alimenta un modelo Deep&Wide; se estima la relevancia de la entrada multivista mediante retropropagación de información sobre los pesos de capas ocultas.

## Resultados
El análisis de relevancia conserva un desempeño de clasificación adecuado y revela contribuciones espaciales y de tiempo-frecuencia.

## Conclusiones principales
La relevancia topográfica tiempo-frecuencia mejora la comprensión de las acciones imaginadas.

## Métodos
- CWT
- CSP
- Deep&Wide
- análisis de relevancia

## Idea para trabajo futuro
Validar la relevancia aprendida frente a mediciones neurofisiológicas independientes, por ejemplo fMRI.

## Relacionados (similitud semántica)
- extiende: [[A075-2020-cnn-based-framework-using-spatial-dropping-for-enhanced-inte]] — CNN-based framework using spatial dropping for enhanced interpretation of neural activity in motor imagery classification

<details><summary>Abstract</summary>

Abstract Medical diagnosis and monitoring benefit from exploiting the advantages of motor imagery (MI) training, which highly depends on the proper interpretation of elicited brain activity responses. Convolutional neural networks (CNN) are increasingly used to improve MI classification performance by employing multi-view extracted features (time, frequency, and spatial). However, deep learning gains knowledge from abundant, complex neural models, resulting in poor interpretability assessments. Here, to enhance the understanding of imagined actions, we develop the relevance analysis of topographic time-frequency representation, preserving an adequate classification performance. Namely, to deal better with the subject variability, a 2D feature combination of continuous wavelet transform and common spatial patterns is extracted to feed a Deep&Wide learning model, assessing the relevance of input multi-view representation that contribute the best to the classifier accuracy. We estimate the feature contribution through the information back-propagated across the hidden layers’ weights before predicting the output label. Evaluation, presented in two databases with bi- and four-label MI tasks, proves that the developed Deep&Wide-based relevance analysis reveals insights about the electrodes, time segments, and frequency bands with relevant MI neural responses, favoring explanation of inter and intra-subject variability because of coordination skills.

</details>
