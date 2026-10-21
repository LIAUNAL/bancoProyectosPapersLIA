---
id: A032
titulo: "Fast Semi-Supervised t-SNE for Transfer Function Enhancement in Direct Volume Rendering-Based Medical Image Visualization"
tipo: articulo
temas: [T13, T03]
cluster: "C10 Visión por computador y representación kernel"
palabras_clave: [función de transferencia, renderizado directo de volumen, visualización médica, t-SNE semisupervisado, segmentación de volumen, reducción de dimensión]
fuente_resumen: abstract
anio: 2024
revista: "Mathematics"
doi: 10.3390/math12121885
citas_openalex: 2
fuentes: [0001330950]
---

# Fast Semi-Supervised t-SNE for Transfer Function Enhancement in Direct Volume Rendering-Based Medical Image Visualization

**Autores:** Walter Serna Serna, Andrés Marino Álvarez-Meza, Alvaro Angel Orozco  
**Revista:** Mathematics (2024)  
**DOI:** https://doi.org/10.3390/math12121885  
**Temas:** T13 Representación de datos, reducción de dimensión y agrupamiento; T03 Imagen médica y neuroimagen  
**Clúster:** C10 Visión por computador y representación kernel

## Aplicación
Visualización médica por renderizado directo de volumen (DVR) en RM y TC, con diseño de funciones de transferencia.

## Problema de investigación
Los voxels vecinos aportan características con relaciones complejas, y las etiquetas son costosas en grandes volúmenes médicos.

## Propuesta o novedad
FSS.t-SNE, una versión rápida y semisupervisada de t-SNE con preservación multiescala de vecindarios, que genera dominios 2D de funciones de transferencia. Usa etiquetas parciales, separa trayectorias entre subvolúmenes y aplica Barnes-Hut para reducir la complejidad de O(N^2) a O(N log N).

## Resultados
Funciona con cientos de miles de voxels sin hacinamiento y con mejor separación en el histograma 2D frente a dominios tradicionales; los experimentos muestran desempeño prometedor en segmentación de volumen e inspección visual.

## Conclusiones principales
FSS.t-SNE mejora la exploración de bordes y transiciones entre subvolúmenes, aunque requiere generar el dominio 2D a partir de varias características.

## Métodos
- t-SNE semisupervisado
- Barnes-Hut
- DVR
- reducción de dimensión multiescala

## Idea para trabajo futuro
Automatizar la selección de funciones de transferencia con el espacio incrustado para uso interactivo en tiempo real por radiólogos.

## Relacionados (similitud semántica)
- extiende: [[A048-2023-semi-supervised-t-sne-with-multi-scale-neighborhood-preserva]] — Semi-supervised t-SNE with multi-scale neighborhood preservation

<details><summary>Abstract</summary>

Magnetic resonance imaging and computed tomography produce three-dimensional volumetric medical images. While a scalar value represents each individual volume element, or voxel, volumetric data are characterized by features derived from groups of neighboring voxels and their inherent relationships, which may vary depending on the specific clinical application. Labeled samples are also required in most applications, which can be problematic for large datasets such as medical images. We propose a direct volume rendering (DVR) framework based on multi-scale dimensionality reduction neighbor embedding that generates two-dimensional transfer function (TF) domains. In this way, we present FSS.t-SNE, a fast semi-supervised version of the t-distributed stochastic neighbor embedding (t-SNE) method that works over hundreds of thousands of voxels without the problem of crowding and with better separation in a 2D histogram compared to traditional TF domains. Our FSS.t-SNE scatters voxels of the same sub-volume in a wider region through multi-scale neighbor embedding, better preserving both local and global data structures and allowing for its internal exploration based on the original features of the multi-dimensional space, taking advantage of the partially provided labels. Furthermore, FSS.t-SNE untangles sample paths among sub-volumes, allowing us to explore edges and transitions. In addition, our approach employs a Barnes–Hut approximation to reduce computational complexity from O(N2) (t-SNE) to O(NlogN). Although we require the additional step of generating the 2D TF domain from multiple features, our experiments show promising performance in volume segmentation and visual inspection.

</details>
