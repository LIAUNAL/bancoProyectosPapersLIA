---
id: A005
titulo: "STF-KernelSHAP: A Model-Agnostic Space-Time-Frequency Shapley Framework for Physiologically Informed EEG Explainability"
tipo: articulo
temas: [T07, T01, T04]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [KernelSHAP, valores de Shapley, explicabilidad agnóstica, EEG, imaginación motora, TDAH]
fuente_resumen: abstract
anio: 2026
revista: "Computers"
doi: 10.20944/preprints202606.0375.v1
citas_openalex: 0
fuentes: [0001330950]
---

# STF-KernelSHAP: A Model-Agnostic Space-Time-Frequency Shapley Framework for Physiologically Informed EEG Explainability

**Autores:** Diego Armando Pérez-Rosero, Andres Camilo Lopez-Boscan, Andrés Marino Álvarez-Meza, David  Augusto Cardenas Peña, German Castellanos-Dominguez  
**Revista:** Computers (2026)  
**DOI:** https://doi.org/10.20944/preprints202606.0375.v1  
**Temas:** T07 Aprendizaje profundo y explicabilidad; T01 Interfaces cerebro-computador y decodificación EEG; T04 Bioseñales y soporte al diagnóstico clínico  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Explicabilidad de modelos de aprendizaje profundo para EEG en BCI de imaginación motora y detección de TDAH.

## Problema de investigación
Los métodos XAI post hoc suelen dar mapas de un solo dominio; los basados en perturbación alteran la organización fisiológica y los basados en gradiente dependen de la arquitectura.

## Propuesta o novedad
STF-KernelSHAP, un marco Shapley agnóstico al modelo que descompone los ensayos EEG en celdas canal-tiempo-frecuencia. Forma coaliciones sobre celdas completas reconstruidas en el dominio de la señal y estima relevancia condicional por clase con un sustituto ponderado tipo KernelSHAP usando solo las salidas del modelo.

## Resultados
Se evaluó en el conjunto GIGA MI-ME y en el de TDAH de IEEE DataPort; el clasificador T-GARNet interpretado alcanzó 73.33% de exactitud y 79.86% de AUC. Frente a KernelSHAP, LIME, Occlusion, Integrated Gradients y Grad-CAM++, resultó competitivo con fidelidad medida por Deletion y ROAD.

## Conclusiones principales
Ofrece explicaciones dependientes de ventana y específicas por frecuencia, fisiológicamente informadas e independientes del modelo.

## Métodos
- KernelSHAP
- valores de Shapley
- descomposición espectral
- Deletion/ROAD

## Idea para trabajo futuro
Validar las explicaciones STF con expertos clínicos y estudiar su estabilidad entre sujetos y sesiones.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Interpretability is essential for deploying deep learning (DL) models in electroencephalography (EEG)-based neurotechnology, particularly in brain–computer interfaces and clinical decision-support settings. Existing post hoc explainable artificial intelligence (XAI) methods often yield single-domain attribution maps, limiting their capacity to characterize the joint spatial, temporal, and spectral structure of EEG dynamics. In addition, perturbation-based strategies may disrupt physiological signal organization, whereas gradient-based methods require access to model internals and are therefore tied to specific classifier architectures. Here, we introduce space–time–frequency KernelSHAP (STF-KernelSHAP), a model-agnostic Shapley framework for physiologically coherent EEG explainability. The method comprises three stages. First, EEG trials are decomposed into structured channel–time–frequency cells using segment-wise spectral analysis. Second, coalitions are formed over complete channel–time–frequency cells and reconstructed in the signal domain to support physiologically informed perturbations. Third, class-conditional relevance is estimated with a KernelSHAP-based weighted surrogate model that uses only model outputs, enabling architecture-independent Shapley estimation. We evaluate STF-KernelSHAP on two prerecorded public datasets: the GIGA motor imagery/movement execution (MI-ME) dataset for motor imagery (MI) decoding and the IEEE DataPort EEG Data for Attention-Deficit/Hyperactivity Disorder (ADHD)/Control Children dataset for ADHD detection. For ADHD detection, the T-GARNet base classifier interpreted with STF-KernelSHAP achieved 73.33% accuracy and 79.86% area under the curve (AUC); these values characterize classifier performance rather than the explainer itself. We compare the framework against KernelSHAP, local interpretable model-agnostic explanations (LIME), Occlusion, Integrated Gradients, and gradient-weighted class activation mapping++ (Grad-CAM++). Fidelity is assessed with Deletion and remove and debias (ROAD), while qualitative analyses examine topographic and frequency-band attribution maps. Results show that STF-KernelSHAP remains functionally competitive with established XAI methods while providing window-dependent and frequency-specific explanations. Overall, STF-KernelSHAP offers a physiologically informed and model-agnostic alternative for multidomain EEG interpretability.

</details>
