---
id: A058
titulo: "Subject-dependent artifact removal for enhancing motor imagery classifier performance under poor skills"
tipo: articulo
temas: [T01, T02]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, remoción de artefactos, ICA, Laplaciano de superficie, conectividad funcional, relación señal-ruido]
fuente_resumen: abstract
anio: 2022
revista: "Sensors"
doi: 10.3390/s22155771
citas_openalex: 7
fuentes: [0000043222, 0001330950]
---

# Subject-dependent artifact removal for enhancing motor imagery classifier performance under poor skills

**Autores:** Mateo Tobón-Henao, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Sensors (2022)  
**DOI:** https://doi.org/10.3390/s22155771  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T02 Conectividad cerebral e imagen de fuentes neuronales  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
BCI de imaginación motora con EEG, especialmente para usuarios con bajas habilidades motoras.

## Problema de investigación
La baja relación señal-ruido, la no estacionariedad y la variabilidad entre sujetos dificultan la extracción de rasgos discriminantes, sobre todo en sujetos con pobre desempeño.

## Propuesta o novedad
Se propone el preprocesamiento dependiente del sujeto SD-AR, que combina filtrado Laplaciano de superficie e ICA para remover artefactos según el desempeño MI, y estudia medidas de conectividad funcional por potencia y fase para identificar sujetos ineficientes.

## Resultados
SD-AR mejora el desempeño de clasificación MI en sujetos con pobres habilidades motoras.

## Conclusiones principales
El preprocesamiento adaptado al sujeto aumenta la separabilidad y aporta patrones interpretables.

## Métodos
- ICA
- filtro Laplaciano de superficie
- conectividad funcional

## Idea para trabajo futuro
Automatizar la selección de componentes ICA a eliminar mediante un criterio de desempeño en línea para BCI en tiempo real.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P012-2021-procesamiento-de-senales-de-eeg-en-bci-orientado-a-la-detecc]] — Procesamiento de señales de EEG en BCI orientado a la detección de IM utilizando modelos de aprendizaje profundo y medidas de conectividad
- derivado del proyecto: [[P027-2019-discriminating-mental-states-by-extracting-relevant-spatial]] — DISCRIMINATING MENTAL STATES BY EXTRACTING RELEVANT SPATIAL PATTERNS UNDER NON-STATIONARY AND SUBJECT-INDEPENDENT CONSTRAINTS

<details><summary>Abstract</summary>

The Electroencephalography (EEG)-based motor imagery (MI) paradigm is one of the most studied technologies for Brain-Computer Interface (BCI) development. Still, the low Signal-to-Noise Ratio (SNR) poses a challenge when constructing EEG-based BCI systems. Moreover, the non-stationary and nonlinear signal issues, the low-spatial data resolution, and the inter- and intra-subject variability hamper the extraction of discriminant features. Indeed, subjects with poor motor skills have difficulties in practicing MI tasks against low SNR scenarios. Here, we propose a subject-dependent preprocessing approach that includes the well-known Surface Laplacian Filtering and Independent Component Analysis algorithms to remove signal artifacts based on the MI performance. In addition, power- and phase-based functional connectivity measures are studied to extract relevant and interpretable patterns and identify subjects of inefficency. As a result, our proposal, Subject-dependent Artifact Removal (SD-AR), improves the MI classification performance in subjects with poor motor skills. Consequently, electrooculography and volume-conduction EEG artifacts are mitigated within a functional connectivity feature-extraction strategy, which favors the classification performance of a straightforward linear classifier.

</details>
