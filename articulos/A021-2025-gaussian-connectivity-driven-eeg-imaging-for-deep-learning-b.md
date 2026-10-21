---
id: A021
titulo: "Gaussian Connectivity-Driven EEG Imaging for Deep Learning-Based Motor Imagery Classification"
tipo: articulo
temas: [T01, T02, T07]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, BCI, conectividad funcional, autoencoder variacional, ineficiencia BCI, interpretabilidad]
fuente_resumen: abstract
anio: 2025
revista: "Sensors"
doi: 10.3390/s26010227
citas_openalex: 2
fuentes: [0001330950]
---

# Gaussian Connectivity-Driven EEG Imaging for Deep Learning-Based Motor Imagery Classification

**Autores:** Alejandra Gomez-Rivera, Diego Fabián Collazos-Huertas, David  Augusto Cardenas Peña, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Sensors (2025)  
**DOI:** https://doi.org/10.3390/s26010227  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T02 Conectividad cerebral e imagen de fuentes neuronales; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
BCI de imaginación motora para neurorrehabilitación y tecnologías asistivas.

## Problema de investigación
Baja resolución espacial, ruido, artefactos y fuerte variabilidad intersujeto limitan CSP y CNN en robustez, generalización e interpretabilidad.

## Propuesta o novedad
EEG-GCIRNet integra EEG crudo y mapas topográficos de conectividad funcional gaussiana en un autoencoder variacional acoplado a una LeNet regularizada, con pérdida multiobjetivo de reconstrucción, clasificación y regularización del espacio latente.

## Resultados
Alcanza 81.82% de exactitud promedio y variabilidad ±10.15 en clasificación binaria, eliminando el grupo de desempeño malo (<60%) con ganancias de ~22% en esos usuarios. En 5 clases logra 75.20% ± 4.63 con superioridad estadística (p = 0.002).

## Conclusiones principales
Captura mecanismos neurofisiológicos genuinos y reduce la ineficiencia BCI.

## Métodos
- autoencoder variacional
- conectividad gaussiana
- LeNet
- Grad-CAM++

## Idea para trabajo futuro
Probar EEG-GCIRNet en pacientes de rehabilitación y en sesiones en línea de calibración corta.

## Relacionados (similitud semántica)
- extiende: [[A049-2023-posthoc-interpretability-of-neural-responses-by-grouping-sub]] — Posthoc Interpretability of Neural Responses by Grouping Subject Motor Imagery Skills Using CNN-Based Connectivity

<details><summary>Abstract</summary>

Electroencephalography (EEG)-based motor imagery (MI) brain–computer interfaces (BCIs) hold considerable potential for applications in neuro-rehabilitation and assistive technologies. Yet, their development remains constrained by challenges such as low spatial resolution, vulnerability to noise and artifacts, and pronounced inter-subject variability. Conventional approaches, including common spatial patterns (CSP) and convolutional neural networks (CNNs), often exhibit limited robustness, weak generalization, and reduced interpretability. To overcome these limitations, we introduce EEG-GCIRNet, a Gaussian connectivity-driven EEG imaging representation network coupled with a regularized LeNet architecture for MI classification. Our method integrates raw EEG signals with topographic maps derived from functional connectivity into a unified variational autoencoder framework. The network is trained with a multi-objective loss that jointly optimizes reconstruction fidelity, classification accuracy, and latent space regularization. The model’s interpretability is enhanced through its variational autoencoder design, allowing for qualitative validation of its learned representations. Experimental evaluations demonstrate that EEG-GCIRNet outperforms state-of-the-art methods, achieving the highest average accuracy (81.82%) and lowest variability (±10.15) in binary classification. Most notably, it effectively mitigates BCI illiteracy by completely eliminating the “Bad” performance group (<60% accuracy), yielding substantial gains of ∼22% for these challenging users. Furthermore, the framework demonstrates good scalability in complex 5-class scenarios, performing competitive classification accuracy (75.20% ± 4.63) with notable statistical superiority (p = 0.002) against advanced baselines. Extensive interpretability analyses, including analysis of the reconstructed connectivity maps, latent space visualizations, Grad-CAM++ and functional connectivity patterns, confirm that the model captures genuine neurophysiological mechanisms, correctly identifying integrated fronto-centro-parietal networks in high performers and compensatory midline circuits in mid-performers. These findings suggest that EEG-GCIRNet provides a robust and interpretable end-to-end framework for EEG-based BCIs, advancing the development of reliable neurotechnology for rehabilitation and assistive applications.

</details>
