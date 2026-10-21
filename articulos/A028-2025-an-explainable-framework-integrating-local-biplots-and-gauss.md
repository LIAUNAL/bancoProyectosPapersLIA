---
id: A028
titulo: "An Explainable Framework Integrating Local Biplots and Gaussian Processes for Unemployment Rate Prediction in Colombia"
tipo: articulo
temas: [T14, T13, T06]
cluster: "C12 Pronóstico energético y series de tiempo"
palabras_clave: [desempleo, Local Biplot, UMAP, procesos gaussianos, relevancia de características, series no estacionarias]
fuente_resumen: abstract
anio: 2025
revista: "Computation"
doi: 10.3390/computation13050116
citas_openalex: 1
fuentes: [0001330950]
---

# An Explainable Framework Integrating Local Biplots and Gaussian Processes for Unemployment Rate Prediction in Colombia

**Autores:** Diego Armando Pérez-Rosero, Diego Alejandro Manrique-Cabezas, Jenniffer Carolina Triana-Martinez, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Computation (2025)  
**DOI:** https://doi.org/10.3390/computation13050116  
**Temas:** T14 Educación, sociedad y analítica de datos; T13 Representación de datos, reducción de dimensión y agrupamiento; T06 Aprendizaje probabilístico y bayesiano  
**Clúster:** C12 Pronóstico energético y series de tiempo

## Aplicación
Predicción de la tasa de desempleo en Colombia con variables monetarias y socioeconómicas.

## Problema de investigación
Las series laborales son no estacionarias y no lineales, y se requiere interpretabilidad en muestras y variables para apoyar decisiones públicas.

## Propuesta o novedad
Un marco explicable que reúne una base de datos colombiana de desempleo, un Local Biplot basado en UMAP con transformaciones afines locales como representación no supervisada, y un regresor de procesos gaussianos con análisis de relevancia de características basado en kernels.

## Resultados
En la base personalizada, el marco mejora el agrupamiento y la predicción frente a técnicas estadísticas tradicionales y métodos modernos, y destaca la importancia de muestras y variables.

## Conclusiones principales
La combinación de Local Biplot y procesos gaussianos aporta precisión e interpretabilidad para políticas laborales.

## Métodos
- UMAP Local Biplot
- procesos gaussianos
- relevancia de características kernel

## Idea para trabajo futuro
Incorporar dinámica temporal explícita y choques exógenos para pronosticar desempleo regional con intervalos de incertidumbre.

## Relacionados (similitud semántica)
- extiende: [[A034-2024-crop-water-status-analysis-from-complex-agricultural-data-us]] — Crop Water Status Analysis from Complex Agricultural Data Using UMAP-Based Local Biplot

<details><summary>Abstract</summary>

Addressing unemployment is essential for formulating effective public policies. In particular, socioeconomic and monetary variables serve as essential indicators for anticipating labor market trends, given their strong influence on employment dynamics and economic stability. However, effective unemployment rate prediction requires addressing the non-stationary and non-linear characteristics of labor data. Equally important is the preservation of interpretability in both samples and features to ensure that forecasts can meaningfully inform public decision-making. Here, we provide an explainable framework integrating unsupervised and supervised machine learning to enhance unemployment rate prediction and interpretability. Our approach is threefold: (i) we gather a dataset for Colombian unemployment rate prediction including monetary and socioeconomic variables. (ii) Then, we used a Local Biplot technique from the widely recognized Uniform Manifold Approximation and Projection (UMAP) method along with local affine transformations as an unsupervised representation of non-stationary and non-linear data patterns in a simplified and comprehensible manner. (iii) A Gaussian Processes regressor with kernel-based feature relevance analysis is coupled as a supervised counterpart for both unemployment rate prediction and input feature importance analysis. We demonstrated the effectiveness of our proposed approach through a series of experiments conducted on our customized database focused on unemployment indicators in Colombia. Furthermore, we carried out a comparative analysis between traditional statistical techniques and modern machine learning methods. The results revealed that our framework significantly enhances both clustering and predictive performance, while also emphasizing the importance of input samples and feature selection in driving accurate outcomes.

</details>
