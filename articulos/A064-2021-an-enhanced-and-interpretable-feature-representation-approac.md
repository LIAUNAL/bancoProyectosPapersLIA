---
id: A064
titulo: "An enhanced and interpretable feature representation approach to support shape classification from binary images"
tipo: articulo
temas: [T08, T05]
cluster: "C10 Visión por computador y representación kernel"
palabras_clave: [clasificación de formas, imágenes binarias, fragmentos de contorno, ReliefF, alineamiento de kernel, interpretabilidad]
fuente_resumen: abstract
anio: 2021
revista: "Pattern Recognition Letters"
doi: 10.1016/j.patrec.2021.08.020
citas_openalex: 6
fuentes: [0001330950]
---

# An enhanced and interpretable feature representation approach to support shape classification from binary images

**Autores:** J. S. Blandon, Alvaro Angel Orozco, Andrés Marino Álvarez-Meza  
**Revista:** Pattern Recognition Letters (2021)  
**DOI:** https://doi.org/10.1016/j.patrec.2021.08.020  
**Temas:** T08 Visión por computador y análisis de video; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C10 Visión por computador y representación kernel

## Aplicación
Clasificación de formas a partir de imágenes binarias en visión por computador.

## Problema de investigación
Los descriptores de contorno y estructura generan espacios de alta dimensión que reducen el desempeño y la interpretabilidad.

## Propuesta o novedad
Se introduce EIFR: bolsa de fragmentos de contorno (robusta a oclusión y deformación), selección con ReliefF y proyección por alineamiento de kernel que mide relevancia entre una matriz de similitud y un kernel de etiquetas.

## Resultados
En conjuntos de referencia, EIFR mejora los resultados de enfoques basados en curvatura.

## Conclusiones principales
EIFR ofrece un espacio de rasgos más compacto e interpretable.

## Métodos
- ReliefF
- alineamiento de kernel
- bolsa de fragmentos

## Idea para trabajo futuro
Evaluar EIFR en formas 3D o imágenes con ruido fuerte para probar su robustez a oclusión.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Abstract Shape classification from binary images is a challenging task within the computer vision community. Commonly, contour and structural features are computed to describe the objects and code patterns robust against rotation, scaling, and shape deformation. However, current techniques get a high-dimensional feature space decreasing the system performance and the attribute interpretability. Here, we introduce an enhanced and interpretable feature representation approach to support shape classification from binary images. Our method, named EIFR, employs a bag of contour fragments-based feature estimation, intrinsically robust to occlusion and shape deformation. Then, a ReliefF-based feature selection is applied to filter non-discriminative attributes. In turn, a kernel-alignment-based projection is used to measure the feature relevance enhancing the data representation through the matching between a similarity matrix computed from filtered attributes and a kernel matrix built from the shape labels. Attained results on benchmark datasets prove that EIFR improves the curvature-based features’ interpretability and favors the classification performance.

</details>
