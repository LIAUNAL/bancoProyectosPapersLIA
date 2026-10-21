---
id: A013
titulo: "Explainable Deep Kernel Learning for Interpretable Automatic Modulation Classification"
tipo: articulo
temas: [T05, T07]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [clasificación de modulación, aprendizaje profundo de kernels, random Fourier features, IA explicable, redes ligeras, baja SNR]
fuente_resumen: abstract
anio: 2025
revista: "Computers"
doi: 10.3390/computers14090372
citas_openalex: 2
fuentes: [0001330950]
---

# Explainable Deep Kernel Learning for Interpretable Automatic Modulation Classification

**Autores:** Carlos Enrique Mosquera-Trujilo, Juan Camilo Lugo-Rojas, Diego Fabián Collazos-Huertas, Andrés Marino Álvarez-Meza, German Castellanos-Dominguez  
**Revista:** Computers (2025)  
**DOI:** https://doi.org/10.3390/computers14090372  
**Temas:** T05 Métodos kernel y aprendizaje basado en teoría de la información; T07 Aprendizaje profundo y explicabilidad  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Clasificación automática de modulación (AMC) en comunicaciones inalámbricas de bajo consumo.

## Problema de investigación
Los modelos de AMC tienen alto costo computacional, mal desempeño con baja relación señal-ruido y poca interpretabilidad.

## Propuesta o novedad
CRFFDT-Net, una arquitectura de kernel profundo que integra Convolutional Random Fourier Features (CRFFSinCos), un módulo de umbralización automática para eliminar ruido y un extractor temporal híbrido CNN-GRU.

## Resultados
En RadioML 2016.10A (once tipos de modulación), logra exactitud promedio estadísticamente comparable a la del estado del arte con muchos menos parámetros y menor latencia. GradCAM++ resalta el papel de las CRFF en la representación aprendida.

## Conclusiones principales
CRFFDT-Net es una solución ligera y explicable para AMC en sistemas de bajo consumo.

## Métodos
- CRFF
- CNN-GRU
- umbralización
- Grad-CAM++

## Idea para trabajo futuro
Evaluar CRFFDT-Net con señales reales sobre hardware embebido y en presencia de interferencia y desvanecimiento.

## Relacionados (similitud semántica)
- extiende: [[A041-2024-lightweight-and-interpretable-dl-model-using-convolutional-r]] — Lightweight and Interpretable DL Model Using Convolutional RFF for AMC

<details><summary>Abstract</summary>

Modern wireless communication systems increasingly rely on Automatic Modulation Classification (AMC) to enhance reliability and adaptability, especially in the presence of severe signal degradation. However, despite significant progress driven by deep learning, many AMC models still struggle with high computational overhead, suboptimal performance under low-signal-to-noise conditions, and limited interpretability, factors that hinder their deployment in real-time, resource-constrained environments. To address these challenges, we propose the Convolutional Random Fourier Features with Denoising Thresholding Network (CRFFDT-Net), a compact and interpretable deep kernel architecture that integrates Convolutional Random Fourier Features (CRFFSinCos), an automatic threshold-based denoising module, and a hybrid time-domain feature extractor composed of CNN and GRU layers. Our approach is validated on the RadioML 2016.10A benchmark dataset, encompassing eleven modulation types across a wide signal-to-noise ratio (SNR) spectrum. Experimental results demonstrate that CRFFDT-Net achieves an average classification accuracy that is statistically comparable to state-of-the-art models, while requiring significantly fewer parameters and offering lower inference latency. This highlights an exceptional accuracy–complexity trade-off. Moreover, interpretability analysis using GradCAM++ highlights the pivotal role of the Convolutional Random Fourier Features in the representation learning process, providing valuable insight into the model’s decision-making. These results underscore the promise of CRFFDT-Net as a lightweight and explainable solution for AMC in real-world, low-power communication systems.

</details>
