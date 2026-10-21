---
id: A034
titulo: "Crop Water Status Analysis from Complex Agricultural Data Using UMAP-Based Local Biplot"
tipo: articulo
temas: [T10, T13]
cluster: "C12 Pronóstico energético y series de tiempo"
palabras_clave: [estado hídrico del cultivo, UMAP, Local Biplot, agricultura de precisión, datos no estacionarios, ranking de características]
fuente_resumen: abstract
anio: 2024
revista: "Remote Sensing"
doi: 10.3390/rs16152854
citas_openalex: 5
fuentes: [0001330950]
---

# Crop Water Status Analysis from Complex Agricultural Data Using UMAP-Based Local Biplot

**Autores:** Jenniffer Carolina Triana-Martinez, Andrés Marino Álvarez-Meza, Julián Gil-González, Tom De Swaef, José A. Fernandez-Gallego  
**Revista:** Remote Sensing (2024)  
**DOI:** https://doi.org/10.3390/rs16152854  
**Temas:** T10 Agricultura de precisión, ambiente y teledetección; T13 Representación de datos, reducción de dimensión y agrupamiento  
**Clúster:** C12 Pronóstico energético y series de tiempo

## Aplicación
Análisis del estado hídrico de cultivos de pasto y arroz con sensores en vehículos aéreos no tripulados.

## Problema de investigación
Los datos agrícolas tienen relaciones no lineales localizadas en subgrupos, con ruido, alta variabilidad y no estacionariedad.

## Propuesta o novedad
Local Biplot, un marco basado en UMAP y transformaciones afines locales que codifica patrones no estacionarios y no lineales preservando la interpretabilidad. Incluye una estrategia de análisis de relevancia que explica la existencia de los clústeres y considera contribuciones de variables y observaciones por clúster.

## Resultados
En datos sintéticos y reales con pasto y arroz, mejora el agrupamiento y la predicción de variables de estado hídrico usando bosque aleatorio y regresión lineal sobre el ranking de características y clústeres.

## Conclusiones principales
Local Biplot sirve para visualizar, analizar y comparar estructuras de datos agrícolas complejos.

## Métodos
- UMAP
- Local Biplot
- bosque aleatorio
- regresión lineal

## Idea para trabajo futuro
Combinar Local Biplot con imágenes multiespectrales multitemporales para anticipar estrés hídrico antes de síntomas visibles.

## Relacionados (similitud semántica)
- extendido por: [[A017-2025-enhancing-agricultural-data-interpretability-and-visualizati]] — Enhancing agricultural data interpretability and visualization with TabNet-driven feature extraction and Local Biplots
- extendido por: [[A028-2025-an-explainable-framework-integrating-local-biplots-and-gauss]] — An Explainable Framework Integrating Local Biplots and Gaussian Processes for Unemployment Rate Prediction in Colombia

<details><summary>Abstract</summary>

To optimize growth and management, precision agriculture relies on a deep understanding of agricultural dynamics, particularly crop water status analysis. Leveraging unmanned aerial vehicles, we can efficiently acquire high-resolution spatiotemporal samples by utilizing remote sensors. However, non-linear relationships among data features, localized within specific subgroups, frequently emerge in agricultural data. Interpreting these complex patterns requires sophisticated analysis due to the presence of noise, high variability, and non-stationarity behavior in the collected samples. Here, we introduce Local Biplot, a methodological framework tailored for discerning meaningful data patterns in non-stationary contexts for precision agriculture. Local Biplot relies on the well-known uniform manifold approximation and projection method, such as UMAP, and local affine transformations to codify non-stationary and non-linear data patterns while maintaining interpretability. This lets us find important clusters for transformation and projection within a single global axis pair. Hence, our framework encompasses variable and observational contributions within individual clusters. At the same time, we provide a relevance analysis strategy to help explain why those clusters exist, facilitating the understanding of data dynamics while favoring interpretability. We demonstrated our method’s capabilities through experiments on both synthetic and real-world datasets, covering scenarios involving grass and rice crops. Moreover, we use random forest and linear regression models to predict water status variables from our Local Biplot-based feature ranking and clusters. Our findings revealed enhanced clustering and prediction capability while emphasizing the importance of input features in precision agriculture. As a result, Local Biplot is a useful tool to visualize, analyze, and compare the intricate underlying patterns and internal structures of complex agricultural datasets.

</details>
