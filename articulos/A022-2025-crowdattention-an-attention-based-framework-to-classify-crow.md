---
id: A022
titulo: "CrowdAttention: An Attention Based Framework to Classify Crowdsourced Data in Medical Scenarios"
tipo: articulo
temas: [T06, T07, T04]
cluster: "C11 Aprendizaje con múltiples anotadores"
palabras_clave: [crowdsourcing, ruido de etiquetas, fiabilidad del anotador, atención cruzada, datos médicos, aprendizaje profundo]
fuente_resumen: abstract
anio: 2025
revista: "Sensors"
doi: 10.3390/s25206435
citas_openalex: 1
fuentes: [0001330950]
---

# CrowdAttention: An Attention Based Framework to Classify Crowdsourced Data in Medical Scenarios

**Autores:** Julián Gil-González, David  Augusto Cardenas Peña, Alvaro Angel Orozco, German Castellanos-Dominguez, Andrés Marino Álvarez-Meza  
**Revista:** Sensors (2025)  
**DOI:** https://doi.org/10.3390/s25206435  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T07 Aprendizaje profundo y explicabilidad; T04 Bioseñales y soporte al diagnóstico clínico  
**Clúster:** C11 Aprendizaje con múltiples anotadores

## Aplicación
Clasificación de datos médicos etiquetados por anotadores no expertos (crowdsourcing).

## Problema de investigación
Obtener etiquetas verificadas por expertos es costoso, y los anotadores no expertos introducen ruido por su heterogeneidad.

## Propuesta o novedad
CrowdAttention, un marco de aprendizaje profundo de extremo a extremo con dos redes acopladas: una de clasificación que estima la etiqueta verdadera latente y una red de multitud que asigna fiabilidad dependiente de la instancia a cada anotador mediante atención cruzada.

## Resultados
En conjuntos sintéticos y reales muestra mayor exactitud y robustez frente a métodos multi-anotador del estado del arte. El resumen no detalla métricas.

## Conclusiones principales
El modelado conjunto de clasificación y fiabilidad mediante atención cruzada es eficaz para datos médicos ruidosos.

## Métodos
- atención cruzada
- aprendizaje profundo
- multi-anotador

## Idea para trabajo futuro
Evaluar CrowdAttention con anotadores clínicos reales de imagen médica y estudiar su calibración de incertidumbre.

## Relacionados (similitud semántica)
- extiende: [[A045-2023-chained-deep-learning-using-generalized-cross-entropy-for-mu]] — Chained deep learning using generalized cross-entropy for multiple annotators classification

<details><summary>Abstract</summary>

Supervised learning models in healthcare and other domains heavily depend on high-quality, labeled data. However, acquiring expert-verified labels (i.e., the gold standard) is often impractical due to cost, time, and subjectivity. Crowdsourcing offers a scalable alternative by collecting labels from multiple non-expert annotators; however, it introduces label noise due to the heterogeneity of annotators. In this work, we propose CrowdAttention, a novel end-to-end deep learning framework that jointly models classification and annotator reliability using a cross-attention mechanism. The architecture consists of two coupled networks: a classification network that estimates the latent true label, and a crowd network that assigns instance-dependent reliability scores to each annotator’s label based on its alignment with the model’s current prediction. We demonstrate the effectiveness of our approach on both synthetic and real-world datasets, showing improved accuracy and robustness compared to state-of-the-art multi-annotator learning methods.

</details>
