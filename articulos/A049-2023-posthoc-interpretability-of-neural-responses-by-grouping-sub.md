---
id: A049
titulo: "Posthoc Interpretability of Neural Responses by Grouping Subject Motor Imagery Skills Using CNN-Based Connectivity"
tipo: articulo
temas: [T01, T02, T07]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, BCI, conectividad funcional, mapas de activación, explicación post hoc, ineficiencia BCI]
fuente_resumen: abstract
anio: 2023
revista: "Sensors"
doi: 10.3390/s23052750
citas_openalex: 7
fuentes: [0000043222, 0001330950]
---

# Posthoc Interpretability of Neural Responses by Grouping Subject Motor Imagery Skills Using CNN-Based Connectivity

**Autores:** Diego Fabián Collazos-Huertas, Andrés Marino Álvarez-Meza, David  Augusto Cardenas Peña, Germán Albeiro Castaño Duque, German Castellanos-Dominguez  
**Revista:** Sensors (2023)  
**DOI:** https://doi.org/10.3390/s23052750  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T02 Conectividad cerebral e imagen de fuentes neuronales; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Identificación temprana de usuarios con bajo desempeño en BCI de imaginación motora.

## Problema de investigación
Un tercio de las personas carece de la habilidad para realizar MI con precisión; la decodificación está limitada por la no estacionariedad y la baja resolución espacial.

## Propuesta o novedad
Un marco CNN que extrae conectividad funcional de mapas de activación de clase mediante un nuevo estimador de distribución espectral cruzada basado en kernels, y agrupa a los sujetos según su exactitud para hallar patrones comunes.

## Resultados
En una base bi-clase, la exactitud promedio mejora 10% frente a EEGNet y los sujetos de bajo desempeño bajan de 40% a 20%.

## Conclusiones principales
El método explica las respuestas neuronales incluso en sujetos con habilidades MI deficientes.

## Métodos
- CNN
- CAM
- estimador espectral cruzado kernel
- clustering de sujetos

## Idea para trabajo futuro
Predecir en las primeras sesiones el grupo de habilidad del usuario para personalizar el entrenamiento.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P012-2021-procesamiento-de-senales-de-eeg-en-bci-orientado-a-la-detecc]] — Procesamiento de señales de EEG en BCI orientado a la detección de IM utilizando modelos de aprendizaje profundo y medidas de conectividad
- extendido por: [[A021-2025-gaussian-connectivity-driven-eeg-imaging-for-deep-learning-b]] — Gaussian Connectivity-Driven EEG Imaging for Deep Learning-Based Motor Imagery Classification

<details><summary>Abstract</summary>

Motor Imagery (MI) refers to imagining the mental representation of motor movements without overt motor activity, enhancing physical action execution and neural plasticity with potential applications in medical and professional fields like rehabilitation and education. Currently, the most promising approach for implementing the MI paradigm is the Brain-Computer Interface (BCI), which uses Electroencephalogram (EEG) sensors to detect brain activity. However, MI-BCI control depends on a synergy between user skills and EEG signal analysis. Thus, decoding brain neural responses recorded by scalp electrodes poses still challenging due to substantial limitations, such as non-stationarity and poor spatial resolution. Also, an estimated third of people need more skills to accurately perform MI tasks, leading to underperforming MI-BCI systems. As a strategy to deal with BCI-Inefficiency, this study identifies subjects with poor motor performance at the early stages of BCI training by assessing and interpreting the neural responses elicited by MI across the evaluated subject set. Using connectivity features extracted from class activation maps, we propose a Convolutional Neural Network-based framework for learning relevant information from high-dimensional dynamical data to distinguish between MI tasks while preserving the post-hoc interpretability of neural responses. Two approaches deal with inter/intra-subject variability of MI EEG data: (a) Extracting functional connectivity from spatiotemporal class activation maps through a novel kernel-based cross-spectral distribution estimator, (b) Clustering the subjects according to their achieved classifier accuracy, aiming to find common and discriminative patterns of motor skills. According to the validation results obtained on a bi-class database, an average accuracy enhancement of 10% is achieved compared to the baseline EEGNet approach, reducing the number of "poor skill" subjects from 40% to 20%. Overall, the proposed method can be used to help explain brain neural responses even in subjects with deficient MI skills, who have neural responses with high variability and poor EEG-BCI performance.

</details>
