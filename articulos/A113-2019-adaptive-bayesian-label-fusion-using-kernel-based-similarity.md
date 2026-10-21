---
id: A113
titulo: "Adaptive Bayesian label fusion using kernel-based similarity metrics in hippocampus segmentation"
tipo: articulo
temas: [T03, T05]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [segmentación de hipocampo, fusión de etiquetas bayesiana, atlas, kernel tensorial, resonancia magnética, ADNI]
fuente_resumen: abstract
anio: 2019
revista: "Journal of medical imaging"
doi: 10.1117/1.JMI.6.1.014003
citas_openalex: 4
fuentes: [0000043222]
---

# Adaptive Bayesian label fusion using kernel-based similarity metrics in hippocampus segmentation

**Autores:** David  Augusto Cardenas Peña, Andres Tobar-Rodríguez, German Castellanos-Dominguez  
**Revista:** Journal of medical imaging (2019)  
**DOI:** https://doi.org/10.1117/1.JMI.6.1.014003  
**Temas:** T03 Imagen médica y neuroimagen; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Segmentación de hipocampo en resonancia magnética cerebral.

## Problema de investigación
La segmentación depende de manejar la variabilidad anatómica entre sujetos y la baja diferenciación entre tejidos.

## Propuesta o novedad
Se propone fusión bayesiana adaptativa de etiquetas con priors probabilísticos específicos del objetivo, construidos con atlas ordenados mediante métricas de similitud basadas en kernel. Incluye representación de vóxeles por parches, modelo dependiente de la vecindad y una métrica kernel tensorial que usa también las etiquetas de entrenamiento.

## Resultados
Evaluada en cinco colecciones de referencia de RM, incluida ADNI, la propuesta obtiene mayor desempeño medido con el índice Dice frente a trabajos recientes.

## Conclusiones principales
La selección adaptativa de atlas con similitud kernel mejora la segmentación del hipocampo.

## Métodos
- fusión bayesiana de etiquetas
- métrica kernel tensorial
- segmentación por parches

## Idea para trabajo futuro
Aplicar el esquema a otras estructuras cerebrales y evaluar su costo computacional frente a redes profundas de segmentación.

## Relacionados (similitud semántica)
- extendido por: [[A047-2023-hippocampus-segmentation-using-patch-based-representation-an]] — Hippocampus Segmentation using Patch-based Representation and ROC Label Enhancement

<details><summary>Abstract</summary>

The effectiveness of brain magnetic resonance imaging (MRI) as a useful evaluation tool strongly depends on the performed segmentation of associated tissues or anatomical structures. We introduce an enhanced brain segmentation approach of Bayesian label fusion that includes the construction of adaptive target-specific probabilistic priors using atlases ranked by kernel-based similarity metrics to deal with the anatomical variability of collected MRI data. In particular, the developed segmentation approach appraises patch-based voxel representation to enhance the voxel embedding in spaces with increased tissue discrimination, as well as the construction of a neighborhood-dependent model that addresses the label assignment of each region with a different patch complexity. To measure the similarity between the target and training atlases, we propose a tensor-based kernel metric that also includes the training labeling set. We evaluate the proposed approach, adaptive Bayesian label fusion using kernel-based similarity metrics, in the specific case of hippocampus segmentation of five benchmark MRI collections, including ADNI dataset, resulting in an increased performance (assessed through the Dice index) as compared to other recent works.

</details>
