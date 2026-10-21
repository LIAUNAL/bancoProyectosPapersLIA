---
id: A100
titulo: "A data-driven measure of effective connectivity based on Renyi's α-entropy"
tipo: articulo
temas: [T02, T05]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [entropía de transferencia, conectividad efectiva, entropía de Rényi, estimación con kernels, kernels definidos positivos]
fuente_resumen: abstract
anio: 2019
revista: "Frontiers in Neuroscience"
doi: 10.3389/fnins.2019.01277
citas_openalex: 25
fuentes: [0001330950]
---

# A data-driven measure of effective connectivity based on Renyi's α-entropy

**Autores:** Iván De La Pava Panche, Andrés Marino Álvarez-Meza, Alvaro Angel Orozco  
**Revista:** Frontiers in Neuroscience (2019)  
**DOI:** https://doi.org/10.3389/fnins.2019.01277  
**Temas:** T02 Conectividad cerebral e imagen de fuentes neuronales; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Medición de conectividad efectiva en neurociencia con entropía de transferencia.

## Problema de investigación
La estimación de TE depende de estimar distribuciones, difícil en la práctica.

## Propuesta o novedad
Se propone un estimador de TE con funcionales sobre matrices de kernel definidas positivas e infinitamente divisibles que aproximan entropías de Rényi de orden alfa, estimando TE directamente de los datos.

## Resultados
El estimador se propone como alternativa a vecinos cercanos y simbolización.

## Conclusiones principales
Estimar TE sin pasos intermedios de densidad es viable.

## Métodos
- TE
- entropía de Rényi
- matrices de kernel

## Idea para trabajo futuro
Estudiar selección automática del ancho de kernel para la TE de Rényi en series cortas.

## Relacionados (similitud semántica)
- extendido por: [[A063-2021-kernel-based-phase-transfer-entropy-with-enhanced-feature-re]] — Kernel-based phase transfer entropy with enhanced feature relevance analysis for brain computer interfaces
- extendido por: [[A067-2021-estimating-directed-phase-amplitude-interactions-from-eeg-da]] — Estimating Directed Phase-Amplitude Interactions from EEG Data through Kernel-Based Phase Transfer Entropy

<details><summary>Abstract</summary>

Transfer entropy (TE) is a model-free effective connectivity measure based on information theory. It has been increasingly used in neuroscience because of its ability to detect unknown non-linear interactions, which makes it well suited for exploratory brain effective connectivity analyses. Like all information theoretic quantities, TE is defined regarding the probability distributions of the system under study, which in practice are unknown and must be estimated from data. Commonly used methods for TE estimation rely on a local approximation of the probability distributions from nearest neighbor distances, or on symbolization schemes that then allow the probabilities to be estimated from the symbols' relative frequencies. However, probability estimation is a challenging problem, and avoiding this intermediate step in TE computation is desirable. In this work, we propose a novel TE estimator using functionals defined on positive definite and infinitely divisible kernels matrices that approximate Renyi's entropy measures of order α. Our data-driven approach estimates TE directly from data, sidestepping the need for probability distribution estimation. Also, the proposed estimator encompasses the well-known definition of TE as a sum of Shannon entropies in the limiting case when α → 1. We tested our proposal on a simulation framework consisting of two linear models, based on autoregressive approaches and a linear coupling function, respectively, and on the public electroencephalogram (EEG) database BCI Competition IV, obtained under a motor imagery paradigm. For the synthetic data, the proposed kernel-based TE estimation method satisfactorily identifies the causal interactions present in the data. Also, it displays robustness to varying noise levels and data sizes, and to the presence of multiple interaction delays in the same connected network. Obtained results for the motor imagery task show that our approach codes discriminant spatiotemporal patterns for the left and right-hand motor imagination tasks, with classification performances that compare favorably to the state-of-the-art.

</details>
