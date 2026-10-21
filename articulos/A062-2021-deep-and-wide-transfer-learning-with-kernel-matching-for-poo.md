---
id: A062
titulo: "Deep and wide transfer learning with kernel matching for pooling data from electroencephalography and psychological questionnaires"
tipo: articulo
temas: [T01, T05]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, transfer learning, kernel matching, cuestionarios psicológicos, decodificación EEG]
fuente_resumen: abstract
anio: 2021
revista: "Sensors"
doi: 10.3390/s21155105
citas_openalex: 8
fuentes: [0000043222, 0001330950]
---

# Deep and wide transfer learning with kernel matching for pooling data from electroencephalography and psychological questionnaires

**Autores:** Diego Fabián Collazos-Huertas, Luisa Fernanda Velasquez-Martinez, Hernán Darío Pérez-Nastar, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Sensors (2021)  
**DOI:** https://doi.org/10.3390/s21155105  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
BCI de imaginación motora, apoyando a usuarios con baja eficiencia mediante datos de EEG y cuestionarios psicológicos.

## Problema de investigación
Dominar la autorregulación de ritmos cerebrales requiere largo entrenamiento y deja a muchos usuarios con ineficiencia MI.

## Propuesta o novedad
Se plantea transfer learning entre sujetos basado en parámetros: una red Deep and Wide preentrenada en el dominio fuente, con fusión de rasgos categóricos y reales mediante kernel matching por incrustación gaussiana, y selección de pares fuente-destino por agrupamiento según ineficiencia.

## Resultados
Se mejora el desempeño de sujetos de bajo rendimiento al fusionar EEG y cuestionarios.

## Conclusiones principales
La combinación de transferencia de parámetros y datos psicológicos es una vía para reducir la ineficiencia BCI.

## Métodos
- Deep&Wide
- transfer learning
- kernel matching
- MLP

## Idea para trabajo futuro
Explorar qué rasgos psicológicos predicen mejor la ineficiencia para personalizar la selección de sujetos fuente.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Motor imagery (MI) promotes motor learning and encourages brain-computer interface systems that entail electroencephalogram (EEG) decoding. However, a long period of training is required to master brain rhythms' self-regulation, resulting in users with MI inefficiency. We introduce a parameter-based approach of cross-subject transfer-learning to improve the performances of poor-performing individuals in MI-based BCI systems, pooling data from labeled EEG measurements and psychological questionnaires via kernel-embedding. To this end, a Deep and Wide neural network for MI classification is implemented to pre-train the network from the source domain. Then, the parameter layers are transferred to initialize the target network within a fine-tuning procedure to recompute the Multilayer Perceptron-based accuracy. To perform data-fusion combining categorical features with the real-valued features, we implement stepwise kernel-matching via Gaussian-embedding. Finally, the paired source-target sets are selected for evaluation purposes according to the inefficiency-based clustering by subjects to consider their influence on BCI motor skills, exploring two choosing strategies of the best-performing subjects (source space): single-subject and multiple-subjects. Validation results achieved for discriminant MI tasks demonstrate that the introduced Deep and Wide neural network presents competitive performance of accuracy even after the inclusion of questionnaire data.

</details>
