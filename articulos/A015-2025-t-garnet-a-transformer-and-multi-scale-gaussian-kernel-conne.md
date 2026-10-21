---
id: A015
titulo: "T-GARNet: A Transformer and Multi-Scale Gaussian Kernel Connectivity Network with Alpha-Rényi Regularization for EEG-Based ADHD Detection"
tipo: articulo
temas: [T04, T02, T05]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [TDAH, EEG, Transformer, conectividad funcional, regularización de Rényi, atención espacial]
fuente_resumen: abstract
anio: 2025
revista: "Mathematics"
doi: 10.3390/math13244026
citas_openalex: 6
fuentes: [0001330950]
---

# T-GARNet: A Transformer and Multi-Scale Gaussian Kernel Connectivity Network with Alpha-Rényi Regularization for EEG-Based ADHD Detection

**Autores:** Danna Valentina Salazar-Dubois, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Mathematics (2025)  
**DOI:** https://doi.org/10.3390/math13244026  
**Temas:** T04 Bioseñales y soporte al diagnóstico clínico; T02 Conectividad cerebral e imagen de fuentes neuronales; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Detección de TDAH con EEG con modelos interpretables, evaluados en un conjunto público.

## Problema de investigación
La clasificación de TDAH con EEG sufre sobreajuste, dependencia de preprocesamiento extenso y baja interpretabilidad.

## Propuesta o novedad
T-GARNet integra atención temporal tipo Transformer con conectividad funcional por mezcla gaussiana multiescala (núcleos gaussianos paralelos) y una entropía cruzada regularizada con información mutua α-Rényi. Modela dependencias de largo alcance directamente desde EEG crudo.

## Resultados
Con validación LOSO y SGKF-CV en un conjunto público, logra desempeño competitivo o superior (82.10% de exactitud), sobre todo en SGKF-CV, con patrones de atención espacial coherentes con hallazgos neurofisiológicos del TDAH.

## Conclusiones principales
T-GARNet es un marco robusto y explicable para la detección objetiva de TDAH con EEG.

## Métodos
- Transformer
- núcleos gaussianos
- información mutua α-Rényi
- LOSO

## Idea para trabajo futuro
Analizar si la regularización de Rényi mejora también la generalización entre bases de datos de TDAH distintas.

## Relacionados (similitud semántica)
- extendido por: [[A002-2026-explainable-ai-based-connectivity-learning-for-adhd-detectio]] — Explainable AI-Based Connectivity Learning for ADHD Detection from EEG Signals

<details><summary>Abstract</summary>

Attention-Deficit/Hyperactivity Disorder (ADHD) is a highly prevalent neurodevelopmental condition that is typically identified through behavioral assessments and subjective clinical reports. However, electroencephalography (EEG) offers a cost-effective and non-invasive alternative for capturing neural activity patterns closely associated with this disorder. Despite this potential, EEG-based ADHD classification remains challenged by overfitting, dependence on extensive preprocessing, and limited interpretability. Here, we propose a novel neural architecture that integrates transformer-based temporal attention with Gaussian mixture functional connectivity modeling and a cross-entropy loss regularized through α-Rényi mutual information, termed T-GARNet. The multi-scale Gaussian kernel functional connectivity leverages parallel Gaussian kernels to identify complex spatial dependencies, which are further stabilized and regularized by the α-Rényi term. This design enables direct modeling of long-range temporal dependencies from raw EEG while enhancing spatial interpretability and reducing feature redundancy. We evaluate T-GARNet on a publicly available ADHD EEG dataset using both leave-one-subject-out (LOSO) and stratified group k-fold cross-validation (SGKF-CV), where groups correspond to control and ADHD, and compare its performance against classical and modern state-of-the-art methods. Results show that T-GARNet achieves competitive or superior performance (82.10% accuracy), particularly under the more challenging SGKF-CV setting, while producing interpretable spatial attention patterns consistent with ADHD-related neurophysiological findings. These results underscore T-GARNet’s potential as a robust and explainable framework for objective EEG-based ADHD detection.

</details>
