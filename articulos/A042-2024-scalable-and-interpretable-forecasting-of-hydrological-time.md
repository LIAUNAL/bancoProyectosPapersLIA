---
id: A042
titulo: "Scalable and Interpretable Forecasting of Hydrological Time Series Based on Variational Gaussian Processes"
tipo: articulo
temas: [T06, T09, T10]
cluster: "C12 Pronóstico energético y series de tiempo"
palabras_clave: [pronóstico de caudales, procesos gaussianos variacionales, series hidrológicas, cuantificación de incertidumbre, embalses, inferencia bayesiana]
fuente_resumen: abstract
anio: 2024
revista: "Water"
doi: 10.3390/w16142006
citas_openalex: 5
fuentes: [0001330950]
---

# Scalable and Interpretable Forecasting of Hydrological Time Series Based on Variational Gaussian Processes

**Autores:** Julián David Pastrana-Cortés, Julián Gil-González, Andrés Marino Álvarez-Meza, David  Augusto Cardenas Peña, Alvaro Angel Orozco  
**Revista:** Water (2024)  
**DOI:** https://doi.org/10.3390/w16142006  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T09 Monitoreo industrial y sistemas de energía; T10 Agricultura de precisión, ambiente y teledetección  
**Clúster:** C12 Pronóstico energético y series de tiempo

## Aplicación
Pronóstico de caudales afluentes de 23 embalses colombianos para planeación hidroeléctrica.

## Problema de investigación
Los modelos físicos son complejos; LAR y LSTM no cuantifican incertidumbre.

## Propuesta o novedad
Procesos gaussianos variacionales dispersos (SVGP) para pronóstico multisalida de caudales, con hiperparámetros óptimos y puntos inductores compartidos que capturan relaciones de corto y largo plazo entre embalses y reducen el costo frente a GP tradicionales.

## Resultados
Con 12 años de datos de 23 embalses geográficamente dispersos, supera a LAR y LSTM en adaptabilidad a dinámicas cambiantes, intervalos de confianza informativos y exactitud.

## Conclusiones principales
La metodología es escalable e interpretable para gestión de recursos hídricos y planeación hidroeléctrica.

## Métodos
- SVGP
- puntos inductores
- LAR
- LSTM

## Idea para trabajo futuro
Incorporar covariables climáticas (ENSO, precipitación) en el SVGP para pronósticos estacionales con incertidumbre calibrada.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P010-2021-desarrollo-de-una-herramienta-para-la-planeacion-a-largo-pla]] — Desarrollo de una herramienta para la planeación a largo plazo de la operación del sistema de transporte de gas natural de Colombia

<details><summary>Abstract</summary>

Accurate streamflow forecasting is crucial for effectively managing water resources, particularly in countries like Colombia, where hydroelectric power generation significantly contributes to the national energy grid. Although highly interpretable, traditional deterministic, physically-driven models often suffer from complexity and require extensive parameterization. Data-driven models like Linear Autoregressive (LAR) and Long Short-Term Memory (LSTM) networks offer simplicity and performance but cannot quantify uncertainty. This work introduces Sparse Variational Gaussian Processes (SVGPs) for forecasting streamflow contributions. The proposed SVGP model reduces computational complexity compared to traditional Gaussian Processes, making it highly scalable for large datasets. The methodology employs optimal hyperparameters and shared inducing points to capture short-term and long-term relationships among reservoirs. Training, validation, and analysis of the proposed approach consider the streamflow dataset from 23 geographically dispersed reservoirs recorded during twelve years in Colombia. Performance assessment reveals that the proposal outperforms baseline Linear Autoregressive (LAR) and Long Short-Term Memory (LSTM) models in three key aspects: adaptability to changing dynamics, provision of informative confidence intervals through Bayesian inference, and enhanced forecasting accuracy. Therefore, the SVGP-based forecasting methodology offers a scalable and interpretable solution for multi-output streamflow forecasting, thereby contributing to more effective water resource management and hydroelectric planning.

</details>
