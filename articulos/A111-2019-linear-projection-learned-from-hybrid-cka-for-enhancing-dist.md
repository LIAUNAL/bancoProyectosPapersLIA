---
id: A111
titulo: "Linear Projection Learned from Hybrid CKA for Enhancing Distance-Based Classifiers"
tipo: articulo
temas: [T05, T13]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [alineamiento de kernel centrado, proyección lineal, función de costo híbrida, k vecinos más cercanos, dígitos manuscritos]
fuente_resumen: abstract
anio: 2019
revista: "Lecture notes in computer science"
doi: 10.1007/978-3-030-13469-3_12
citas_openalex: 0
fuentes: [0000043222]
---

# Linear Projection Learned from Hybrid CKA for Enhancing Distance-Based Classifiers

**Autores:** Diego Fabián Collazos-Huertas, David  Augusto Cardenas Peña, German Castellanos-Dominguez  
**Revista:** Lecture notes in computer science (2019)  
**DOI:** https://doi.org/10.1007/978-3-030-13469-3_12  
**Temas:** T05 Métodos kernel y aprendizaje basado en teoría de la información; T13 Representación de datos, reducción de dimensión y agrupamiento  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Clasificadores basados en distancia (p. ej., k-NN) para reconocimiento de dígitos manuscritos.

## Problema de investigación
Los clasificadores por distancia dependen de una buena representación; las proyecciones puramente discriminativas pueden descuidar la estructura de los datos.

## Propuesta o novedad
Se propone aprender una proyección lineal con una función de costo híbrida basada en alineamiento de kernel centrado (CKA): un término discriminativo que mide la afinidad entre datos proyectados y etiquetas, y un término generativo que mide la similitud entre las distribuciones de entrada y proyectada.

## Resultados
El abstract describe la función de costo propuesta; no reporta cifras específicas.

## Conclusiones principales
La combinación de componentes discriminativo y generativo mejora la proyección para clasificadores por distancia.

## Métodos
- CKA
- proyección lineal
- k-NN

## Idea para trabajo futuro
Explorar el balance automático entre los términos discriminativo y generativo y extender la proyección a versiones no lineales.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

A new hybrid cost function based on the linear combination of two computed terms: a discriminative component that accounts for the affinity between projected data and their labels, and a generative part that measures the similarity between the input and projected distributions is proposed.

</details>
