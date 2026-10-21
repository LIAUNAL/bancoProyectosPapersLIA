---
id: A099
titulo: "Regression Networks for Neurophysiological Indicator Evaluation in Practicing Motor Imagery Tasks"
tipo: articulo
temas: [T01, T07]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, marcadores neurofisiológicos, BCI, sincronización neuronal, desincronización, variabilidad interindividual]
fuente_resumen: abstract
anio: 2019
revista: "Brain Sciences"
doi: 10.3390/brainsci10100707
citas_openalex: 6
fuentes: [0000043222, 0001330950]
---

# Regression Networks for Neurophysiological Indicator Evaluation in Practicing Motor Imagery Tasks

**Autores:** Luisa Fernanda Velasquez-Martinez, Julián Caicedo-Acosta, Carlos Daniel Acosta-Medina, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Brain Sciences (2019)  
**DOI:** https://doi.org/10.3390/brainsci10100707  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Evaluación de eficiencia de redes cerebrales en imaginación motora para rehabilitación y entrenamiento.

## Problema de investigación
Hasta 30% de los usuarios no desarrolla suficiente coordinación tras el entrenamiento por variabilidad.

## Propuesta o novedad
Se desarrolla la Deep Regression Network (DRN), estimador de dos etapas que extrae patrones profundos y los pasa a regresión neuronal para predecir la exactitud bi-clase.

## Resultados
Con datos reales de MI, la DRN encuentra que la desincronización previa y la sincronización inicial favorecen predecir la respuesta de exactitud.

## Conclusiones principales
DRN ayuda a entender la ineficiencia BCI.

## Métodos
- red de regresión profunda
- regresión neuronal

## Idea para trabajo futuro
Usar predicciones DRN previas al entrenamiento para identificar usuarios para intervención temprana.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Motor Imagery (MI) promotes motor learning in activities, like developing professional motor skills, sports gestures, and patient rehabilitation. However, up to 30% of users may not develop enough coordination skills after training sessions because of inter and intra-subject variability. Here, we develop a data-driven estimator, termed Deep Regression Network (DRN), which jointly extracts and performs the regression analysis in order to assess the efficiency of the individual brain networks in practicing MI tasks. The proposed double-stage estimator initially learns a pool of deep patterns, extracted from the input data, in order to feed a neural regression model, allowing for infering the distinctiveness between subject assemblies having similar variability. The results, which were obtained on real-world MI data, prove that the DRN estimator fosters pre-training neural desynchronization and initial training synchronization to predict the bi-class accuracy response, thus providing a better understanding of the Brain-Computer Interface inefficiency of subjects.

</details>
