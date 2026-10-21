---
id: A006
titulo: "Learning from Crowds Using a Focal Loss Function: Dealing with Imbalanced Annotations"
tipo: articulo
temas: [T06, T05]
cluster: "C11 Aprendizaje con múltiples anotadores"
palabras_clave: [crowdsourcing, desbalance de clases, focal loss, procesos gaussianos, fiabilidad del anotador, inferencia variacional]
fuente_resumen: abstract
anio: 2026
revista: "Technologies"
doi: 10.3390/technologies14060370
citas_openalex: 0
fuentes: [0001330950]
---

# Learning from Crowds Using a Focal Loss Function: Dealing with Imbalanced Annotations

**Autores:** Julián Gil-González, David  Augusto Cardenas Peña, Alvaro Orozco-Gutierrez, Enrique Guijarro-Estellés, Andrés Marino Álvarez-Meza  
**Revista:** Technologies (2026)  
**DOI:** https://doi.org/10.3390/technologies14060370  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C11 Aprendizaje con múltiples anotadores

## Aplicación
Aprendizaje a partir de múltiples anotadores (crowdsourcing) con anotaciones dispersas y desbalanceadas.

## Problema de investigación
Cada anotador etiqueta pocas instancias, lo que amplifica el desbalance de clases y sesga los modelos de entropía cruzada hacia la clase mayoritaria.

## Propuesta o novedad
CCGPFL, un proceso gaussiano encadenado correlacionado entrenado con un objetivo variacional basado en focal loss. Modela conjuntamente la verdad latente y la fiabilidad dependiente de la instancia de cada anotador, considerando sus correlaciones, y la focal loss da más peso a los ejemplos difíciles.

## Resultados
En datos sintéticos, semisintéticos y reales multi-anotador, CCGPFL logra desempeño competitivo y a menudo superior frente a métodos de referencia en exactitud global (OA) y AUC.

## Conclusiones principales
La combinación de procesos gaussianos y focal loss mitiga el desbalance inducido por anotaciones dispersas.

## Métodos
- procesos gaussianos encadenados
- focal loss
- inferencia variacional

## Idea para trabajo futuro
Extender CCGPFL a tareas multimodales o de segmentación con anotadores heterogéneos y desbalance extremo.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Obtaining high-quality labeled data for supervised learning is costly, motivating the use of crowdsourcing, which distributes the annotation process across multiple workers with varying levels of expertise. A key challenge in crowdsourced data is annotation sparsity, as each worker labels only a limited subset of instances. This sparsity can amplify class imbalance, reduce supervision for minority classes, and bias standard cross-entropy-based models toward the majority classes. To address this problem, we propose a correlated chained Gaussian process framework trained on a focal-loss-based variational objective (CCGPFL). This probabilistic framework jointly models latent ground-truth and instance-dependent annotator reliability while accounting for correlations among annotators. In addition, the focal-weighted objective mitigates the imbalance induced by sparse annotations by assigning greater importance to harder examples during training. Experiments on synthetic, semi-synthetic, and fully real multi-annotator datasets show that CCGPFL achieves competitive and often superior performance relative to state-of-the-art learning-from-crowds baselines in terms of Overall Accuracy (OA) and Area Under the ROC Curve (AUC).

</details>
