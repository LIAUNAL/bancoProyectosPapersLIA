---
id: A043
titulo: "Affective Neural Responses Sonified through Labeled Correlation Alignment"
tipo: articulo
temas: [T01, T11, T05]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [sonificación, respuestas neuronales, generación musical, CKA, valor de sincronización de fase, BCI]
fuente_resumen: abstract
anio: 2023
revista: "Sensors"
doi: 10.3390/s23125574
citas_openalex: 1
fuentes: [0000043222, 0001330950]
---

# Affective Neural Responses Sonified through Labeled Correlation Alignment

**Autores:** Andrés Marino Álvarez-Meza, Héctor Fabio Torres-Cardona, Mauricio Orozco‐Alzate, Hernán Darío Pérez-Nastar, German Castellanos-Dominguez  
**Revista:** Sensors (2023)  
**DOI:** https://doi.org/10.3390/s23125574  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T11 Procesamiento de voz, audio y música; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Sonificación de respuestas neuronales afectivas para generación de música a partir de EEG.

## Problema de investigación
Los modelos de aprendizaje automático tienen dificultad para aprender estructuras musicales desde corpus arbitrarios y adaptarlas a un objetivo de composición.

## Propuesta o novedad
Labeled Correlation Alignment (LCA) en dos pasos: acoplamiento de características con conjuntos de etiquetas emocionales mediante CKA, seguido de análisis de correlación canónica para seleccionar representaciones multimodales. Combina PLV y conectividad funcional gaussiana para variabilidad inter/intrasujeto, y añade transformación inversa para explicación fisiológica.

## Resultados
Con la base Affective Music-Listening y un VQ-VAE que crea la envolvente acústica, el método genera música de bajo nivel desde actividad neuronal emocional manteniendo la distinguibilidad de las salidas.

## Conclusiones principales
LCA vincula características cerebrales con auditivas de forma interpretable.

## Métodos
- CKA
- CCA
- VQ-VAE
- PLV

## Idea para trabajo futuro
Evaluar perceptualmente la música sonificada con oyentes y explorar retroalimentación emocional en lazo cerrado.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P022-2020-brain-music-prototipo-de-interfaz-interactiva-para-generacio]] — Brain Music: Prototipo de interfaz interactiva para generación de piezas musicales basado respuestas eléctricas cerebrales y técnicas de composición atonal
- extendido por: [[A010-2025-eeg-based-music-emotion-prediction-using-supervised-feature]] — EEG-based music emotion prediction using supervised feature extraction for MIDI generation

<details><summary>Abstract</summary>

Sound synthesis refers to the creation of original acoustic signals with broad applications in artistic innovation, such as music creation for games and videos. Nonetheless, machine learning architectures face numerous challenges when learning musical structures from arbitrary corpora. This issue involves adapting patterns borrowed from other contexts to a concrete composition objective. Using Labeled Correlation Alignment (LCA), we propose an approach to sonify neural responses to affective music-listening data, identifying the brain features that are most congruent with the simultaneously extracted auditory features. For dealing with inter/intra-subject variability, a combination of Phase Locking Value and Gaussian Functional Connectivity is employed. The proposed two-step LCA approach embraces a separate coupling stage of input features to a set of emotion label sets using Centered Kernel Alignment. This step is followed by canonical correlation analysis to select multimodal representations with higher relationships. LCA enables physiological explanation by adding a backward transformation to estimate the matching contribution of each extracted brain neural feature set. Correlation estimates and partition quality represent performance measures. The evaluation uses a Vector Quantized Variational AutoEncoder to create an acoustic envelope from the tested Affective Music-Listening database. Validation results demonstrate the ability of the developed LCA approach to generate low-level music based on neural activity elicited by emotions while maintaining the ability to distinguish between the acoustic outputs.

</details>
