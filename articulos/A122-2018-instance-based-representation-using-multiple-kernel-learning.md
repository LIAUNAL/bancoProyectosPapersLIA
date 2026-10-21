---
id: A122
titulo: "Instance-Based Representation Using Multiple Kernel Learning for Predicting Conversion to Alzheimer Disease"
tipo: articulo
temas: [T03, T05]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [enfermedad de Alzheimer, deterioro cognitivo leve, aprendizaje de múltiples kernels, alineamiento de kernel, ADNI, predicción de conversión]
fuente_resumen: abstract
anio: 2018
revista: "International Journal of Neural Systems"
doi: 10.1142/S0129065718500429
citas_openalex: 25
fuentes: [0000043222]
---

# Instance-Based Representation Using Multiple Kernel Learning for Predicting Conversion to Alzheimer Disease

**Autores:** Diego Fabián Collazos-Huertas, David  Augusto Cardenas Peña, German Castellanos-Dominguez  
**Revista:** International Journal of Neural Systems (2018)  
**DOI:** https://doi.org/10.1142/S0129065718500429  
**Temas:** T03 Imagen médica y neuroimagen; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Predicción de la conversión de deterioro cognitivo leve a Alzheimer con RM estructural.

## Problema de investigación
Los datos faltantes y la interpretabilidad dificultan la predicción temprana de Alzheimer.

## Propuesta o novedad
Se construye una representación basada en instancias a partir de medidas morfológicas de cada estructura cerebral para tolerar visitas perdidas; los mapeos se combinan por combinación convexa de kernels reproductores con pesos ajustados maximizando el alineamiento de kernel centrado.

## Resultados
Sobre ADNI, el método permite detectar deterioro cognitivo leve y predecir la conversión a Alzheimer en un horizonte de tres años; además identifica las estructuras cerebrales más relevantes.

## Conclusiones principales
El aprendizaje de múltiples kernels aporta rendimiento e interpretabilidad en el pronóstico de Alzheimer.

## Métodos
- aprendizaje de múltiples kernels
- CKA
- representación basada en instancias

## Idea para trabajo futuro
Integrar biomarcadores adicionales (LCR, PET) como nuevos kernels y evaluar el aporte marginal de cada fuente.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

The early detection of Alzheimer's disease and quantification of its progression poses multiple difficulties for machine learning algorithms. Two of the most relevant issues are related to missing data and results interpretability. To deal with both issues, we introduce a methodology to predict conversion of mild cognitive impairment patients to Alzheimer's from structural brain MRI volumes. First, we use morphological measures of each brain structure to build an instance-based feature mapping that copes with missed follow-up visits. Then, the extracted multiple feature mappings are combined into a single representation through the convex combination of reproducing kernels. The weighting parameters per structure are tuned based on the maximization of the centered-kernel alignment criterion. We evaluate the proposed methodology on a couple of well-known classification machines employing the ADNI database devoted to assessing the combined prognostic value of several AD biomarkers. The obtained experimental results show that our proposed method of Instance-based representation using multiple kernel learning enables detecting mild cognitive impairment as well as predicting conversion to Alzheimers disease within three years from the initial screening. Besides, the brain structures with larger combination weights are directly related to memory and cognitive functions.

</details>
