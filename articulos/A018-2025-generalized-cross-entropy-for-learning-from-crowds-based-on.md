---
id: A018
titulo: "Generalized cross-entropy for learning from crowds based on correlated chained Gaussian processes"
tipo: articulo
temas: [T06, T05]
cluster: "C11 Aprendizaje con múltiples anotadores"
palabras_clave: [crowdsourcing, ruido de etiquetas, entropía cruzada generalizada, procesos gaussianos, calidad de etiquetas, robustez]
fuente_resumen: abstract
anio: 2025
revista: "Results in Engineering"
doi: 10.1016/j.rineng.2024.103863
citas_openalex: 5
fuentes: [0001330950]
---

# Generalized cross-entropy for learning from crowds based on correlated chained Gaussian processes

**Autores:** Julián Gil-González, Genaro Daza-Santacoloma, David  Augusto Cardenas Peña, Alvaro Angel Orozco, Andrés Marino Álvarez-Meza  
**Revista:** Results in Engineering (2025)  
**DOI:** https://doi.org/10.1016/j.rineng.2024.103863  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C11 Aprendizaje con múltiples anotadores

## Aplicación
Aprendizaje a partir de múltiples anotadores para clasificación con etiquetas ruidosas.

## Problema de investigación
Los métodos tradicionales asumen comportamiento homogéneo de los anotadores en el espacio de entrada e independencia entre sus salidas.

## Propuesta o novedad
CGP-GCE: un proceso gaussiano encadenado correlacionado con pérdida de entropía cruzada generalizada. Modela de forma bayesiana el comportamiento no estacionario e interdependiente de los anotadores y equilibra el error absoluto medio con la entropía cruzada para resistir ruido de etiquetas.

## Resultados
En experimentos simulados y reales supera a modelos multi-etiquetador del estado del arte en exactitud y en estimación de fiabilidad de expertos.

## Conclusiones principales
El modelo es robusto frente a ruido en crowdsourcing; como trabajo futuro se plantea manejar anotaciones dispersas y desbalanceadas y tareas multimodales.

## Métodos
- procesos gaussianos encadenados
- entropía cruzada generalizada
- inferencia bayesiana

## Idea para trabajo futuro
Combinar CGP-GCE con pérdidas sensibles al desbalance para anotaciones dispersas, como proponen los propios autores.

## Relacionados (similitud semántica)
- extiende: [[A045-2023-chained-deep-learning-using-generalized-cross-entropy-for-mu]] — Chained deep learning using generalized cross-entropy for multiple annotators classification

<details><summary>Abstract</summary>

Machine learning applications heavily depend on labeled data provided by domain experts to train accurate models. However, the cost and time constraints associated with expert labeling often make obtaining ground truth labels impractical. Crowdsourcing offers a cost-effective alternative for collecting annotations but introduces challenges such as varying label quality and noisy data. To address these issues, the field of learning from crowds has emerged, enabling supervised learning directly from crowdsourced data. Still, traditional approaches often fall short by assuming homogeneous behavior across the input feature space and imposing independence constraints on outputs. We introduced the correlated chained Gaussian process with enhanced generalized cross-entropy loss, termed CGP-GCE, which effectively models multiple annotators' non-stationary and interdependent behaviors by a Bayesian approach. Besides, our proposal achieves a suitable trade-off between mean absolute error and cross-entropy function, significantly mitigating the impact of noisy labels and enhancing the robustness and accuracy of classification tasks in crowdsourced data environments. Through extensive simulated and real-world experiments, CCGP-GCE demonstrated superior classification performance, outperforming state-of-the-art multilabeler models in terms of both accuracy and expert reliability estimation. We aim to extend CCGP-GCE for future work to handle sparse and imbalanced annotations. Additionally, we plan to apply this model to multimodal tasks.

</details>
