---
id: A003
titulo: "Multi-Scale Spectral Recurrent Network Based on Random Fourier Features for Wind Speed Forecasting"
tipo: articulo
temas: [T09, T10, T05]
cluster: "C12 Pronóstico energético y series de tiempo"
palabras_clave: [pronóstico de viento, random Fourier features, sesgo espectral, GRU, LSTM, optimización bayesiana]
fuente_resumen: abstract
anio: 2026
revista: "Technologies"
doi: 10.3390/technologies14040238
citas_openalex: 0
fuentes: [0001330950]
---

# Multi-Scale Spectral Recurrent Network Based on Random Fourier Features for Wind Speed Forecasting

**Autores:** Eder Arley Leon-Gomez, V́ıctor Elvira, Jorge Iván Montes-Monsalve, Andrés Marino Álvarez-Meza, Alvaro Orozco-Gutierrez, German Castellanos-Dominguez  
**Revista:** Technologies (2026)  
**DOI:** https://doi.org/10.3390/technologies14040238  
**Temas:** T09 Monitoreo industrial y sistemas de energía; T10 Agricultura de precisión, ambiente y teledetección; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C12 Pronóstico energético y series de tiempo

## Aplicación
Pronóstico de velocidad del viento para integración de energía eólica, con seis conjuntos de datos reales de EE. UU., China y Países Bajos.

## Problema de investigación
Las series de viento son no estacionarias y multiescala; LSTM, GRU y Transformers sufren sesgo espectral, sensibilidad a hiperparámetros y baja generalización entre regímenes.

## Propuesta o novedad
RFF-RNN, un marco espectral-recurrente que combina codificaciones multibanda de Random Fourier Features con redes recurrentes. Su novedad es relajar la invariancia al desplazamiento optimizando conjuntamente frecuencias, sesgos de fase y escalas de ancho de banda junto con los pesos, con optimización bayesiana externa de hiperparámetros.

## Resultados
En un benchmark sintético y seis conjuntos reales, RFF-GRU y RFF-LSTM superan a las redes recurrentes estándar y a Autoformer y FEDformer según la prueba de Friedman. Reportan menor MAE y RMSE, mayor R2 y menor acumulación de error en horizontes largos.

## Conclusiones principales
Los embeddings espectrales aprendibles mitigan el sesgo espectral y mejoran la robustez del pronóstico.

## Métodos
- RFF
- GRU/LSTM
- optimización bayesiana
- prueba de Friedman

## Idea para trabajo futuro
Evaluar RFF-RNN en pronóstico multivariado con variables meteorológicas exógenas y cuantificación de incertidumbre.

## Relacionados (similitud semántica)
- extiende: [[A030-2025-cross-dataset-data-augmentation-using-umap-for-deep-learning]] — Cross-Dataset Data Augmentation Using UMAP for Deep Learning-Based Wind Speed Prediction

<details><summary>Abstract</summary>

Accurate wind speed forecasting is critical for reliable wind-power integration, yet it remains challenging due to the strongly non-stationary and inherently multi-scale nature of atmospheric processes. While deep learning models—such as LSTM, GRU, and Transformer architectures—achieve competitive short- and medium-term performance, they frequently suffer from spectral bias, hyperparameter sensitivity, and reduced generalization under heterogeneous operating regimes. To address these limitations, we propose a multi-scale spectral–recurrent framework, termed RFF-RNN, which integrates multi-band Random Fourier Feature (RFF) encodings with parameterizable recurrent backbones. A key innovation of our approach is the deliberate relaxation of strict shift-invariance constraints; by jointly optimizing spectral frequencies, phase biases, and bandwidth scales alongside the neural weights, the framework dynamically shapes a fully data-driven spectral embedding. To ensure robust adaptation, we employ a two-stage optimization strategy combining gradient-based inner-loop learning with outer-loop Bayesian hyperparameter tuning. Extensive evaluations on a controlled synthetic benchmark and six geographically diverse real-world wind datasets (spanning the USA, China, and the Netherlands) demonstrate the superiority of the proposed framework. Statistical validation via the Friedman test confirms that RFF-enhanced models—particularly RFF-GRU and RFF-LSTM—systematically outperform standard recurrent networks and state-of-the-art Transformer architectures (Autoformer and FEDformer). The proposed approach yields significantly lower error metrics (MAE and RMSE) and higher explained variance (R2), while exhibiting remarkable resilience against error accumulation at extended forecasting horizons.

</details>
