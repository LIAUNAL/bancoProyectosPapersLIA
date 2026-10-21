---
id: A017
titulo: "Enhancing agricultural data interpretability and visualization with TabNet-driven feature extraction and Local Biplots"
tipo: articulo
temas: [T10, T13, T07]
cluster: "C12 Pronóstico energético y series de tiempo"
palabras_clave: [TabNet, UMAP, biplot local, agricultura de precisión, índice de área foliar, explicabilidad]
fuente_resumen: abstract
anio: 2025
revista: "Results in Engineering"
doi: 10.1016/j.rineng.2025.106672
citas_openalex: 3
fuentes: [0001330950]
---

# Enhancing agricultural data interpretability and visualization with TabNet-driven feature extraction and Local Biplots

**Autores:** Jenniffer Carolina Triana-Martinez, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Results in Engineering (2025)  
**DOI:** https://doi.org/10.1016/j.rineng.2025.106672  
**Temas:** T10 Agricultura de precisión, ambiente y teledetección; T13 Representación de datos, reducción de dimensión y agrupamiento; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C12 Pronóstico energético y series de tiempo

## Aplicación
Agricultura de precisión: estimación del índice de área foliar (trigo WMBD) y puntaje de mejoramiento en pastos forrajeros.

## Problema de investigación
Los datos agrícolas de teledetección son complejos y no lineales, y los agrónomos requieren modelos precisos e interpretables.

## Propuesta o novedad
UL-Biplot, que combina la atribución por atención de TabNet con el Local Biplot basado en UMAP; las máscaras secuenciales de TabNet filtran y ordenan variables para proyecciones afines locales y ejes globales.

## Resultados
Obtuvo R2 = 0.79 ± 0.01 para LAI y R2 = 0.77 ± 0.01 para puntaje de mejoramiento. Los embeddings de TabNet mejoraron la trustworthiness (0.94 a 0.98) y la preservación de vecindarios de clase (0.047 frente a 0.018), y revelaron grupos agronómicos asociados a riego y estrés hídrico.

## Conclusiones principales
UL-Biplot supera a SVD en fidelidad de vecindario y cohesión de clases, aportando información accionable para manejo por sitio.

## Métodos
- TabNet
- UMAP
- Local Biplot
- regresión

## Idea para trabajo futuro
Extender UL-Biplot a series temporales multiespectrales para seguir la evolución de grupos agronómicos durante el ciclo de cultivo.

## Relacionados (similitud semántica)
- extiende: [[A034-2024-crop-water-status-analysis-from-complex-agricultural-data-us]] — Crop Water Status Analysis from Complex Agricultural Data Using UMAP-Based Local Biplot

<details><summary>Abstract</summary>

Modern agriculture faces escalating challenges that demand predictive models balancing accuracy and interpretability to support informed decision-making. While precision agriculture has advanced through high-resolution remote sensing technologies capturing spectral, thermal, and soil data, interpreting these complex, nonlinear datasets remains a significant challenge for agronomists. This study introduces the TabNet-informed UMAP-based Local Biplot (UL-Biplot) framework, which combines TabNet's attention-based feature attribution with a Local Biplot technique from the widely recognized Uniform Manifold Approximation and Projection (UMAP). The method provides an intuitive representation of non-stationary and non-linear data patterns, enhancing both global and cluster-level explainability. Also, we highlight feature loadings based on TabNet's attention scores and evaluate the framework on a synthetic benchmark and two real-world datasets: a forage grasses trial for breeder score prediction and the WMBD wheat dataset for LAI estimation. Quantitative results demonstrate that our framework achieved an R 2 = 0.79 ± 0.01 for LAI and delivered more consistent performance for breeder scores ( R 2 = 0.77 ± 0.01 ) relative to standard machine learning models. Moreover, TabNet's latent embeddings improved significantly in trustworthiness (from 0.94 to 0.98) and in class-neighbourhood preservation (0.047 versus 0.018 with conventional methods). The UL-Biplot also revealed distinct agronomic clusters associated with irrigation-induced greenness indices and moisture stress responses, providing actionable insights for site-specific crop management. • TabNet-informed UL-Biplot integrates attention-based feature selection with dimensionality reduction for interpretable agricultural data. • Combines TabNet’s sequential masks with local affine biplots for traceable visual analytics. • TabNet’s attention masks filter and rank features for Local Biplot reduction and global-axis projection. • UL-Biplot outperforms SVD in neighbourhood fidelity and class cohesion.

</details>
