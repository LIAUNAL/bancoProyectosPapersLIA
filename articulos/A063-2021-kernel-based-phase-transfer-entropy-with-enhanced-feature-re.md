---
id: A063
titulo: "Kernel-based phase transfer entropy with enhanced feature relevance analysis for brain computer interfaces"
tipo: articulo
temas: [T02, T01, T05]
cluster: "C03 Conectividad cerebral e imagen de fuentes"
palabras_clave: [entropía de transferencia de fase, conectividad efectiva, entropía de Rényi, alineamiento de kernel, oscilaciones neuronales]
fuente_resumen: abstract
anio: 2021
revista: "Applied Sciences"
doi: 10.3390/app11156689
citas_openalex: 10
fuentes: [0001330950]
---

# Kernel-based phase transfer entropy with enhanced feature relevance analysis for brain computer interfaces

**Autores:** Iván De La Pava Panche, Andrés Marino Álvarez-Meza, Paula Herrera, David  Augusto Cardenas Peña, Jorge Iván Ríos Patiño, Alvaro Angel Orozco  
**Revista:** Applied Sciences (2021)  
**DOI:** https://doi.org/10.3390/app11156689  
**Temas:** T02 Conectividad cerebral e imagen de fuentes neuronales; T01 Interfaces cerebro-computador y decodificación EEG; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C03 Conectividad cerebral e imagen de fuentes

## Aplicación
Medición de conectividad dirigida entre oscilaciones neuronales en EEG para BCI.

## Problema de investigación
La entropía de transferencia de fase suele requerir estimación de probabilidades sobre múltiples ensayos, lo que impide usarla en BCI ensayo a ensayo.

## Propuesta o novedad
Se propone un estimador de TE de fase basado en kernels y entropía de Rényi alfa, que evita estimar distribuciones, aplicado a pares de series de fase instantánea, más un análisis de relevancia por alineamiento de kernel.

## Resultados
El método permite estimar TE entre pares individuales de series de fase y resaltar los rasgos relevantes de conectividad efectiva.

## Conclusiones principales
La TE de fase basada en kernel es viable para caracterización por ensayo en BCI.

## Métodos
- transfer entropy
- entropía de Rényi
- alineamiento de kernel

## Idea para trabajo futuro
Combinar la TE de fase kernel con clasificadores en línea para evaluar su aporte en BCI en tiempo real.

## Relacionados (similitud semántica)
- extiende: [[A100-2019-a-data-driven-measure-of-effective-connectivity-based-on-ren]] — A data-driven measure of effective connectivity based on Renyi's α-entropy

<details><summary>Abstract</summary>

Neural oscillations are present in the brain at different spatial and temporal scales, and they are linked to several cognitive functions. Furthermore, the information carried by their phases is fundamental for the coordination of anatomically distributed processing in the brain. The concept of phase transfer entropy refers to an information theory-based measure of directed connectivity among neural oscillations that allows studying such distributed processes. Phase TE is commonly obtained from probability estimations carried out over data from multiple trials, which bars its use as a characterization strategy in brain–computer interfaces. In this work, we propose a novel methodology to estimate TE between single pairs of instantaneous phase time series. Our approach combines a kernel-based TE estimator defined in terms of Renyi’s α entropy, which sidesteps the need for probability distribution computation with phase time series obtained by complex filtering the neural signals. Besides, a kernel-alignment-based relevance analysis is added to highlight relevant features from effective connectivity-based representation supporting further classification stages in EEG-based brain–computer interface systems. Our proposal is tested on simulated coupled data and two publicly available databases containing EEG signals recorded under motor imagery and visual working memory paradigms. Attained results demonstrate how the introduced effective connectivity succeeds in detecting the interactions present in the data for the former, with statistically significant results around the frequencies of interest. It also reflects differences in coupling strength, is robust to realistic noise and signal mixing levels, and captures bidirectional interactions of localized frequency content. Obtained results for the motor imagery and working memory databases show that our approach, combined with the relevance analysis strategy, codes discriminant spatial and frequency-dependent patterns for the different conditions in each experimental paradigm, with classification performances that do well in comparison with those of alternative methods of similar nature.

</details>
