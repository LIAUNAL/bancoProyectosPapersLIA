---
id: A081
titulo: "Entropy-based Estimation of Event-Related De/Synchronization in Motor Imagery Using Vector-Quantized Patterns"
tipo: articulo
temas: [T01, T05]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [desincronización relacionada con eventos, imaginación motora, entropía, cuantización vectorial, EEG]
fuente_resumen: abstract
anio: 2020
revista: "Entropy"
doi: 10.3390/e22060703
citas_openalex: 17
fuentes: [0000043222]
---

# Entropy-based Estimation of Event-Related De/Synchronization in Motor Imagery Using Vector-Quantized Patterns

**Autores:** Luisa Fernanda Velasquez-Martinez, Julián Caicedo-Acosta, German Castellanos-Dominguez  
**Revista:** Entropy (2020)  
**DOI:** https://doi.org/10.3390/e22060703  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Estimación de ERD/S en imaginación motora con EEG para aplicaciones clínicas y de aprendizaje.

## Problema de investigación
Las señales EEG tienen amplia variación de complejidad, afectando la discriminabilidad de ERD/S.

## Propuesta o novedad
Se presenta VQEnt, método basado en entropía que usa patrones estocásticos cuantizados vectorialmente como espacio simbólico y construye priors probabilísticos por similitud gaussiana con la representación reducida.

## Resultados
En una base bi-clase mano izquierda/derecha, VQEnt alcanza exactitud similar o mejor que estimadores de entropía basados en muestras; las series ERD/S se acercan a las del cambio porcentual de potencia.

## Conclusiones principales
El método ofrece mejor discriminabilidad e interpretabilidad fisiológica.

## Métodos
- VQEnt
- cuantización vectorial
- entropía
- kernel gaussiano

## Idea para trabajo futuro
Extender VQEnt a tareas multiclase y comparar con entropías de Rényi de orden alfa.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P027-2019-discriminating-mental-states-by-extracting-relevant-spatial]] — DISCRIMINATING MENTAL STATES BY EXTRACTING RELEVANT SPATIAL PATTERNS UNDER NON-STATIONARY AND SUBJECT-INDEPENDENT CONSTRAINTS

<details><summary>Abstract</summary>

Assessment of brain dynamics elicited by motor imagery (MI) tasks contributes to clinical and learning applications. In this regard, Event-Related Desynchronization/Synchronization (ERD/S) is computed from Electroencephalographic signals, which show considerable variations in complexity. We present an Entropy-based method, termed VQEnt, for estimation of ERD/S using quantized stochastic patterns as a symbolic space, aiming to improve their discriminability and physiological interpretability. The proposed method builds the probabilistic priors by assessing the Gaussian similarity between the input measured data and their reduced vector-quantized representation. The validating results of a bi-class imagine task database (left and right hand) prove that VQEnt holds symbols that encode several neighboring samples, providing similar or even better accuracy than the other baseline sample-based algorithms of Entropy estimation. Besides, the performed ERD/S time-series are close enough to the trajectories extracted by the variational percentage of EEG signal power and fulfill the physiological MI paradigm. In BCI literate individuals, the VQEnt estimator presents the most accurate outcomes at a lower amount of electrodes placed in the sensorimotor cortex so that reduced channel set directly involved with the MI paradigm is enough to discriminate between tasks, providing an accuracy similar to the performed by the whole electrode set.

</details>
