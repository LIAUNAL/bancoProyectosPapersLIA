---
id: A044
titulo: "Kernel-based regularized EEGNet using centered alignment and Gaussian connectivity for motor imagery discrimination"
tipo: articulo
temas: [T01, T02, T05]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, EEGNet, regularización kernel, alineamiento kernel centrado, BCI, variabilidad intrasujeto]
fuente_resumen: abstract
anio: 2023
revista: "Computers"
doi: 10.3390/computers12070145
citas_openalex: 11
fuentes: [0000043222, 0001330950]
---

# Kernel-based regularized EEGNet using centered alignment and Gaussian connectivity for motor imagery discrimination

**Autores:** Mateo Tobón-Henao, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Computers (2023)  
**DOI:** https://doi.org/10.3390/computers12070145  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T02 Conectividad cerebral e imagen de fuentes neuronales; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Clasificación de imaginación motora con EEG para interacción humano-tecnología.

## Problema de investigación
El ruido del EEG genera variabilidad intrasujeto y falta interpretabilidad espacial en marcos de extremo a extremo.

## Propuesta o novedad
KREEGNet, un refinamiento de EEGNet con una capa adicional basada en kernels que estima conectividad funcional gaussiana regularizada con Centered Kernel Alignment (CKA).

## Resultados
En bases de MI binaria y multiclase supera a EEGNet y otros métodos del estado del arte; analiza la interpretabilidad a nivel individual y de grupo con conectividades podadas.

## Conclusiones principales
Es una alternativa adecuada para EEG-BCI interpretable de extremo a extremo.

## Métodos
- EEGNet
- CKA
- conectividad gaussiana

## Idea para trabajo futuro
Explorar la adaptación en línea de la regularización CKA para calibración rápida con nuevos usuarios.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

Brain-computer interfaces (BCI) from electroencephalography (EEG) provide a practical approach to support human-technology interaction. In particular, motor imagery (MI) is a widely-used BCI paradigm that guides the mental trial of motor tasks without physical movement. Here, we present a deep learning methodology, named Kernel-based Regularized EEGNet (KREEGNet), leveled on Centered Kernel Alignment and Gaussian Functional Connectivity, explicitly designed for EEG-based MI classification. The approach proactively tackles the challenge of intra-subject variability brought on by noisy EEG records and the lack of spatial interpretability within end-to-end frameworks applied for MI classification. KREEGNet is a refinement of the widely accepted EEGNet architecture, featuring an additional kernel-based layer for regularized Gaussian functional connectivity estimation based on CKA. The superiority of KREEGNet is evidenced by our experimental results from binary and multi-class MI classification databases, outperforming the baseline EEGNet and other state-of-the-art methods. Further exploration of our model’s interpretability is conducted at individual and group levels, utilizing classification performance measures and pruned functional connectivities. Our approach is a suitable alternative for interpretable end-to-end EEG-BCI based on deep learning.

</details>
