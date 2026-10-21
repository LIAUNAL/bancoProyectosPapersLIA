---
id: A072
titulo: "Learning from multiple inconsistent and dependent annotators to support classification tasks"
tipo: articulo
temas: [T06, T05]
cluster: "C11 Aprendizaje con múltiples anotadores"
palabras_clave: [múltiples anotadores, alineamiento de kernel, relevancia de anotadores, aprendizaje desde multitudes]
fuente_resumen: abstract
anio: 2021
revista: "Neurocomputing"
doi: 10.1016/j.neucom.2020.10.045
citas_openalex: 11
fuentes: [0001330950]
---

# Learning from multiple inconsistent and dependent annotators to support classification tasks

**Autores:** Julián Gil-González, Alvaro Angel Orozco, Andrés Marino Álvarez-Meza  
**Revista:** Neurocomputing (2021)  
**DOI:** https://doi.org/10.1016/j.neucom.2020.10.045  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C11 Aprendizaje con múltiples anotadores

## Aplicación
Aprendizaje supervisado con múltiples anotadores inconsistentes y dependientes.

## Problema de investigación
No hay estándar de oro; los métodos asumen desempeño independiente del espacio de rasgos e independencia entre anotadores.

## Propuesta o novedad
Se introduce LKAAR, análisis de relevancia de anotadores basado en alineamiento de kernel localizado, que codifica la experticia como acople entre espacios de rasgos y etiquetas, considerando dependencias entre anotadores.

## Resultados
Los experimentos indican mejor desempeño de LKAAR en tareas de clasificación frente a alternativas del estado del arte.

## Conclusiones principales
Modelar la experticia como función del espacio de entrada y dependencias mejora el aprendizaje desde multitudes.

## Métodos
- alineamiento de kernel localizado
- análisis de relevancia

## Idea para trabajo futuro
Combinar LKAAR con procesos gaussianos para obtener incertidumbre sobre la experticia de cada anotador.

## Relacionados (similitud semántica)
- extiende: [[A120-2018-learning-from-multiple-annotators-using-kernel-alignment]] — Learning from multiple annotators using kernel alignment

<details><summary>Abstract</summary>

Abstract Training a supervised learning model requires a labeled dataset, where the labeling process is usually carried out by an expert to provide the ground truth/gold standard for each sample. However, in many applications, such a gold standard is not available. Instead, several real-world scenarios give us access to annotations provided by crowds, holding different and unknown levels of expertise. Thus, Learning from crowds is a subject undergoing intense study, and its main aim is to manage various machine learning paradigms in the presence of multiple annotators. Most of the state-of-the-art approaches reside on two key assumptions: i) the labeler’s performance does not depend on the input feature space, and ii) independence among the annotators is imposed. Here, we introduce a localized kernel alignment-based annotator relevance analysis (LKAAR) to code each labeler’s expertise as the matching between the feature and label spaces. Namely, LKAAR takes into account inter-annotators dependencies and models labelers’ knowledge as a function of the input feature space. Experimental results devoted to classification, show that LKAAR achieves suitable performances from inconsistent labelers, even if the gold standard is not available.

</details>
