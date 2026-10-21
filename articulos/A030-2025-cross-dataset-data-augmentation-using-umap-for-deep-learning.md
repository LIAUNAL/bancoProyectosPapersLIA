---
id: A030
titulo: "Cross-Dataset Data Augmentation Using UMAP for Deep Learning-Based Wind Speed Prediction"
tipo: articulo
temas: [T09, T13, T10]
cluster: "C12 Pronóstico energético y series de tiempo"
palabras_clave: [pronóstico de viento, UMAP, aumento de datos, redes recurrentes, series de tiempo, energía renovable]
fuente_resumen: abstract
anio: 2025
revista: "Computers"
doi: 10.3390/computers14040123
citas_openalex: 2
fuentes: [0001330950]
---

# Cross-Dataset Data Augmentation Using UMAP for Deep Learning-Based Wind Speed Prediction

**Autores:** Eder Arley Leon-Gomez, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Computers (2025)  
**DOI:** https://doi.org/10.3390/computers14040123  
**Temas:** T09 Monitoreo industrial y sistemas de energía; T13 Representación de datos, reducción de dimensión y agrupamiento; T10 Agricultura de precisión, ambiente y teledetección  
**Clúster:** C12 Pronóstico energético y series de tiempo

## Aplicación
Pronóstico de velocidad del viento a alto horizonte con datos de EE. UU. y China, para energías renovables.

## Problema de investigación
La intermitencia del viento, la no linealidad, la no estacionariedad y la necesidad de grandes conjuntos de datos limitan los métodos existentes.

## Propuesta o novedad
Un marco de aumento de datos entre conjuntos con preservación de vecindarios: UMAP como reducción no lineal para codificar relaciones locales de las series, aumento de datos localizado en espacios UMAP para elevar la diversidad y mitigar la variabilidad entre conjuntos, y entrenamiento de RNN sobre los datos aumentados.

## Resultados
Con datos de Argonne Weather Observatory (EE. UU.), Chengdu Airport y Beijing Capital International Airport (China), probando RNN, GRU y LSTM, el método mejoró la exactitud y generalización con una reducción promedio del error.

## Conclusiones principales
Integrar reducción de dimensión, aumento de datos y aprendizaje profundo ayuda a los retos del pronóstico renovable.

## Métodos
- UMAP
- aumento de datos
- RNN/GRU/LSTM

## Idea para trabajo futuro
Estudiar aumento entre conjuntos con ubicaciones de clima muy distinto mediante adaptación de dominio para pronóstico en sitios sin histórico.

## Relacionados (similitud semántica)
- extendido por: [[A003-2026-multi-scale-spectral-recurrent-network-based-on-random-fouri]] — Multi-Scale Spectral Recurrent Network Based on Random Fourier Features for Wind Speed Forecasting

<details><summary>Abstract</summary>

Wind energy has emerged as a cornerstone in global efforts to transition to renewable energy, driven by its low environmental impact and significant generation potential. However, the inherent intermittency of wind, influenced by complex and dynamic atmospheric patterns, poses significant challenges for accurate wind speed prediction. Existing approaches, including statistical methods, machine learning, and deep learning, often struggle with limitations such as non-linearity, non-stationarity, computational demands, and the requirement for extensive, high-quality datasets. In response to these challenges, we propose a novel neighborhood preserving cross-dataset data augmentation framework for high-horizon wind speed prediction. The proposed method addresses data variability and dynamic behaviors through three key components: (i) the uniform manifold approximation and projection (UMAP) is employed as a non-linear dimensionality reduction technique to encode local relationships in wind speed time-series data while preserving neighborhood structures, (ii) a localized cross-dataset data augmentation (DA) approach is introduced using UMAP-reduced spaces to enhance data diversity and mitigate variability across datasets, and (iii) recurrent neural networks (RNNs) are trained on the augmented datasets to model temporal dependencies and non-linear patterns effectively. Our framework was evaluated using datasets from diverse geographical locations, including the Argonne Weather Observatory (USA), Chengdu Airport (China), and Beijing Capital International Airport (China). Comparative tests using regression-based measures on RNN, GRU, and LSTM architectures showed that the proposed method was better at improving the accuracy and generalizability of predictions, leading to an average reduction in prediction error. Consequently, our study highlights the potential of integrating advanced dimensionality reduction, data augmentation, and deep learning techniques to address critical challenges in renewable energy forecasting.

</details>
