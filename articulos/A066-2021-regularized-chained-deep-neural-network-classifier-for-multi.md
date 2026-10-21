---
id: A066
titulo: "Regularized chained deep neural network classifier for multiple annotators"
tipo: articulo
temas: [T06, T07]
cluster: "C11 Aprendizaje con múltiples anotadores"
palabras_clave: [múltiples anotadores, crowdsourcing, regularización, Monte Carlo dropout, redes profundas]
fuente_resumen: abstract
anio: 2021
revista: "Applied Sciences"
doi: 10.3390/app11125409
citas_openalex: 10
fuentes: [0001330950]
---

# Regularized chained deep neural network classifier for multiple annotators

**Autores:** Julián Gil-González, Andrés Felipe Valencia-Duque, Andrés Marino Álvarez-Meza, Alvaro Angel Orozco, Andrea García-Moreno  
**Revista:** Applied Sciences (2021)  
**DOI:** https://doi.org/10.3390/app11125409  
**Temas:** T06 Aprendizaje probabilístico y bayesiano; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C11 Aprendizaje con múltiples anotadores

## Aplicación
Clasificación supervisada con etiquetas de plataformas de crowdsourcing como Amazon Mechanical Turk.

## Problema de investigación
Los métodos usuales suponen comportamiento homogéneo del anotador en el espacio de rasgos e independencia entre anotadores.

## Propuesta o novedad
Se presenta RCDNN, red neuronal profunda encadenada regularizada que predice conjuntamente la etiqueta real y el desempeño de los anotadores, codifica dependencias analizando pesos de capas e incluye regularizadores l1, l2 y Monte-Carlo Dropout.

## Resultados
Con datos simulados y anotaciones reales, RCDNN muestra desempeño competitivo frente al estado del arte.

## Conclusiones principales
La regularización y la modelación de dependencias mitigan el sobreajuste en aprendizaje profundo con anotadores múltiples.

## Métodos
- RCDNN
- Monte-Carlo Dropout
- regularización l1/l2

## Idea para trabajo futuro
Incorporar incertidumbre bayesiana sobre la confiabilidad de cada anotador dentro de RCDNN.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P012-2021-procesamiento-de-senales-de-eeg-en-bci-orientado-a-la-detecc]] — Procesamiento de señales de EEG en BCI orientado a la detección de IM utilizando modelos de aprendizaje profundo y medidas de conectividad

<details><summary>Abstract</summary>

The increasing popularity of crowdsourcing platforms, i.e., Amazon Mechanical Turk, changes how datasets for supervised learning are built. In these cases, instead of having datasets labeled by one source (which is supposed to be an expert who provided the absolute gold standard), databases holding multiple annotators are provided. However, most state-of-the-art methods devoted to learning from multiple experts assume that the labeler’s behavior is homogeneous across the input feature space. Besides, independence constraints are imposed on annotators’ outputs. This paper presents a regularized chained deep neural network to deal with classification tasks from multiple annotators. The introduced method, termed RCDNN, jointly predicts the ground truth label and the annotators’ performance from input space samples. In turn, RCDNN codes interdependencies among the experts by analyzing the layers’ weights and includes l1, l2, and Monte-Carlo Dropout-based regularizers to deal with the over-fitting issue in deep learning models. Obtained results (using both simulated and real-world annotators) demonstrate that RCDNN can deal with multi-labelers scenarios for classification tasks, defeating state-of-the-art techniques.

</details>
