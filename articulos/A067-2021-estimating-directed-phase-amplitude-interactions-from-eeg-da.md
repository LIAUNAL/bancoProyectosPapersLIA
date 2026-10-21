---
id: A067
titulo: "Estimating Directed Phase-Amplitude Interactions from EEG Data through Kernel-Based Phase Transfer Entropy"
tipo: articulo
temas: [T02, T05]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [acoplamiento fase-amplitud, acoplamiento entre frecuencias, entropía de transferencia, EEG, memoria de trabajo]
fuente_resumen: abstract
anio: 2021
revista: "Applied Sciences"
doi: 10.3390/app11219803
citas_openalex: 4
fuentes: [0001330950]
---

# Estimating Directed Phase-Amplitude Interactions from EEG Data through Kernel-Based Phase Transfer Entropy

**Autores:** Iván De La Pava Panche, Viviana Gómez-Orozco, Andrés Marino Álvarez-Meza, David  Augusto Cardenas Peña, Alvaro Angel Orozco  
**Revista:** Applied Sciences (2021)  
**DOI:** https://doi.org/10.3390/app11219803  
**Temas:** T02 Conectividad cerebral e imagen de fuentes neuronales; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Detección de interacciones dirigidas fase-amplitud (acoplamiento entre frecuencias) en EEG, por ejemplo durante memoria de trabajo.

## Problema de investigación
Los métodos convencionales alimentan fase y amplitud a un estimador de TE, siendo sensibles a ruido y factores de confusión.

## Propuesta o novedad
Se replantea la detección como un problema de TE de fase entre dos series de fase, implementado con un estimador basado en kernels (Rényi), bajo la hipótesis de mayor robustez al usar datos de la misma naturaleza.

## Resultados
El enfoque se valida sobre acoplamiento fase-amplitud en EEG y busca mayor robustez frente a niveles altos de ruido.

## Conclusiones principales
Recasting a TE de fase mejora la robustez en la estimación de acoplamiento entre frecuencias.

## Métodos
- TE de fase
- estimador basado en kernel
- entropía de Rényi

## Idea para trabajo futuro
Contrastar el método con modelos de masa neuronal simulados con acoplamiento conocido para cuantificar sesgos.

## Relacionados (similitud semántica)
- extiende: [[A100-2019-a-data-driven-measure-of-effective-connectivity-based-on-ren]] — A data-driven measure of effective connectivity based on Renyi's α-entropy

<details><summary>Abstract</summary>

Cross-frequency interactions, a form of oscillatory neural activity, are thought to play an essential role in the integration of distributed information in the brain. Indeed, phase-amplitude interactions are believed to allow for the transfer of information from large-scale brain networks, oscillating at low frequencies, to local, rapidly oscillating neural assemblies. A promising approach to estimating such interactions is the use of transfer entropy (TE), a non-linear, information-theory-based effective connectivity measure. The conventional method involves feeding instantaneous phase and amplitude time series, extracted at the target frequencies, to a TE estimator. In this work, we propose that the problem of directed phase-amplitude interaction detection is recast as a phase TE estimation problem, under the hypothesis that estimating TE from data of the same nature, i.e., two phase time series, will improve the robustness to the common confounding factors that affect connectivity measures, such as the presence of high noise levels. We implement our proposal using a kernel-based TE estimator, defined in terms of Renyi’s α entropy, which has successfully been used to compute single-trial phase TE. We tested our approach on the synthetic data generated through a simulation model capable of producing a time series with directed phase-amplitude interactions at two given frequencies, and on EEG data from a cognitive task designed to activate working memory, a memory system whose underpinning mechanisms are thought to include phase–amplitude couplings. Our proposal detected statistically significant interactions between the simulated signals at the desired frequencies for the synthetic data, identifying the correct direction of the interaction. It also displayed higher robustness to noise than the alternative methods. The results attained for the working memory data showed that the proposed approach codes connectivity patterns based on directed phase–amplitude interactions, that allow for the different cognitive load levels of the working memory task to be differentiated.

</details>
