---
id: A087
titulo: "Analysis and Classification of MoCap Data by Hilbert Space Embedding-Based Distance and Multikernel Learning"
tipo: articulo
temas: [T08, T05]
cluster: "C10 Visión por computador y representación kernel"
palabras_clave: [captura de movimiento, filtros adaptativos de kernel, MMD, aprendizaje multikernel, biomecánica]
fuente_resumen: abstract
anio: 2019
revista: "Lecture notes in computer science"
doi: 10.1007/978-3-030-13469-3_22
citas_openalex: 3
fuentes: [0000043222, 0001330950]
---

# Analysis and Classification of MoCap Data by Hilbert Space Embedding-Based Distance and Multikernel Learning

**Autores:** Juan Diego Pulgarin-Giraldo, Andrés Marino Álvarez-Meza, Steven Van Vaerenbergh, Ignacio Santamarı́a, German Castellanos-Dominguez  
**Revista:** Lecture notes in computer science (2019)  
**DOI:** https://doi.org/10.1007/978-3-030-13469-3_22  
**Temas:** T08 Visión por computador y análisis de video; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C10 Visión por computador y representación kernel

## Aplicación
Clasificación de datos de captura de movimiento (MoCap) de golpes de tenis.

## Problema de investigación
Los datos MoCap son multicanal y dinámicos, requiriendo representar la dinámica de cada canal y su relevancia.

## Propuesta o novedad
Se combina un filtro adaptativo de kernel (KAF) para extraer la dinámica de cada canal con el criterio de discrepancia media máxima (MMD) y alineamiento de kernel centrado (CKA) para ponderar su relevancia en clasificación multikernel.

## Resultados
En una base de jugadores de tenis se logra buena exactitud de clasificación de golpes y la relevancia por canal concuerda con hallazgos biomecánicos.

## Conclusiones principales
KAF junto con CKA genera una representación adecuada de dinámicas relevantes.

## Métodos
- KAF
- MMD
- CKA
- aprendizaje multikernel

## Idea para trabajo futuro
Evaluar la representación en otros deportes y en análisis de rehabilitación.

## Relacionados (similitud semántica)
- extendido por: [[A065-2021-an-enhanced-joint-hilbert-embedding-based-metric-to-support]] — An enhanced joint Hilbert embedding-based metric to support mocap data classification with preserved interpretability

<details><summary>Abstract</summary>

A framework is presented to carry out prediction and classification of Motion Capture (MoCap) multichannel data, based on kernel adaptive filters and multi-kernel learning. To this end, a Kernel Adaptive Filter (KAF) algorithm extracts the dynamic of each channel, relying on the similarity between multiple realizations through the Maximum Mean Discrepancy (MMD) criterion. To assemble dynamics extracted from all MoCap data, center kernel alignment (CKA) is used to assess the contribution of each to the classification tasks (that is, its relevance). Validation is performed on a database of tennis players, performing a good classification accuracy of the considered stroke classes. Besides, we find that the relevance of each channel agrees with the findings reported in the biomechanical analysis. Therefore, the combination of KAF together with CKA allows building a proper representation for extracting relevant dynamics from multiple-channel MoCap data.

</details>
