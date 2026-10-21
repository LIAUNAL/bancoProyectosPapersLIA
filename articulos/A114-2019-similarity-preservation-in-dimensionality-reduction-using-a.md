---
id: A114
titulo: "Similarity preservation in dimensionality reduction using a kernel-based cost function"
tipo: articulo
temas: [T13, T05]
cluster: "C10 Visión por computador y representación kernel"
palabras_clave: [reducción de dimensión, preservación de similitud, calidad del embebimiento, variedades, preservación de vecindades]
fuente_resumen: abstract
anio: 2019
revista: "Pattern Recognition Letters"
doi: 10.1016/j.patrec.2019.05.009
citas_openalex: 3
fuentes: [0000043222]
---

# Similarity preservation in dimensionality reduction using a kernel-based cost function

**Autores:** Sergio García-Vega, German Castellanos-Dominguez  
**Revista:** Pattern Recognition Letters (2019)  
**DOI:** https://doi.org/10.1016/j.patrec.2019.05.009  
**Temas:** T13 Representación de datos, reducción de dimensión y agrupamiento; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C10 Visión por computador y representación kernel

## Aplicación
Reducción de dimensión y análisis exploratorio de datos de alta dimensión.

## Problema de investigación
Es difícil medir la estructura de la variedad y cuantificar la preservación del embebimiento; las medidas basadas en divergencias (KL, JS) son las habituales.

## Propuesta o novedad
Se propone un método de reducción de dimensión que minimiza el desajuste entre espacios de alta y baja dimensión usando una función de costo basada en kernel para cuantificar la calidad del embebimiento, en lugar de divergencias.

## Resultados
En datos sintéticos y reales, por inspección visual y evaluación cuantitativa de preservación de vecindades, la propuesta preserva estructuras globales en el espacio de baja dimensión.

## Conclusiones principales
La función de costo basada en kernel es una alternativa efectiva a las divergencias para evaluar embebimientos.

## Métodos
- función de costo kernel
- reducción de dimensión
- preservación de vecindades

## Idea para trabajo futuro
Estudiar la selección automática del kernel y la escalabilidad del método a conjuntos de datos grandes.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Abstract Dimensionality reduction aims to preserve, as much as possible, the significant structure of high-dimensional data in the low-dimensional space. This allows removing noise and redundant features, which is useful in exploratory data analysis, classification, and regression tasks. There are two main challenges in dimensionality reduction: (1) how to measure the manifold structures; (2) how to quantify the embedding preservation. On the one hand, previous approaches try to measure the manifold structure using variance, dot product, distance, and similarity preservation. On the other hand, usually, the embedding quality is quantified using divergence-based measures such as Kullback–Leibler and Jensen–Shannon. We propose a dimensionality reduction method that minimizes the mismatch between high and low dimensional spaces. Unlike traditional dimensionality reduction formulations, the proposed approach uses a kernel-based cost function to quantify the embedding quality. Our approach is validated on both synthetic and real-world datasets. In terms of visual inspection and quantitative evaluation of neighborhood preservation, results show that our proposal preserves global data structures in the low-dimensional representation.

</details>
