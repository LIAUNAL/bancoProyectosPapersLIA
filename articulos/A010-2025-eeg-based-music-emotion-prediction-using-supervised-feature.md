---
id: A010
titulo: "EEG-based music emotion prediction using supervised feature extraction for MIDI generation"
tipo: articulo
temas: [T01, T11, T05]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [emoción musical, EEG, generación MIDI, composición algorítmica, EEGNet, alineamiento kernel centrado]
fuente_resumen: abstract
anio: 2025
revista: "Sensors"
doi: 10.3390/s25051471
citas_openalex: 6
fuentes: [0001330950]
---

# EEG-based music emotion prediction using supervised feature extraction for MIDI generation

**Autores:** Óscar Wladimir Gómez Morales, Hernán Darío Pérez-Nastar, Andrés Marino Álvarez-Meza, Héctor Fabio Torres-Cardona, German Castellanos-Dominguez  
**Revista:** Sensors (2025)  
**DOI:** https://doi.org/10.3390/s25051471  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T11 Procesamiento de voz, audio y música; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Generación de secuencias MIDI alineadas con emociones predichas desde EEG, para composición algorítmica.

## Problema de investigación
Existe una brecha semántica entre características neuronales de bajo nivel y conceptos musicales de alto nivel que dificulta alinear ambos dominios.

## Propuesta o novedad
Un marco de aprendizaje profundo con extracción supervisada de características: EEGNet para el EEG y un autoencoder de piano para el audio, con Centered Kernel Alignment (CKA) para separar estados emocionales. Aplica regresión entre dominios para reducir la variabilidad intrasujeto y agrupa las representaciones latentes auditivas.

## Resultados
Con métricas musicales sobre datos reales, mejora la clasificación de emoción (arousal y valencia) y genera MIDI con mejor alineación temporal, consistencia tonal e integridad estructural. Los sujetos con paradigmas de imaginería más fuertes produjeron MIDI de mejor calidad.

## Conclusiones principales
El desempeño depende de la consistencia de los patrones neuronales y auditivos de cada sujeto.

## Métodos
- EEGNet
- autoencoder
- CKA
- clustering

## Idea para trabajo futuro
Incorporar evaluación perceptual con oyentes para validar que la música generada refleja el estado emocional objetivo.

## Relacionados (similitud semántica)
- extiende: [[A043-2023-affective-neural-responses-sonified-through-labeled-correlat]] — Affective Neural Responses Sonified through Labeled Correlation Alignment

<details><summary>Abstract</summary>

Advancements in music emotion prediction are driving AI-driven algorithmic composition, enabling the generation of complex melodies. However, bridging neural and auditory domains remains challenging due to the semantic gap between brain-derived low-level features and high-level musical concepts, making alignment computationally demanding. This study proposes a deep learning framework for generating MIDI sequences aligned with labeled emotion predictions through supervised feature extraction from neural and auditory domains. EEGNet is employed to process neural data, while an autoencoder-based piano algorithm handles auditory data. To address modality heterogeneity, Centered Kernel Alignment is incorporated to enhance the separation of emotional states. Furthermore, regression between feature domains is applied to reduce intra-subject variability in extracted Electroencephalography (EEG) patterns, followed by the clustering of latent auditory representations into denser partitions to improve MIDI reconstruction quality. Using musical metrics, evaluation on real-world data shows that the proposed approach improves emotion classification (namely, between arousal and valence) and the system's ability to produce MIDI sequences that better preserve temporal alignment, tonal consistency, and structural integrity. Subject-specific analysis reveals that subjects with stronger imagery paradigms produced higher-quality MIDI outputs, as their neural patterns aligned more closely with the training data. In contrast, subjects with weaker performance exhibited auditory data that were less consistent.

</details>
