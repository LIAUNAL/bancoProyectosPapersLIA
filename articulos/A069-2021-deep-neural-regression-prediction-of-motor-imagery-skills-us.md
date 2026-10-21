---
id: A069
titulo: "Deep Neural Regression Prediction of Motor Imagery Skills Using EEG Functional Connectivity Indicators"
tipo: articulo
temas: [T01, T02]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, conectividad funcional EEG, regresión profunda, sobreajuste, Monte Carlo dropout]
fuente_resumen: abstract
anio: 2021
revista: "Sensors"
doi: 10.3390/s21061932
citas_openalex: 13
fuentes: [0000043222, 0001330950]
---

# Deep Neural Regression Prediction of Motor Imagery Skills Using EEG Functional Connectivity Indicators

**Autores:** Julián Caicedo-Acosta, German A. Castaño, Carlos Daniel Acosta-Medina, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Sensors (2021)  
**DOI:** https://doi.org/10.3390/s21061932  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T02 Conectividad cerebral e imagen de fuentes neuronales  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Predicción de habilidades de imaginación motora a partir de conectividad funcional EEG.

## Problema de investigación
Una fracción de usuarios no logra coordinar el control sensoriomotor, y predecir su ineficiencia con redes de regresión implica riesgo de sobreajuste.

## Propuesta o novedad
Se desarrolla un modelo de regresión neuronal profunda con validación leave-one-out y capas Monte Carlo dropout, agrupamiento de sujetos por ineficiencia MI y transferencia de aprendizaje entre corridas vecinas.

## Resultados
Las estrategias mejoran el desempeño de predicción de la habilidad MI a partir de indicadores de conectividad.

## Conclusiones principales
La regresión sobre conectividad permite anticipar la ineficiencia BCI.

## Métodos
- regresión neuronal
- Monte Carlo dropout
- transfer learning
- agrupamiento

## Idea para trabajo futuro
Usar la predicción de ineficiencia antes del entrenamiento para asignar a cada usuario un paradigma BCI adecuado.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P012-2021-procesamiento-de-senales-de-eeg-en-bci-orientado-a-la-detecc]] — Procesamiento de señales de EEG en BCI orientado a la detección de IM utilizando modelos de aprendizaje profundo y medidas de conectividad

<details><summary>Abstract</summary>

Motor imaging (MI) induces recovery and neuroplasticity in neurophysical regulation. However, a non-negligible portion of users presents insufficient coordination skills of sensorimotor cortex control. Assessments of the relationship between wakefulness and tasks states are conducted to foster neurophysiological and mechanistic interpretation in MI-related applications. Thus, to understand the organization of information processing, measures of functional connectivity are used. Also, models of neural network regression prediction are becoming popular, These intend to reduce the need for extracting features manually. However, predicting MI practicing's neurophysiological inefficiency raises several problems, like enhancing network regression performance because of the overfitting risk. Here, to increase the prediction performance, we develop a deep network regression model that includes three procedures: leave-one-out cross-validation combined with Monte Carlo dropout layers, subject clustering of MI inefficiency, and transfer learning between neighboring runs. Validation is performed using functional connectivity predictors extracted from two electroencephalographic databases acquired in conditions close to real MI applications (150 users), resulting in a high prediction of pretraining desynchronization and initial training synchronization with adequate physiological interpretability.

</details>
