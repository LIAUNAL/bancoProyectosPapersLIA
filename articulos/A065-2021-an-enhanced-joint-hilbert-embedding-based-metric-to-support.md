---
id: A065
titulo: "An enhanced joint Hilbert embedding-based metric to support mocap data classification with preserved interpretability"
tipo: articulo
temas: [T08, T05]
cluster: "C10 Visión por computador y representación kernel"
palabras_clave: [espacio de Hilbert con kernel reproductor, captura de movimiento, distribución conjunta, reconocimiento de acciones, interpretabilidad]
fuente_resumen: abstract
anio: 2021
revista: "Sensors"
doi: 10.3390/s21134443
citas_openalex: 9
fuentes: [0000043222, 0001330950]
---

# An enhanced joint Hilbert embedding-based metric to support mocap data classification with preserved interpretability

**Autores:** Cristian Kaori Valencia-Marin, Juan Diego Pulgarin-Giraldo, Luisa Fernanda Velasquez-Martinez, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Sensors (2021)  
**DOI:** https://doi.org/10.3390/s21134443  
**Temas:** T08 Visión por computador y análisis de video; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C10 Visión por computador y representación kernel

## Aplicación
Clasificación de datos de captura de movimiento (Mocap) para animación, biomecánica y rehabilitación.

## Problema de investigación
Clasificar series multicanal Mocap requiere codificar dependencias no lineales entre articulaciones y manejar variabilidad entre clases e individuos.

## Propuesta o novedad
Se propone EHECCO, que mapea las series Mocap a un espacio tensorial construido con articulaciones 3D y proyección PCA, usando incrustación de Hilbert basada en un operador de covarianza cruzada.

## Resultados
EHECCO discrimina distribuciones conjuntas en un RKHS tensorial y logra resultados competitivos en reconocimiento de estilo, sujeto y acción en bases conocidas.

## Conclusiones principales
El método conserva interpretabilidad respecto a variables antropométricas.

## Métodos
- incrustación de Hilbert
- operador de covarianza cruzada
- RKHS tensorial
- PCA

## Idea para trabajo futuro
Aplicar EHECCO a rehabilitación para cuantificar desviaciones del gesto respecto a un patrón sano.

## Relacionados (similitud semántica)
- extiende: [[A087-2019-analysis-and-classification-of-mocap-data-by-hilbert-space-e]] — Analysis and Classification of MoCap Data by Hilbert Space Embedding-Based Distance and Multikernel Learning

<details><summary>Abstract</summary>

Motion capture (Mocap) data are widely used as time series to study human movement. Indeed, animation movies, video games, and biomechanical systems for rehabilitation are significant applications related to Mocap data. However, classifying multi-channel time series from Mocap requires coding the intrinsic dependencies (even nonlinear relationships) between human body joints. Furthermore, the same human action may have variations because the individual alters their movement and therefore the inter/intraclass variability. Here, we introduce an enhanced Hilbert embedding-based approach from a cross-covariance operator, termed EHECCO, to map the input Mocap time series to a tensor space built from both 3D skeletal joints and a principal component analysis-based projection. Obtained results demonstrate how EHECCO represents and discriminates joint probability distributions as kernel-based evaluation of input time series within a tensor reproducing kernel Hilbert space (RKHS). Our approach achieves competitive classification results for style/subject and action recognition tasks on well-known publicly available databases. Moreover, EHECCO favors the interpretation of relevant anthropometric variables correlated with players' expertise and acted movement on a Tennis-Mocap database (also publicly available with this work). Thereby, our EHECCO-based framework provides a unified representation (through the tensor RKHS) of the Mocap time series to compute linear correlations between a coded metric from joint distributions and player properties, i.e., age, body measurements, and sport movement (action class).

</details>
