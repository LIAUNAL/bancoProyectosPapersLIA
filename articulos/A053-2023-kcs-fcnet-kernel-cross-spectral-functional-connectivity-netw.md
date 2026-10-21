---
id: A053
titulo: "Kcs-fcnet: Kernel cross-spectral functional connectivity network for eeg-based motor imagery classification"
tipo: articulo
temas: [T01, T02, T05]
cluster: "C02 BCI por imaginación motora"
palabras_clave: [imaginación motora, EEG, conectividad funcional, BCI, redes interpretables, kernel gaussiano]
fuente_resumen: abstract
anio: 2023
revista: "Diagnostics"
doi: 10.3390/diagnostics13061122
citas_openalex: 13
fuentes: [0000043222, 0001330950]
---

# Kcs-fcnet: Kernel cross-spectral functional connectivity network for eeg-based motor imagery classification

**Autores:** Daniel Guillermo García-Murillo, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Diagnostics (2023)  
**DOI:** https://doi.org/10.3390/diagnostics13061122  
**Temas:** T01 Interfaces cerebro-computador y decodificación EEG; T02 Conectividad cerebral e imagen de fuentes neuronales; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C02 BCI por imaginación motora

## Aplicación
Clasificación EEG de imaginación motora de mano derecha e izquierda en BCI.

## Problema de investigación
Los enfoques actuales exigen arquitecturas complejas y ofrecen poca interpretabilidad.

## Propuesta o novedad
KCS-FCnet: una red 1D convolucional que extrae características temporo-frecuenciales del EEG crudo y una capa de conectividad de núcleo gaussiano espectral cruzado que modela relaciones funcionales entre canales, con mapas más ricos, menos parámetros y adaptables al sujeto.

## Resultados
Los resultados de validación indican que la arquitectura superficial es prometedora para clasificación MI-EEG; el resumen disponible no entrega cifras.

## Conclusiones principales
KCS-FCnet tiene potencial para BCI en el mundo real.

## Métodos
- CNN 1D
- kernel gaussiano espectral cruzado
- conectividad funcional

## Idea para trabajo futuro
Evaluar KCS-FCnet con más clases de MI y en tiempo real para control de dispositivos.

## Relacionados (similitud semántica)
- Ninguno sobre el umbral

<details><summary>Abstract</summary>

This paper uses EEG data to introduce an approach for classifying right and left-hand classes in Motor Imagery (MI) tasks. The Kernel Cross-Spectral Functional Connectivity Network (KCS-FCnet) method addresses these limitations by providing richer spatial-temporal-spectral feature maps, a simpler architecture, and a more interpretable approach for EEG-driven MI discrimination. In particular, KCS-FCnet uses a single 1D-convolutional-based neural network to extract temporal-frequency features from raw EEG data and a cross-spectral Gaussian kernel connectivity layer to model channel functional relationships. As a result, the functional connectivity feature map reduces the number of parameters, improving interpretability by extracting meaningful patterns related to MI tasks. These patterns can be adapted to the subject's unique characteristics. The validation results prove that introducing KCS-FCnet shallow architecture is a promising approach for EEG-based MI classification with the potential for real-world use in brain-computer interface systems.

</details>
