---
id: A026
titulo: "Takens-Based Kernel Transfer Entropy Connectivity Network for Motor Imagery Classification"
tipo: articulo
temas: [T01, T02, T05]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [imaginación motora, BCI, entropía de transferencia, embedding de Takens, conectividad funcional, decodificación EEG]
fuente_resumen: abstract
anio: 2025
revista: "Sensors"
doi: 10.3390/s25227067
citas_openalex: 2
fuentes: [0001330950]
---

# Takens-Based Kernel Transfer Entropy Connectivity Network for Motor Imagery Classification

**Autores:** Alejandra Gomez-Rivera, Andrés Marino Álvarez-Meza, David  Augusto Cardenas Peña, Alvaro Angel Orozco  
**Revista:** Sensors (2025)  
**DOI:** https://doi.org/10.3390/s25227067  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T02 Conectividad cerebral e imagen de fuentes neuronales; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Decodificación de imaginación motora con EEG en BCI mediante conectividad funcional dirigida.

## Problema de investigación
La decodificación de MI es difícil por la naturaleza no lineal, ruidosa y no estacionaria del EEG.

## Propuesta o novedad
TEKTE-Net, modelo de extremo a extremo que integra embeddings de Takens mediante un módulo convolucional con un estimador kernelizado de entropía de transferencia (kernels cuadráticos racionales) en un marco diferenciable, sin preprocesamiento explícito.

## Resultados
Evaluado en benchmarks causales semisintéticos y en BCI Competition IV 2a, muestra robustez a baja relación señal-ruido e interpretabilidad temporal, espacial y espectral, destacando activaciones contralaterales y selectividad en bandas beta y gamma.

## Conclusiones principales
TEKTE-Net es un estimador entrenable de conectividad funcional útil para BCI de MI.

## Métodos
- entropía de transferencia kernelizada
- Takens
- kernel cuadrático racional
- CNN

## Idea para trabajo futuro
Evaluar la estabilidad de la conectividad dirigida aprendida entre sesiones y su uso para adaptación del decodificador.

## Relacionados (similitud semántica)
- extendido por: [[A009-2026-transformer-based-modeling-of-directed-transfer-entropy-conn]] — Transformer-Based Modeling of Directed Transfer Entropy Connectivity for EEG-Based ADHD Classification in Children

<details><summary>Abstract</summary>

Reliable decoding of motor imagery (MI) from electroencephalographic signals remains a challenging problem due to their nonlinear, noisy, and non-stationary nature. To address this issue, this work proposes an end-to-end deep learning model, termed TEKTE-Net, that integrates time embeddings with a kernelized Transfer Entropy estimator to infer directed functional connectivity in MI-based brain-computer interface (BCI) systems. The proposed model incorporates a customized convolutional module that performs Takens' embedding, enabling the decoding of the underlying EEG activity without requiring explicit preprocessing. Further, the architecture estimates nonlinear and time-delayed interactions between cortical regions using Rational Quadratic kernels within a differentiable framework. Evaluation of TEKTE-Net on semi-synthetic causal benchmarks and the BCI Competition IV 2a dataset demonstrates robustness to low signal-to-noise conditions and interpretability through temporal, spatial, and spectral analyses of learned connectivity patterns. In particular, the model automatically highlights contralateral activations during MI and promotes spectral selectivity for the beta and gamma bands. Overall, TEKTE-Net offers a fully trainable estimator of functional brain connectivity for decoding EEG activity, supporting MI-BCI applications, and promoting interpretability of deep learning models.

</details>
