---
id: A009
titulo: "Transformer-Based Modeling of Directed Transfer Entropy Connectivity for EEG-Based ADHD Classification in Children"
tipo: articulo
temas: [T04, T02, T05]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [TDAH, EEG, entropía de transferencia, conectividad dirigida, Transformer, kernel cuadrático racional]
fuente_resumen: abstract
anio: 2026
revista: "Sensors"
doi: 10.3390/s26185786
citas_openalex: 0
fuentes: [scholar]
---

# Transformer-Based Modeling of Directed Transfer Entropy Connectivity for EEG-Based ADHD Classification in Children

**Autores:** Alejandra Gomez-Rivera, Julián David Pastrana-Cortés, Andrés Marino Álvarez-Meza, Julián Gil-González, David  Augusto Cardenas Peña  
**Revista:** Sensors (2026)  
**DOI:** https://doi.org/10.3390/s26185786  
**Temas:** T04 Bioseñales y soporte al diagnóstico clínico; T02 Conectividad cerebral e imagen de fuentes neuronales; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Clasificación de TDAH infantil con EEG mediante conectividad dirigida por entropía de transferencia.

## Problema de investigación
La no estacionariedad del EEG genera gran variabilidad entre ventanas de un mismo participante y predicciones inconsistentes.

## Propuesta o novedad
CTE-Net, una red de extremo a extremo que contextualiza cada ventana multicanal con un codificador Transformer, aplica filtros temporales no lineales y embeddings de Takens, y estima entropía de transferencia dirigida diferenciable entre pares de electrodos usando entropía alfa de Rényi y kernel cuadrático racional.

## Resultados
En un conjunto pediátrico público de 120 participantes, a nivel de ventana logró exactitud de 80.9±1.7%; a nivel de participante, 83.4% de exactitud y 90.2% de ROC-AUC. La entropía de transferencia redujo la dispersión intrasujeto en una mediana de 38.35% frente al EEG crudo.

## Conclusiones principales
Los resultados, sobre un solo conjunto, respaldan a CTE-Net como marco compacto e interpretable para representar interacciones dirigidas.

## Métodos
- entropía de transferencia
- Rényi
- Transformer
- embedding de Takens

## Idea para trabajo futuro
Validar CTE-Net en conjuntos independientes y examinar si la conectividad dirigida aprendida se relaciona con subtipos clínicos de TDAH.

## Relacionados (similitud semántica)
- extiende: [[A026-2025-takens-based-kernel-transfer-entropy-connectivity-network-fo]] — Takens-Based Kernel Transfer Entropy Connectivity Network for Motor Imagery Classification

<details><summary>Abstract</summary>

Electroencephalography (EEG) provides a non-invasive and cost-effective tool for supporting the assessment of attention-deficit/hyperactivity disorder (ADHD). However, the nonstationary nature of EEG produces substantial variability among signal windows recorded from the same participant, which can obscure diagnostic structure and lead to inconsistent predictions. To address this problem, we propose the Contextualized Transfer Entropy Network (CTE-Net), an end-to-end deep-learning architecture that combines global content-based contextualization with nonlinear and directed EEG connectivity estimation. CTE-Net first employs a Transformer encoder to contextualize the multichannel representations within each EEG window. The resulting signals are processed using channel-wise nonlinear temporal filters and Takens delay-coordinate embeddings. A differentiable matrix-based Transfer Entropy module, formulated using Rényi's α-entropy and a rational quadratic kernel, then estimates directed predictive information dependencies between all ordered electrode pairs. The resulting connectivity coefficients are used for ADHD-versus-control classification. The model was evaluated on a publicly available pediatric EEG dataset comprising 120 participants, equally divided between ADHD and control groups, using five fixed subject-wise folds and ten random training repetitions. At the window level, CTE-Net achieved an accuracy of 80.9±1.7%, precision of 82.7±2.1%, and sensitivity of 84.2±2.3%. At the participant level, it achieved an accuracy of 83.4% (95% CI: 78.2-88.2) and an ROC-AUC of 90.2% (95% CI: 85.1-94.6), demonstrating competitive and comparatively balanced classification performance. Beyond classification performance, the directed Transfer Entropy representation exhibited the lowest within-subject dispersion among the analyzed representation stages, with a median reduction of 38.35% relative to raw EEG. This reduction remained consistent across different PCA dimensionalities and distance definitions. These single-dataset findings support CTE-Net as a compact and interpretable methodological framework for representing directed EEG interactions while attenuating window-specific variability within individual participants.

</details>
