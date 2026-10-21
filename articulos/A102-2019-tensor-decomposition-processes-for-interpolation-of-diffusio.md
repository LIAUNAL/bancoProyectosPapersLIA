---
id: A102
titulo: "Tensor decomposition processes for interpolation of diffusion magnetic resonance imaging"
tipo: articulo
temas: [T03, T13]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [resonancia de difusión, tensores de orden superior, interpolación de tensores, descomposición Tucker, descomposición canónica, modelos probabilísticos]
fuente_resumen: abstract
anio: 2019
revista: "Expert Systems with Applications"
doi: 10.1016/j.eswa.2018.10.005
citas_openalex: 5
fuentes: [0001330950]
---

# Tensor decomposition processes for interpolation of diffusion magnetic resonance imaging

**Autores:** Hernán Darío Vargas Cardona, Alvaro Angel Orozco, Andrés Marino Álvarez-Meza, Mauricio A. Álvarez  
**Revista:** Expert Systems with Applications (2019)  
**DOI:** https://doi.org/10.1016/j.eswa.2018.10.005  
**Temas:** T03 Imagen médica y neuroimagen; T13 Representación de datos, reducción de dimensión y agrupamiento  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Interpolación de imágenes de resonancia de difusión (dMRI) con tensores de orden superior.

## Problema de investigación
Los tensores de orden 2 no representan fibras cruzadas, la resolución es mayor al tamaño de estructuras, y falta generalización para tensores de orden superior.

## Propuesta o novedad
Se proponen procesos de descomposición tensorial (Tucker, canónica) con modelos probabilísticos para interpolar tensores de orden superior (4 y 6).

## Resultados
El resumen visible expone el problema y el uso de descomposición tensorial; sin cifras.

## Conclusiones principales
La descomposición tensorial generaliza la interpolación a tensores de orden superior.

## Métodos
- descomposición Tucker
- descomposición canónica
- interpolación de tensores

## Idea para trabajo futuro
Evaluar el impacto de la interpolación en tractografía de fibras cruzadas.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Abstract Diffusion magnetic resonance imaging (dMRI) is an established medical technique used for describing water diffusion in an organic tissue. Typically, rank-2 or 2nd-order tensors quantify this diffusion. From this quantification, it is possible to calculate relevant scalar measures (i.e. fractional anisotropy) employed in the clinical diagnosis of neurological diseases. Nonetheless, 2nd-order tensors fail to represent complex tissue structures like crossing fibers. To overcome this limitation, several researchers proposed a diffusion representation with higher order tensors (HOT), specifically 4th and 6th orders. However, the current acquisition protocols of dMRI data allow images with a spatial resolution between 1 mm3 and 2 mm3, and this voxel size is much bigger than tissue structures. Therefore, several clinical procedures derived from dMRI may be inaccurate. Concerning this, interpolation has been used to enhance the resolution of dMRI in a tensorial space. Most interpolation methods are valid only for rank-2 tensors and a generalization for HOT data is missing. In this work, we propose a probabilistic framework for performing HOT data interpolation. In particular, we introduce two novel probabilistic models based on the Tucker and the canonical decompositions. We call our approaches: Tucker decomposition process (TDP) and canonical decomposition process (CDP). We test the TDP and CDP in rank-2, 4 and 6 HOT fields. For rank-2 tensors, we compare against direct interpolation, log-Euclidean approach, and Generalized Wishart processes. For rank-4 and 6 tensors, we compare against direct interpolation and raw dMRI interpolation. Results obtained show that TDP and CDP interpolate accurately the HOT fields in terms of Frobenius distance, anisotropy measurements, and fiber tracts. Besides, CDP and TDP can be generalized to any rank. Also, the proposed framework keeps the mandatory constraint of positive definite tensors, and preserves morphological properties such as fractional anisotropy (FA), generalized anisotropy (GA) and tractography.

</details>
