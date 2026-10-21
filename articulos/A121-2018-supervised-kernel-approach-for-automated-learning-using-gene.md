---
id: A121
titulo: "Supervised kernel approach for automated learning using General Stochastic Networks"
tipo: articulo
temas: [T07, T05]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [redes estocásticas generales, alineamiento de kernel centrado, autoencoder, preentrenamiento supervisado, clasificación de imágenes]
fuente_resumen: abstract
anio: 2018
revista: "Engineering Applications of Artificial Intelligence"
doi: 10.1016/j.engappai.2017.10.003
citas_openalex: 8
fuentes: [0000043222, 0001330950]
---

# Supervised kernel approach for automated learning using General Stochastic Networks

**Autores:** David  Augusto Cardenas Peña, Diego Fabián Collazos-Huertas, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Engineering Applications of Artificial Intelligence (2018)  
**DOI:** https://doi.org/10.1016/j.engappai.2017.10.003  
**Temas:** T07 Aprendizaje profundo y explicabilidad; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Aprendizaje automático profundo para clasificación de imágenes y reconocimiento de objetos.

## Problema de investigación
El ajuste fino de redes estocásticas generales (GSN) es un problema de optimización no convexo y lento.

## Propuesta o novedad
Se propone un preentrenamiento supervisado por capas que inicializa el ajuste fino de la GSN con matrices de proyección más discriminativas, usando alineamiento de kernel centrado.

## Resultados
El abstract indica mayor velocidad de convergencia, captura de dependencias complejas entre parámetros y favorecimiento de la discriminación entre clases.

## Conclusiones principales
El preentrenamiento supervisado con CKA facilita la optimización de GSN.

## Métodos
- GSN
- CKA
- autoencoder de eliminación de ruido

## Idea para trabajo futuro
Aplicar el preentrenamiento supervisado a arquitecturas convolucionales modernas.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

A novel supervised layer-wise pre-training that initializes the fine tuning stage of the GSN with more discriminative projection matrices favoring the optimization of the non-convex cost function and captures the complex dependencies between parameters, increases the convergence speed in the learning stage, and unravels the data distribution to favor the class discrimination.

</details>
