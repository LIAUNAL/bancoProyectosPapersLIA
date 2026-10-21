---
id: A060
titulo: "Random fourier features-based deep learning improvement with class activation interpretability for nerve structure segmentation"
tipo: articulo
temas: [T03, T07, T05]
cluster: "C05 Kernels, optimización y resonancia magnética"
palabras_clave: [características aleatorias de Fourier, bloqueo de nervios, segmentación de ultrasonido, Grad-CAM, kernels]
fuente_resumen: abstract
anio: 2021
revista: "Sensors"
doi: 10.3390/s21227741
citas_openalex: 18
fuentes: [0001330950]
---

# Random fourier features-based deep learning improvement with class activation interpretability for nerve structure segmentation

**Autores:** Cristian Alfonso Jimenez-Castaño, Andrés Marino Álvarez-Meza, Oscar David Aguirre-Ospina, David  Augusto Cardenas Peña, Alvaro Angel Orozco  
**Revista:** Sensors (2021)  
**DOI:** https://doi.org/10.3390/s21227741  
**Temas:** T03 Imagen médica y neuroimagen; T07 Aprendizaje profundo y explicabilidad; T05 Métodos kernel y aprendizaje basado en teoría de la información  
**Clúster:** C05 Kernels, optimización y resonancia magnética

## Aplicación
Segmentación de estructuras nerviosas en imágenes de ultrasonido para bloqueo regional de nervios periféricos.

## Problema de investigación
La atenuación y el ruido speckle dificultan localizar el nervio, y las arquitecturas profundas complejas carecen de interpretabilidad.

## Propuesta o novedad
Se complementan tres arquitecturas de segmentación (FCN, U-Net y ResUnet) con características aleatorias de Fourier (random Fourier features) como mejora basada en kernels, junto con mapas de activación de clase (Grad-CAM) para interpretar.

## Resultados
Con dos bases de ultrasonido de bloqueo de nervios, el enfoque ofrece mejor capacidad de generalización en la segmentación.

## Conclusiones principales
La integración de kernels aproximados con redes profundas mejora generalización y permite interpretar las regiones relevantes.

## Métodos
- random Fourier features
- U-Net
- ResUnet
- Grad-CAM

## Idea para trabajo futuro
Evaluar la robustez de la mejora kernel ante equipos de ultrasonido distintos mediante adaptación de dominio.

## Relacionados (similitud semántica)
- derivado del proyecto: [[P033-2016-desarrollo-de-un-sistema-de-identificacion-de-estructuras-ne]] — Desarrollo de un sistema de identificación de estructuras nerviosas en imágenes de ultrasonido para la asistencia del bloqueo de nervios periféricos. Aplicación al tratamiento de dolor agudo traumático y prevención del dolor neuropático crónico.
- extendido por: [[A052-2023-feet-segmentation-for-regional-analgesia-monitoring-using-co]] — Feet Segmentation for Regional Analgesia Monitoring Using Convolutional RFF and Layer-Wise Weighted CAM Interpretability

<details><summary>Abstract</summary>

Peripheral nerve blocking (PNB) is a standard procedure to support regional anesthesia. Still, correct localization of the nerve's structure is needed to avoid adverse effects; thereby, ultrasound images are used as an aid approach. In addition, image-based automatic nerve segmentation from deep learning methods has been proposed to mitigate attenuation and speckle noise ultrasonography issues. Notwithstanding, complex architectures highlight the region of interest lacking suitable data interpretability concerning the learned features from raw instances. Here, a kernel-based deep learning enhancement is introduced for nerve structure segmentation. In a nutshell, a random Fourier features-based approach was utilized to complement three well-known semantic segmentation architectures, e.g., fully convolutional network, U-net, and ResUnet. Moreover, two ultrasound image datasets for PNB were tested. Obtained results show that our kernel-based approach provides a better generalization capability from image segmentation-based assessments on different nerve structures. Further, for data interpretability, a semantic segmentation extension of the GradCam++ for class-activation mapping was used to reveal relevant learned features separating between nerve and background. Thus, our proposal favors both straightforward (shallow) and complex architectures (deeper neural networks).

</details>
