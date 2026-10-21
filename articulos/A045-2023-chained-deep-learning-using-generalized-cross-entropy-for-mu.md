---
id: A045
titulo: "Chained deep learning using generalized cross-entropy for multiple annotators classification"
tipo: articulo
temas: [T06, T07, T05]
cluster: "C11 Aprendizaje con múltiples anotadores"
palabras_clave: [crowdsourcing, ruido de etiquetas, entropía cruzada generalizada, aprendizaje profundo encadenado, fiabilidad del etiquetador, multi-anotador]
fuente_resumen: abstract
anio: 2023
revista: "Sensors"
doi: 10.3390/s23073518
citas_openalex: 10
fuentes: [0000043222, 0001330950]
---

# Chained deep learning using generalized cross-entropy for multiple annotators classification

**Autores:** Jenniffer Carolina Triana-Martinez, Julián Gil-González, José A. Fernandez-Gallego, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Sensors (2023)  
**DOI:** https://doi.org/10.3390/s23073518  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T07 Aprendizaje profundo y explicabilidad; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C11 Aprendizaje con múltiples anotadores

## Aplicación
Clasificación con etiquetas de múltiples anotadores en plataformas de crowdsourcing.

## Problema de investigación
Los métodos multi-anotador no consideran bien la experiencia variable, el ruido ni la heterogeneidad espacial, e imponen independencia entre salidas.

## Propuesta o novedad
GCECDL, un marco de aprendizaje profundo encadenado con entropía cruzada generalizada que codifica los patrones no estacionarios de cada anotador respecto al espacio de entrada, preservando las interdependencias entre expertos y autorregulando la red mediante la fiabilidad estimada.

## Resultados
En varios conjuntos conocidos logra desempeño predictivo robusto, superando algoritmos del estado del arte; el análisis de relevancia revela la codificación no estacionaria del método.

## Conclusiones principales
GCECDL pondera a los etiquetadores confiables por muestra y conserva interpretabilidad sobre su confiabilidad.

## Métodos
- entropía cruzada generalizada
- aprendizaje profundo encadenado
- análisis de relevancia

## Idea para trabajo futuro
Combinar GCECDL con arquitecturas basadas en atención para escalar a conjuntos de imagen médica anotados por muchos expertos.

## Relacionados (similitud semántica)
- extendido por: [[A018-2025-generalized-cross-entropy-for-learning-from-crowds-based-on]] — Generalized cross-entropy for learning from crowds based on correlated chained Gaussian processes
- extendido por: [[A022-2025-crowdattention-an-attention-based-framework-to-classify-crow]] — CrowdAttention: An Attention Based Framework to Classify Crowdsourced Data in Medical Scenarios

<details><summary>Abstract</summary>

Supervised learning requires the accurate labeling of instances, usually provided by an expert. Crowdsourcing platforms offer a practical and cost-effective alternative for large datasets when individual annotation is impractical. In addition, these platforms gather labels from multiple labelers. Still, traditional multiple-annotator methods must account for the varying levels of expertise and the noise introduced by unreliable outputs, resulting in decreased performance. In addition, they assume a homogeneous behavior of the labelers across the input feature space, and independence constraints are imposed on outputs. We propose a Generalized Cross-Entropy-based framework using Chained Deep Learning (GCECDL) to code each annotator's non-stationary patterns regarding the input space while preserving the inter-dependencies among experts through a chained deep learning approach. Experimental results devoted to multiple-annotator classification tasks on several well-known datasets demonstrate that our GCECDL can achieve robust predictive properties, outperforming state-of-the-art algorithms by combining the power of deep learning with a noise-robust loss function to deal with noisy labels. Moreover, network self-regularization is achieved by estimating each labeler's reliability within the chained approach. Lastly, visual inspection and relevance analysis experiments are conducted to reveal the non-stationary coding of our method. In a nutshell, GCEDL weights reliable labelers as a function of each input sample and achieves suitable discrimination performance with preserved interpretability regarding each annotator's trustworthiness estimation.

</details>
