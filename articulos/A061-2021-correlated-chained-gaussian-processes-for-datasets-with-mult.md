---
id: A061
titulo: "Correlated Chained Gaussian Processes for Datasets with Multiple Annotators"
tipo: articulo
temas: [T06]
cluster: "C11 Aprendizaje con múltiples anotadores"
palabras_clave: [múltiples anotadores, procesos gaussianos, aprendizaje desde multitudes, clasificación, regresión]
fuente_resumen: abstract
anio: 2021
revista: "IEEE Transactions on Neural Networks and Learning Systems"
doi: 10.1109/TNNLS.2021.3116943
citas_openalex: 5
fuentes: [0001330950]
---

# Correlated Chained Gaussian Processes for Datasets with Multiple Annotators

**Autores:** Julián Gil-González, Juan-José Giraldo, Andrés Marino Álvarez-Meza, Alvaro Angel Orozco, Mauricio A. Álvarez  
**Revista:** IEEE Transactions on Neural Networks and Learning Systems (2021)  
**DOI:** https://doi.org/10.1109/TNNLS.2021.3116943  
**Temas:** T06 Aprendizaje probabilístico y bayesiano  
**Clúster:** C11 Aprendizaje con múltiples anotadores

## Aplicación
Aprendizaje supervisado con etiquetas provenientes de múltiples anotadores (crowdsourcing) en clasificación y regresión.

## Problema de investigación
Los métodos de aprendizaje desde multitudes asumen que el desempeño del anotador no depende del espacio de entrada y que los anotadores son independientes.

## Propuesta o novedad
Se propone CCGPMA (procesos gaussianos encadenados correlacionados para múltiples anotadores), que modela el desempeño de cada anotador como función del espacio de entrada y aprovecha las correlaciones entre expertos.

## Resultados
En tareas de clasificación y regresión, CCGPMA modela mejor el comportamiento de los anotadores y supera de forma consistente a otros métodos del estado del arte.

## Conclusiones principales
Modelar dependencia de entrada y correlación entre anotadores mejora el aprendizaje desde multitudes.

## Métodos
- procesos gaussianos encadenados
- aprendizaje desde multitudes

## Idea para trabajo futuro
Escalar CCGPMA con inferencia variacional estocástica para conjuntos con miles de anotadores.

## Relacionados (similitud semántica)
- extiende: [[A097-2019-gaussian-processes-regression-with-multiple-annotators-when]] — Gaussian Processes Regression with Multiple Annotators: When the Annotator Performance Is Not Homogeneous

<details><summary>Abstract</summary>

The labeling process within a supervised learning task is usually carried out by an expert, which provides the ground truth (gold standard) for each sample. However, in many real-world applications, we typically have access to annotations provided by crowds holding different and unknown expertise levels. Learning from crowds (LFC) intends to configure machine learning paradigms in the presence of multilabelers, residing on two key assumptions: the labeler's performance does not depend on the input space, and independence among the annotators is imposed. Here, we propose the correlated chained Gaussian processes from the multiple annotators (CCGPMA) approach, which models each annotator's performance as a function of the input space and exploits the correlations among experts. Experimental results associated with classification and regression tasks show that our CCGPMA performs better modeling of the labelers' behavior, indicating that it consistently outperforms other state-of-the-art LFC approaches.

</details>
