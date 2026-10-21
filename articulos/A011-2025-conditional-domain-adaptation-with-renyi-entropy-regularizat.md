---
id: A011
titulo: "Conditional Domain Adaptation with α-Rényi Entropy Regularization and Noise-Aware Label Weighting"
tipo: articulo
temas: [T05, T07]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [adaptación de dominio, entropía de Rényi, pseudoetiquetas, cambio de covariables, alineación condicional, mapas de activación]
fuente_resumen: abstract
anio: 2025
revista: "Mathematics"
doi: 10.3390/math13162602
citas_openalex: 0
fuentes: [0001330950]
---

# Conditional Domain Adaptation with α-Rényi Entropy Regularization and Noise-Aware Label Weighting

**Autores:** Diego Armando Pérez-Rosero, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Mathematics (2025)  
**DOI:** https://doi.org/10.3390/math13162602  
**Temas:** T05 Métodos kernel y aprendizaje basado en teoría de la información; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Adaptación de dominio para clasificación de imágenes bajo cambio de covariables y pseudoetiquetas ruidosas.

## Problema de investigación
Los métodos existentes tienen dificultad para preservar a la vez representaciones invariantes al dominio y estructura discriminativa, con pseudoetiquetas ruidosas en el dominio objetivo.

## Propuesta o novedad
CREDA (Conditional Rényi α-Entropy Domain Adaptation) integra alineación condicional basada en kernels con una formulación matricial diferenciable de la entropía cuadrática de Rényi. Incluye un extractor profundo, una ponderación por entropía que reduce el peso de pseudoetiquetas poco confiables y una pérdida de alineación condicional por clase.

## Resultados
Se validó en Digits, ImageCLEF-DA y Office-31 con desempeño competitivo frente a métodos clásicos y profundos. Mapas de activación y reducción de dimensión no lineal muestran alineamiento significativo en el espacio de características.

## Conclusiones principales
CREDA mejora la generalización entre dominios con exactitud, robustez e interpretabilidad.

## Métodos
- entropía matricial de Rényi
- alineación kernel
- adaptación de dominio
- CAM

## Idea para trabajo futuro
Aplicar CREDA a señales biomédicas con cambio de sujeto o dispositivo, donde las pseudoetiquetas son especialmente inciertas.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Domain adaptation is a key approach to ensure that artificial intelligence models maintain reliable performance when facing distributional shifts between training (source) and testing (target) domains. However, existing methods often struggle to simultaneously preserve domain-invariant representations and discriminative class structures, particularly in the presence of complex covariate shifts and noisy pseudo-labels in the target domain. In this work, we introduce Conditional Rényi α-Entropy Domain Adaptation, named CREDA, a novel deep learning framework for domain adaptation that integrates kernel-based conditional alignment with a differentiable, matrix-based formulation of Rényi’s quadratic entropy. The proposed method comprises three main components: (i) a deep feature extractor that learns domain-invariant representations from labeled source and unlabeled target data; (ii) an entropy-weighted approach that down-weights low-confidence pseudo-labels, enhancing stability in uncertain regions; and (iii) a class-conditional alignment loss, formulated as a Rényi-based entropy kernel estimator, that enforces semantic consistency in the latent space. We validate CREDA on standard benchmark datasets for image classification, including Digits, ImageCLEF-DA, and Office-31, showing competitive performance against both classical and deep learning-based approaches. Furthermore, we employ nonlinear dimensionality reduction and class activation maps visualizations to provide interpretability, revealing meaningful alignment in feature space and offering insights into the relevance of individual samples and attributes. Experimental results confirm that CREDA improves cross-domain generalization while promoting accuracy, robustness, and interpretability.

</details>
