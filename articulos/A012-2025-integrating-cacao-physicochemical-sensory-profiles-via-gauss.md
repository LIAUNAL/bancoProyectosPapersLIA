---
id: A012
titulo: "Integrating Cacao Physicochemical-Sensory Profiles via Gaussian Processes Crowd Learning and Localized Annotator Trustworthiness"
tipo: articulo
temas: [T06, T14]
cluster: "C11 Aprendizaje con múltiples anotadores"
palabras_clave: [análisis sensorial, cacao, procesos gaussianos, aprendizaje de multitudes, confiabilidad del anotador, regresión multi-anotador]
fuente_resumen: abstract
anio: 2025
revista: "Foods"
doi: 10.3390/foods14172961
citas_openalex: 2
fuentes: [0001330950]
---

# Integrating Cacao Physicochemical-Sensory Profiles via Gaussian Processes Crowd Learning and Localized Annotator Trustworthiness

**Autores:** Juan Camilo Lugo-Rojas, Maria José Chica-Morales, Sergio Leonardo Florez-González, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Foods (2025)  
**DOI:** https://doi.org/10.3390/foods14172961  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T14 Educación, sociedad y analítica de datos  
**Clúster:** C11 Aprendizaje con múltiples anotadores

## Aplicación
Control de calidad y análisis sensorial de productos de cacao (base de datos Casa Luker) a partir de perfiles fisicoquímicos.

## Problema de investigación
Las evaluaciones sensoriales de múltiples expertos son subjetivas, ruidosas y no estacionarias, y es difícil integrarlas con datos fisicoquímicos.

## Propuesta o novedad
MAR-CCGP, un proceso gaussiano encadenado correlacionado para aprendizaje de multitudes en regresión. Se articula en tres etapas: base de datos integrada fisicoquímica-sensorial, inferencia de la verdad latente desde anotaciones ruidosas y un enfoque novedoso de confiabilidad local del experto dependiente del espacio de entrada.

## Resultados
En datos semisintéticos y en una base real nueva con Casa Luker, supera a los métodos de aprendizaje de multitudes en predicción y en estimación de la confiabilidad de anotadores.

## Conclusiones principales
El marco ofrece una base robusta e interpretable para análisis sensorial guiado por datos y optimización de producto.

## Métodos
- procesos gaussianos encadenados
- MAR-CCGP
- regresión

## Idea para trabajo futuro
Usar la confiabilidad local de los catadores para diseñar protocolos de panel sensorial más eficientes y reducir el costo de anotación.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Understanding the intricate relationship between sensory perception and physicochemical properties of cacao-based products is crucial for advancing quality control and driving product innovation. However, effectively integrating these heterogeneous data sources poses a significant challenge, particularly when sensory evaluations are derived from low-quality, subjective, and often inconsistent annotations provided by multiple experts. We propose a comprehensive framework that leverages a correlated chained Gaussian processes model for learning from crowds, termed MAR-CCGP, specifically designed for a customized Casa Luker database that integrates sensory and physicochemical data on cacao-based products. By formulating sensory evaluations as regression tasks, our approach enables the estimation of continuous perceptual scores from physicochemical inputs, while concurrently inferring the latent, input-dependent reliability of each annotator. To address the inherent noise, subjectivity, and non-stationarity in expert-generated sensory data, we introduce a three-stage methodology: (i) construction of an integrated database that unifies physicochemical parameters with corresponding sensory descriptors; (ii) application of a MAR-CCGP model to infer the underlying ground truth from noisy, crowd-sourced, and non-stationary sensory annotations; and (iii) development of a novel localized expert trustworthiness approach, also based on MAR-CCGP, which dynamically adjusts for variations in annotator consistency across the input space. Our approach provides a robust, interpretable, and scalable solution for learning from heterogeneous and noisy sensory data, establishing a principled foundation for advancing data-driven sensory analysis and product optimization in the food science domain. We validate the effectiveness of our method through a series of experiments on both semi-synthetic data and a novel real-world dataset developed in collaboration with Casa Luker, which integrates sensory evaluations with detailed physicochemical profiles of cacao-based products. Compared to state-of-the-art learning-from-crowds baselines, our framework consistently achieves superior predictive performance and more precise annotator reliability estimation, demonstrating its efficacy in multi-annotator regression settings. Of note, our unique combination of a novel database, robust noisy-data regression, and input-dependent trust scoring sets MAR-CCGP apart from existing approaches.

</details>
