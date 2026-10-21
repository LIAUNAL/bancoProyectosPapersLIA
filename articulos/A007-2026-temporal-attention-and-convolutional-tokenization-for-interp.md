---
id: A007
titulo: "Temporal Attention and Convolutional Tokenization for Interpretable EEG-Based ADHD Identification in Children"
tipo: articulo
temas: [T04, T01, T07]
cluster: "C04 EEG, TDAH y soporte diagnóstico"
palabras_clave: [TDAH, EEG, atención temporal, EEGNet, Transformer, evaluación independiente del sujeto]
fuente_resumen: abstract
anio: 2026
revista: "Technologies"
doi: 10.3390/technologies14070392
citas_openalex: 0
fuentes: [0001330950]
---

# Temporal Attention and Convolutional Tokenization for Interpretable EEG-Based ADHD Identification in Children

**Autores:** Julián David Pastrana-Cortés, Alejandra Gomez-Rivera, Andrés Marino Álvarez-Meza, Julián Gil-González, David  Augusto Cardenas Peña  
**Revista:** Technologies (2026)  
**DOI:** https://doi.org/10.3390/technologies14070392  
**Temas:** T04 Bioseñales y soporte al diagnóstico clínico; T01 Interfaces cerebro-computador y decodificación EEG; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C04 EEG, TDAH y soporte diagnóstico

## Aplicación
Identificación de niños con TDAH a partir de épocas EEG, con evaluación independiente de sujeto.

## Problema de investigación
La clasificación robusta e independiente del sujeto sigue siendo difícil por variabilidad intersujeto, datos limitados y necesidad de interpretabilidad.

## Propuesta o novedad
EEG-TACT, una arquitectura compacta de extremo a extremo que integra un embedding convolucional tipo EEGNet, un codificador Transformer y pooling por atención. Se evalúa con particiones estratificadas por grupo sin compartir sujetos entre entrenamiento, validación y prueba.

## Resultados
En un conjunto EEG público, alcanzó exactitud de 87.5%, recall de 96.0% y precisión de 82.8% a nivel de sujeto con pocos miles de parámetros. Obtuvo el mejor ranking promedio frente a arquitecturas de referencia, y un estudio de ablación cuantificó cada componente.

## Conclusiones principales
EEG-TACT es un modelo compacto, robusto e interpretable para TDAH bajo evaluación independiente del sujeto.

## Métodos
- EEGNet
- Transformer
- pooling por atención
- ablación

## Idea para trabajo futuro
Probar EEG-TACT en cohortes multicéntricas y con tareas distintas para evaluar su estabilidad clínica.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Attention Deficit Hyperactivity Disorder (ADHD) is a prevalent neurodevelopmental condition commonly assessed through clinical interviews, behavioral observation, and rating scales. Although electroencephalography (EEG) has emerged as a promising complementary tool for ADHD assessment, robust subject-independent classification remains challenging due to inter-subject variability, limited datasets, and the need for interpretable computational models. This work introduces EEG-TACT, a compact end-to-end deep learning architecture for identifying ADHD subjects from EEG epochs. The proposed model integrates an EEGNet-inspired convolutional embedding, a Transformer encoder operator, and an attention-based pooling mechanism to jointly capture local spatiotemporal EEG patterns, contextual temporal dependencies, and task-relevant latent representations. EEG-TACT was evaluated on a publicly available EEG dataset using strict, subject-independent stratified group partitions, ensuring that data from the same subject were never shared across the training, validation, and test subsets. Model interpretability is examined through learned temporal filter responses, class-conditioned self-attention maps, and latent-space projections, while an ablation study quantifies the contribution of each architectural component. Performance was assessed at the fold, subject, and epoch levels, together with statistical significance comparisons against representative state-of-the-art architectures. EEG-TACT outperformed the contrasted models, achieving subject-level accuracy of 87.5%, recall of 96.0%, and precision of 82.8%, while requiring only a few thousand trainable parameters. By exhaustively repeating the initialization, the proposed model demonstrated improved labeling reliability and achieved the best average ranking among the evaluated architectures. The reported results therefore prove that EEG-TACT provides a compact, robust, and interpretable model for EEG-based ADHD identification under subject-independent evaluation settings.

</details>
